from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ticket_body import TicketBody
from ...models.ticket_entry import TicketEntry
from ...types import Response


def _get_kwargs(
    *,
    body: TicketBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/tickets",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, TicketEntry]]:
    if response.status_code == 201:
        response_201 = TicketEntry.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, TicketEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TicketBody,
) -> Response[Union[Any, TicketEntry]]:
    r"""Create ticket (login)

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Logs in and returns the new authentication ticket.

    The userId and password properties are mandatory in the request body. For example:
    ```JSON
    {
        \"userId\": \"jbloggs\",
        \"password\": \"password\"
    }
    ```
    To use the ticket in future requests you should pass it in the request header.
    For example using Javascript:
      ```Javascript
        request.setRequestHeader (\"Authorization\", \"Basic \" + btoa(ticket));
      ```

    Args:
        body (TicketBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TicketEntry]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TicketBody,
) -> Optional[Union[Any, TicketEntry]]:
    r"""Create ticket (login)

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Logs in and returns the new authentication ticket.

    The userId and password properties are mandatory in the request body. For example:
    ```JSON
    {
        \"userId\": \"jbloggs\",
        \"password\": \"password\"
    }
    ```
    To use the ticket in future requests you should pass it in the request header.
    For example using Javascript:
      ```Javascript
        request.setRequestHeader (\"Authorization\", \"Basic \" + btoa(ticket));
      ```

    Args:
        body (TicketBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TicketEntry]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TicketBody,
) -> Response[Union[Any, TicketEntry]]:
    r"""Create ticket (login)

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Logs in and returns the new authentication ticket.

    The userId and password properties are mandatory in the request body. For example:
    ```JSON
    {
        \"userId\": \"jbloggs\",
        \"password\": \"password\"
    }
    ```
    To use the ticket in future requests you should pass it in the request header.
    For example using Javascript:
      ```Javascript
        request.setRequestHeader (\"Authorization\", \"Basic \" + btoa(ticket));
      ```

    Args:
        body (TicketBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TicketEntry]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: TicketBody,
) -> Optional[Union[Any, TicketEntry]]:
    r"""Create ticket (login)

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Logs in and returns the new authentication ticket.

    The userId and password properties are mandatory in the request body. For example:
    ```JSON
    {
        \"userId\": \"jbloggs\",
        \"password\": \"password\"
    }
    ```
    To use the ticket in future requests you should pass it in the request header.
    For example using Javascript:
      ```Javascript
        request.setRequestHeader (\"Authorization\", \"Basic \" + btoa(ticket));
      ```

    Args:
        body (TicketBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TicketEntry]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
