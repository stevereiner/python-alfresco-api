from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.favorite_paging import FavoritePaging
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: str,
    *,
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
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
        "url": f"/people/{person_id}/favorites",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, FavoritePaging]]:
    if response.status_code == 200:
        response_200 = FavoritePaging.from_dict(response.json())

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
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, FavoritePaging]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, FavoritePaging]]:
    """List favorites

     Gets a list of favorites for person **personId**.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

    The default sort order for the returned list of favorites is type ascending, createdAt descending.
    You can override the default by using the **orderBy** parameter.

    You can use any of the following fields to order the results:
    *   `type`
    *   `createdAt`
    *   `title`

    You can use the **where** parameter to restrict the list in the response
    to entries of a specific kind. The **where** parameter takes a value.
    The value is a single predicate that can include one or more **EXISTS**
    conditions. The **EXISTS** condition uses a single operand to limit the
    list to include entries that include that one property. The property values are:

    *   `target/file`
    *   `target/folder`
    *   `target/site`

    For example, the following **where** parameter restricts the returned list to the file favorites for
    a person:

    ```SQL
    (EXISTS(target/file))
    ```
    You can specify more than one condition using **OR**. The predicate must be enclosed in parentheses.


    For example, the following **where** parameter restricts the returned list to the file and folder
    favorites for a person:

    ```SQL
    (EXISTS(target/file) OR EXISTS(target/folder))
    ```

    Args:
        person_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        where (Union[Unset, str]):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FavoritePaging]]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        skip_count=skip_count,
        max_items=max_items,
        order_by=order_by,
        where=where,
        include=include,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, FavoritePaging]]:
    """List favorites

     Gets a list of favorites for person **personId**.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

    The default sort order for the returned list of favorites is type ascending, createdAt descending.
    You can override the default by using the **orderBy** parameter.

    You can use any of the following fields to order the results:
    *   `type`
    *   `createdAt`
    *   `title`

    You can use the **where** parameter to restrict the list in the response
    to entries of a specific kind. The **where** parameter takes a value.
    The value is a single predicate that can include one or more **EXISTS**
    conditions. The **EXISTS** condition uses a single operand to limit the
    list to include entries that include that one property. The property values are:

    *   `target/file`
    *   `target/folder`
    *   `target/site`

    For example, the following **where** parameter restricts the returned list to the file favorites for
    a person:

    ```SQL
    (EXISTS(target/file))
    ```
    You can specify more than one condition using **OR**. The predicate must be enclosed in parentheses.


    For example, the following **where** parameter restricts the returned list to the file and folder
    favorites for a person:

    ```SQL
    (EXISTS(target/file) OR EXISTS(target/folder))
    ```

    Args:
        person_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        where (Union[Unset, str]):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FavoritePaging]
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
        skip_count=skip_count,
        max_items=max_items,
        order_by=order_by,
        where=where,
        include=include,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    person_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, FavoritePaging]]:
    """List favorites

     Gets a list of favorites for person **personId**.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

    The default sort order for the returned list of favorites is type ascending, createdAt descending.
    You can override the default by using the **orderBy** parameter.

    You can use any of the following fields to order the results:
    *   `type`
    *   `createdAt`
    *   `title`

    You can use the **where** parameter to restrict the list in the response
    to entries of a specific kind. The **where** parameter takes a value.
    The value is a single predicate that can include one or more **EXISTS**
    conditions. The **EXISTS** condition uses a single operand to limit the
    list to include entries that include that one property. The property values are:

    *   `target/file`
    *   `target/folder`
    *   `target/site`

    For example, the following **where** parameter restricts the returned list to the file favorites for
    a person:

    ```SQL
    (EXISTS(target/file))
    ```
    You can specify more than one condition using **OR**. The predicate must be enclosed in parentheses.


    For example, the following **where** parameter restricts the returned list to the file and folder
    favorites for a person:

    ```SQL
    (EXISTS(target/file) OR EXISTS(target/folder))
    ```

    Args:
        person_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        where (Union[Unset, str]):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FavoritePaging]]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        skip_count=skip_count,
        max_items=max_items,
        order_by=order_by,
        where=where,
        include=include,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, FavoritePaging]]:
    """List favorites

     Gets a list of favorites for person **personId**.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

    The default sort order for the returned list of favorites is type ascending, createdAt descending.
    You can override the default by using the **orderBy** parameter.

    You can use any of the following fields to order the results:
    *   `type`
    *   `createdAt`
    *   `title`

    You can use the **where** parameter to restrict the list in the response
    to entries of a specific kind. The **where** parameter takes a value.
    The value is a single predicate that can include one or more **EXISTS**
    conditions. The **EXISTS** condition uses a single operand to limit the
    list to include entries that include that one property. The property values are:

    *   `target/file`
    *   `target/folder`
    *   `target/site`

    For example, the following **where** parameter restricts the returned list to the file favorites for
    a person:

    ```SQL
    (EXISTS(target/file))
    ```
    You can specify more than one condition using **OR**. The predicate must be enclosed in parentheses.


    For example, the following **where** parameter restricts the returned list to the file and folder
    favorites for a person:

    ```SQL
    (EXISTS(target/file) OR EXISTS(target/folder))
    ```

    Args:
        person_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        where (Union[Unset, str]):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FavoritePaging]
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            skip_count=skip_count,
            max_items=max_items,
            order_by=order_by,
            where=where,
            include=include,
            fields=fields,
        )
    ).parsed
