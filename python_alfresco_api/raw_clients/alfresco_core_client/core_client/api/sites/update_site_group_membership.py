from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.site_group_entry import SiteGroupEntry
from ...models.site_membership_body_update import SiteMembershipBodyUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_id: str,
    group_id: str,
    *,
    body: SiteMembershipBodyUpdate,
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
        "url": f"/sites/{site_id}/group-members/{group_id}",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, SiteGroupEntry]]:
    if response.status_code == 200:
        response_200 = SiteGroupEntry.from_dict(response.json())

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
    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, SiteGroupEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    site_id: str,
    group_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteMembershipBodyUpdate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, SiteGroupEntry]]:
    """Update site membership of group

     **Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.

    Update the membership of person **groupId** in site **siteId**.
    You can set the **role** to one of four types:
    * SiteConsumer
    * SiteCollaborator
    * SiteContributor
    * SiteManager

    Args:
        site_id (str):
        group_id (str):
        fields (Union[Unset, list[str]]):
        body (SiteMembershipBodyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SiteGroupEntry]]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        group_id=group_id,
        body=body,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    site_id: str,
    group_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteMembershipBodyUpdate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, SiteGroupEntry]]:
    """Update site membership of group

     **Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.

    Update the membership of person **groupId** in site **siteId**.
    You can set the **role** to one of four types:
    * SiteConsumer
    * SiteCollaborator
    * SiteContributor
    * SiteManager

    Args:
        site_id (str):
        group_id (str):
        fields (Union[Unset, list[str]]):
        body (SiteMembershipBodyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SiteGroupEntry]
    """

    return sync_detailed(
        site_id=site_id,
        group_id=group_id,
        client=client,
        body=body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    site_id: str,
    group_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteMembershipBodyUpdate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, SiteGroupEntry]]:
    """Update site membership of group

     **Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.

    Update the membership of person **groupId** in site **siteId**.
    You can set the **role** to one of four types:
    * SiteConsumer
    * SiteCollaborator
    * SiteContributor
    * SiteManager

    Args:
        site_id (str):
        group_id (str):
        fields (Union[Unset, list[str]]):
        body (SiteMembershipBodyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, SiteGroupEntry]]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        group_id=group_id,
        body=body,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    site_id: str,
    group_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteMembershipBodyUpdate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, SiteGroupEntry]]:
    """Update site membership of group

     **Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.

    Update the membership of person **groupId** in site **siteId**.
    You can set the **role** to one of four types:
    * SiteConsumer
    * SiteCollaborator
    * SiteContributor
    * SiteManager

    Args:
        site_id (str):
        group_id (str):
        fields (Union[Unset, list[str]]):
        body (SiteMembershipBodyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, SiteGroupEntry]
    """

    return (
        await asyncio_detailed(
            site_id=site_id,
            group_id=group_id,
            client=client,
            body=body,
            fields=fields,
        )
    ).parsed
