from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_all_user_assets_response_200 import GetAllUserAssetsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    color: Union[Unset, None, str] = UNSET,
    vin: Union[Unset, None, str] = UNSET,
    year: Union[Unset, None, str] = UNSET,
    make: Union[Unset, None, str] = UNSET,
    model: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/assets".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["id"] = id

    params["color"] = color

    params["vin"] = vin

    params["year"] = year

    params["make"] = make

    params["model"] = model

    params["status"] = status

    params["active"] = active

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GetAllUserAssetsResponse200]]:
    if response.status_code == 200:
        response_200 = GetAllUserAssetsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, GetAllUserAssetsResponse200]]:
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
    color: Union[Unset, None, str] = UNSET,
    vin: Union[Unset, None, str] = UNSET,
    year: Union[Unset, None, str] = UNSET,
    make: Union[Unset, None, str] = UNSET,
    model: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, GetAllUserAssetsResponse200]]:
    """Get all user assets

    Args:
        id (Union[Unset, None, str]): Asset ID Example: 272956057382HD3JBSD24.
        color (Union[Unset, None, str]):  Example: black.
        vin (Union[Unset, None, str]):  Example: VINNUMBER12345.
        year (Union[Unset, None, str]):  Example: 2022.
        make (Union[Unset, None, str]):  Example: Ford.
        model (Union[Unset, None, str]):  Example: Explorer.
        status (Union[Unset, None, str]):  Example: Stopped.
        active (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]): Limit of results to show Example: 100.
        offset (Union[Unset, None, int]): Result offset used for pagination

    Returns:
        Response[Union[Any, GetAllUserAssetsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        id=id,
        color=color,
        vin=vin,
        year=year,
        make=make,
        model=model,
        status=status,
        active=active,
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
    color: Union[Unset, None, str] = UNSET,
    vin: Union[Unset, None, str] = UNSET,
    year: Union[Unset, None, str] = UNSET,
    make: Union[Unset, None, str] = UNSET,
    model: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, GetAllUserAssetsResponse200]]:
    """Get all user assets

    Args:
        id (Union[Unset, None, str]): Asset ID Example: 272956057382HD3JBSD24.
        color (Union[Unset, None, str]):  Example: black.
        vin (Union[Unset, None, str]):  Example: VINNUMBER12345.
        year (Union[Unset, None, str]):  Example: 2022.
        make (Union[Unset, None, str]):  Example: Ford.
        model (Union[Unset, None, str]):  Example: Explorer.
        status (Union[Unset, None, str]):  Example: Stopped.
        active (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]): Limit of results to show Example: 100.
        offset (Union[Unset, None, int]): Result offset used for pagination

    Returns:
        Response[Union[Any, GetAllUserAssetsResponse200]]
    """

    return sync_detailed(
        client=client,
        id=id,
        color=color,
        vin=vin,
        year=year,
        make=make,
        model=model,
        status=status,
        active=active,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    id: Union[Unset, None, str] = UNSET,
    color: Union[Unset, None, str] = UNSET,
    vin: Union[Unset, None, str] = UNSET,
    year: Union[Unset, None, str] = UNSET,
    make: Union[Unset, None, str] = UNSET,
    model: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, GetAllUserAssetsResponse200]]:
    """Get all user assets

    Args:
        id (Union[Unset, None, str]): Asset ID Example: 272956057382HD3JBSD24.
        color (Union[Unset, None, str]):  Example: black.
        vin (Union[Unset, None, str]):  Example: VINNUMBER12345.
        year (Union[Unset, None, str]):  Example: 2022.
        make (Union[Unset, None, str]):  Example: Ford.
        model (Union[Unset, None, str]):  Example: Explorer.
        status (Union[Unset, None, str]):  Example: Stopped.
        active (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]): Limit of results to show Example: 100.
        offset (Union[Unset, None, int]): Result offset used for pagination

    Returns:
        Response[Union[Any, GetAllUserAssetsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        id=id,
        color=color,
        vin=vin,
        year=year,
        make=make,
        model=model,
        status=status,
        active=active,
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
    color: Union[Unset, None, str] = UNSET,
    vin: Union[Unset, None, str] = UNSET,
    year: Union[Unset, None, str] = UNSET,
    make: Union[Unset, None, str] = UNSET,
    model: Union[Unset, None, str] = UNSET,
    status: Union[Unset, None, str] = UNSET,
    active: Union[Unset, None, bool] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, GetAllUserAssetsResponse200]]:
    """Get all user assets

    Args:
        id (Union[Unset, None, str]): Asset ID Example: 272956057382HD3JBSD24.
        color (Union[Unset, None, str]):  Example: black.
        vin (Union[Unset, None, str]):  Example: VINNUMBER12345.
        year (Union[Unset, None, str]):  Example: 2022.
        make (Union[Unset, None, str]):  Example: Ford.
        model (Union[Unset, None, str]):  Example: Explorer.
        status (Union[Unset, None, str]):  Example: Stopped.
        active (Union[Unset, None, bool]):
        limit (Union[Unset, None, int]): Limit of results to show Example: 100.
        offset (Union[Unset, None, int]): Result offset used for pagination

    Returns:
        Response[Union[Any, GetAllUserAssetsResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            color=color,
            vin=vin,
            year=year,
            make=make,
            model=model,
            status=status,
            active=active,
            limit=limit,
            offset=offset,
        )
    ).parsed
