# Cloudflare test-resource status

Generated: 2026-08-08T18:16:49.382956+00:00

- Token verified: **False**
- Intended private test artifact bucket: `hhm-artifacts-test`
- DNS changes: **none**
- Worker route changes: **none**


## Errors

- `list-buckets` (HTTP 0): [{'message': 'URLError: <urlopen error [Errno -3] Temporary failure in name resolution>'}]
- `create-bucket` (HTTP 0): [{'message': 'URLError: <urlopen error [Errno -3] Temporary failure in name resolution>'}]

DNS, custom-domain, WAF, and Worker routing remain intentionally untouched until the hostnames and origin health checks are explicit.
