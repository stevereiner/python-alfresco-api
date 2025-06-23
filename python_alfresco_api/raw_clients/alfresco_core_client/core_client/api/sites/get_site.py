from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    site_id: str,
    *,
    relations: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_relations: Union[Unset, list[str]] = UNSET
    if not isinstance(relations, Unset):
        json_relations = relations

    params["relations"] = json_relations

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/sites/{site_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 401:
        return None
    if response.status_code == 404:
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
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    relations: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Any]:
    """Get a site

     Gets information for site **siteId**.

    You can use the **relations** parameter to include one or more related
    entities in a single response and so reduce network traffic.

    The entity types in Alfresco are organized in a tree structure.
    The **sites** entity has two children, **containers** and **members**.
    The following relations parameter returns all the container and member
    objects related to the site **siteId**:

    ```
    containers,members
    ```

    Args:
        site_id (str):
        relations (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        relations=relations,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    site_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    relations: Union[Unset, list[str]] = UNSET,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Any]:
    """Get a site

     Gets information for site **siteId**.

    You can use the **relations** parameter to include one or more related
    entities in a single response and so reduce network traffic.

    The entity types in Alfresco are organized in a tree structure.
    The **sites** entity has two children, **containers** and **members**.
    The following relations parameter returns all the container and member
    objects related to the site **siteId**:

    ```
    containers,members
    ```

    Args:
        site_id (str):
        relations (Union[Unset, list[str]]):
        fields (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        site_id=site_id,
        relations=relations,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
