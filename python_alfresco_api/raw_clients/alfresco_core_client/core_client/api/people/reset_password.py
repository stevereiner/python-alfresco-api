from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.password_reset_body import PasswordResetBody
from ...types import Response


def _get_kwargs(
    person_id: str,
    *,
    body: PasswordResetBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/people/{person_id}/reset-password",
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
    body: PasswordResetBody,
) -> Response[Any]:
    r"""Reset password

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Resets user's password

    The password, id and key properties are mandatory in the request body. For example:
    ```JSON
    {
      \"password\":\"newPassword\",
      \"id\":\"activiti$10\",
      \"key\":\"4dad6d00-0daf-413a-b200-f64af4e12345\"
    }
    ```
    **Note:** No authentication is required to call this endpoint.

    Args:
        person_id (str):
        body (PasswordResetBody):

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
    body: PasswordResetBody,
) -> Response[Any]:
    r"""Reset password

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Resets user's password

    The password, id and key properties are mandatory in the request body. For example:
    ```JSON
    {
      \"password\":\"newPassword\",
      \"id\":\"activiti$10\",
      \"key\":\"4dad6d00-0daf-413a-b200-f64af4e12345\"
    }
    ```
    **Note:** No authentication is required to call this endpoint.

    Args:
        person_id (str):
        body (PasswordResetBody):

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
