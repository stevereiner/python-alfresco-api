from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_definition_entry import ActionDefinitionEntry
from ...types import Response


def _get_kwargs(
    action_definition_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/action-definitions/{action_definition_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ActionDefinitionEntry, Any]]:
    if response.status_code == 200:
        response_200 = ActionDefinitionEntry.from_dict(response.json())

        return response_200
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
) -> Response[Union[ActionDefinitionEntry, Any]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    action_definition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ActionDefinitionEntry, Any]]:
    """Retrieve the details of an action definition

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Retrieve the details of the action denoted by **actionDefinitionId**.

    Args:
        action_definition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionDefinitionEntry, Any]]
    """

    kwargs = _get_kwargs(
        action_definition_id=action_definition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    action_definition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ActionDefinitionEntry, Any]]:
    """Retrieve the details of an action definition

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Retrieve the details of the action denoted by **actionDefinitionId**.

    Args:
        action_definition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActionDefinitionEntry, Any]
    """

    return sync_detailed(
        action_definition_id=action_definition_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    action_definition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[ActionDefinitionEntry, Any]]:
    """Retrieve the details of an action definition

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Retrieve the details of the action denoted by **actionDefinitionId**.

    Args:
        action_definition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionDefinitionEntry, Any]]
    """

    kwargs = _get_kwargs(
        action_definition_id=action_definition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    action_definition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[ActionDefinitionEntry, Any]]:
    """Retrieve the details of an action definition

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Retrieve the details of the action denoted by **actionDefinitionId**.

    Args:
        action_definition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActionDefinitionEntry, Any]
    """

    return (
        await asyncio_detailed(
            action_definition_id=action_definition_id,
            client=client,
        )
    ).parsed
