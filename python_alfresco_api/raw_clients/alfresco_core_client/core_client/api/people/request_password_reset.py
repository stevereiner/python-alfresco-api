from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.client_body import ClientBody
from ...types import Response


def _get_kwargs(
    person_id: str,
    *,
    body: ClientBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/people/{person_id}/request-password-reset",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 202:
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
    *,
    client: Union[AuthenticatedClient, Client],
    body: ClientBody,
) -> Response[Any]:
    r"""Request password reset

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Initiates the reset password workflow to send an email with reset password instruction to the user's
    registered email.

    The client is mandatory in the request body. For example:
    ```JSON
    {
      \"client\": \"myClient\"
    }
    ```
    **Note:** The client must be registered before this API can send an email. See [server
    documentation]. However, out-of-the-box
    share is registered as a default client, so you could pass **share** as the client name:
    ```JSON
    {
      \"client\": \"share\"
    }
    ```
    **Note:** No authentication is required to call this endpoint.

    Args:
        person_id (str):
        body (ClientBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    person_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ClientBody,
) -> Response[Any]:
    r"""Request password reset

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Initiates the reset password workflow to send an email with reset password instruction to the user's
    registered email.

    The client is mandatory in the request body. For example:
    ```JSON
    {
      \"client\": \"myClient\"
    }
    ```
    **Note:** The client must be registered before this API can send an email. See [server
    documentation]. However, out-of-the-box
    share is registered as a default client, so you could pass **share** as the client name:
    ```JSON
    {
      \"client\": \"share\"
    }
    ```
    **Note:** No authentication is required to call this endpoint.

    Args:
        person_id (str):
        body (ClientBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
