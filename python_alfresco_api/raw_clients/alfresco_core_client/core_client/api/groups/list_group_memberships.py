from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.group_member_paging import GroupMemberPaging
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: str,
    *,
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["skipCount"] = skip_count

    params["maxItems"] = max_items

    json_order_by: Union[Unset, list[str]] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by

    params["orderBy"] = json_order_by

    params["where"] = where

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/groups/{group_id}/members",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GroupMemberPaging]]:
    if response.status_code == 200:
        response_200 = GroupMemberPaging.from_dict(response.json())

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
    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GroupMemberPaging]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    group_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, GroupMemberPaging]]:
    """List memberships of a group

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Gets a list of the group memberships for the group **groupId**.

    You can use the **where** parameter to filter the returned groups by **memberType**.

    Example to filter by **memberType**, use any one of:

    ```
    (memberType='GROUP')
    (memberType='PERSON')
    ```

    The default sort order for the returned list is for group members to be sorted by ascending
    displayName.
    You can override the default by using the **orderBy** parameter. You can specify one of the
    following fields in the **orderBy** parameter:
    * id
    * displayName

    Args:
        group_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        where (Union[Unset, str]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GroupMemberPaging]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        skip_count=skip_count,
        max_items=max_items,
        order_by=order_by,
        where=where,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    group_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, GroupMemberPaging]]:
    """List memberships of a group

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Gets a list of the group memberships for the group **groupId**.

    You can use the **where** parameter to filter the returned groups by **memberType**.

    Example to filter by **memberType**, use any one of:

    ```
    (memberType='GROUP')
    (memberType='PERSON')
    ```

    The default sort order for the returned list is for group members to be sorted by ascending
    displayName.
    You can override the default by using the **orderBy** parameter. You can specify one of the
    following fields in the **orderBy** parameter:
    * id
    * displayName

    Args:
        group_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        where (Union[Unset, str]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GroupMemberPaging]
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        skip_count=skip_count,
        max_items=max_items,
        order_by=order_by,
        where=where,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, GroupMemberPaging]]:
    """List memberships of a group

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Gets a list of the group memberships for the group **groupId**.

    You can use the **where** parameter to filter the returned groups by **memberType**.

    Example to filter by **memberType**, use any one of:

    ```
    (memberType='GROUP')
    (memberType='PERSON')
    ```

    The default sort order for the returned list is for group members to be sorted by ascending
    displayName.
    You can override the default by using the **orderBy** parameter. You can specify one of the
    following fields in the **orderBy** parameter:
    * id
    * displayName

    Args:
        group_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        where (Union[Unset, str]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GroupMemberPaging]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        skip_count=skip_count,
        max_items=max_items,
        order_by=order_by,
        where=where,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, GroupMemberPaging]]:
    """List memberships of a group

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Gets a list of the group memberships for the group **groupId**.

    You can use the **where** parameter to filter the returned groups by **memberType**.

    Example to filter by **memberType**, use any one of:

    ```
    (memberType='GROUP')
    (memberType='PERSON')
    ```

    The default sort order for the returned list is for group members to be sorted by ascending
    displayName.
    You can override the default by using the **orderBy** parameter. You can specify one of the
    following fields in the **orderBy** parameter:
    * id
    * displayName

    Args:
        group_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        where (Union[Unset, str]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GroupMemberPaging]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            skip_count=skip_count,
            max_items=max_items,
            order_by=order_by,
            where=where,
            fields=fields,
        )
    ).parsed
