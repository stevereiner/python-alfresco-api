from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.node_body_lock import NodeBodyLock
from ...models.node_entry import NodeEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    node_id: str,
    *,
    body: NodeBodyLock,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_include: Union[Unset, list[str]] = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/nodes/{node_id}/lock",
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
    body: NodeBodyLock,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, NodeEntry]]:
    """Lock a node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Places a lock on node **nodeId**.

    **Note:** you can only lock files. More specifically, a node can only be locked if it is
    of type `cm:content` or a subtype of `cm:content`.

    The lock is owned by the current user, and prevents other users or processes from making updates to
    the node until the lock is released.

    If the **timeToExpire** is not set or is zero, then the lock never expires.  Otherwise, the
    **timeToExpire** is the number of seconds before the lock expires.

    When a lock expires, the lock is released.

    If the node is already locked, and the user is the lock owner, then the lock is renewed with the new
    **timeToExpire**.

    By default, a lock is applied that allows the owner to update or delete the node.
    You can use **type** to change the lock type to one of the following:
    * **ALLOW_OWNER_CHANGES** (default) changes to the node can be made only by the lock owner. This
    enum is the same value as the deprecated WRITE_LOCK described in
    `org.alfresco.service.cmr.lock.LockType` in the Alfresco Public Java API. This is the default value.
    * **FULL** no changes by any user are allowed. This enum is the same value as the deprecated
    READ_ONLY_LOCK described in `org.alfresco.service.cmr.lock.LockType` in the Alfresco Public Java
    API.

    By default, a lock is persisted in the database. You can create a volatile in-memory lock by setting
    the **lifetime** property to EPHEMERAL.
    You might choose use EPHEMERAL locks, for example, if you are taking frequent short-term locks that
    you don't need
    to be kept over a restart of the repository. In this case you don't need the
    overhead of writing the locks to the database.

    If a lock on the node cannot be taken, then an error is returned.

    Args:
        node_id (str):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        body (NodeBodyLock):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NodeEntry]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        body=body,
        include=include,
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
    body: NodeBodyLock,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, NodeEntry]]:
    """Lock a node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Places a lock on node **nodeId**.

    **Note:** you can only lock files. More specifically, a node can only be locked if it is
    of type `cm:content` or a subtype of `cm:content`.

    The lock is owned by the current user, and prevents other users or processes from making updates to
    the node until the lock is released.

    If the **timeToExpire** is not set or is zero, then the lock never expires.  Otherwise, the
    **timeToExpire** is the number of seconds before the lock expires.

    When a lock expires, the lock is released.

    If the node is already locked, and the user is the lock owner, then the lock is renewed with the new
    **timeToExpire**.

    By default, a lock is applied that allows the owner to update or delete the node.
    You can use **type** to change the lock type to one of the following:
    * **ALLOW_OWNER_CHANGES** (default) changes to the node can be made only by the lock owner. This
    enum is the same value as the deprecated WRITE_LOCK described in
    `org.alfresco.service.cmr.lock.LockType` in the Alfresco Public Java API. This is the default value.
    * **FULL** no changes by any user are allowed. This enum is the same value as the deprecated
    READ_ONLY_LOCK described in `org.alfresco.service.cmr.lock.LockType` in the Alfresco Public Java
    API.

    By default, a lock is persisted in the database. You can create a volatile in-memory lock by setting
    the **lifetime** property to EPHEMERAL.
    You might choose use EPHEMERAL locks, for example, if you are taking frequent short-term locks that
    you don't need
    to be kept over a restart of the repository. In this case you don't need the
    overhead of writing the locks to the database.

    If a lock on the node cannot be taken, then an error is returned.

    Args:
        node_id (str):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        body (NodeBodyLock):

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
        include=include,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NodeBodyLock,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, NodeEntry]]:
    """Lock a node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Places a lock on node **nodeId**.

    **Note:** you can only lock files. More specifically, a node can only be locked if it is
    of type `cm:content` or a subtype of `cm:content`.

    The lock is owned by the current user, and prevents other users or processes from making updates to
    the node until the lock is released.

    If the **timeToExpire** is not set or is zero, then the lock never expires.  Otherwise, the
    **timeToExpire** is the number of seconds before the lock expires.

    When a lock expires, the lock is released.

    If the node is already locked, and the user is the lock owner, then the lock is renewed with the new
    **timeToExpire**.

    By default, a lock is applied that allows the owner to update or delete the node.
    You can use **type** to change the lock type to one of the following:
    * **ALLOW_OWNER_CHANGES** (default) changes to the node can be made only by the lock owner. This
    enum is the same value as the deprecated WRITE_LOCK described in
    `org.alfresco.service.cmr.lock.LockType` in the Alfresco Public Java API. This is the default value.
    * **FULL** no changes by any user are allowed. This enum is the same value as the deprecated
    READ_ONLY_LOCK described in `org.alfresco.service.cmr.lock.LockType` in the Alfresco Public Java
    API.

    By default, a lock is persisted in the database. You can create a volatile in-memory lock by setting
    the **lifetime** property to EPHEMERAL.
    You might choose use EPHEMERAL locks, for example, if you are taking frequent short-term locks that
    you don't need
    to be kept over a restart of the repository. In this case you don't need the
    overhead of writing the locks to the database.

    If a lock on the node cannot be taken, then an error is returned.

    Args:
        node_id (str):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        body (NodeBodyLock):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NodeEntry]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        body=body,
        include=include,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: NodeBodyLock,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, NodeEntry]]:
    """Lock a node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Places a lock on node **nodeId**.

    **Note:** you can only lock files. More specifically, a node can only be locked if it is
    of type `cm:content` or a subtype of `cm:content`.

    The lock is owned by the current user, and prevents other users or processes from making updates to
    the node until the lock is released.

    If the **timeToExpire** is not set or is zero, then the lock never expires.  Otherwise, the
    **timeToExpire** is the number of seconds before the lock expires.

    When a lock expires, the lock is released.

    If the node is already locked, and the user is the lock owner, then the lock is renewed with the new
    **timeToExpire**.

    By default, a lock is applied that allows the owner to update or delete the node.
    You can use **type** to change the lock type to one of the following:
    * **ALLOW_OWNER_CHANGES** (default) changes to the node can be made only by the lock owner. This
    enum is the same value as the deprecated WRITE_LOCK described in
    `org.alfresco.service.cmr.lock.LockType` in the Alfresco Public Java API. This is the default value.
    * **FULL** no changes by any user are allowed. This enum is the same value as the deprecated
    READ_ONLY_LOCK described in `org.alfresco.service.cmr.lock.LockType` in the Alfresco Public Java
    API.

    By default, a lock is persisted in the database. You can create a volatile in-memory lock by setting
    the **lifetime** property to EPHEMERAL.
    You might choose use EPHEMERAL locks, for example, if you are taking frequent short-term locks that
    you don't need
    to be kept over a restart of the repository. In this case you don't need the
    overhead of writing the locks to the database.

    If a lock on the node cannot be taken, then an error is returned.

    Args:
        node_id (str):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        body (NodeBodyLock):

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
            include=include,
            fields=fields,
        )
    ).parsed
