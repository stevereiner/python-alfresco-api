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
    where: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["skipCount"] = skip_count

    params["maxItems"] = max_items

    params["where"] = where

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/site-membership-requests",
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
    where: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Any]:
    """Get site membership requests

     Get the list of site membership requests the user can action.

    You can use the **where** parameter to filter the returned site membership requests by **siteId**.
    For example:

    ```
    (siteId=mySite)
    ```

    The **where** parameter can also be used to filter by ***personId***. For example:

    ```
    where=(personId=person)
    ```

    This may be combined with the siteId filter, as shown below:

    ```
    where=(siteId=mySite AND personId=person))
    ```

    Args:
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        where (Union[Unset, str]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        skip_count=skip_count,
        max_items=max_items,
        where=where,
        fields=fields,
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
    where: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Any]:
    """Get site membership requests

     Get the list of site membership requests the user can action.

    You can use the **where** parameter to filter the returned site membership requests by **siteId**.
    For example:

    ```
    (siteId=mySite)
    ```

    The **where** parameter can also be used to filter by ***personId***. For example:

    ```
    where=(personId=person)
    ```

    This may be combined with the siteId filter, as shown below:

    ```
    where=(siteId=mySite AND personId=person))
    ```

    Args:
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        where (Union[Unset, str]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        skip_count=skip_count,
        max_items=max_items,
        where=where,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
