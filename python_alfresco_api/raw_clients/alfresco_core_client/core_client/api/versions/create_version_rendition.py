from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rendition_body_create import RenditionBodyCreate
from ...types import Response


def _get_kwargs(
    node_id: str,
    version_id: str,
    *,
    body: RenditionBodyCreate,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/nodes/{node_id}/versions/{version_id}/renditions",
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
    if response.status_code == 403:
        return None
    if response.status_code == 404:
        return None
    if response.status_code == 409:
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
    node_id: str,
    version_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RenditionBodyCreate,
) -> Response[Any]:
    r"""Create rendition for a file version

     **Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.

    An asynchronous request to create a rendition for version of file **nodeId** and **versionId**.

    The version rendition is specified by name **id** in the request body:
    ```JSON
    {
      \"id\":\"doclib\"
    }
    ```
      Multiple names may be specified as a comma separated list or using a list format:
    ```JSON
    [
      {
          \"id\": \"doclib\"
      },
      {
          \"id\": \"avatar\"
      }
    ]
    ```

    Args:
        node_id (str):
        version_id (str):
        body (RenditionBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        version_id=version_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    node_id: str,
    version_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: RenditionBodyCreate,
) -> Response[Any]:
    r"""Create rendition for a file version

     **Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.

    An asynchronous request to create a rendition for version of file **nodeId** and **versionId**.

    The version rendition is specified by name **id** in the request body:
    ```JSON
    {
      \"id\":\"doclib\"
    }
    ```
      Multiple names may be specified as a comma separated list or using a list format:
    ```JSON
    [
      {
          \"id\": \"doclib\"
      },
      {
          \"id\": \"avatar\"
      }
    ]
    ```

    Args:
        node_id (str):
        version_id (str):
        body (RenditionBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        version_id=version_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
