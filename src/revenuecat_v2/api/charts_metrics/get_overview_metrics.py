from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_overview_metrics_currency import GetOverviewMetricsCurrency
from ...models.get_overview_metrics_response_400 import GetOverviewMetricsResponse400
from ...models.get_overview_metrics_response_401 import GetOverviewMetricsResponse401
from ...models.get_overview_metrics_response_403 import GetOverviewMetricsResponse403
from ...models.get_overview_metrics_response_404 import GetOverviewMetricsResponse404
from ...models.get_overview_metrics_response_423 import GetOverviewMetricsResponse423
from ...models.get_overview_metrics_response_429 import GetOverviewMetricsResponse429
from ...models.get_overview_metrics_response_500 import GetOverviewMetricsResponse500
from ...models.get_overview_metrics_response_503 import GetOverviewMetricsResponse503
from ...models.overview_metrics import OverviewMetrics
from ...types import UNSET, Response, Unset


def _get_kwargs(
    project_id: str,
    *,
    currency: GetOverviewMetricsCurrency | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_currency: str | Unset = UNSET
    if not isinstance(currency, Unset):
        json_currency = currency.value

    params["currency"] = json_currency

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/projects/{project_id}/metrics/overview".format(
            project_id=quote(str(project_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    GetOverviewMetricsResponse400
    | GetOverviewMetricsResponse401
    | GetOverviewMetricsResponse403
    | GetOverviewMetricsResponse404
    | GetOverviewMetricsResponse423
    | GetOverviewMetricsResponse429
    | GetOverviewMetricsResponse500
    | GetOverviewMetricsResponse503
    | OverviewMetrics
    | None
):
    if response.status_code == 200:
        response_200 = OverviewMetrics.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = GetOverviewMetricsResponse400.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = GetOverviewMetricsResponse401.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = GetOverviewMetricsResponse403.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = GetOverviewMetricsResponse404.from_dict(response.json())

        return response_404

    if response.status_code == 423:
        response_423 = GetOverviewMetricsResponse423.from_dict(response.json())

        return response_423

    if response.status_code == 429:
        response_429 = GetOverviewMetricsResponse429.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = GetOverviewMetricsResponse500.from_dict(response.json())

        return response_500

    if response.status_code == 503:
        response_503 = GetOverviewMetricsResponse503.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    GetOverviewMetricsResponse400
    | GetOverviewMetricsResponse401
    | GetOverviewMetricsResponse403
    | GetOverviewMetricsResponse404
    | GetOverviewMetricsResponse423
    | GetOverviewMetricsResponse429
    | GetOverviewMetricsResponse500
    | GetOverviewMetricsResponse503
    | OverviewMetrics
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
    currency: GetOverviewMetricsCurrency | Unset = UNSET,
) -> Response[
    GetOverviewMetricsResponse400
    | GetOverviewMetricsResponse401
    | GetOverviewMetricsResponse403
    | GetOverviewMetricsResponse404
    | GetOverviewMetricsResponse423
    | GetOverviewMetricsResponse429
    | GetOverviewMetricsResponse500
    | GetOverviewMetricsResponse503
    | OverviewMetrics
]:
    """Get overview metrics for a project

     This endpoint requires the following permission(s): <code>charts_metrics:overview:read</code>. This
    endpoint belongs to the <strong>Charts & Metrics</strong> domain, which has a default rate limit of
    <strong>5 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        currency (GetOverviewMetricsCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOverviewMetricsResponse400 | GetOverviewMetricsResponse401 | GetOverviewMetricsResponse403 | GetOverviewMetricsResponse404 | GetOverviewMetricsResponse423 | GetOverviewMetricsResponse429 | GetOverviewMetricsResponse500 | GetOverviewMetricsResponse503 | OverviewMetrics]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        currency=currency,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    currency: GetOverviewMetricsCurrency | Unset = UNSET,
) -> (
    GetOverviewMetricsResponse400
    | GetOverviewMetricsResponse401
    | GetOverviewMetricsResponse403
    | GetOverviewMetricsResponse404
    | GetOverviewMetricsResponse423
    | GetOverviewMetricsResponse429
    | GetOverviewMetricsResponse500
    | GetOverviewMetricsResponse503
    | OverviewMetrics
    | None
):
    """Get overview metrics for a project

     This endpoint requires the following permission(s): <code>charts_metrics:overview:read</code>. This
    endpoint belongs to the <strong>Charts & Metrics</strong> domain, which has a default rate limit of
    <strong>5 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        currency (GetOverviewMetricsCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOverviewMetricsResponse400 | GetOverviewMetricsResponse401 | GetOverviewMetricsResponse403 | GetOverviewMetricsResponse404 | GetOverviewMetricsResponse423 | GetOverviewMetricsResponse429 | GetOverviewMetricsResponse500 | GetOverviewMetricsResponse503 | OverviewMetrics
    """

    return sync_detailed(
        project_id=project_id,
        client=client,
        currency=currency,
    ).parsed


async def asyncio_detailed(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    currency: GetOverviewMetricsCurrency | Unset = UNSET,
) -> Response[
    GetOverviewMetricsResponse400
    | GetOverviewMetricsResponse401
    | GetOverviewMetricsResponse403
    | GetOverviewMetricsResponse404
    | GetOverviewMetricsResponse423
    | GetOverviewMetricsResponse429
    | GetOverviewMetricsResponse500
    | GetOverviewMetricsResponse503
    | OverviewMetrics
]:
    """Get overview metrics for a project

     This endpoint requires the following permission(s): <code>charts_metrics:overview:read</code>. This
    endpoint belongs to the <strong>Charts & Metrics</strong> domain, which has a default rate limit of
    <strong>5 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        currency (GetOverviewMetricsCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GetOverviewMetricsResponse400 | GetOverviewMetricsResponse401 | GetOverviewMetricsResponse403 | GetOverviewMetricsResponse404 | GetOverviewMetricsResponse423 | GetOverviewMetricsResponse429 | GetOverviewMetricsResponse500 | GetOverviewMetricsResponse503 | OverviewMetrics]
    """

    kwargs = _get_kwargs(
        project_id=project_id,
        currency=currency,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    project_id: str,
    *,
    client: AuthenticatedClient | Client,
    currency: GetOverviewMetricsCurrency | Unset = UNSET,
) -> (
    GetOverviewMetricsResponse400
    | GetOverviewMetricsResponse401
    | GetOverviewMetricsResponse403
    | GetOverviewMetricsResponse404
    | GetOverviewMetricsResponse423
    | GetOverviewMetricsResponse429
    | GetOverviewMetricsResponse500
    | GetOverviewMetricsResponse503
    | OverviewMetrics
    | None
):
    """Get overview metrics for a project

     This endpoint requires the following permission(s): <code>charts_metrics:overview:read</code>. This
    endpoint belongs to the <strong>Charts & Metrics</strong> domain, which has a default rate limit of
    <strong>5 requests per minute</strong>.

    Args:
        project_id (str):  Example: proj1ab2c3d4.
        currency (GetOverviewMetricsCurrency | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GetOverviewMetricsResponse400 | GetOverviewMetricsResponse401 | GetOverviewMetricsResponse403 | GetOverviewMetricsResponse404 | GetOverviewMetricsResponse423 | GetOverviewMetricsResponse429 | GetOverviewMetricsResponse500 | GetOverviewMetricsResponse503 | OverviewMetrics
    """

    return (
        await asyncio_detailed(
            project_id=project_id,
            client=client,
            currency=currency,
        )
    ).parsed
