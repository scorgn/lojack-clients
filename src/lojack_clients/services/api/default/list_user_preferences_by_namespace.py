from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.list_user_preferences_by_namespace_namespace import ListUserPreferencesByNamespaceNamespace
from ...models.list_user_preferences_by_namespace_response_200 import ListUserPreferencesByNamespaceResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    namespace: ListUserPreferencesByNamespaceNamespace,
    *,
    client: Client,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Dict[str, Any]:
    url = "{}/preferences/{namespace}".format(client.base_url, namespace=namespace)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ListUserPreferencesByNamespaceResponse200]]:
    if response.status_code == 200:
        response_200 = ListUserPreferencesByNamespaceResponse200.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ListUserPreferencesByNamespaceResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    namespace: ListUserPreferencesByNamespaceNamespace,
    *,
    client: Client,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ListUserPreferencesByNamespaceResponse200]]:
    """List User Preferences By Namespace

    Args:
        namespace (ListUserPreferencesByNamespaceNamespace):
        limit (Union[Unset, None, int]): Limit of results to show Example: 100.
        offset (Union[Unset, None, int]): Result offset used for pagination

    Returns:
        Response[Union[Any, ListUserPreferencesByNamespaceResponse200]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        client=client,
        limit=limit,
        offset=offset,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    namespace: ListUserPreferencesByNamespaceNamespace,
    *,
    client: Client,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ListUserPreferencesByNamespaceResponse200]]:
    """List User Preferences By Namespace

    Args:
        namespace (ListUserPreferencesByNamespaceNamespace):
        limit (Union[Unset, None, int]): Limit of results to show Example: 100.
        offset (Union[Unset, None, int]): Result offset used for pagination

    Returns:
        Response[Union[Any, ListUserPreferencesByNamespaceResponse200]]
    """

    return sync_detailed(
        namespace=namespace,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    namespace: ListUserPreferencesByNamespaceNamespace,
    *,
    client: Client,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Response[Union[Any, ListUserPreferencesByNamespaceResponse200]]:
    """List User Preferences By Namespace

    Args:
        namespace (ListUserPreferencesByNamespaceNamespace):
        limit (Union[Unset, None, int]): Limit of results to show Example: 100.
        offset (Union[Unset, None, int]): Result offset used for pagination

    Returns:
        Response[Union[Any, ListUserPreferencesByNamespaceResponse200]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        client=client,
        limit=limit,
        offset=offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    namespace: ListUserPreferencesByNamespaceNamespace,
    *,
    client: Client,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
) -> Optional[Union[Any, ListUserPreferencesByNamespaceResponse200]]:
    """List User Preferences By Namespace

    Args:
        namespace (ListUserPreferencesByNamespaceNamespace):
        limit (Union[Unset, None, int]): Limit of results to show Example: 100.
        offset (Union[Unset, None, int]): Result offset used for pagination

    Returns:
        Response[Union[Any, ListUserPreferencesByNamespaceResponse200]]
    """

    return (
        await asyncio_detailed(
            namespace=namespace,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
