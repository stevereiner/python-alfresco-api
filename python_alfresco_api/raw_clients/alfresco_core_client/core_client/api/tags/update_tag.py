from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tag_body import TagBody
from ...models.tag_entry import TagEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    tag_id: str,
    *,
    body: TagBody,
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
        "method": "put",
        "url": f"/tags/{tag_id}",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, TagEntry]]:
    if response.status_code == 200:
        response_200 = TagEntry.from_dict(response.json())

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
) -> Response[Union[Any, TagEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    tag_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TagBody,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, TagEntry]]:
    """Update a tag

     Updates the tag **tagId**.

    Args:
        tag_id (str):
        fields (Union[Unset, list[str]]):
        body (TagBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TagEntry]]
    """

    kwargs = _get_kwargs(
        tag_id=tag_id,
        body=body,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    tag_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TagBody,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, TagEntry]]:
    """Update a tag

     Updates the tag **tagId**.

    Args:
        tag_id (str):
        fields (Union[Unset, list[str]]):
        body (TagBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TagEntry]
    """

    return sync_detailed(
        tag_id=tag_id,
        client=client,
        body=body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    tag_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TagBody,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, TagEntry]]:
    """Update a tag

     Updates the tag **tagId**.

    Args:
        tag_id (str):
        fields (Union[Unset, list[str]]):
        body (TagBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TagEntry]]
    """

    kwargs = _get_kwargs(
        tag_id=tag_id,
        body=body,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    tag_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TagBody,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, TagEntry]]:
    """Update a tag

     Updates the tag **tagId**.

    Args:
        tag_id (str):
        fields (Union[Unset, list[str]]):
        body (TagBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TagEntry]
    """

    return (
        await asyncio_detailed(
            tag_id=tag_id,
            client=client,
            body=body,
            fields=fields,
        )
    ).parsed
