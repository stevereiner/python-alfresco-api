from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.shared_link_body_email import SharedLinkBodyEmail
from ...types import Response


def _get_kwargs(
    shared_id: str,
    *,
    body: SharedLinkBodyEmail,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/shared-links/{shared_id}/email",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 202:
        return None
    if response.status_code == 400:
        return None
    if response.status_code == 401:
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
    shared_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SharedLinkBodyEmail,
) -> Response[Any]:
    r"""Email shared link

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Sends email with app-specific url including identifier **sharedId**.

    The client and recipientEmails properties are mandatory in the request body. For example, to email a
    shared link with minimum info:
    ```JSON
    {
        \"client\": \"myClient\",
        \"recipientEmails\": [\"john.doe@acme.com\", \"joe.bloggs@acme.com\"]
    }
    ```
    A plain text message property can be optionally provided in the request body to customise the sent
    email.
    Also, a locale property can be optionally provided in the request body to send the emails in a
    particular language (if the locale is supported by Alfresco).
    For example, to email a shared link with a messages and a locale:
    ```JSON
    {
        \"client\": \"myClient\",
        \"recipientEmails\": [\"john.doe@acme.com\", \"joe.bloggs@acme.com\"],
        \"message\": \"myMessage\",
        \"locale\":\"en-GB\"
    }
    ```
    **Note:** The client must be registered before you can send a shared link email. See [server
    documentation]. However, out-of-the-box
     share is registered as a default client, so you could pass **share** as the client name:
    ```JSON
    {
        \"client\": \"share\",
        \"recipientEmails\": [\"john.doe@acme.com\"]
    }
    ```

    Args:
        shared_id (str):
        body (SharedLinkBodyEmail):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        shared_id=shared_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    shared_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SharedLinkBodyEmail,
) -> Response[Any]:
    r"""Email shared link

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Sends email with app-specific url including identifier **sharedId**.

    The client and recipientEmails properties are mandatory in the request body. For example, to email a
    shared link with minimum info:
    ```JSON
    {
        \"client\": \"myClient\",
        \"recipientEmails\": [\"john.doe@acme.com\", \"joe.bloggs@acme.com\"]
    }
    ```
    A plain text message property can be optionally provided in the request body to customise the sent
    email.
    Also, a locale property can be optionally provided in the request body to send the emails in a
    particular language (if the locale is supported by Alfresco).
    For example, to email a shared link with a messages and a locale:
    ```JSON
    {
        \"client\": \"myClient\",
        \"recipientEmails\": [\"john.doe@acme.com\", \"joe.bloggs@acme.com\"],
        \"message\": \"myMessage\",
        \"locale\":\"en-GB\"
    }
    ```
    **Note:** The client must be registered before you can send a shared link email. See [server
    documentation]. However, out-of-the-box
     share is registered as a default client, so you could pass **share** as the client name:
    ```JSON
    {
        \"client\": \"share\",
        \"recipientEmails\": [\"john.doe@acme.com\"]
    }
    ```

    Args:
        shared_id (str):
        body (SharedLinkBodyEmail):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        shared_id=shared_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
