from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.process_definition_paging import ProcessDefinitionPaging
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
    order_by: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
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

    params["where"] = where

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/process-definitions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProcessDefinitionPaging]]:
    if response.status_code == 200:
        response_200 = ProcessDefinitionPaging.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ProcessDefinitionPaging]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
    order_by: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ProcessDefinitionPaging]]:
    """List process definitions

     Gets a list of process definitions.

    In non-network deployments, any authenticated user will see all the
    process definitions.

    If networks are enabled, the network admin can only see the deployments
    in the given network.

    Args:
        skip_count (Union[Unset, int]):
        max_items (Union[Unset, int]):
        properties (Union[Unset, list[str]]):
        order_by (Union[Unset, list[str]]):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProcessDefinitionPaging]]
    """

    kwargs = _get_kwargs(
        skip_count=skip_count,
        max_items=max_items,
        properties=properties,
        order_by=order_by,
        where=where,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
    order_by: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ProcessDefinitionPaging]]:
    """List process definitions

     Gets a list of process definitions.

    In non-network deployments, any authenticated user will see all the
    process definitions.

    If networks are enabled, the network admin can only see the deployments
    in the given network.

    Args:
        skip_count (Union[Unset, int]):
        max_items (Union[Unset, int]):
        properties (Union[Unset, list[str]]):
        order_by (Union[Unset, list[str]]):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProcessDefinitionPaging]
    """

    return sync_detailed(
        client=client,
        skip_count=skip_count,
        max_items=max_items,
        properties=properties,
        order_by=order_by,
        where=where,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
    order_by: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
) -> Response[Union[Any, ProcessDefinitionPaging]]:
    """List process definitions

     Gets a list of process definitions.

    In non-network deployments, any authenticated user will see all the
    process definitions.

    If networks are enabled, the network admin can only see the deployments
    in the given network.

    Args:
        skip_count (Union[Unset, int]):
        max_items (Union[Unset, int]):
        properties (Union[Unset, list[str]]):
        order_by (Union[Unset, list[str]]):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProcessDefinitionPaging]]
    """

    kwargs = _get_kwargs(
        skip_count=skip_count,
        max_items=max_items,
        properties=properties,
        order_by=order_by,
        where=where,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
    order_by: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, ProcessDefinitionPaging]]:
    """List process definitions

     Gets a list of process definitions.

    In non-network deployments, any authenticated user will see all the
    process definitions.

    If networks are enabled, the network admin can only see the deployments
    in the given network.

    Args:
        skip_count (Union[Unset, int]):
        max_items (Union[Unset, int]):
        properties (Union[Unset, list[str]]):
        order_by (Union[Unset, list[str]]):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProcessDefinitionPaging]
    """

    return (
        await asyncio_detailed(
            client=client,
            skip_count=skip_count,
            max_items=max_items,
            properties=properties,
            order_by=order_by,
            where=where,
        )
    ).parsed
