from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.attach_products_to_package_body import AttachProductsToPackageBody
from ...models.attach_products_to_package_response_400 import AttachProductsToPackageResponse400
from ...models.attach_products_to_package_response_401 import AttachProductsToPackageResponse401
from ...models.attach_products_to_package_response_403 import AttachProductsToPackageResponse403
from ...models.attach_products_to_package_response_404 import AttachProductsToPackageResponse404
from ...models.attach_products_to_package_response_409 import AttachProductsToPackageResponse409
from ...models.attach_products_to_package_response_422 import AttachProductsToPackageResponse422
from ...models.attach_products_to_package_response_423 import AttachProductsToPackageResponse423
from ...models.attach_products_to_package_response_429 import AttachProductsToPackageResponse429
from ...models.attach_products_to_package_response_500 import AttachProductsToPackageResponse500
from ...models.attach_products_to_package_response_503 import AttachProductsToPackageResponse503
from ...models.package import Package
from ...types import Response


def _get_kwargs(
    project_id: str,
    package_id: str,
    *,
    body: AttachProductsToPackageBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/packages/{package_id}/actions/attach_products".format(
            project_id=quote(str(project_id), safe=""),
            package_id=quote(str(package_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    AttachProductsToPackageResponse400
    | AttachProductsToPackageResponse401
    | AttachProductsToPackageResponse403
    | AttachProductsToPackageResponse404
    | AttachProductsToPackageResponse409
    | AttachProductsToPackageResponse422
    | AttachProductsToPackageResponse423
    | AttachProductsToPackageResponse429
    | AttachProductsToPackageResponse500
    | AttachProductsToPackageResponse503
    | Package
    | None
):
    if response.status_code == 200:
        response_200 = Package.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AttachProductsToPackageResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AttachProductsToPackageResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AttachProductsToPackageResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AttachProductsToPackageResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = AttachProductsToPackageResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = AttachProductsToPackageResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = AttachProductsToPackageResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = AttachProductsToPackageResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = AttachProductsToPackageResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = AttachProductsToPackageResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    AttachProductsToPackageResponse400
    | AttachProductsToPackageResponse401
    | AttachProductsToPackageResponse403
    | AttachProductsToPackageResponse404
    | AttachProductsToPackageResponse409
    | AttachProductsToPackageResponse422
    | AttachProductsToPackageResponse423
    | AttachProductsToPackageResponse429
    | AttachProductsToPackageResponse500
    | AttachProductsToPackageResponse503
    | Package
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    project_id: str,
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AttachProductsToPackageBody,
) -> Response[
    AttachProductsToPackageResponse400
    | AttachProductsToPackageResponse401
    | AttachProductsToPackageResponse403
    | AttachProductsToPackageResponse404
    | AttachProductsToPackageResponse409
    | AttachProductsToPackageResponse422
    | AttachProductsToPackageResponse423
    | AttachProductsToPackageResponse429
    | AttachProductsToPackageResponse500
    | AttachProductsToPackageResponse503
    | Package
]:
    """Attach a set of products to a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        body (AttachProductsToPackageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachProductsToPackageResponse400 | AttachProductsToPackageResponse401 | AttachProductsToPackageResponse403 | AttachProductsToPackageResponse404 | AttachProductsToPackageResponse409 | AttachProductsToPackageResponse422 | AttachProductsToPackageResponse423 | AttachProductsToPackageResponse429 | AttachProductsToPackageResponse500 | AttachProductsToPackageResponse503 | Package]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        package_id=package_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AttachProductsToPackageBody,
) -> (
    AttachProductsToPackageResponse400
    | AttachProductsToPackageResponse401
    | AttachProductsToPackageResponse403
    | AttachProductsToPackageResponse404
    | AttachProductsToPackageResponse409
    | AttachProductsToPackageResponse422
    | AttachProductsToPackageResponse423
    | AttachProductsToPackageResponse429
    | AttachProductsToPackageResponse500
    | AttachProductsToPackageResponse503
    | Package
    | None
):
    """Attach a set of products to a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        body (AttachProductsToPackageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachProductsToPackageResponse400 | AttachProductsToPackageResponse401 | AttachProductsToPackageResponse403 | AttachProductsToPackageResponse404 | AttachProductsToPackageResponse409 | AttachProductsToPackageResponse422 | AttachProductsToPackageResponse423 | AttachProductsToPackageResponse429 | AttachProductsToPackageResponse500 | AttachProductsToPackageResponse503 | Package
    """

    return sync_detailed(
        project_id=project_id,
        package_id=package_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AttachProductsToPackageBody,
) -> Response[
    AttachProductsToPackageResponse400
    | AttachProductsToPackageResponse401
    | AttachProductsToPackageResponse403
    | AttachProductsToPackageResponse404
    | AttachProductsToPackageResponse409
    | AttachProductsToPackageResponse422
    | AttachProductsToPackageResponse423
    | AttachProductsToPackageResponse429
    | AttachProductsToPackageResponse500
    | AttachProductsToPackageResponse503
    | Package
]:
    """Attach a set of products to a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        body (AttachProductsToPackageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AttachProductsToPackageResponse400 | AttachProductsToPackageResponse401 | AttachProductsToPackageResponse403 | AttachProductsToPackageResponse404 | AttachProductsToPackageResponse409 | AttachProductsToPackageResponse422 | AttachProductsToPackageResponse423 | AttachProductsToPackageResponse429 | AttachProductsToPackageResponse500 | AttachProductsToPackageResponse503 | Package]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        package_id=package_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    package_id: str,
    *,
    client: AuthenticatedClient | Client,
    body: AttachProductsToPackageBody,
) -> (
    AttachProductsToPackageResponse400
    | AttachProductsToPackageResponse401
    | AttachProductsToPackageResponse403
    | AttachProductsToPackageResponse404
    | AttachProductsToPackageResponse409
    | AttachProductsToPackageResponse422
    | AttachProductsToPackageResponse423
    | AttachProductsToPackageResponse429
    | AttachProductsToPackageResponse500
    | AttachProductsToPackageResponse503
    | Package
    | None
):
    """Attach a set of products to a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        body (AttachProductsToPackageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AttachProductsToPackageResponse400 | AttachProductsToPackageResponse401 | AttachProductsToPackageResponse403 | AttachProductsToPackageResponse404 | AttachProductsToPackageResponse409 | AttachProductsToPackageResponse422 | AttachProductsToPackageResponse423 | AttachProductsToPackageResponse429 | AttachProductsToPackageResponse500 | AttachProductsToPackageResponse503 | Package
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            package_id=package_id,
            client=client,
            body=body,
        )
    ).parsed
