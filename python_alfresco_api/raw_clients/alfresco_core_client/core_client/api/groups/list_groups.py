from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.group_paging import GroupPaging
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
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

    json_include: Union[Unset, list[str]] = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params["where"] = where

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/groups",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GroupPaging]]:
    if response.status_code == 200:
        response_200 = GroupPaging.from_dict(response.json())

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
) -> Response[Union[Any, GroupPaging]]:
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
    include: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, GroupPaging]]:
    """List groups

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Gets a list of groups.

    You can use the **include** parameter to return additional information.

    You can use the **where** parameter to filter the returned groups by **isRoot**. For example, the
    following **where**
    clause will return just the root groups:

    ```
    (isRoot=true)
    ```

    The **where** parameter can also be used to filter by ***zone*** and ***displayName***.
    They may be combined with isRoot to narrow a result set even further.
    For example, the following where clause will only return groups belonging to the `MY.ZONE` zone.

    ```
    where=(zones in ('MY.ZONE'))
    ```

    This may be combined with the isRoot filter, as shown below:

    ```
    where=(isRoot=false AND zones in ('MY.ZONE'))
    ```
    The following where clause will only return groups with displayName `MY.GROUP.NAME`.

    ```
    where=(displayName in ('MY.GROUP.NAME'))
    ```
    This may be combined with the isRoot and zones filter, as shown below:

    ```
    where=(isRoot=false AND displayName in ('MY.GROUP.NAME'))
    ```

    ```
    where=(zones in ('MY.ZONE') AND displayName in ('MY.GROUP.NAME'))
    ```

    ```
    where=(isRoot=false AND zones in ('MY.ZONE') AND displayName in ('MY.GROUP.NAME'))
    ```

    ***Note:*** restrictions include
    * `AND` is the only supported operator when combining `isRoot`, `zones` and `displayName` filters
    * Only one zone is supported by the filter
    * Only one displayName is supported by the filter
    * The quoted zone name and displayName must be placed in parenthesis — a 400 error will result if
    these are omitted.

    The default sort order for the returned list is for groups to be sorted by ascending displayName.
    You can override the default by using the **orderBy** parameter. You can specify one of the
    following fields in the **orderBy** parameter:
    * id
    * displayName

    Args:
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        include (Union[Unset, list[str]]):
        where (Union[Unset, str]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GroupPaging]]
    """

    kwargs = _get_kwargs(
        skip_count=skip_count,
        max_items=max_items,
        order_by=order_by,
        include=include,
        where=where,
        fields=fields,
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
    order_by: Union[Unset, list[str]] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, GroupPaging]]:
    """List groups

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Gets a list of groups.

    You can use the **include** parameter to return additional information.

    You can use the **where** parameter to filter the returned groups by **isRoot**. For example, the
    following **where**
    clause will return just the root groups:

    ```
    (isRoot=true)
    ```

    The **where** parameter can also be used to filter by ***zone*** and ***displayName***.
    They may be combined with isRoot to narrow a result set even further.
    For example, the following where clause will only return groups belonging to the `MY.ZONE` zone.

    ```
    where=(zones in ('MY.ZONE'))
    ```

    This may be combined with the isRoot filter, as shown below:

    ```
    where=(isRoot=false AND zones in ('MY.ZONE'))
    ```
    The following where clause will only return groups with displayName `MY.GROUP.NAME`.

    ```
    where=(displayName in ('MY.GROUP.NAME'))
    ```
    This may be combined with the isRoot and zones filter, as shown below:

    ```
    where=(isRoot=false AND displayName in ('MY.GROUP.NAME'))
    ```

    ```
    where=(zones in ('MY.ZONE') AND displayName in ('MY.GROUP.NAME'))
    ```

    ```
    where=(isRoot=false AND zones in ('MY.ZONE') AND displayName in ('MY.GROUP.NAME'))
    ```

    ***Note:*** restrictions include
    * `AND` is the only supported operator when combining `isRoot`, `zones` and `displayName` filters
    * Only one zone is supported by the filter
    * Only one displayName is supported by the filter
    * The quoted zone name and displayName must be placed in parenthesis — a 400 error will result if
    these are omitted.

    The default sort order for the returned list is for groups to be sorted by ascending displayName.
    You can override the default by using the **orderBy** parameter. You can specify one of the
    following fields in the **orderBy** parameter:
    * id
    * displayName

    Args:
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        include (Union[Unset, list[str]]):
        where (Union[Unset, str]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GroupPaging]
    """

    return sync_detailed(
        client=client,
        skip_count=skip_count,
        max_items=max_items,
        order_by=order_by,
        include=include,
        where=where,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, GroupPaging]]:
    """List groups

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Gets a list of groups.

    You can use the **include** parameter to return additional information.

    You can use the **where** parameter to filter the returned groups by **isRoot**. For example, the
    following **where**
    clause will return just the root groups:

    ```
    (isRoot=true)
    ```

    The **where** parameter can also be used to filter by ***zone*** and ***displayName***.
    They may be combined with isRoot to narrow a result set even further.
    For example, the following where clause will only return groups belonging to the `MY.ZONE` zone.

    ```
    where=(zones in ('MY.ZONE'))
    ```

    This may be combined with the isRoot filter, as shown below:

    ```
    where=(isRoot=false AND zones in ('MY.ZONE'))
    ```
    The following where clause will only return groups with displayName `MY.GROUP.NAME`.

    ```
    where=(displayName in ('MY.GROUP.NAME'))
    ```
    This may be combined with the isRoot and zones filter, as shown below:

    ```
    where=(isRoot=false AND displayName in ('MY.GROUP.NAME'))
    ```

    ```
    where=(zones in ('MY.ZONE') AND displayName in ('MY.GROUP.NAME'))
    ```

    ```
    where=(isRoot=false AND zones in ('MY.ZONE') AND displayName in ('MY.GROUP.NAME'))
    ```

    ***Note:*** restrictions include
    * `AND` is the only supported operator when combining `isRoot`, `zones` and `displayName` filters
    * Only one zone is supported by the filter
    * Only one displayName is supported by the filter
    * The quoted zone name and displayName must be placed in parenthesis — a 400 error will result if
    these are omitted.

    The default sort order for the returned list is for groups to be sorted by ascending displayName.
    You can override the default by using the **orderBy** parameter. You can specify one of the
    following fields in the **orderBy** parameter:
    * id
    * displayName

    Args:
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        include (Union[Unset, list[str]]):
        where (Union[Unset, str]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GroupPaging]]
    """

    kwargs = _get_kwargs(
        skip_count=skip_count,
        max_items=max_items,
        order_by=order_by,
        include=include,
        where=where,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, GroupPaging]]:
    """List groups

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Gets a list of groups.

    You can use the **include** parameter to return additional information.

    You can use the **where** parameter to filter the returned groups by **isRoot**. For example, the
    following **where**
    clause will return just the root groups:

    ```
    (isRoot=true)
    ```

    The **where** parameter can also be used to filter by ***zone*** and ***displayName***.
    They may be combined with isRoot to narrow a result set even further.
    For example, the following where clause will only return groups belonging to the `MY.ZONE` zone.

    ```
    where=(zones in ('MY.ZONE'))
    ```

    This may be combined with the isRoot filter, as shown below:

    ```
    where=(isRoot=false AND zones in ('MY.ZONE'))
    ```
    The following where clause will only return groups with displayName `MY.GROUP.NAME`.

    ```
    where=(displayName in ('MY.GROUP.NAME'))
    ```
    This may be combined with the isRoot and zones filter, as shown below:

    ```
    where=(isRoot=false AND displayName in ('MY.GROUP.NAME'))
    ```

    ```
    where=(zones in ('MY.ZONE') AND displayName in ('MY.GROUP.NAME'))
    ```

    ```
    where=(isRoot=false AND zones in ('MY.ZONE') AND displayName in ('MY.GROUP.NAME'))
    ```

    ***Note:*** restrictions include
    * `AND` is the only supported operator when combining `isRoot`, `zones` and `displayName` filters
    * Only one zone is supported by the filter
    * Only one displayName is supported by the filter
    * The quoted zone name and displayName must be placed in parenthesis — a 400 error will result if
    these are omitted.

    The default sort order for the returned list is for groups to be sorted by ascending displayName.
    You can override the default by using the **orderBy** parameter. You can specify one of the
    following fields in the **orderBy** parameter:
    * id
    * displayName

    Args:
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        include (Union[Unset, list[str]]):
        where (Union[Unset, str]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GroupPaging]
    """

    return (
        await asyncio_detailed(
            client=client,
            skip_count=skip_count,
            max_items=max_items,
            order_by=order_by,
            include=include,
            where=where,
            fields=fields,
        )
    ).parsed
