from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.geofence import Geofence
from ...types import Response


def _get_kwargs(
    id: str,
    geofence_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/assets/{id}/geofences/{geofence_id}".format(client.base_url, id=id, geofence_id=geofence_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Geofence]]:
    if response.status_code == 200:
        response_200 = Geofence.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Geofence]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    geofence_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Geofence]]:
    """Get Single Geofences

    Args:
        id (str): Asset ID Example: 272956057382HD3JBSD24.
        geofence_id (str):  Example: 1140762987615GIDWGA.

    Returns:
        Response[Union[Any, Geofence]]
    """

    kwargs = _get_kwargs(
        id=id,
        geofence_id=geofence_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    geofence_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Geofence]]:
    """Get Single Geofences

    Args:
        id (str): Asset ID Example: 272956057382HD3JBSD24.
        geofence_id (str):  Example: 1140762987615GIDWGA.

    Returns:
        Response[Union[Any, Geofence]]
    """

    return sync_detailed(
        id=id,
        geofence_id=geofence_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    id: str,
    geofence_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Geofence]]:
    """Get Single Geofences

    Args:
        id (str): Asset ID Example: 272956057382HD3JBSD24.
        geofence_id (str):  Example: 1140762987615GIDWGA.

    Returns:
        Response[Union[Any, Geofence]]
    """

    kwargs = _get_kwargs(
        id=id,
        geofence_id=geofence_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    geofence_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Geofence]]:
    """Get Single Geofences

    Args:
        id (str): Asset ID Example: 272956057382HD3JBSD24.
        geofence_id (str):  Example: 1140762987615GIDWGA.

    Returns:
        Response[Union[Any, Geofence]]
    """

    return (
        await asyncio_detailed(
            id=id,
            geofence_id=geofence_id,
            client=client,
        )
    ).parsed
