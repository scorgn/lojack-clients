from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_all_user_devices_response_200 import GetAllUserDevicesResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    serial_number: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/devices".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["id"] = id

    params["active"] = active

    params["serialNumber"] = serial_number

    params["type"] = type

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GetAllUserDevicesResponse200]]:
    if response.status_code == 200:
        response_200 = GetAllUserDevicesResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, GetAllUserDevicesResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    serial_number: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, GetAllUserDevicesResponse200]]:
    """Get all user devices

    Args:
        id (Union[Unset, None, str]): Device ID Example: 38261738B7DG937BXMQ3.
        active (Union[Unset, None, bool]):
        serial_number (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        limit (Union[Unset, None, int]): Limit of results to show Example: 100.
        offset (Union[Unset, None, int]): Result offset used for pagination

    Returns:
        Response[Union[Any, GetAllUserDevicesResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        id=id,
        active=active,
        serial_number=serial_number,
        type=type,
        limit=limit,
        offset=offset,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    serial_number: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, GetAllUserDevicesResponse200]]:
    """Get all user devices

    Args:
        id (Union[Unset, None, str]): Device ID Example: 38261738B7DG937BXMQ3.
        active (Union[Unset, None, bool]):
        serial_number (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        limit (Union[Unset, None, int]): Limit of results to show Example: 100.
        offset (Union[Unset, None, int]): Result offset used for pagination

    Returns:
        Response[Union[Any, GetAllUserDevicesResponse200]]
    """

    return sync_detailed(
        client=client,
        id=id,
        active=active,
        serial_number=serial_number,
        type=type,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    serial_number: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, GetAllUserDevicesResponse200]]:
    """Get all user devices

    Args:
        id (Union[Unset, None, str]): Device ID Example: 38261738B7DG937BXMQ3.
        active (Union[Unset, None, bool]):
        serial_number (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        limit (Union[Unset, None, int]): Limit of results to show Example: 100.
        offset (Union[Unset, None, int]): Result offset used for pagination

    Returns:
        Response[Union[Any, GetAllUserDevicesResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        id=id,
        active=active,
        serial_number=serial_number,
        type=type,
        limit=limit,
        offset=offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    serial_number: Union[Unset, None, str] = UNSET,
    type: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, GetAllUserDevicesResponse200]]:
    """Get all user devices

    Args:
        id (Union[Unset, None, str]): Device ID Example: 38261738B7DG937BXMQ3.
        active (Union[Unset, None, bool]):
        serial_number (Union[Unset, None, str]):
        type (Union[Unset, None, str]):
        limit (Union[Unset, None, int]): Limit of results to show Example: 100.
        offset (Union[Unset, None, int]): Result offset used for pagination

    Returns:
        Response[Union[Any, GetAllUserDevicesResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            active=active,
            serial_number=serial_number,
            type=type,
            limit=limit,
            offset=offset,
        )
    ).parsed
