from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import File, Response


def _get_kwargs(
    person_id: str,
    *,
    body: File,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/people/{person_id}/avatar",
    }

    _kwargs["content"] = body.payload

    headers["Content-Type"] = "application/octet-stream"

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
    if response.status_code == 413:
        return None
    if response.status_code == 501:
        return None
    if response.status_code == 507:
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
    body: File,
) -> Response[Any]:
    r"""Update avatar image

     **Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.

    Updates the avatar image related to the person **personId**.

    The request body should be the binary stream for the avatar image. The content type of the file
    should be an image file. This will be used to generate an \"avatar\" thumbnail rendition.

    You must be the person or have admin rights to update a person's avatar.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

    Args:
        person_id (str):
        body (File):

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
    body: File,
) -> Response[Any]:
    r"""Update avatar image

     **Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.

    Updates the avatar image related to the person **personId**.

    The request body should be the binary stream for the avatar image. The content type of the file
    should be an image file. This will be used to generate an \"avatar\" thumbnail rendition.

    You must be the person or have admin rights to update a person's avatar.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

    Args:
        person_id (str):
        body (File):

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
