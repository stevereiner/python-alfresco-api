from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deleted_node_entry import DeletedNodeEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    node_id: str,
    *,
    include: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_include: Union[Unset, list[str]] = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/deleted-nodes/{node_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, DeletedNodeEntry]]:
    if response.status_code == 200:
        response_200 = DeletedNodeEntry.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, DeletedNodeEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, DeletedNodeEntry]]:
    """Get a deleted node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets the specific deleted node **nodeId**.

    Args:
        node_id (str):
        include (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeletedNodeEntry]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, DeletedNodeEntry]]:
    """Get a deleted node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets the specific deleted node **nodeId**.

    Args:
        node_id (str):
        include (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeletedNodeEntry]
    """

    return sync_detailed(
        node_id=node_id,
        client=client,
        include=include,
    ).parsed


async def asyncio_detailed(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, DeletedNodeEntry]]:
    """Get a deleted node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets the specific deleted node **nodeId**.

    Args:
        node_id (str):
        include (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DeletedNodeEntry]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    include: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, DeletedNodeEntry]]:
    """Get a deleted node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets the specific deleted node **nodeId**.

    Args:
        node_id (str):
        include (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DeletedNodeEntry]
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
            include=include,
        )
    ).parsed
