from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.asset import Asset
from ...models.update_asset_json_body import UpdateAssetJsonBody
from ...types import Response


def _get_kwargs(
    id: str,
    *,
    client: Client,
    json_body: UpdateAssetJsonBody,
) -> Dict[str, Any]:
    url = "{}/assets/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Asset]]:
    if response.status_code == 200:
        response_200 = Asset.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Asset]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: Client,
    json_body: UpdateAssetJsonBody,
) -> Response[Union[Any, Asset]]:
    """Update asset

    Args:
        id (str): Asset ID Example: 272956057382HD3JBSD24.
        json_body (UpdateAssetJsonBody):

    Returns:
        Response[Union[Any, Asset]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: Client,
    json_body: UpdateAssetJsonBody,
) -> Optional[Union[Any, Asset]]:
    """Update asset

    Args:
        id (str): Asset ID Example: 272956057382HD3JBSD24.
        json_body (UpdateAssetJsonBody):

    Returns:
        Response[Union[Any, Asset]]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    json_body: UpdateAssetJsonBody,
) -> Response[Union[Any, Asset]]:
    """Update asset

    Args:
        id (str): Asset ID Example: 272956057382HD3JBSD24.
        json_body (UpdateAssetJsonBody):

    Returns:
        Response[Union[Any, Asset]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    json_body: UpdateAssetJsonBody,
) -> Optional[Union[Any, Asset]]:
    """Update asset

    Args:
        id (str): Asset ID Example: 272956057382HD3JBSD24.
        json_body (UpdateAssetJsonBody):

    Returns:
        Response[Union[Any, Asset]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
        )
    ).parsed
