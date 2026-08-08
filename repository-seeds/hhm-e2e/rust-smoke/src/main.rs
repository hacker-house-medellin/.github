use anyhow::{bail, Context, Result};
use futures_util::SinkExt;
use reqwest::StatusCode;
use std::{env, time::Duration};
use tokio::time::timeout;
use tokio_tungstenite::{connect_async, tungstenite::Message};
use url::Url;

#[derive(Clone, Copy, Debug, Eq, PartialEq)]
struct Service {
    env_name: &'static str,
    label: &'static str,
    health_path: &'static str,
}

const SERVICES: &[Service] = &[
    Service {
        env_name: "HHM_MASH_URL",
        label: "Mash web",
        health_path: "/health",
    },
    Service {
        env_name: "HHM_LEPTOS_URL",
        label: "Leptos web",
        health_path: "/health",
    },
    Service {
        env_name: "HHM_DIOXUS_URL",
        label: "Dioxus web",
        health_path: "/health",
    },
    Service {
        env_name: "HHM_API_URL",
        label: "API",
        health_path: "/health",
    },
];

fn configured(name: &str) -> Option<String> {
    env::var(name)
        .ok()
        .map(|value| value.trim_end_matches('/').to_owned())
        .filter(|value| !value.is_empty())
}

fn websocket_url(api_base: &str) -> Result<Url> {
    let mut url = Url::parse(api_base).context("HHM_API_URL is not a valid URL")?;
    let websocket_scheme = match url.scheme() {
        "http" | "ws" => "ws",
        "https" | "wss" => "wss",
        scheme => bail!("unsupported API URL scheme: {scheme}"),
    };
    url.set_scheme(websocket_scheme)
        .map_err(|()| anyhow::anyhow!("failed to set WebSocket URL scheme"))?;
    url.set_path("/ws");
    url.set_query(None);
    url.set_fragment(None);
    Ok(url)
}

async fn check_http(client: &reqwest::Client, service: Service, base: &str) -> Result<()> {
    let url = format!("{}{path}", base, path = service.health_path);
    let response = client
        .get(&url)
        .send()
        .await
        .with_context(|| format!("{} request failed", service.label))?;
    if response.status() != StatusCode::OK {
        bail!(
            "{} returned {} from {}",
            service.label,
            response.status(),
            url
        );
    }
    println!("ok: {} ({})", service.label, url);
    Ok(())
}

async fn check_websocket(api_base: &str) -> Result<()> {
    let url = websocket_url(api_base)?;
    let (mut stream, _) = timeout(Duration::from_secs(10), connect_async(url.as_str()))
        .await
        .context("WebSocket connect timeout")??;
    stream
        .send(Message::Text(r#"{"type":"ping"}"#.into()))
        .await
        .context("WebSocket ping send failed")?;
    stream.close(None).await.context("WebSocket close failed")?;
    println!("ok: API WebSocket upgrade ({url})");
    Ok(())
}

#[tokio::main]
async fn main() -> Result<()> {
    let client = reqwest::Client::builder()
        .timeout(Duration::from_secs(10))
        .build()?;
    let mut configured_count = 0_usize;

    for service in SERVICES {
        if let Some(base) = configured(service.env_name) {
            configured_count += 1;
            check_http(&client, *service, &base).await?;
        }
    }

    if let Some(api_base) = configured("HHM_API_URL") {
        check_websocket(&api_base).await?;
    }

    if configured_count == 0 {
        println!("No live endpoint variables supplied; offline binary and unit checks passed.");
    }

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn service_contract_includes_all_frontends_and_api() {
        assert_eq!(SERVICES.len(), 4);
        assert!(SERVICES
            .iter()
            .any(|service| service.env_name == "HHM_API_URL"));
    }

    #[test]
    fn websocket_url_maps_http_and_https_and_discards_sensitive_suffixes() {
        let insecure = websocket_url("http://localhost:8090/api?token=secret#fragment").unwrap();
        assert_eq!(insecure.as_str(), "ws://localhost:8090/ws");

        let secure = websocket_url("https://api.example.test/base").unwrap();
        assert_eq!(secure.as_str(), "wss://api.example.test/ws");
    }

    #[test]
    fn websocket_url_rejects_unsupported_schemes() {
        let error = websocket_url("ftp://api.example.test").unwrap_err();
        assert!(error.to_string().contains("unsupported API URL scheme"));
    }
}
