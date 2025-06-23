from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.audit_entry_entry import AuditEntryEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    audit_application_id: str,
    audit_entry_id: str,
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
        "url": f"/audit-applications/{audit_application_id}/audit-entries/{audit_entry_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, AuditEntryEntry]]:
    if response.status_code == 200:
        response_200 = AuditEntryEntry.from_dict(response.json())

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
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, AuditEntryEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    audit_application_id: str,
    audit_entry_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, AuditEntryEntry]]:
    """Get audit entry

     **Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.

    Gets audit entry **auditEntryId**.

    You must have admin rights to access audit information.

    Args:
        audit_application_id (str):
        audit_entry_id (str):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AuditEntryEntry]]
    """

    kwargs = _get_kwargs(
        audit_application_id=audit_application_id,
        audit_entry_id=audit_entry_id,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    audit_application_id: str,
    audit_entry_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, AuditEntryEntry]]:
    """Get audit entry

     **Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.

    Gets audit entry **auditEntryId**.

    You must have admin rights to access audit information.

    Args:
        audit_application_id (str):
        audit_entry_id (str):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AuditEntryEntry]
    """

    return sync_detailed(
        audit_application_id=audit_application_id,
        audit_entry_id=audit_entry_id,
        client=client,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    audit_application_id: str,
    audit_entry_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, AuditEntryEntry]]:
    """Get audit entry

     **Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.

    Gets audit entry **auditEntryId**.

    You must have admin rights to access audit information.

    Args:
        audit_application_id (str):
        audit_entry_id (str):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, AuditEntryEntry]]
    """

    kwargs = _get_kwargs(
        audit_application_id=audit_application_id,
        audit_entry_id=audit_entry_id,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    audit_application_id: str,
    audit_entry_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, AuditEntryEntry]]:
    """Get audit entry

     **Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.

    Gets audit entry **auditEntryId**.

    You must have admin rights to access audit information.

    Args:
        audit_application_id (str):
        audit_entry_id (str):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, AuditEntryEntry]
    """

    return (
        await asyncio_detailed(
            audit_application_id=audit_application_id,
            audit_entry_id=audit_entry_id,
            client=client,
            fields=fields,
        )
    ).parsed
