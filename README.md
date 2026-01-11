# revenuecat

Modern Python API client for RevenueCat, generated from the official OpenAPI specs.

Supports both API versions:
- v1 (`plugin-redoc-3.yaml`)
- v2 (`plugin-redoc-0.yaml`)

## Install

This project uses `uv` for dependency management.

## Usage

```python
from revenuecat import api_client, clients
from revenuecat.v2 import AuthenticatedClient as V2AuthenticatedClient

client_v2 = api_client(api_key="REVENUECAT_SECRET_KEY", version="v2")
client_v1 = api_client(api_key="REVENUECAT_SECRET_KEY", version="v1")

rc = clients(api_key="REVENUECAT_SECRET_KEY")
client_v1 = rc.v1
client_v2 = rc.v2

# Or use the versioned modules directly:
client_v2 = V2AuthenticatedClient(base_url="https://api.revenuecat.com/v2", token="REVENUECAT_SECRET_KEY")
```

## Regenerate

```bash
uv run ./scripts/regenerate.sh
```
