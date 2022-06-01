from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.event_type import EventType
from ...models.list_all_events_response_200 import ListAllEventsResponse200
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: Client,
    type: Union[Unset, None, List[EventType]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    start_date: Union[Unset, None, str] = UNSET,
    end_date: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/assets/{id}/events".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    json_type: Union[Unset, None, List[str]] = UNSET
    if not isinstance(type, Unset):
        if type is None:
            json_type = None
        else:
            json_type = []
            for type_item_data in type:
                type_item = type_item_data.value

                json_type.append(type_item)

    params["type"] = json_type

    params["limit"] = limit

    params["offset"] = offset

    params["startDate"] = start_date

    params["endDate"] = end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, ListAllEventsResponse200]]:
    if response.status_code == 200:
        response_200 = ListAllEventsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, ListAllEventsResponse200]]:
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
    type: Union[Unset, None, List[EventType]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    start_date: Union[Unset, None, str] = UNSET,
    end_date: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ListAllEventsResponse200]]:
    """List All Events

    Args:
        id (str): Asset ID Example: 272956057382HD3JBSD24.
        type (Union[Unset, None, List[EventType]]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        start_date (Union[Unset, None, str]):  Example: 2022-05-10T03:59:59.999+0000.
        end_date (Union[Unset, None, str]):  Example: 2022-05-10T03:59:59.999+0000.

    Returns:
        Response[Union[Any, ListAllEventsResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        type=type,
        limit=limit,
        offset=offset,
        start_date=start_date,
        end_date=end_date,
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
    type: Union[Unset, None, List[EventType]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    start_date: Union[Unset, None, str] = UNSET,
    end_date: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ListAllEventsResponse200]]:
    """List All Events

    Args:
        id (str): Asset ID Example: 272956057382HD3JBSD24.
        type (Union[Unset, None, List[EventType]]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        start_date (Union[Unset, None, str]):  Example: 2022-05-10T03:59:59.999+0000.
        end_date (Union[Unset, None, str]):  Example: 2022-05-10T03:59:59.999+0000.

    Returns:
        Response[Union[Any, ListAllEventsResponse200]]
    """

    return sync_detailed(
        id=id,
        client=client,
        type=type,
        limit=limit,
        offset=offset,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: Client,
    type: Union[Unset, None, List[EventType]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    start_date: Union[Unset, None, str] = UNSET,
    end_date: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, ListAllEventsResponse200]]:
    """List All Events

    Args:
        id (str): Asset ID Example: 272956057382HD3JBSD24.
        type (Union[Unset, None, List[EventType]]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        start_date (Union[Unset, None, str]):  Example: 2022-05-10T03:59:59.999+0000.
        end_date (Union[Unset, None, str]):  Example: 2022-05-10T03:59:59.999+0000.

    Returns:
        Response[Union[Any, ListAllEventsResponse200]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        type=type,
        limit=limit,
        offset=offset,
        start_date=start_date,
        end_date=end_date,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: Client,
    type: Union[Unset, None, List[EventType]] = UNSET,
    limit: Union[Unset, None, int] = UNSET,
    offset: Union[Unset, None, int] = UNSET,
    start_date: Union[Unset, None, str] = UNSET,
    end_date: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, ListAllEventsResponse200]]:
    """List All Events

    Args:
        id (str): Asset ID Example: 272956057382HD3JBSD24.
        type (Union[Unset, None, List[EventType]]):
        limit (Union[Unset, None, int]):
        offset (Union[Unset, None, int]):
        start_date (Union[Unset, None, str]):  Example: 2022-05-10T03:59:59.999+0000.
        end_date (Union[Unset, None, str]):  Example: 2022-05-10T03:59:59.999+0000.

    Returns:
        Response[Union[Any, ListAllEventsResponse200]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            type=type,
            limit=limit,
            offset=offset,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
