from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.command_request_json_body import CommandRequestJsonBody
from ...models.command_request_response_201 import CommandRequestResponse201
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: CommandRequestJsonBody,
) -> Dict[str, Any]:
    url = "{}/commandRequests".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, CommandRequestResponse201]]:
    if response.status_code == 201:
        response_201 = CommandRequestResponse201.from_dict(response.json())

        return response_201
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, CommandRequestResponse201]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CommandRequestJsonBody,
) -> Response[Union[Any, CommandRequestResponse201]]:
    """Command request

    Args:
        json_body (CommandRequestJsonBody):

    Returns:
        Response[Union[Any, CommandRequestResponse201]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: CommandRequestJsonBody,
) -> Optional[Union[Any, CommandRequestResponse201]]:
    """Command request

    Args:
        json_body (CommandRequestJsonBody):

    Returns:
        Response[Union[Any, CommandRequestResponse201]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CommandRequestJsonBody,
) -> Response[Union[Any, CommandRequestResponse201]]:
    """Command request

    Args:
        json_body (CommandRequestJsonBody):

    Returns:
        Response[Union[Any, CommandRequestResponse201]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CommandRequestJsonBody,
) -> Optional[Union[Any, CommandRequestResponse201]]:
    """Command request

    Args:
        json_body (CommandRequestJsonBody):

    Returns:
        Response[Union[Any, CommandRequestResponse201]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
