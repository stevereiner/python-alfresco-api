from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    relations: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["skipCount"] = skip_count

    params["maxItems"] = max_items

    json_order_by: Union[Unset, list[str]] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by

    params["orderBy"] = json_order_by

    json_relations: Union[Unset, list[str]] = UNSET
    if not isinstance(relations, Unset):
        json_relations = relations

    params["relations"] = json_relations

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params["where"] = where

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/sites",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 400:
        return None
    if response.status_code == 401:
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
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    relations: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """List sites

     Gets a list of sites in this repository.

    You can use the **where** parameter to filter the returned sites by **visibility** or site
    **preset**.

    Example to filter by **visibility**, use any one of:

    ```
    (visibility='PRIVATE')
    (visibility='PUBLIC')
    (visibility='MODERATED')
    ```

    Example to filter by site **preset**:

    ```
    (preset='site-dashboard')
    ```

    The default sort order for the returned list is for sites to be sorted by ascending title.
    You can override the default by using the **orderBy** parameter. You can specify one or more of the
    following fields in the **orderBy** parameter:
    * id
    * title
    * description

    You can use the **relations** parameter to include one or more related
    entities in a single response and so reduce network traffic.

    The entity types in Alfresco are organized in a tree structure.
    The **sites** entity has two children, **containers** and **members**.
    The following relations parameter returns all the container and member
    objects related to each site:

    ```
    containers,members
    ```

    Args:
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        relations (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        skip_count=skip_count,
        max_items=max_items,
        order_by=order_by,
        relations=relations,
        fields=fields,
        where=where,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    relations: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
) -> Response[Any]:
    """List sites

     Gets a list of sites in this repository.

    You can use the **where** parameter to filter the returned sites by **visibility** or site
    **preset**.

    Example to filter by **visibility**, use any one of:

    ```
    (visibility='PRIVATE')
    (visibility='PUBLIC')
    (visibility='MODERATED')
    ```

    Example to filter by site **preset**:

    ```
    (preset='site-dashboard')
    ```

    The default sort order for the returned list is for sites to be sorted by ascending title.
    You can override the default by using the **orderBy** parameter. You can specify one or more of the
    following fields in the **orderBy** parameter:
    * id
    * title
    * description

    You can use the **relations** parameter to include one or more related
    entities in a single response and so reduce network traffic.

    The entity types in Alfresco are organized in a tree structure.
    The **sites** entity has two children, **containers** and **members**.
    The following relations parameter returns all the container and member
    objects related to each site:

    ```
    containers,members
    ```

    Args:
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        relations (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        skip_count=skip_count,
        max_items=max_items,
        order_by=order_by,
        relations=relations,
        fields=fields,
        where=where,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
