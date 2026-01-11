from __future__ import annotations

from dataclasses import dataclass
from typing import Literal, overload

from revenuecat_v1 import AuthenticatedClient as RevenueCatV1AuthenticatedClient
from revenuecat_v2 import AuthenticatedClient as RevenueCatV2AuthenticatedClient

ApiVersion = Literal["v1", "v2"]


@dataclass(frozen=True, slots=True)
class RevenueCatClient:
    v1: RevenueCatV1AuthenticatedClient
    v2: RevenueCatV2AuthenticatedClient

    @classmethod
    def from_api_key(
        cls,
        *,
        api_key: str,
        base_url_v1: str = "https://api.revenuecat.com/v1",
        base_url_v2: str = "https://api.revenuecat.com/v2",
    ) -> "RevenueCatClient":
        return cls(
            v1=RevenueCatV1AuthenticatedClient(base_url=base_url_v1, token=api_key),
            v2=RevenueCatV2AuthenticatedClient(base_url=base_url_v2, token=api_key),
        )


def clients(
    *,
    api_key: str,
    base_url_v1: str = "https://api.revenuecat.com/v1",
    base_url_v2: str = "https://api.revenuecat.com/v2",
) -> RevenueCatClient:
    """Construct authenticated clients for both RevenueCat API versions."""
    return RevenueCatClient.from_api_key(
        api_key=api_key, base_url_v1=base_url_v1, base_url_v2=base_url_v2
    )


@overload
def api_client(
    *,
    api_key: str,
    version: Literal["v1"],
    base_url: str | None = None,
) -> RevenueCatV1AuthenticatedClient: ...


@overload
def api_client(
    *,
    api_key: str,
    version: Literal["v2"],
    base_url: str | None = None,
) -> RevenueCatV2AuthenticatedClient: ...


def api_client(*, api_key: str, version: ApiVersion, base_url: str | None = None):
    """
    Construct an authenticated client for a specific RevenueCat API version.

    Notes:
    - The generated clients expose both sync and async endpoint helpers.
    - Default `base_url` values come from the OpenAPI specs (generated code).
    """
    if version == "v1":
        return RevenueCatV1AuthenticatedClient(
            base_url=base_url or "https://api.revenuecat.com/v1", token=api_key
        )
    if version == "v2":
        return RevenueCatV2AuthenticatedClient(
            base_url=base_url or "https://api.revenuecat.com/v2", token=api_key
        )
    raise ValueError(f"Unsupported RevenueCat API version: {version!r}")
