from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.site_member_paging import SiteMemberPaging
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_id: str,
    *,
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    fields: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["skipCount"] = skip_count

    params["maxItems"] = max_items

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params["where"] = where

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/sites/{site_id}/members",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SiteMemberPaging]]:
    if response.status_code == 200:
        response_200 = SiteMemberPaging.from_dict(response.json())

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
) -> Response[Union[Any, SiteMemberPaging]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    fields: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
) -> Response[Union[Any, SiteMemberPaging]]:
    """List site memberships

     Gets a list of site memberships for site **siteId**.

    Args:
        site_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        fields (Union[Unset, list[str]]):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SiteMemberPaging]]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        skip_count=skip_count,
        max_items=max_items,
        fields=fields,
        where=where,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    fields: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, SiteMemberPaging]]:
    """List site memberships

     Gets a list of site memberships for site **siteId**.

    Args:
        site_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        fields (Union[Unset, list[str]]):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SiteMemberPaging]
    """

    return sync_detailed(
        site_id=site_id,
        client=client,
        skip_count=skip_count,
        max_items=max_items,
        fields=fields,
        where=where,
    ).parsed


async def asyncio_detailed(
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    fields: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
) -> Response[Union[Any, SiteMemberPaging]]:
    """List site memberships

     Gets a list of site memberships for site **siteId**.

    Args:
        site_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        fields (Union[Unset, list[str]]):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SiteMemberPaging]]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        skip_count=skip_count,
        max_items=max_items,
        fields=fields,
        where=where,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    fields: Union[Unset, list[str]] = UNSET,
    where: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, SiteMemberPaging]]:
    """List site memberships

     Gets a list of site memberships for site **siteId**.

    Args:
        site_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        fields (Union[Unset, list[str]]):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SiteMemberPaging]
    """

    return (
        await asyncio_detailed(
            site_id=site_id,
            client=client,
            skip_count=skip_count,
            max_items=max_items,
            fields=fields,
            where=where,
        )
    ).parsed
