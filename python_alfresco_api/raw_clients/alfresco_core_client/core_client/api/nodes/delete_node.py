from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    node_id: str,
    *,
    permanent: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["permanent"] = permanent

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/nodes/{node_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 204:
        return None
    if response.status_code == 400:
        return None
    if response.status_code == 401:
        return None
    if response.status_code == 403:
        return None
    if response.status_code == 404:
        return None
    if response.status_code == 409:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    permanent: Union[Unset, bool] = False,
) -> Response[Any]:
    """Delete a node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Deletes the node **nodeId**.

    If **nodeId** is a folder, then its children are also deleted.

    Deleted nodes move to the trashcan unless the **permanent** query parameter is **true** and the
    current user is the owner of the node or an admin.

    Deleting a node deletes it from its primary parent and also from any secondary parents. Peer
    associations are also deleted, where the deleted
    node is either a source or target of an association. This applies recursively to any hierarchy of
    primary children of the deleted node.

    **Note:** If the node is not permanently deleted, and is later successfully restored to its former
    primary parent, then the primary
    child association is restored. This applies recursively for any primary children. No other secondary
    child associations or
    peer associations are restored for any of the nodes in the primary parent-child hierarchy of
    restored nodes, regardless of whether the original
    associations were to nodes inside or outside the restored hierarchy.

    Args:
        node_id (str):
        permanent (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        permanent=permanent,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    permanent: Union[Unset, bool] = False,
) -> Response[Any]:
    """Delete a node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Deletes the node **nodeId**.

    If **nodeId** is a folder, then its children are also deleted.

    Deleted nodes move to the trashcan unless the **permanent** query parameter is **true** and the
    current user is the owner of the node or an admin.

    Deleting a node deletes it from its primary parent and also from any secondary parents. Peer
    associations are also deleted, where the deleted
    node is either a source or target of an association. This applies recursively to any hierarchy of
    primary children of the deleted node.

    **Note:** If the node is not permanently deleted, and is later successfully restored to its former
    primary parent, then the primary
    child association is restored. This applies recursively for any primary children. No other secondary
    child associations or
    peer associations are restored for any of the nodes in the primary parent-child hierarchy of
    restored nodes, regardless of whether the original
    associations were to nodes inside or outside the restored hierarchy.

    Args:
        node_id (str):
        permanent (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        permanent=permanent,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
