from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.deleted_node_body_restore import DeletedNodeBodyRestore
from ...models.node_entry import NodeEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    node_id: str,
    *,
    body: DeletedNodeBodyRestore,
    fields: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/deleted-nodes/{node_id}/restore",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, NodeEntry]]:
    if response.status_code == 200:
        response_200 = NodeEntry.from_dict(response.json())

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
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, NodeEntry]]:
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
    body: DeletedNodeBodyRestore,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, NodeEntry]]:
    """Restore a deleted node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Attempts to restore the deleted node **nodeId** to its original location or to a new location.

    If the node is successfully restored to its former primary parent, then only the
    primary child association will be restored, including recursively for any primary
    children. It should be noted that no other secondary child associations or peer
    associations will be restored, for any of the nodes within the primary parent-child
    hierarchy of restored nodes, irrespective of whether these associations were to
    nodes within or outside of the restored hierarchy.

    Also, any previously shared link will not be restored since it is deleted at the time
    of delete of each node.

    Args:
        node_id (str):
        fields (Union[Unset, list[str]]):
        body (DeletedNodeBodyRestore):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NodeEntry]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        body=body,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeletedNodeBodyRestore,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, NodeEntry]]:
    """Restore a deleted node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Attempts to restore the deleted node **nodeId** to its original location or to a new location.

    If the node is successfully restored to its former primary parent, then only the
    primary child association will be restored, including recursively for any primary
    children. It should be noted that no other secondary child associations or peer
    associations will be restored, for any of the nodes within the primary parent-child
    hierarchy of restored nodes, irrespective of whether these associations were to
    nodes within or outside of the restored hierarchy.

    Also, any previously shared link will not be restored since it is deleted at the time
    of delete of each node.

    Args:
        node_id (str):
        fields (Union[Unset, list[str]]):
        body (DeletedNodeBodyRestore):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NodeEntry]
    """

    return sync_detailed(
        node_id=node_id,
        client=client,
        body=body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeletedNodeBodyRestore,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, NodeEntry]]:
    """Restore a deleted node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Attempts to restore the deleted node **nodeId** to its original location or to a new location.

    If the node is successfully restored to its former primary parent, then only the
    primary child association will be restored, including recursively for any primary
    children. It should be noted that no other secondary child associations or peer
    associations will be restored, for any of the nodes within the primary parent-child
    hierarchy of restored nodes, irrespective of whether these associations were to
    nodes within or outside of the restored hierarchy.

    Also, any previously shared link will not be restored since it is deleted at the time
    of delete of each node.

    Args:
        node_id (str):
        fields (Union[Unset, list[str]]):
        body (DeletedNodeBodyRestore):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NodeEntry]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        body=body,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeletedNodeBodyRestore,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, NodeEntry]]:
    """Restore a deleted node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Attempts to restore the deleted node **nodeId** to its original location or to a new location.

    If the node is successfully restored to its former primary parent, then only the
    primary child association will be restored, including recursively for any primary
    children. It should be noted that no other secondary child associations or peer
    associations will be restored, for any of the nodes within the primary parent-child
    hierarchy of restored nodes, irrespective of whether these associations were to
    nodes within or outside of the restored hierarchy.

    Also, any previously shared link will not be restored since it is deleted at the time
    of delete of each node.

    Args:
        node_id (str):
        fields (Union[Unset, list[str]]):
        body (DeletedNodeBodyRestore):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NodeEntry]
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
            body=body,
            fields=fields,
        )
    ).parsed
