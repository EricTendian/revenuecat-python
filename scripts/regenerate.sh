#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

"${ROOT_DIR}/scripts/download_openapi.sh"

rm -rf "${ROOT_DIR}/.generated"
mkdir -p "${ROOT_DIR}/.generated"

uv run openapi-python-client generate \
  --path "${ROOT_DIR}/openapi/revenuecat-v1.yaml" \
  --config "${ROOT_DIR}/openapi/openapi-python-client-v1.yaml" \
  --output-path "${ROOT_DIR}/.generated/revenuecat-v1" \
  --overwrite

uv run openapi-python-client generate \
  --path "${ROOT_DIR}/openapi/revenuecat-v2.yaml" \
  --config "${ROOT_DIR}/openapi/openapi-python-client-v2.yaml" \
  --output-path "${ROOT_DIR}/.generated/revenuecat-v2" \
  --overwrite

rm -rf "${ROOT_DIR}/src/revenuecat_v1" "${ROOT_DIR}/src/revenuecat_v2"
mkdir -p "${ROOT_DIR}/src"

cp -R "${ROOT_DIR}/.generated/revenuecat-v1/revenuecat_v1" "${ROOT_DIR}/src/revenuecat_v1"
cp -R "${ROOT_DIR}/.generated/revenuecat-v2/revenuecat_v2" "${ROOT_DIR}/src/revenuecat_v2"

echo "Generated packages:"
echo " - src/revenuecat_v1"
echo " - src/revenuecat_v2"

