from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.task_paging import TaskPaging
from ...types import UNSET, Response, Unset


def _get_kwargs(
    process_id: str,
    *,
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
    order_by: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["skipCount"] = skip_count

    params["maxItems"] = max_items

    json_properties: Union[Unset, list[str]] = UNSET
    if not isinstance(properties, Unset):
        json_properties = properties

    params["properties"] = json_properties

    json_order_by: Union[Unset, list[str]] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by

    params["orderBy"] = json_order_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/processes/{process_id}/tasks",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, TaskPaging]]:
    if response.status_code == 200:
        response_200 = TaskPaging.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
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
) -> Response[Union[Any, TaskPaging]]:
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
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
    order_by: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, TaskPaging]]:
    """List tasks for a process

     Gets a list of tasks for the specified process **processId**.

    An authenticated user will have access to a processes tasks if the
    user has started the process or if the user is involved in any of the
    process’s tasks.  In a network, only tasks for a process that is
    inside the given network are returned.

    In non-network deployments, administrators can see all tasks and
    perform all operations  on those tasks. In network deployments,
    network administrators can see all tasks in their network and
    perform all operations on tasks in their network.

    Args:
        process_id (str):
        skip_count (Union[Unset, int]):
        max_items (Union[Unset, int]):
        properties (Union[Unset, list[str]]):
        order_by (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TaskPaging]]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
        skip_count=skip_count,
        max_items=max_items,
        properties=properties,
        order_by=order_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    process_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
    order_by: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, TaskPaging]]:
    """List tasks for a process

     Gets a list of tasks for the specified process **processId**.

    An authenticated user will have access to a processes tasks if the
    user has started the process or if the user is involved in any of the
    process’s tasks.  In a network, only tasks for a process that is
    inside the given network are returned.

    In non-network deployments, administrators can see all tasks and
    perform all operations  on those tasks. In network deployments,
    network administrators can see all tasks in their network and
    perform all operations on tasks in their network.

    Args:
        process_id (str):
        skip_count (Union[Unset, int]):
        max_items (Union[Unset, int]):
        properties (Union[Unset, list[str]]):
        order_by (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TaskPaging]
    """

    return sync_detailed(
        process_id=process_id,
        client=client,
        skip_count=skip_count,
        max_items=max_items,
        properties=properties,
        order_by=order_by,
    ).parsed


async def asyncio_detailed(
    process_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
    order_by: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, TaskPaging]]:
    """List tasks for a process

     Gets a list of tasks for the specified process **processId**.

    An authenticated user will have access to a processes tasks if the
    user has started the process or if the user is involved in any of the
    process’s tasks.  In a network, only tasks for a process that is
    inside the given network are returned.

    In non-network deployments, administrators can see all tasks and
    perform all operations  on those tasks. In network deployments,
    network administrators can see all tasks in their network and
    perform all operations on tasks in their network.

    Args:
        process_id (str):
        skip_count (Union[Unset, int]):
        max_items (Union[Unset, int]):
        properties (Union[Unset, list[str]]):
        order_by (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TaskPaging]]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
        skip_count=skip_count,
        max_items=max_items,
        properties=properties,
        order_by=order_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    process_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
    order_by: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, TaskPaging]]:
    """List tasks for a process

     Gets a list of tasks for the specified process **processId**.

    An authenticated user will have access to a processes tasks if the
    user has started the process or if the user is involved in any of the
    process’s tasks.  In a network, only tasks for a process that is
    inside the given network are returned.

    In non-network deployments, administrators can see all tasks and
    perform all operations  on those tasks. In network deployments,
    network administrators can see all tasks in their network and
    perform all operations on tasks in their network.

    Args:
        process_id (str):
        skip_count (Union[Unset, int]):
        max_items (Union[Unset, int]):
        properties (Union[Unset, list[str]]):
        order_by (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TaskPaging]
    """

    return (
        await asyncio_detailed(
            process_id=process_id,
            client=client,
            skip_count=skip_count,
            max_items=max_items,
            properties=properties,
            order_by=order_by,
        )
    ).parsed
