from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.site_membership_request_body_update import SiteMembershipRequestBodyUpdate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: str,
    site_id: str,
    *,
    body: SiteMembershipRequestBodyUpdate,
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
        "url": f"/people/{person_id}/site-membership-requests/{site_id}",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 400:
        return None
    if response.status_code == 401:
        return None
    if response.status_code == 404:
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
    person_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteMembershipRequestBodyUpdate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Any]:
    """Update a site membership request

     Updates the message for the site membership request to site **siteId** for person **personId**.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

    Args:
        person_id (str):
        site_id (str):
        fields (Union[Unset, list[str]]):
        body (SiteMembershipRequestBodyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        site_id=site_id,
        body=body,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    person_id: str,
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteMembershipRequestBodyUpdate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Any]:
    """Update a site membership request

     Updates the message for the site membership request to site **siteId** for person **personId**.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

    Args:
        person_id (str):
        site_id (str):
        fields (Union[Unset, list[str]]):
        body (SiteMembershipRequestBodyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        site_id=site_id,
        body=body,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
