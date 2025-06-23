from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deleted_nodes_paging import DeletedNodesPaging
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    include: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["skipCount"] = skip_count

    params["maxItems"] = max_items

    json_include: Union[Unset, list[str]] = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/deleted-nodes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DeletedNodesPaging]]:
    if response.status_code == 200:
        response_200 = DeletedNodesPaging.from_dict(response.json())

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
) -> Response[Union[Any, DeletedNodesPaging]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    include: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, DeletedNodesPaging]]:
    """List deleted nodes

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets a list of deleted nodes for the current user.

    If the current user is an administrator deleted nodes for all users will be returned.

    The list of deleted nodes will be ordered with the most recently deleted node at the top of the
    list.

    Args:
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        include (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeletedNodesPaging]]
    """

    kwargs = _get_kwargs(
        skip_count=skip_count,
        max_items=max_items,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    include: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, DeletedNodesPaging]]:
    """List deleted nodes

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets a list of deleted nodes for the current user.

    If the current user is an administrator deleted nodes for all users will be returned.

    The list of deleted nodes will be ordered with the most recently deleted node at the top of the
    list.

    Args:
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        include (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeletedNodesPaging]
    """

    return sync_detailed(
        client=client,
        skip_count=skip_count,
        max_items=max_items,
        include=include,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    include: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, DeletedNodesPaging]]:
    """List deleted nodes

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets a list of deleted nodes for the current user.

    If the current user is an administrator deleted nodes for all users will be returned.

    The list of deleted nodes will be ordered with the most recently deleted node at the top of the
    list.

    Args:
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        include (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeletedNodesPaging]]
    """

    kwargs = _get_kwargs(
        skip_count=skip_count,
        max_items=max_items,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    include: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, DeletedNodesPaging]]:
    """List deleted nodes

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets a list of deleted nodes for the current user.

    If the current user is an administrator deleted nodes for all users will be returned.

    The list of deleted nodes will be ordered with the most recently deleted node at the top of the
    list.

    Args:
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        include (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeletedNodesPaging]
    """

    return (
        await asyncio_detailed(
            client=client,
            skip_count=skip_count,
            max_items=max_items,
            include=include,
        )
    ).parsed
