#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OPENAPI_DIR="${ROOT_DIR}/openapi"

mkdir -p "${OPENAPI_DIR}"

curl -fsSL \
  -H "User-Agent: revenuecat-python (openapi spec download)" \
  "https://www.revenuecat.com/docs/redocusaurus/plugin-redoc-3.yaml" \
  -o "${OPENAPI_DIR}/revenuecat-v1.yaml"

curl -fsSL \
  -H "User-Agent: revenuecat-python (openapi spec download)" \
  "https://www.revenuecat.com/docs/redocusaurus/plugin-redoc-0.yaml" \
  -o "${OPENAPI_DIR}/revenuecat-v2.yaml"

echo "Downloaded OpenAPI specs to ${OPENAPI_DIR}"

