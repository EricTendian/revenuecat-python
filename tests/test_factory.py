import pytest

from revenuecat import api_client, clients
from revenuecat_v1 import AuthenticatedClient as V1AuthenticatedClient
from revenuecat_v2 import AuthenticatedClient as V2AuthenticatedClient


def test_clients_from_api_key_builds_both_versions() -> None:
    rc = clients(api_key="secret", base_url_v1="https://v1.example", base_url_v2="https://v2.example")

    assert isinstance(rc.v1, V1AuthenticatedClient)
    assert isinstance(rc.v2, V2AuthenticatedClient)
    assert rc.v1._base_url == "https://v1.example"
    assert rc.v2._base_url == "https://v2.example"
    assert rc.v1.token == "secret"
    assert rc.v2.token == "secret"


@pytest.mark.parametrize(
    ("version", "expected_base_url"),
    [
        ("v1", "https://api.revenuecat.com/v1"),
        ("v2", "https://api.revenuecat.com/v2"),
    ],
)
def test_api_client_uses_default_base_url(version: str, expected_base_url: str) -> None:
    client = api_client(api_key="secret", version=version)

    assert client._base_url == expected_base_url


def test_api_client_rejects_unknown_version() -> None:
    with pytest.raises(ValueError, match="Unsupported RevenueCat API version"):
        api_client(api_key="secret", version="v3")  # type: ignore[arg-type]
