from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.shared_link_entry import SharedLinkEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    shared_id: str,
    *,
    fields: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/shared-links/{shared_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SharedLinkEntry]]:
    if response.status_code == 200:
        response_200 = SharedLinkEntry.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
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
) -> Response[Union[Any, SharedLinkEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    shared_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, SharedLinkEntry]]:
    """Get a shared link

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets minimal information for the file with shared link identifier **sharedId**.

    **Note:** No authentication is required to call this endpoint.

    Args:
        shared_id (str):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SharedLinkEntry]]
    """

    kwargs = _get_kwargs(
        shared_id=shared_id,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    shared_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, SharedLinkEntry]]:
    """Get a shared link

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets minimal information for the file with shared link identifier **sharedId**.

    **Note:** No authentication is required to call this endpoint.

    Args:
        shared_id (str):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SharedLinkEntry]
    """

    return sync_detailed(
        shared_id=shared_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    shared_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, SharedLinkEntry]]:
    """Get a shared link

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets minimal information for the file with shared link identifier **sharedId**.

    **Note:** No authentication is required to call this endpoint.

    Args:
        shared_id (str):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SharedLinkEntry]]
    """

    kwargs = _get_kwargs(
        shared_id=shared_id,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    shared_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, SharedLinkEntry]]:
    """Get a shared link

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets minimal information for the file with shared link identifier **sharedId**.

    **Note:** No authentication is required to call this endpoint.

    Args:
        shared_id (str):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SharedLinkEntry]
    """

    return (
        await asyncio_detailed(
            shared_id=shared_id,
            client=client,
            fields=fields,
        )
    ).parsed
