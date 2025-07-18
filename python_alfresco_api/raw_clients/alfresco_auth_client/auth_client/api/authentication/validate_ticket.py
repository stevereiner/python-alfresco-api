from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.valid_ticket_entry import ValidTicketEntry
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/tickets/-me-",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ValidTicketEntry]]:
    if response.status_code == 200:
        response_200 = ValidTicketEntry.from_dict(response.json())

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
) -> Response[Union[Any, ValidTicketEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ValidTicketEntry]]:
    r"""Validate ticket

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Validates the specified ticket (derived from Authorization header) is still valid.

    For example, you can pass the Authorization request header using Javascript:
      ```Javascript
        request.setRequestHeader (\"Authorization\", \"Basic \" + btoa(ticket));
      ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ValidTicketEntry]]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ValidTicketEntry]]:
    r"""Validate ticket

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Validates the specified ticket (derived from Authorization header) is still valid.

    For example, you can pass the Authorization request header using Javascript:
      ```Javascript
        request.setRequestHeader (\"Authorization\", \"Basic \" + btoa(ticket));
      ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ValidTicketEntry]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ValidTicketEntry]]:
    r"""Validate ticket

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Validates the specified ticket (derived from Authorization header) is still valid.

    For example, you can pass the Authorization request header using Javascript:
      ```Javascript
        request.setRequestHeader (\"Authorization\", \"Basic \" + btoa(ticket));
      ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ValidTicketEntry]]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ValidTicketEntry]]:
    r"""Validate ticket

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Validates the specified ticket (derived from Authorization header) is still valid.

    For example, you can pass the Authorization request header using Javascript:
      ```Javascript
        request.setRequestHeader (\"Authorization\", \"Basic \" + btoa(ticket));
      ```

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ValidTicketEntry]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
