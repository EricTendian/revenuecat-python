import httpx
import pytest

import revenuecat_v1
import revenuecat_v2


@pytest.mark.parametrize("module", [revenuecat_v1, revenuecat_v2])
def test_authenticated_client_sets_auth_header(module) -> None:
    client = module.AuthenticatedClient(base_url="https://example.com", token="token-123")

    httpx_client = client.get_httpx_client()

    assert httpx_client.headers["Authorization"] == "Bearer token-123"


@pytest.mark.parametrize("module", [revenuecat_v1, revenuecat_v2])
def test_authenticated_client_respects_custom_prefix(module) -> None:
    client = module.AuthenticatedClient(
        base_url="https://example.com",
        token="token-123",
        prefix="",
    )

    httpx_client = client.get_httpx_client()

    assert httpx_client.headers["Authorization"] == "token-123"


@pytest.mark.parametrize("module", [revenuecat_v1, revenuecat_v2])
def test_authenticated_client_with_headers_updates_existing_client(module) -> None:
    client = module.AuthenticatedClient(
        base_url="https://example.com",
        token="token-123",
        headers={"X-Initial": "1"},
    )

    httpx_client = client.get_httpx_client()
    assert httpx_client.headers["X-Initial"] == "1"

    updated = client.with_headers({"X-Next": "2"})

    assert updated._headers["X-Initial"] == "1"
    assert updated._headers["X-Next"] == "2"
    assert httpx_client.headers["X-Next"] == "2"


@pytest.mark.parametrize("module", [revenuecat_v1, revenuecat_v2])
def test_authenticated_client_with_cookies_updates_existing_client(module) -> None:
    client = module.AuthenticatedClient(
        base_url="https://example.com",
        token="token-123",
        cookies={"initial": "1"},
    )

    httpx_client = client.get_httpx_client()
    assert httpx_client.cookies["initial"] == "1"

    updated = client.with_cookies({"next": "2"})

    assert updated._cookies["initial"] == "1"
    assert updated._cookies["next"] == "2"
    assert httpx_client.cookies["next"] == "2"


@pytest.mark.parametrize("module", [revenuecat_v1, revenuecat_v2])
def test_authenticated_client_with_timeout_updates_existing_client(module) -> None:
    timeout = httpx.Timeout(2.0)
    client = module.AuthenticatedClient(
        base_url="https://example.com",
        token="token-123",
    )

    httpx_client = client.get_httpx_client()
    updated = client.with_timeout(timeout)

    assert updated._timeout == timeout
    assert httpx_client.timeout == timeout
