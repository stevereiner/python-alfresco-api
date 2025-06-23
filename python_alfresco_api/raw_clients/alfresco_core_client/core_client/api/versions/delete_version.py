from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs(
    node_id: str,
    version_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/nodes/{node_id}/versions/{version_id}",
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
    if response.status_code == 422:
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
) -> Response[Any]:
    r"""Delete a version

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Delete the version identified by **versionId** and **nodeId*.

    If the version is successfully deleted then the content and metadata for that versioned node
    will be deleted and will no longer appear in the version history. This operation cannot be undone.

    If the most recent version is deleted the live node will revert to the next most recent version.

    We currently do not allow the last version to be deleted. If you wish to clear the history then you
    can remove the \"cm:versionable\" aspect (via update node) which will also disable versioning. In
    this
    case, you can re-enable versioning by adding back the \"cm:versionable\" aspect or using the version
    params (majorVersion and comment) on a subsequent file content update.

    Args:
        node_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        version_id=version_id,
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
) -> Response[Any]:
    r"""Delete a version

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Delete the version identified by **versionId** and **nodeId*.

    If the version is successfully deleted then the content and metadata for that versioned node
    will be deleted and will no longer appear in the version history. This operation cannot be undone.

    If the most recent version is deleted the live node will revert to the next most recent version.

    We currently do not allow the last version to be deleted. If you wish to clear the history then you
    can remove the \"cm:versionable\" aspect (via update node) which will also disable versioning. In
    this
    case, you can re-enable versioning by adding back the \"cm:versionable\" aspect or using the version
    params (majorVersion and comment) on a subsequent file content update.

    Args:
        node_id (str):
        version_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        version_id=version_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
