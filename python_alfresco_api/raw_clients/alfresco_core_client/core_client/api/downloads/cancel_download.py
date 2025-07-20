from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors




def _get_kwargs(
    download_id: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": "/downloads/{download_id}".format(download_id=download_id,),
    }


    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 202:
        return None
    if response.status_code == 400:
        return None
    if response.status_code == 401:
        return None
    if response.status_code == 403:
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
    download_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    """ Cancel a download

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Cancels the creation of a download request.

    **Note:** The download node can be deleted using the **DELETE /nodes/{downloadId}** endpoint

    By default, if the download node is not deleted it will be picked up by a cleaner job which removes
    download nodes older than a configurable amount of time (default is 1 hour)

    Information about the existing progress at the time of cancelling can be retrieved by calling the
    **GET /downloads/{downloadId}** endpoint

    The cancel operation is done asynchronously.

    Args:
        download_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        download_id=download_id,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    download_id: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[Any]:
    """ Cancel a download

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Cancels the creation of a download request.

    **Note:** The download node can be deleted using the **DELETE /nodes/{downloadId}** endpoint

    By default, if the download node is not deleted it will be picked up by a cleaner job which removes
    download nodes older than a configurable amount of time (default is 1 hour)

    Information about the existing progress at the time of cancelling can be retrieved by calling the
    **GET /downloads/{downloadId}** endpoint

    The cancel operation is done asynchronously.

    Args:
        download_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
     """


    kwargs = _get_kwargs(
        download_id=download_id,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

