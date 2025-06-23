from http import HTTPStatus
from io import BytesIO
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import File, Response


def _get_kwargs(
    process_definition_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/process-definitions/{process_definition_id}/image",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, File]]:
    if response.status_code == 200:
        response_200 = File(payload=BytesIO(response.json()))

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
) -> Response[Union[Any, File]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    process_definition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, File]]:
    """Get a process definition image

     Gets an image that represents a single process definition identified by **processDefinitionId**.

    In non-network deployments, any authenticated user will see all the
    process definitions.

    If networks are enabled, the network admin can only see the deployments
    in the given network.

    Args:
        process_definition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        process_definition_id=process_definition_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    process_definition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, File]]:
    """Get a process definition image

     Gets an image that represents a single process definition identified by **processDefinitionId**.

    In non-network deployments, any authenticated user will see all the
    process definitions.

    If networks are enabled, the network admin can only see the deployments
    in the given network.

    Args:
        process_definition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, File]
    """

    return sync_detailed(
        process_definition_id=process_definition_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    process_definition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, File]]:
    """Get a process definition image

     Gets an image that represents a single process definition identified by **processDefinitionId**.

    In non-network deployments, any authenticated user will see all the
    process definitions.

    If networks are enabled, the network admin can only see the deployments
    in the given network.

    Args:
        process_definition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, File]]
    """

    kwargs = _get_kwargs(
        process_definition_id=process_definition_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    process_definition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, File]]:
    """Get a process definition image

     Gets an image that represents a single process definition identified by **processDefinitionId**.

    In non-network deployments, any authenticated user will see all the
    process definitions.

    If networks are enabled, the network admin can only see the deployments
    in the given network.

    Args:
        process_definition_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, File]
    """

    return (
        await asyncio_detailed(
            process_definition_id=process_definition_id,
            client=client,
        )
    ).parsed
