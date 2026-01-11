from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.detach_products_from_package_body import DetachProductsFromPackageBody
from ...models.detach_products_from_package_response_400 import DetachProductsFromPackageResponse400
from ...models.detach_products_from_package_response_401 import DetachProductsFromPackageResponse401
from ...models.detach_products_from_package_response_403 import DetachProductsFromPackageResponse403
from ...models.detach_products_from_package_response_404 import DetachProductsFromPackageResponse404
from ...models.detach_products_from_package_response_409 import DetachProductsFromPackageResponse409
from ...models.detach_products_from_package_response_422 import DetachProductsFromPackageResponse422
from ...models.detach_products_from_package_response_423 import DetachProductsFromPackageResponse423
from ...models.detach_products_from_package_response_429 import DetachProductsFromPackageResponse429
from ...models.detach_products_from_package_response_500 import DetachProductsFromPackageResponse500
from ...models.detach_products_from_package_response_503 import DetachProductsFromPackageResponse503
from ...models.package import Package
from ...types import Response


def _get_kwargs(
    project_id: str,
    package_id: str,
    *,
    body: DetachProductsFromPackageBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/projects/{project_id}/packages/{package_id}/actions/detach_products".format(
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
    DetachProductsFromPackageResponse400
    | DetachProductsFromPackageResponse401
    | DetachProductsFromPackageResponse403
    | DetachProductsFromPackageResponse404
    | DetachProductsFromPackageResponse409
    | DetachProductsFromPackageResponse422
    | DetachProductsFromPackageResponse423
    | DetachProductsFromPackageResponse429
    | DetachProductsFromPackageResponse500
    | DetachProductsFromPackageResponse503
    | Package
    | None
):
    if response.status_code == 200:
        response_200 = Package.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = DetachProductsFromPackageResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = DetachProductsFromPackageResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = DetachProductsFromPackageResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = DetachProductsFromPackageResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 409:
        response_409 = DetachProductsFromPackageResponse409.from_dict(response.json())

        return response_409

    if response.status_code == 422:
        response_422 = DetachProductsFromPackageResponse422.from_dict(response.json())

        return response_422

    if response.status_code == 423:
        response_423 = DetachProductsFromPackageResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = DetachProductsFromPackageResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = DetachProductsFromPackageResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = DetachProductsFromPackageResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    DetachProductsFromPackageResponse400
    | DetachProductsFromPackageResponse401
    | DetachProductsFromPackageResponse403
    | DetachProductsFromPackageResponse404
    | DetachProductsFromPackageResponse409
    | DetachProductsFromPackageResponse422
    | DetachProductsFromPackageResponse423
    | DetachProductsFromPackageResponse429
    | DetachProductsFromPackageResponse500
    | DetachProductsFromPackageResponse503
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
    body: DetachProductsFromPackageBody,
) -> Response[
    DetachProductsFromPackageResponse400
    | DetachProductsFromPackageResponse401
    | DetachProductsFromPackageResponse403
    | DetachProductsFromPackageResponse404
    | DetachProductsFromPackageResponse409
    | DetachProductsFromPackageResponse422
    | DetachProductsFromPackageResponse423
    | DetachProductsFromPackageResponse429
    | DetachProductsFromPackageResponse500
    | DetachProductsFromPackageResponse503
    | Package
]:
    """Detach a set of products from a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        body (DetachProductsFromPackageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DetachProductsFromPackageResponse400 | DetachProductsFromPackageResponse401 | DetachProductsFromPackageResponse403 | DetachProductsFromPackageResponse404 | DetachProductsFromPackageResponse409 | DetachProductsFromPackageResponse422 | DetachProductsFromPackageResponse423 | DetachProductsFromPackageResponse429 | DetachProductsFromPackageResponse500 | DetachProductsFromPackageResponse503 | Package]
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
    body: DetachProductsFromPackageBody,
) -> (
    DetachProductsFromPackageResponse400
    | DetachProductsFromPackageResponse401
    | DetachProductsFromPackageResponse403
    | DetachProductsFromPackageResponse404
    | DetachProductsFromPackageResponse409
    | DetachProductsFromPackageResponse422
    | DetachProductsFromPackageResponse423
    | DetachProductsFromPackageResponse429
    | DetachProductsFromPackageResponse500
    | DetachProductsFromPackageResponse503
    | Package
    | None
):
    """Detach a set of products from a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        body (DetachProductsFromPackageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DetachProductsFromPackageResponse400 | DetachProductsFromPackageResponse401 | DetachProductsFromPackageResponse403 | DetachProductsFromPackageResponse404 | DetachProductsFromPackageResponse409 | DetachProductsFromPackageResponse422 | DetachProductsFromPackageResponse423 | DetachProductsFromPackageResponse429 | DetachProductsFromPackageResponse500 | DetachProductsFromPackageResponse503 | Package
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
    body: DetachProductsFromPackageBody,
) -> Response[
    DetachProductsFromPackageResponse400
    | DetachProductsFromPackageResponse401
    | DetachProductsFromPackageResponse403
    | DetachProductsFromPackageResponse404
    | DetachProductsFromPackageResponse409
    | DetachProductsFromPackageResponse422
    | DetachProductsFromPackageResponse423
    | DetachProductsFromPackageResponse429
    | DetachProductsFromPackageResponse500
    | DetachProductsFromPackageResponse503
    | Package
]:
    """Detach a set of products from a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        body (DetachProductsFromPackageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[DetachProductsFromPackageResponse400 | DetachProductsFromPackageResponse401 | DetachProductsFromPackageResponse403 | DetachProductsFromPackageResponse404 | DetachProductsFromPackageResponse409 | DetachProductsFromPackageResponse422 | DetachProductsFromPackageResponse423 | DetachProductsFromPackageResponse429 | DetachProductsFromPackageResponse500 | DetachProductsFromPackageResponse503 | Package]
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
    body: DetachProductsFromPackageBody,
) -> (
    DetachProductsFromPackageResponse400
    | DetachProductsFromPackageResponse401
    | DetachProductsFromPackageResponse403
    | DetachProductsFromPackageResponse404
    | DetachProductsFromPackageResponse409
    | DetachProductsFromPackageResponse422
    | DetachProductsFromPackageResponse423
    | DetachProductsFromPackageResponse429
    | DetachProductsFromPackageResponse500
    | DetachProductsFromPackageResponse503
    | Package
    | None
):
    """Detach a set of products from a package

     This endpoint requires the following permission(s):
    <code>project_configuration:packages:read_write</code>. This endpoint belongs to the <strong>Project
    Configuration</strong> domain, which has a default rate limit of <strong>60 requests per
    minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        package_id (str):  Example: pkge1a2b3c4d5.
        body (DetachProductsFromPackageBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        DetachProductsFromPackageResponse400 | DetachProductsFromPackageResponse401 | DetachProductsFromPackageResponse403 | DetachProductsFromPackageResponse404 | DetachProductsFromPackageResponse409 | DetachProductsFromPackageResponse422 | DetachProductsFromPackageResponse423 | DetachProductsFromPackageResponse429 | DetachProductsFromPackageResponse500 | DetachProductsFromPackageResponse503 | Package
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            package_id=package_id,
            client=client,
            body=body,
        )
    ).parsed
