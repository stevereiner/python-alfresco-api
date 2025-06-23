from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.node_entry import NodeEntry
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    node_id: str,
    *,
    body: File,
    major_version: Union[Unset, bool] = False,
    comment: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["majorVersion"] = major_version

    params["comment"] = comment

    params["name"] = name

    json_include: Union[Unset, list[str]] = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/nodes/{node_id}/content",
        "params": params,
    }

    _kwargs["content"] = body.payload

    headers["Content-Type"] = "application/octet-stream"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, NodeEntry]]:
    if response.status_code == 200:
        response_200 = NodeEntry.from_dict(response.json())

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
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413
    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422
    if response.status_code == 507:
        response_507 = cast(Any, None)
        return response_507
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, NodeEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: File,
    major_version: Union[Unset, bool] = False,
    comment: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, NodeEntry]]:
    """Update node content

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Updates the content of the node with identifier **nodeId**.

    The request body for this endpoint can be any text or binary stream.

    The **majorVersion** and **comment** parameters can be used to control versioning behaviour. If the
    content is versionable,
    a new minor version is created by default.

    Optionally a new **name** parameter can also be specified that must be unique within the parent
    folder. If specified and valid then this
    will rename the node. If invalid then an error is returned and the content is not updated.

    **Note:** This API method accepts any content type, but for testing with this tool text based
    content can be provided.
    This is because the OpenAPI Specification does not allow a wildcard to be provided or the ability
    for
    tooling to accept an arbitrary file.

    Args:
        node_id (str):
        major_version (Union[Unset, bool]):  Default: False.
        comment (Union[Unset, str]):
        name (Union[Unset, str]):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NodeEntry]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        body=body,
        major_version=major_version,
        comment=comment,
        name=name,
        include=include,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: File,
    major_version: Union[Unset, bool] = False,
    comment: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, NodeEntry]]:
    """Update node content

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Updates the content of the node with identifier **nodeId**.

    The request body for this endpoint can be any text or binary stream.

    The **majorVersion** and **comment** parameters can be used to control versioning behaviour. If the
    content is versionable,
    a new minor version is created by default.

    Optionally a new **name** parameter can also be specified that must be unique within the parent
    folder. If specified and valid then this
    will rename the node. If invalid then an error is returned and the content is not updated.

    **Note:** This API method accepts any content type, but for testing with this tool text based
    content can be provided.
    This is because the OpenAPI Specification does not allow a wildcard to be provided or the ability
    for
    tooling to accept an arbitrary file.

    Args:
        node_id (str):
        major_version (Union[Unset, bool]):  Default: False.
        comment (Union[Unset, str]):
        name (Union[Unset, str]):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NodeEntry]
    """

    return sync_detailed(
        node_id=node_id,
        client=client,
        body=body,
        major_version=major_version,
        comment=comment,
        name=name,
        include=include,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: File,
    major_version: Union[Unset, bool] = False,
    comment: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, NodeEntry]]:
    """Update node content

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Updates the content of the node with identifier **nodeId**.

    The request body for this endpoint can be any text or binary stream.

    The **majorVersion** and **comment** parameters can be used to control versioning behaviour. If the
    content is versionable,
    a new minor version is created by default.

    Optionally a new **name** parameter can also be specified that must be unique within the parent
    folder. If specified and valid then this
    will rename the node. If invalid then an error is returned and the content is not updated.

    **Note:** This API method accepts any content type, but for testing with this tool text based
    content can be provided.
    This is because the OpenAPI Specification does not allow a wildcard to be provided or the ability
    for
    tooling to accept an arbitrary file.

    Args:
        node_id (str):
        major_version (Union[Unset, bool]):  Default: False.
        comment (Union[Unset, str]):
        name (Union[Unset, str]):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NodeEntry]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        body=body,
        major_version=major_version,
        comment=comment,
        name=name,
        include=include,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: File,
    major_version: Union[Unset, bool] = False,
    comment: Union[Unset, str] = UNSET,
    name: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, NodeEntry]]:
    """Update node content

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Updates the content of the node with identifier **nodeId**.

    The request body for this endpoint can be any text or binary stream.

    The **majorVersion** and **comment** parameters can be used to control versioning behaviour. If the
    content is versionable,
    a new minor version is created by default.

    Optionally a new **name** parameter can also be specified that must be unique within the parent
    folder. If specified and valid then this
    will rename the node. If invalid then an error is returned and the content is not updated.

    **Note:** This API method accepts any content type, but for testing with this tool text based
    content can be provided.
    This is because the OpenAPI Specification does not allow a wildcard to be provided or the ability
    for
    tooling to accept an arbitrary file.

    Args:
        node_id (str):
        major_version (Union[Unset, bool]):  Default: False.
        comment (Union[Unset, str]):
        name (Union[Unset, str]):
        include (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):
        body (File):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NodeEntry]
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
            body=body,
            major_version=major_version,
            comment=comment,
            name=name,
            include=include,
            fields=fields,
        )
    ).parsed
