from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_terms_of_service_response_200 import GetTermsOfServiceResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/sass".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GetTermsOfServiceResponse200]]:
    if response.status_code == 200:
        response_200 = GetTermsOfServiceResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, GetTermsOfServiceResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, GetTermsOfServiceResponse200]]:
    """Get terms of service

    Returns:
        Response[Union[Any, GetTermsOfServiceResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[Any, GetTermsOfServiceResponse200]]:
    """Get terms of service

    Returns:
        Response[Union[Any, GetTermsOfServiceResponse200]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, GetTermsOfServiceResponse200]]:
    """Get terms of service

    Returns:
        Response[Union[Any, GetTermsOfServiceResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[Any, GetTermsOfServiceResponse200]]:
    """Get terms of service

    Returns:
        Response[Union[Any, GetTermsOfServiceResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
