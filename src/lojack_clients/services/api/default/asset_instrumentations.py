from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.asset_instrumentations_response_200 import AssetInstrumentationsResponse200
from ...types import Response


def _get_kwargs(
    asset_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/instrumentations/{asset_id}".format(client.base_url, asset_id=asset_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, AssetInstrumentationsResponse200]]:
    if response.status_code == 200:
        response_200 = AssetInstrumentationsResponse200.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, AssetInstrumentationsResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    asset_id: str,
    *,
    client: Client,
) -> Response[Union[Any, AssetInstrumentationsResponse200]]:
    """Asset instrumentations

    Args:
        asset_id (str): Asset ID Example: 272956057382HD3JBSD24.

    Returns:
        Response[Union[Any, AssetInstrumentationsResponse200]]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    asset_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, AssetInstrumentationsResponse200]]:
    """Asset instrumentations

    Args:
        asset_id (str): Asset ID Example: 272956057382HD3JBSD24.

    Returns:
        Response[Union[Any, AssetInstrumentationsResponse200]]
    """

    return sync_detailed(
        asset_id=asset_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    asset_id: str,
    *,
    client: Client,
) -> Response[Union[Any, AssetInstrumentationsResponse200]]:
    """Asset instrumentations

    Args:
        asset_id (str): Asset ID Example: 272956057382HD3JBSD24.

    Returns:
        Response[Union[Any, AssetInstrumentationsResponse200]]
    """

    kwargs = _get_kwargs(
        asset_id=asset_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    asset_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, AssetInstrumentationsResponse200]]:
    """Asset instrumentations

    Args:
        asset_id (str): Asset ID Example: 272956057382HD3JBSD24.

    Returns:
        Response[Union[Any, AssetInstrumentationsResponse200]]
    """

    return (
        await asyncio_detailed(
            asset_id=asset_id,
            client=client,
        )
    ).parsed
