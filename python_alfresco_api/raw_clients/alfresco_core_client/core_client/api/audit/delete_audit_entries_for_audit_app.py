from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response


def _get_kwargs(
    audit_application_id: str,
    *,
    where: str,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["where"] = where

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/audit-applications/{audit_application_id}/audit-entries",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 204:
        return None
    if response.status_code == 400:
        return None
    if response.status_code == 401:
        return None
    if response.status_code == 403:
        return None
    if response.status_code == 404:
        return None
    if response.status_code == 501:
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
    audit_application_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    where: str,
) -> Response[Any]:
    """Permanently delete audit entries for an audit application

     **Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.

    Permanently delete audit entries for an audit application **auditApplicationId**.

    The **where** clause must be specified, either with an inclusive time period or for
    an inclusive range of ids. The delete is within the context of the given audit application.

    For example:

    *   ```where=(createdAt BETWEEN ('2017-06-02T12:13:51.593+01:00' ,
    '2017-06-04T10:05:16.536+01:00')```
    *   ```where=(id BETWEEN ('1234', '4321')```

    You must have admin rights to delete audit information.

    Args:
        audit_application_id (str):
        where (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        audit_application_id=audit_application_id,
        where=where,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    audit_application_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    where: str,
) -> Response[Any]:
    """Permanently delete audit entries for an audit application

     **Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.

    Permanently delete audit entries for an audit application **auditApplicationId**.

    The **where** clause must be specified, either with an inclusive time period or for
    an inclusive range of ids. The delete is within the context of the given audit application.

    For example:

    *   ```where=(createdAt BETWEEN ('2017-06-02T12:13:51.593+01:00' ,
    '2017-06-04T10:05:16.536+01:00')```
    *   ```where=(id BETWEEN ('1234', '4321')```

    You must have admin rights to delete audit information.

    Args:
        audit_application_id (str):
        where (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        audit_application_id=audit_application_id,
        where=where,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
