from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_specific_user_preferences_namespace import GetSpecificUserPreferencesNamespace
from ...models.preference import Preference
from ...models.preference_key import PreferenceKey
from ...types import Response


def _get_kwargs(
    namespace: GetSpecificUserPreferencesNamespace,
    config: PreferenceKey,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/preferences/{namespace}/{config}".format(client.base_url, namespace=namespace, config=config)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Preference]]:
    if response.status_code == 200:
        response_200 = Preference.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Preference]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    namespace: GetSpecificUserPreferencesNamespace,
    config: PreferenceKey,
    *,
    client: Client,
) -> Response[Union[Any, Preference]]:
    """Get Specific User Preferences

    Args:
        namespace (GetSpecificUserPreferencesNamespace):
        config (PreferenceKey):

    Returns:
        Response[Union[Any, Preference]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        config=config,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    namespace: GetSpecificUserPreferencesNamespace,
    config: PreferenceKey,
    *,
    client: Client,
) -> Optional[Union[Any, Preference]]:
    """Get Specific User Preferences

    Args:
        namespace (GetSpecificUserPreferencesNamespace):
        config (PreferenceKey):

    Returns:
        Response[Union[Any, Preference]]
    """

    return sync_detailed(
        namespace=namespace,
        config=config,
        client=client,
    ).parsed


async def asyncio_detailed(
    namespace: GetSpecificUserPreferencesNamespace,
    config: PreferenceKey,
    *,
    client: Client,
) -> Response[Union[Any, Preference]]:
    """Get Specific User Preferences

    Args:
        namespace (GetSpecificUserPreferencesNamespace):
        config (PreferenceKey):

    Returns:
        Response[Union[Any, Preference]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        config=config,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    namespace: GetSpecificUserPreferencesNamespace,
    config: PreferenceKey,
    *,
    client: Client,
) -> Optional[Union[Any, Preference]]:
    """Get Specific User Preferences

    Args:
        namespace (GetSpecificUserPreferencesNamespace):
        config (PreferenceKey):

    Returns:
        Response[Union[Any, Preference]]
    """

    return (
        await asyncio_detailed(
            namespace=namespace,
            config=config,
            client=client,
        )
    ).parsed
