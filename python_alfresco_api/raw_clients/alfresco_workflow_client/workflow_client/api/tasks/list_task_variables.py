from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.variable_paging import VariablePaging
from ...types import UNSET, Response, Unset


def _get_kwargs(
    task_id: str,
    *,
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["skipCount"] = skip_count

    params["maxItems"] = max_items

    json_properties: Union[Unset, list[str]] = UNSET
    if not isinstance(properties, Unset):
        json_properties = properties

    params["properties"] = json_properties

    params["where"] = where

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/tasks/{task_id}/variables",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, VariablePaging]]:
    if response.status_code == 200:
        response_200 = VariablePaging.from_dict(response.json())

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
) -> Response[Union[Any, VariablePaging]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
) -> Response[Union[Any, VariablePaging]]:
    """List variables

     Gets a list of variables for the specified task **taskId**.

    An authenticated user will have access to a tasks variables if the
    user has started the process or if the user is involved in any of the
    process’s tasks.  In a network, only variables for a process that is
    inside the given network are returned.

    In non-network deployments, administrators can see all variables and
    perform all operations  on those variable. In network deployments,
    network administrators can see all variables in  their network and
    perform all operations on variables in their network.

    Args:
        task_id (str):
        skip_count (Union[Unset, int]):
        max_items (Union[Unset, int]):
        properties (Union[Unset, list[str]]):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VariablePaging]]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        skip_count=skip_count,
        max_items=max_items,
        properties=properties,
        where=where,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, VariablePaging]]:
    """List variables

     Gets a list of variables for the specified task **taskId**.

    An authenticated user will have access to a tasks variables if the
    user has started the process or if the user is involved in any of the
    process’s tasks.  In a network, only variables for a process that is
    inside the given network are returned.

    In non-network deployments, administrators can see all variables and
    perform all operations  on those variable. In network deployments,
    network administrators can see all variables in  their network and
    perform all operations on variables in their network.

    Args:
        task_id (str):
        skip_count (Union[Unset, int]):
        max_items (Union[Unset, int]):
        properties (Union[Unset, list[str]]):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VariablePaging]
    """

    return sync_detailed(
        task_id=task_id,
        client=client,
        skip_count=skip_count,
        max_items=max_items,
        properties=properties,
        where=where,
    ).parsed


async def asyncio_detailed(
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
) -> Response[Union[Any, VariablePaging]]:
    """List variables

     Gets a list of variables for the specified task **taskId**.

    An authenticated user will have access to a tasks variables if the
    user has started the process or if the user is involved in any of the
    process’s tasks.  In a network, only variables for a process that is
    inside the given network are returned.

    In non-network deployments, administrators can see all variables and
    perform all operations  on those variable. In network deployments,
    network administrators can see all variables in  their network and
    perform all operations on variables in their network.

    Args:
        task_id (str):
        skip_count (Union[Unset, int]):
        max_items (Union[Unset, int]):
        properties (Union[Unset, list[str]]):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VariablePaging]]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        skip_count=skip_count,
        max_items=max_items,
        properties=properties,
        where=where,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, VariablePaging]]:
    """List variables

     Gets a list of variables for the specified task **taskId**.

    An authenticated user will have access to a tasks variables if the
    user has started the process or if the user is involved in any of the
    process’s tasks.  In a network, only variables for a process that is
    inside the given network are returned.

    In non-network deployments, administrators can see all variables and
    perform all operations  on those variable. In network deployments,
    network administrators can see all variables in  their network and
    perform all operations on variables in their network.

    Args:
        task_id (str):
        skip_count (Union[Unset, int]):
        max_items (Union[Unset, int]):
        properties (Union[Unset, list[str]]):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VariablePaging]
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            client=client,
            skip_count=skip_count,
            max_items=max_items,
            properties=properties,
            where=where,
        )
    ).parsed
