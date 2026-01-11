from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.create_paywall_body import CreatePaywallBody
from ...models.create_paywall_response_400 import CreatePaywallResponse400
from ...models.create_paywall_response_401 import CreatePaywallResponse401
from ...models.create_paywall_response_403 import CreatePaywallResponse403
from ...models.create_paywall_response_404 import CreatePaywallResponse404
from ...models.create_paywall_response_409 import CreatePaywallResponse409
from ...models.create_paywall_response_422 import CreatePaywallResponse422
from ...models.create_paywall_response_423 import CreatePaywallResponse423
from ...models.create_paywall_response_429 import CreatePaywallResponse429
from ...models.create_paywall_response_500 import CreatePaywallResponse500
from ...models.create_paywall_response_503 import CreatePaywallResponse503
from ...models.paywall import Paywall
from ...types import Response


def _get_kwargs(
    project_id: str,
    *,
    body: CreatePaywallBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/paywalls".format(
            project_id=quote(str(project_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    CreatePaywallResponse400
    | CreatePaywallResponse401
    | CreatePaywallResponse403
    | CreatePaywallResponse404
    | CreatePaywallResponse409
    | CreatePaywallResponse422
    | CreatePaywallResponse423
    | CreatePaywallResponse429
    | CreatePaywallResponse500
    | CreatePaywallResponse503
    | Paywall
    | None
):
    if response.status_code == 201:
        response_201 = Paywall.from_dict(response.json())

        return response_201

    if response.status_code == 400:
        response_400 = CreatePaywallResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = CreatePaywallResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = CreatePaywallResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = CreatePaywallResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = CreatePaywallResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = CreatePaywallResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = CreatePaywallResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = CreatePaywallResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = CreatePaywallResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = CreatePaywallResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    CreatePaywallResponse400
    | CreatePaywallResponse401
    | CreatePaywallResponse403
    | CreatePaywallResponse404
    | CreatePaywallResponse409
    | CreatePaywallResponse422
    | CreatePaywallResponse423
    | CreatePaywallResponse429
    | CreatePaywallResponse500
    | CreatePaywallResponse503
    | Paywall
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreatePaywallBody,
) -> Response[
    CreatePaywallResponse400
    | CreatePaywallResponse401
    | CreatePaywallResponse403
    | CreatePaywallResponse404
    | CreatePaywallResponse409
    | CreatePaywallResponse422
    | CreatePaywallResponse423
    | CreatePaywallResponse429
    | CreatePaywallResponse500
    | CreatePaywallResponse503
    | Paywall
]:
    """Create a paywall

     Create a paywall for an offering of the project.
     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreatePaywallBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePaywallResponse400 | CreatePaywallResponse401 | CreatePaywallResponse403 | CreatePaywallResponse404 | CreatePaywallResponse409 | CreatePaywallResponse422 | CreatePaywallResponse423 | CreatePaywallResponse429 | CreatePaywallResponse500 | CreatePaywallResponse503 | Paywall]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreatePaywallBody,
) -> (
    CreatePaywallResponse400
    | CreatePaywallResponse401
    | CreatePaywallResponse403
    | CreatePaywallResponse404
    | CreatePaywallResponse409
    | CreatePaywallResponse422
    | CreatePaywallResponse423
    | CreatePaywallResponse429
    | CreatePaywallResponse500
    | CreatePaywallResponse503
    | Paywall
    | None
):
    """Create a paywall

     Create a paywall for an offering of the project.
     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreatePaywallBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePaywallResponse400 | CreatePaywallResponse401 | CreatePaywallResponse403 | CreatePaywallResponse404 | CreatePaywallResponse409 | CreatePaywallResponse422 | CreatePaywallResponse423 | CreatePaywallResponse429 | CreatePaywallResponse500 | CreatePaywallResponse503 | Paywall
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreatePaywallBody,
) -> Response[
    CreatePaywallResponse400
    | CreatePaywallResponse401
    | CreatePaywallResponse403
    | CreatePaywallResponse404
    | CreatePaywallResponse409
    | CreatePaywallResponse422
    | CreatePaywallResponse423
    | CreatePaywallResponse429
    | CreatePaywallResponse500
    | CreatePaywallResponse503
    | Paywall
]:
    """Create a paywall

     Create a paywall for an offering of the project.
     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreatePaywallBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CreatePaywallResponse400 | CreatePaywallResponse401 | CreatePaywallResponse403 | CreatePaywallResponse404 | CreatePaywallResponse409 | CreatePaywallResponse422 | CreatePaywallResponse423 | CreatePaywallResponse429 | CreatePaywallResponse500 | CreatePaywallResponse503 | Paywall]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: CreatePaywallBody,
) -> (
    CreatePaywallResponse400
    | CreatePaywallResponse401
    | CreatePaywallResponse403
    | CreatePaywallResponse404
    | CreatePaywallResponse409
    | CreatePaywallResponse422
    | CreatePaywallResponse423
    | CreatePaywallResponse429
    | CreatePaywallResponse500
    | CreatePaywallResponse503
    | Paywall
    | None
):
    """Create a paywall

     Create a paywall for an offering of the project.
     This endpoint requires the following permission(s):
    <code>project_configuration:offerings:read_write</code>. This endpoint belongs to the
    <strong>Project Configuration</strong> domain, which has a default rate limit of <strong>60 requests
    per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        body (CreatePaywallBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CreatePaywallResponse400 | CreatePaywallResponse401 | CreatePaywallResponse403 | CreatePaywallResponse404 | CreatePaywallResponse409 | CreatePaywallResponse422 | CreatePaywallResponse423 | CreatePaywallResponse429 | CreatePaywallResponse500 | CreatePaywallResponse503 | Paywall
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            body=body,
        )
    ).parsed
