from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_definition_list import ActionDefinitionList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    node_id: str,
    *,
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["skipCount"] = skip_count

    params["maxItems"] = max_items

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
        "url": f"/nodes/{node_id}/action-definitions",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ActionDefinitionList, Any]]:
    if response.status_code == 200:
        response_200 = ActionDefinitionList.from_dict(response.json())

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
) -> Response[Union[ActionDefinitionList, Any]]:
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
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[ActionDefinitionList, Any]]:
    """Retrieve actions for a node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Retrieve the list of actions that may be executed against the given **nodeId**.

    The default sort order for the returned list is for actions to be sorted by ascending name.
    You can override the default by using the **orderBy** parameter.

    You can use any of the following fields to order the results:
    * name
    * title

    Args:
        node_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionDefinitionList, Any]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        skip_count=skip_count,
        max_items=max_items,
        order_by=order_by,
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
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[ActionDefinitionList, Any]]:
    """Retrieve actions for a node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Retrieve the list of actions that may be executed against the given **nodeId**.

    The default sort order for the returned list is for actions to be sorted by ascending name.
    You can override the default by using the **orderBy** parameter.

    You can use any of the following fields to order the results:
    * name
    * title

    Args:
        node_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActionDefinitionList, Any]
    """

    return sync_detailed(
        node_id=node_id,
        client=client,
        skip_count=skip_count,
        max_items=max_items,
        order_by=order_by,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[ActionDefinitionList, Any]]:
    """Retrieve actions for a node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Retrieve the list of actions that may be executed against the given **nodeId**.

    The default sort order for the returned list is for actions to be sorted by ascending name.
    You can override the default by using the **orderBy** parameter.

    You can use any of the following fields to order the results:
    * name
    * title

    Args:
        node_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionDefinitionList, Any]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        skip_count=skip_count,
        max_items=max_items,
        order_by=order_by,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    order_by: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[ActionDefinitionList, Any]]:
    """Retrieve actions for a node

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Retrieve the list of actions that may be executed against the given **nodeId**.

    The default sort order for the returned list is for actions to be sorted by ascending name.
    You can override the default by using the **orderBy** parameter.

    You can use any of the following fields to order the results:
    * name
    * title

    Args:
        node_id (str):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        order_by (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActionDefinitionList, Any]
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
            skip_count=skip_count,
            max_items=max_items,
            order_by=order_by,
            fields=fields,
        )
    ).parsed
