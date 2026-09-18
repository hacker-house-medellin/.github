# Rust HTTP and WebSocket smoke harness

This crate augments the browser matrix with lightweight service checks for the three Rust web frontends and the API.

```bash
export HHM_MASH_URL=http://localhost:8080
export HHM_LEPTOS_URL=http://localhost:8081
export HHM_DIOXUS_URL=http://localhost:8082
export HHM_API_URL=http://localhost:8090
cargo run --manifest-path rust-smoke/Cargo.toml
```

With no endpoint variables, the binary exits successfully after offline compilation and unit tests. Live URLs and credentials belong only in environment-scoped test secrets.
