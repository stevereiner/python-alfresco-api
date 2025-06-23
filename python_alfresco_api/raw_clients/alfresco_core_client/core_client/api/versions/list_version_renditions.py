from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.rendition_paging import RenditionPaging
from ...types import UNSET, Response, Unset


def _get_kwargs(
    node_id: str,
    version_id: str,
    *,
    where: Union[Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["where"] = where

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/nodes/{node_id}/versions/{version_id}/renditions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, RenditionPaging]]:
    if response.status_code == 200:
        response_200 = RenditionPaging.from_dict(response.json())

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
) -> Response[Union[Any, RenditionPaging]]:
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
    where: Union[Unset, str] = UNSET,
) -> Response[Union[Any, RenditionPaging]]:
    """List renditions for a file version

     **Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.

    Gets a list of the rendition information for each rendition of the version of file **nodeId** and
    **versionId**, including the rendition id.

    Each rendition returned has a **status**: CREATED means it is available to view or download,
    NOT_CREATED means the rendition can be requested.

    You can use the **where** parameter to filter the returned renditions by **status**. For example,
    the following **where**
    clause will return just the CREATED renditions:

    ```
    (status='CREATED')
    ```

    Args:
        node_id (str):
        version_id (str):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RenditionPaging]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        version_id=version_id,
        where=where,
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
    where: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, RenditionPaging]]:
    """List renditions for a file version

     **Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.

    Gets a list of the rendition information for each rendition of the version of file **nodeId** and
    **versionId**, including the rendition id.

    Each rendition returned has a **status**: CREATED means it is available to view or download,
    NOT_CREATED means the rendition can be requested.

    You can use the **where** parameter to filter the returned renditions by **status**. For example,
    the following **where**
    clause will return just the CREATED renditions:

    ```
    (status='CREATED')
    ```

    Args:
        node_id (str):
        version_id (str):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RenditionPaging]
    """

    return sync_detailed(
        node_id=node_id,
        version_id=version_id,
        client=client,
        where=where,
    ).parsed


async def asyncio_detailed(
    node_id: str,
    version_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    where: Union[Unset, str] = UNSET,
) -> Response[Union[Any, RenditionPaging]]:
    """List renditions for a file version

     **Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.

    Gets a list of the rendition information for each rendition of the version of file **nodeId** and
    **versionId**, including the rendition id.

    Each rendition returned has a **status**: CREATED means it is available to view or download,
    NOT_CREATED means the rendition can be requested.

    You can use the **where** parameter to filter the returned renditions by **status**. For example,
    the following **where**
    clause will return just the CREATED renditions:

    ```
    (status='CREATED')
    ```

    Args:
        node_id (str):
        version_id (str):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RenditionPaging]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        version_id=version_id,
        where=where,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: str,
    version_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    where: Union[Unset, str] = UNSET,
) -> Optional[Union[Any, RenditionPaging]]:
    """List renditions for a file version

     **Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.

    Gets a list of the rendition information for each rendition of the version of file **nodeId** and
    **versionId**, including the rendition id.

    Each rendition returned has a **status**: CREATED means it is available to view or download,
    NOT_CREATED means the rendition can be requested.

    You can use the **where** parameter to filter the returned renditions by **status**. For example,
    the following **where**
    clause will return just the CREATED renditions:

    ```
    (status='CREATED')
    ```

    Args:
        node_id (str):
        version_id (str):
        where (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, RenditionPaging]
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            version_id=version_id,
            client=client,
            where=where,
        )
    ).parsed
