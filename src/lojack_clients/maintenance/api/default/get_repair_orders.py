from typing import Any, Dict, Optional, Union

import httpx

from ...client import Client
from ...models.get_repair_orders_response_200 import GetRepairOrdersResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    vin: Union[Unset, None, str] = UNSET,
    asset_id: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/repairOrders".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["vin"] = vin

    params["assetId"] = asset_id

    params["sort"] = sort

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[GetRepairOrdersResponse200]:
    if response.status_code == 200:
        response_200 = GetRepairOrdersResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[GetRepairOrdersResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    vin: Union[Unset, None, str] = UNSET,
    asset_id: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[GetRepairOrdersResponse200]:
    """Get repair orders for vehicle

    Args:
        vin (Union[Unset, None, str]):  Example: VINNUMBER123456.
        asset_id (Union[Unset, None, str]):  Example: 362846328238BASHD2N.
        sort (Union[Unset, None, str]):  Example: openDate:desc.

    Returns:
        Response[GetRepairOrdersResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        vin=vin,
        asset_id=asset_id,
        sort=sort,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    vin: Union[Unset, None, str] = UNSET,
    asset_id: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[GetRepairOrdersResponse200]:
    """Get repair orders for vehicle

    Args:
        vin (Union[Unset, None, str]):  Example: VINNUMBER123456.
        asset_id (Union[Unset, None, str]):  Example: 362846328238BASHD2N.
        sort (Union[Unset, None, str]):  Example: openDate:desc.

    Returns:
        Response[GetRepairOrdersResponse200]
    """

    return sync_detailed(
        client=client,
        vin=vin,
        asset_id=asset_id,
        sort=sort,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    vin: Union[Unset, None, str] = UNSET,
    asset_id: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Response[GetRepairOrdersResponse200]:
    """Get repair orders for vehicle

    Args:
        vin (Union[Unset, None, str]):  Example: VINNUMBER123456.
        asset_id (Union[Unset, None, str]):  Example: 362846328238BASHD2N.
        sort (Union[Unset, None, str]):  Example: openDate:desc.

    Returns:
        Response[GetRepairOrdersResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        vin=vin,
        asset_id=asset_id,
        sort=sort,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    vin: Union[Unset, None, str] = UNSET,
    asset_id: Union[Unset, None, str] = UNSET,
    sort: Union[Unset, None, str] = UNSET,
) -> Optional[GetRepairOrdersResponse200]:
    """Get repair orders for vehicle

    Args:
        vin (Union[Unset, None, str]):  Example: VINNUMBER123456.
        asset_id (Union[Unset, None, str]):  Example: 362846328238BASHD2N.
        sort (Union[Unset, None, str]):  Example: openDate:desc.

    Returns:
        Response[GetRepairOrdersResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            vin=vin,
            asset_id=asset_id,
            sort=sort,
        )
    ).parsed
