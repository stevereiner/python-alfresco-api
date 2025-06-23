from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.task_form_model_paging import TaskFormModelPaging
from ...types import UNSET, Response, Unset


def _get_kwargs(
    process_definition_id: str,
    *,
    properties: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_properties: Union[Unset, list[str]] = UNSET
    if not isinstance(properties, Unset):
        json_properties = properties

    params["properties"] = json_properties

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/process-definitions/{process_definition_id}/start-form-model",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, TaskFormModelPaging]]:
    if response.status_code == 200:
        response_200 = TaskFormModelPaging.from_dict(response.json())

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
) -> Response[Union[Any, TaskFormModelPaging]]:
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
    properties: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, TaskFormModelPaging]]:
    """Get a start form model

     Gets a model of the start form type definition.

    An authenticated user will have access to all start form models.
    In a network, only start form models that are inside the given network are returned.

    Args:
        process_definition_id (str):
        properties (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TaskFormModelPaging]]
    """

    kwargs = _get_kwargs(
        process_definition_id=process_definition_id,
        properties=properties,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    process_definition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    properties: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, TaskFormModelPaging]]:
    """Get a start form model

     Gets a model of the start form type definition.

    An authenticated user will have access to all start form models.
    In a network, only start form models that are inside the given network are returned.

    Args:
        process_definition_id (str):
        properties (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TaskFormModelPaging]
    """

    return sync_detailed(
        process_definition_id=process_definition_id,
        client=client,
        properties=properties,
    ).parsed


async def asyncio_detailed(
    process_definition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    properties: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, TaskFormModelPaging]]:
    """Get a start form model

     Gets a model of the start form type definition.

    An authenticated user will have access to all start form models.
    In a network, only start form models that are inside the given network are returned.

    Args:
        process_definition_id (str):
        properties (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TaskFormModelPaging]]
    """

    kwargs = _get_kwargs(
        process_definition_id=process_definition_id,
        properties=properties,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    process_definition_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    properties: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, TaskFormModelPaging]]:
    """Get a start form model

     Gets a model of the start form type definition.

    An authenticated user will have access to all start form models.
    In a network, only start form models that are inside the given network are returned.

    Args:
        process_definition_id (str):
        properties (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TaskFormModelPaging]
    """

    return (
        await asyncio_detailed(
            process_definition_id=process_definition_id,
            client=client,
            properties=properties,
        )
    ).parsed
