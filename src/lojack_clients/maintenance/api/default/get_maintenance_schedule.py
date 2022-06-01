from typing import Any, Dict, Optional

import httpx

from ...client import Client
from ...models.get_maintenance_schedule_response_200 import GetMaintenanceScheduleResponse200
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    vin: str,
) -> Dict[str, Any]:
    url = "{}/automotive/maintenanceSchedule".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["vin"] = vin

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[GetMaintenanceScheduleResponse200]:
    if response.status_code == 200:
        response_200 = GetMaintenanceScheduleResponse200.from_dict(response.json())

        return response_200
    return None


def _build_response(*, response: httpx.Response) -> Response[GetMaintenanceScheduleResponse200]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    vin: str,
) -> Response[GetMaintenanceScheduleResponse200]:
    """Get maintenance schedule for vehicle by VIN

    Args:
        vin (str):  Example: VINNUMBER123456.

    Returns:
        Response[GetMaintenanceScheduleResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        vin=vin,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    vin: str,
) -> Optional[GetMaintenanceScheduleResponse200]:
    """Get maintenance schedule for vehicle by VIN

    Args:
        vin (str):  Example: VINNUMBER123456.

    Returns:
        Response[GetMaintenanceScheduleResponse200]
    """

    return sync_detailed(
        client=client,
        vin=vin,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    vin: str,
) -> Response[GetMaintenanceScheduleResponse200]:
    """Get maintenance schedule for vehicle by VIN

    Args:
        vin (str):  Example: VINNUMBER123456.

    Returns:
        Response[GetMaintenanceScheduleResponse200]
    """

    kwargs = _get_kwargs(
        client=client,
        vin=vin,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    vin: str,
) -> Optional[GetMaintenanceScheduleResponse200]:
    """Get maintenance schedule for vehicle by VIN

    Args:
        vin (str):  Example: VINNUMBER123456.

    Returns:
        Response[GetMaintenanceScheduleResponse200]
    """

    return (
        await asyncio_detailed(
            client=client,
            vin=vin,
        )
    ).parsed
