from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.process_entry import ProcessEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    process_id: str,
    *,
    properties: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_properties: Union[Unset, list[str]] = UNSET
    if not isinstance(properties, Unset):
        json_properties = properties

    params["properties"] = json_properties

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/processes/{process_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProcessEntry]]:
    if response.status_code == 200:
        response_200 = ProcessEntry.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ProcessEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    process_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    properties: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, ProcessEntry]]:
    """Get a process

     Gets the process identified by **processId**.

    An authenticated user will have access to a process if the user has
    started the process or if the user is involved in any of the process’s
    tasks. In a network, only processes that are inside the given network are
    returned.

    In non-network deployments, administrators can see all processes and
    perform all operations on tasks. In network deployments, network
    administrators can see all processes in their network and perform all
    operations on tasks in their network.

    Args:
        process_id (str):
        properties (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProcessEntry]]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
        properties=properties,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    process_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    properties: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, ProcessEntry]]:
    """Get a process

     Gets the process identified by **processId**.

    An authenticated user will have access to a process if the user has
    started the process or if the user is involved in any of the process’s
    tasks. In a network, only processes that are inside the given network are
    returned.

    In non-network deployments, administrators can see all processes and
    perform all operations on tasks. In network deployments, network
    administrators can see all processes in their network and perform all
    operations on tasks in their network.

    Args:
        process_id (str):
        properties (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProcessEntry]
    """

    return sync_detailed(
        process_id=process_id,
        client=client,
        properties=properties,
    ).parsed


async def asyncio_detailed(
    process_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    properties: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, ProcessEntry]]:
    """Get a process

     Gets the process identified by **processId**.

    An authenticated user will have access to a process if the user has
    started the process or if the user is involved in any of the process’s
    tasks. In a network, only processes that are inside the given network are
    returned.

    In non-network deployments, administrators can see all processes and
    perform all operations on tasks. In network deployments, network
    administrators can see all processes in their network and perform all
    operations on tasks in their network.

    Args:
        process_id (str):
        properties (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProcessEntry]]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
        properties=properties,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    process_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    properties: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, ProcessEntry]]:
    """Get a process

     Gets the process identified by **processId**.

    An authenticated user will have access to a process if the user has
    started the process or if the user is involved in any of the process’s
    tasks. In a network, only processes that are inside the given network are
    returned.

    In non-network deployments, administrators can see all processes and
    perform all operations on tasks. In network deployments, network
    administrators can see all processes in their network and perform all
    operations on tasks in their network.

    Args:
        process_id (str):
        properties (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProcessEntry]
    """

    return (
        await asyncio_detailed(
            process_id=process_id,
            client=client,
            properties=properties,
        )
    ).parsed
