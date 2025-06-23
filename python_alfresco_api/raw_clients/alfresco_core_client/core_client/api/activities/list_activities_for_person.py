from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_paging import ActivityPaging
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: str,
    *,
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    who: Union[Unset, str] = UNSET,
    site_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["skipCount"] = skip_count

    params["maxItems"] = max_items

    params["who"] = who

    params["siteId"] = site_id

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/people/{person_id}/activities",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ActivityPaging, Any]]:
    if response.status_code == 200:
        response_200 = ActivityPaging.from_dict(response.json())

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
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ActivityPaging, Any]]:
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
    who: Union[Unset, str] = UNSET,
    site_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[ActivityPaging, Any]]:
    """List activities

     Gets a list of activities for person **personId**.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

    Args:
        person_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        who (Union[Unset, str]):
        site_id (Union[Unset, str]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActivityPaging, Any]]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        skip_count=skip_count,
        max_items=max_items,
        who=who,
        site_id=site_id,
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
    who: Union[Unset, str] = UNSET,
    site_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[ActivityPaging, Any]]:
    """List activities

     Gets a list of activities for person **personId**.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

    Args:
        person_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        who (Union[Unset, str]):
        site_id (Union[Unset, str]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActivityPaging, Any]
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
        skip_count=skip_count,
        max_items=max_items,
        who=who,
        site_id=site_id,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    person_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    who: Union[Unset, str] = UNSET,
    site_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[ActivityPaging, Any]]:
    """List activities

     Gets a list of activities for person **personId**.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

    Args:
        person_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        who (Union[Unset, str]):
        site_id (Union[Unset, str]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActivityPaging, Any]]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        skip_count=skip_count,
        max_items=max_items,
        who=who,
        site_id=site_id,
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
    who: Union[Unset, str] = UNSET,
    site_id: Union[Unset, str] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[ActivityPaging, Any]]:
    """List activities

     Gets a list of activities for person **personId**.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

    Args:
        person_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        who (Union[Unset, str]):
        site_id (Union[Unset, str]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActivityPaging, Any]
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            skip_count=skip_count,
            max_items=max_items,
            who=who,
            site_id=site_id,
            fields=fields,
        )
    ).parsed
