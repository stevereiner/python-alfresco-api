from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.group_body_create import GroupBodyCreate
from ...models.group_entry import GroupEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: GroupBodyCreate,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

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
        "method": "post",
        "url": "/groups",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, GroupEntry]]:
    if response.status_code == 201:
        response_201 = GroupEntry.from_dict(response.json())

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
) -> Response[Union[Any, GroupEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GroupBodyCreate,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, GroupEntry]]:
    r"""Create a group

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Create a group.

    The group id must start with \"GROUP\_\". If this is omitted it will be added automatically.
    This format is also returned when listing groups or group memberships. It should be noted
    that the other group-related operations also expect the id to start with \"GROUP\_\".

    If one or more parentIds are specified then the group will be created and become a member
    of each of the specified parent groups.

    If no parentIds are specified then the group will be created as a root group.

    The group will be created in the **APP.DEFAULT** and **AUTH.ALF** zones.

    You must have admin rights to create a group.

    Args:
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        body (GroupBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GroupEntry]]
    """

    kwargs = _get_kwargs(
        body=body,
        include=include,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GroupBodyCreate,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, GroupEntry]]:
    r"""Create a group

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Create a group.

    The group id must start with \"GROUP\_\". If this is omitted it will be added automatically.
    This format is also returned when listing groups or group memberships. It should be noted
    that the other group-related operations also expect the id to start with \"GROUP\_\".

    If one or more parentIds are specified then the group will be created and become a member
    of each of the specified parent groups.

    If no parentIds are specified then the group will be created as a root group.

    The group will be created in the **APP.DEFAULT** and **AUTH.ALF** zones.

    You must have admin rights to create a group.

    Args:
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        body (GroupBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GroupEntry]
    """

    return sync_detailed(
        client=client,
        body=body,
        include=include,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GroupBodyCreate,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, GroupEntry]]:
    r"""Create a group

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Create a group.

    The group id must start with \"GROUP\_\". If this is omitted it will be added automatically.
    This format is also returned when listing groups or group memberships. It should be noted
    that the other group-related operations also expect the id to start with \"GROUP\_\".

    If one or more parentIds are specified then the group will be created and become a member
    of each of the specified parent groups.

    If no parentIds are specified then the group will be created as a root group.

    The group will be created in the **APP.DEFAULT** and **AUTH.ALF** zones.

    You must have admin rights to create a group.

    Args:
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        body (GroupBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, GroupEntry]]
    """

    kwargs = _get_kwargs(
        body=body,
        include=include,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: GroupBodyCreate,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, GroupEntry]]:
    r"""Create a group

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Create a group.

    The group id must start with \"GROUP\_\". If this is omitted it will be added automatically.
    This format is also returned when listing groups or group memberships. It should be noted
    that the other group-related operations also expect the id to start with \"GROUP\_\".

    If one or more parentIds are specified then the group will be created and become a member
    of each of the specified parent groups.

    If no parentIds are specified then the group will be created as a root group.

    The group will be created in the **APP.DEFAULT** and **AUTH.ALF** zones.

    You must have admin rights to create a group.

    Args:
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        body (GroupBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, GroupEntry]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            include=include,
            fields=fields,
        )
    ).parsed
