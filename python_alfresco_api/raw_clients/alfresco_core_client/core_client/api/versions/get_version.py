from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.version_entry import VersionEntry
from ...types import Response


def _get_kwargs(
    node_id: str,
    version_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/nodes/{node_id}/versions/{version_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, VersionEntry]]:
    if response.status_code == 200:
        response_200 = VersionEntry.from_dict(response.json())

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
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, VersionEntry]]:
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
) -> Response[Union[Any, VersionEntry]]:
    """Get version information

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets the version information for **versionId** of file node **nodeId**.

    Args:
        node_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VersionEntry]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        version_id=version_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_id: str,
    version_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, VersionEntry]]:
    """Get version information

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets the version information for **versionId** of file node **nodeId**.

    Args:
        node_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VersionEntry]
    """

    return sync_detailed(
        node_id=node_id,
        version_id=version_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    node_id: str,
    version_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, VersionEntry]]:
    """Get version information

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets the version information for **versionId** of file node **nodeId**.

    Args:
        node_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VersionEntry]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        version_id=version_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: str,
    version_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, VersionEntry]]:
    """Get version information

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets the version information for **versionId** of file node **nodeId**.

    Args:
        node_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VersionEntry]
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            version_id=version_id,
            client=client,
        )
    ).parsed
