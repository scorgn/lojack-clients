from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.preference import Preference
from ...models.preference_key import PreferenceKey
from ...models.update_specific_user_preferences_namespace import UpdateSpecificUserPreferencesNamespace
from ...types import Response


def _get_kwargs(
    namespace: UpdateSpecificUserPreferencesNamespace,
    config: PreferenceKey,
    *,
    client: Client,
    json_body: Preference,
) -> Dict[str, Any]:
    url = "{}/preferences/{namespace}/{config}".format(client.base_url, namespace=namespace, config=config)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Preference]]:
    if response.status_code == 200:
        response_200 = Preference.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Preference]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    namespace: UpdateSpecificUserPreferencesNamespace,
    config: PreferenceKey,
    *,
    client: Client,
    json_body: Preference,
) -> Response[Union[Any, Preference]]:
    """Update Specific User Preferences

    Args:
        namespace (UpdateSpecificUserPreferencesNamespace):
        config (PreferenceKey):
        json_body (Preference):

    Returns:
        Response[Union[Any, Preference]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        config=config,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    namespace: UpdateSpecificUserPreferencesNamespace,
    config: PreferenceKey,
    *,
    client: Client,
    json_body: Preference,
) -> Optional[Union[Any, Preference]]:
    """Update Specific User Preferences

    Args:
        namespace (UpdateSpecificUserPreferencesNamespace):
        config (PreferenceKey):
        json_body (Preference):

    Returns:
        Response[Union[Any, Preference]]
    """

    return sync_detailed(
        namespace=namespace,
        config=config,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    namespace: UpdateSpecificUserPreferencesNamespace,
    config: PreferenceKey,
    *,
    client: Client,
    json_body: Preference,
) -> Response[Union[Any, Preference]]:
    """Update Specific User Preferences

    Args:
        namespace (UpdateSpecificUserPreferencesNamespace):
        config (PreferenceKey):
        json_body (Preference):

    Returns:
        Response[Union[Any, Preference]]
    """

    kwargs = _get_kwargs(
        namespace=namespace,
        config=config,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    namespace: UpdateSpecificUserPreferencesNamespace,
    config: PreferenceKey,
    *,
    client: Client,
    json_body: Preference,
) -> Optional[Union[Any, Preference]]:
    """Update Specific User Preferences

    Args:
        namespace (UpdateSpecificUserPreferencesNamespace):
        config (PreferenceKey):
        json_body (Preference):

    Returns:
        Response[Union[Any, Preference]]
    """

    return (
        await asyncio_detailed(
            namespace=namespace,
            config=config,
            client=client,
            json_body=json_body,
        )
    ).parsed
