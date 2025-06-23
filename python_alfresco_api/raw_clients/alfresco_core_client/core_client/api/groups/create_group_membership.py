from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.group_member_entry import GroupMemberEntry
from ...models.group_membership_body_create import GroupMembershipBodyCreate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    group_id: str,
    *,
    body: GroupMembershipBodyCreate,
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
        "method": "post",
        "url": f"/groups/{group_id}/members",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GroupMemberEntry]]:
    if response.status_code == 201:
        response_201 = GroupMemberEntry.from_dict(response.json())

        return response_201
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
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, GroupMemberEntry]]:
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
    body: GroupMembershipBodyCreate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, GroupMemberEntry]]:
    """Create a group membership

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Create a group membership (for an existing person or group) within a group **groupId**.

    If the added group was previously a root group then it becomes a non-root group since it now has a
    parent.

    It is an error to specify an **id** that does not exist.

    You must have admin rights to create a group membership.

    Args:
        group_id (str):
        fields (Union[Unset, list[str]]):
        body (GroupMembershipBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GroupMemberEntry]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
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
    body: GroupMembershipBodyCreate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, GroupMemberEntry]]:
    """Create a group membership

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Create a group membership (for an existing person or group) within a group **groupId**.

    If the added group was previously a root group then it becomes a non-root group since it now has a
    parent.

    It is an error to specify an **id** that does not exist.

    You must have admin rights to create a group membership.

    Args:
        group_id (str):
        fields (Union[Unset, list[str]]):
        body (GroupMembershipBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GroupMemberEntry]
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
        body=body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: GroupMembershipBodyCreate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, GroupMemberEntry]]:
    """Create a group membership

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Create a group membership (for an existing person or group) within a group **groupId**.

    If the added group was previously a root group then it becomes a non-root group since it now has a
    parent.

    It is an error to specify an **id** that does not exist.

    You must have admin rights to create a group membership.

    Args:
        group_id (str):
        fields (Union[Unset, list[str]]):
        body (GroupMembershipBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GroupMemberEntry]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        body=body,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    group_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: GroupMembershipBodyCreate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, GroupMemberEntry]]:
    """Create a group membership

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Create a group membership (for an existing person or group) within a group **groupId**.

    If the added group was previously a root group then it becomes a non-root group since it now has a
    parent.

    It is an error to specify an **id** that does not exist.

    You must have admin rights to create a group membership.

    Args:
        group_id (str):
        fields (Union[Unset, list[str]]):
        body (GroupMembershipBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GroupMemberEntry]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
            body=body,
            fields=fields,
        )
    ).parsed
