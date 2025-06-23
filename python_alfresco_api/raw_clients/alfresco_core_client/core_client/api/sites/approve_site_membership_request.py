from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.site_membership_approval_body import SiteMembershipApprovalBody
from ...types import Response


def _get_kwargs(
    site_id: str,
    invitee_id: str,
    *,
    body: SiteMembershipApprovalBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/sites/{site_id}/site-membership-requests/{invitee_id}/approve",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 200:
        return None
    if response.status_code == 400:
        return None
    if response.status_code == 401:
        return None
    if response.status_code == 403:
        return None
    if response.status_code == 404:
        return None
    if response.status_code == 422:
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
    site_id: str,
    invitee_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteMembershipApprovalBody,
) -> Response[Any]:
    """Approve a site membership request

     Approve a site membership request.

    Args:
        site_id (str):
        invitee_id (str):
        body (SiteMembershipApprovalBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        invitee_id=invitee_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    site_id: str,
    invitee_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteMembershipApprovalBody,
) -> Response[Any]:
    """Approve a site membership request

     Approve a site membership request.

    Args:
        site_id (str):
        invitee_id (str):
        body (SiteMembershipApprovalBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        invitee_id=invitee_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
