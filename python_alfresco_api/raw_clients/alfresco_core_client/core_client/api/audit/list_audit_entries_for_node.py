from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_entry_paging import AuditEntryPaging
from ...types import UNSET, Response, Unset


def _get_kwargs(
    node_id: str,
    *,
    skip_count: Union[Unset, int] = 0,
    order_by: Union[Unset, list[str]] = UNSET,
    max_items: Union[Unset, int] = 100,
    where: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["skipCount"] = skip_count

    json_order_by: Union[Unset, list[str]] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by

    params["orderBy"] = json_order_by

    params["maxItems"] = max_items

    params["where"] = where

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
        "method": "get",
        "url": f"/nodes/{node_id}/audit-entries",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, AuditEntryPaging]]:
    if response.status_code == 200:
        response_200 = AuditEntryPaging.from_dict(response.json())

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
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, AuditEntryPaging]]:
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
    skip_count: Union[Unset, int] = 0,
    order_by: Union[Unset, list[str]] = UNSET,
    max_items: Union[Unset, int] = 100,
    where: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, AuditEntryPaging]]:
    """List audit entries for a node

     **Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.

    Gets a list of audit entries for node **nodeId**.

    The list can be filtered by **createdByUser** and for a given inclusive time period.

    The default sort order is **createdAt** ascending, but you can use an optional **ASC** or **DESC**
    modifier to specify an ascending or descending sort order.

    For example, specifying ```orderBy=createdAt DESC``` returns audit entries in descending
    **createdAt** order.

    This relies on the pre-configured 'alfresco-access' audit application.

    Args:
        node_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        order_by (Union[Unset, list[str]]):
        max_items (Union[Unset, int]):  Default: 100.
        where (Union[Unset, str]):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AuditEntryPaging]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        skip_count=skip_count,
        order_by=order_by,
        max_items=max_items,
        where=where,
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
    skip_count: Union[Unset, int] = 0,
    order_by: Union[Unset, list[str]] = UNSET,
    max_items: Union[Unset, int] = 100,
    where: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, AuditEntryPaging]]:
    """List audit entries for a node

     **Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.

    Gets a list of audit entries for node **nodeId**.

    The list can be filtered by **createdByUser** and for a given inclusive time period.

    The default sort order is **createdAt** ascending, but you can use an optional **ASC** or **DESC**
    modifier to specify an ascending or descending sort order.

    For example, specifying ```orderBy=createdAt DESC``` returns audit entries in descending
    **createdAt** order.

    This relies on the pre-configured 'alfresco-access' audit application.

    Args:
        node_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        order_by (Union[Unset, list[str]]):
        max_items (Union[Unset, int]):  Default: 100.
        where (Union[Unset, str]):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AuditEntryPaging]
    """

    return sync_detailed(
        node_id=node_id,
        client=client,
        skip_count=skip_count,
        order_by=order_by,
        max_items=max_items,
        where=where,
        include=include,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    order_by: Union[Unset, list[str]] = UNSET,
    max_items: Union[Unset, int] = 100,
    where: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, AuditEntryPaging]]:
    """List audit entries for a node

     **Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.

    Gets a list of audit entries for node **nodeId**.

    The list can be filtered by **createdByUser** and for a given inclusive time period.

    The default sort order is **createdAt** ascending, but you can use an optional **ASC** or **DESC**
    modifier to specify an ascending or descending sort order.

    For example, specifying ```orderBy=createdAt DESC``` returns audit entries in descending
    **createdAt** order.

    This relies on the pre-configured 'alfresco-access' audit application.

    Args:
        node_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        order_by (Union[Unset, list[str]]):
        max_items (Union[Unset, int]):  Default: 100.
        where (Union[Unset, str]):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AuditEntryPaging]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        skip_count=skip_count,
        order_by=order_by,
        max_items=max_items,
        where=where,
        include=include,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    order_by: Union[Unset, list[str]] = UNSET,
    max_items: Union[Unset, int] = 100,
    where: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, AuditEntryPaging]]:
    """List audit entries for a node

     **Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.

    Gets a list of audit entries for node **nodeId**.

    The list can be filtered by **createdByUser** and for a given inclusive time period.

    The default sort order is **createdAt** ascending, but you can use an optional **ASC** or **DESC**
    modifier to specify an ascending or descending sort order.

    For example, specifying ```orderBy=createdAt DESC``` returns audit entries in descending
    **createdAt** order.

    This relies on the pre-configured 'alfresco-access' audit application.

    Args:
        node_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        order_by (Union[Unset, list[str]]):
        max_items (Union[Unset, int]):  Default: 100.
        where (Union[Unset, str]):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AuditEntryPaging]
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
            skip_count=skip_count,
            order_by=order_by,
            max_items=max_items,
            where=where,
            include=include,
            fields=fields,
        )
    ).parsed
