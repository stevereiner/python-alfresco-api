from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.node_paging import NodePaging
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    term: str,
    root_node_id: Union[Unset, str] = UNSET,
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    node_type: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    order_by: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["term"] = term

    params["rootNodeId"] = root_node_id

    params["skipCount"] = skip_count

    params["maxItems"] = max_items

    params["nodeType"] = node_type

    json_include: Union[Unset, list[str]] = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    json_order_by: Union[Unset, list[str]] = UNSET
    if not isinstance(order_by, Unset):
        json_order_by = order_by

    params["orderBy"] = json_order_by

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/queries/nodes",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, NodePaging]]:
    if response.status_code == 200:
        response_200 = NodePaging.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, NodePaging]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    term: str,
    root_node_id: Union[Unset, str] = UNSET,
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    node_type: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    order_by: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, NodePaging]]:
    r"""Find nodes

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets a list of nodes that match the given search criteria.

    The search term is used to look for nodes that match against name, title, description, full text
    content or tags.

    The search term:
    - must contain a minimum of 3 alphanumeric characters
    - allows \"quoted term\"
    - can optionally use '*' for wildcard matching

    By default, file and folder types will be searched unless a specific type is provided as a query
    parameter.

    By default, the search will be across the repository unless a specific root node id is provided to
    start the search from.

    You can sort the result list using the **orderBy** parameter. You can specify one or more of the
    following fields in the **orderBy** parameter:
    * name
    * modifiedAt
    * createdAt

    Args:
        term (str):
        root_node_id (Union[Unset, str]):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        node_type (Union[Unset, str]):
        include (Union[Unset, list[str]]):
        order_by (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NodePaging]]
    """

    kwargs = _get_kwargs(
        term=term,
        root_node_id=root_node_id,
        skip_count=skip_count,
        max_items=max_items,
        node_type=node_type,
        include=include,
        order_by=order_by,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    term: str,
    root_node_id: Union[Unset, str] = UNSET,
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    node_type: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    order_by: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, NodePaging]]:
    r"""Find nodes

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets a list of nodes that match the given search criteria.

    The search term is used to look for nodes that match against name, title, description, full text
    content or tags.

    The search term:
    - must contain a minimum of 3 alphanumeric characters
    - allows \"quoted term\"
    - can optionally use '*' for wildcard matching

    By default, file and folder types will be searched unless a specific type is provided as a query
    parameter.

    By default, the search will be across the repository unless a specific root node id is provided to
    start the search from.

    You can sort the result list using the **orderBy** parameter. You can specify one or more of the
    following fields in the **orderBy** parameter:
    * name
    * modifiedAt
    * createdAt

    Args:
        term (str):
        root_node_id (Union[Unset, str]):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        node_type (Union[Unset, str]):
        include (Union[Unset, list[str]]):
        order_by (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NodePaging]
    """

    return sync_detailed(
        client=client,
        term=term,
        root_node_id=root_node_id,
        skip_count=skip_count,
        max_items=max_items,
        node_type=node_type,
        include=include,
        order_by=order_by,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    term: str,
    root_node_id: Union[Unset, str] = UNSET,
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    node_type: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    order_by: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, NodePaging]]:
    r"""Find nodes

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets a list of nodes that match the given search criteria.

    The search term is used to look for nodes that match against name, title, description, full text
    content or tags.

    The search term:
    - must contain a minimum of 3 alphanumeric characters
    - allows \"quoted term\"
    - can optionally use '*' for wildcard matching

    By default, file and folder types will be searched unless a specific type is provided as a query
    parameter.

    By default, the search will be across the repository unless a specific root node id is provided to
    start the search from.

    You can sort the result list using the **orderBy** parameter. You can specify one or more of the
    following fields in the **orderBy** parameter:
    * name
    * modifiedAt
    * createdAt

    Args:
        term (str):
        root_node_id (Union[Unset, str]):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        node_type (Union[Unset, str]):
        include (Union[Unset, list[str]]):
        order_by (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, NodePaging]]
    """

    kwargs = _get_kwargs(
        term=term,
        root_node_id=root_node_id,
        skip_count=skip_count,
        max_items=max_items,
        node_type=node_type,
        include=include,
        order_by=order_by,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    term: str,
    root_node_id: Union[Unset, str] = UNSET,
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    node_type: Union[Unset, str] = UNSET,
    include: Union[Unset, list[str]] = UNSET,
    order_by: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, NodePaging]]:
    r"""Find nodes

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Gets a list of nodes that match the given search criteria.

    The search term is used to look for nodes that match against name, title, description, full text
    content or tags.

    The search term:
    - must contain a minimum of 3 alphanumeric characters
    - allows \"quoted term\"
    - can optionally use '*' for wildcard matching

    By default, file and folder types will be searched unless a specific type is provided as a query
    parameter.

    By default, the search will be across the repository unless a specific root node id is provided to
    start the search from.

    You can sort the result list using the **orderBy** parameter. You can specify one or more of the
    following fields in the **orderBy** parameter:
    * name
    * modifiedAt
    * createdAt

    Args:
        term (str):
        root_node_id (Union[Unset, str]):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        node_type (Union[Unset, str]):
        include (Union[Unset, list[str]]):
        order_by (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, NodePaging]
    """

    return (
        await asyncio_detailed(
            client=client,
            term=term,
            root_node_id=root_node_id,
            skip_count=skip_count,
            max_items=max_items,
            node_type=node_type,
            include=include,
            order_by=order_by,
            fields=fields,
        )
    ).parsed
