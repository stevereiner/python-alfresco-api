from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.task_form_model_paging import TaskFormModelPaging
from ...types import UNSET, Response, Unset


def _get_kwargs(
    task_id: str,
    *,
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["skipCount"] = skip_count

    params["maxItems"] = max_items

    json_properties: Union[Unset, list[str]] = UNSET
    if not isinstance(properties, Unset):
        json_properties = properties

    params["properties"] = json_properties

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/tasks/{task_id}/task-form-model",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, TaskFormModelPaging]]:
    if response.status_code == 200:
        response_200 = TaskFormModelPaging.from_dict(response.json())

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
) -> Response[Union[Any, TaskFormModelPaging]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, TaskFormModelPaging]]:
    """Get a task form model

     Gets the model of the task form type definition.

    An authenticated user will have access to  access to all task form models.
    In a network, only task form models that are inside the given network
    are returned.

    Args:
        task_id (str):
        skip_count (Union[Unset, int]):
        max_items (Union[Unset, int]):
        properties (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TaskFormModelPaging]]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        skip_count=skip_count,
        max_items=max_items,
        properties=properties,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, TaskFormModelPaging]]:
    """Get a task form model

     Gets the model of the task form type definition.

    An authenticated user will have access to  access to all task form models.
    In a network, only task form models that are inside the given network
    are returned.

    Args:
        task_id (str):
        skip_count (Union[Unset, int]):
        max_items (Union[Unset, int]):
        properties (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TaskFormModelPaging]
    """

    return sync_detailed(
        task_id=task_id,
        client=client,
        skip_count=skip_count,
        max_items=max_items,
        properties=properties,
    ).parsed


async def asyncio_detailed(
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, TaskFormModelPaging]]:
    """Get a task form model

     Gets the model of the task form type definition.

    An authenticated user will have access to  access to all task form models.
    In a network, only task form models that are inside the given network
    are returned.

    Args:
        task_id (str):
        skip_count (Union[Unset, int]):
        max_items (Union[Unset, int]):
        properties (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TaskFormModelPaging]]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        skip_count=skip_count,
        max_items=max_items,
        properties=properties,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    skip_count: Union[Unset, int] = UNSET,
    max_items: Union[Unset, int] = UNSET,
    properties: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, TaskFormModelPaging]]:
    """Get a task form model

     Gets the model of the task form type definition.

    An authenticated user will have access to  access to all task form models.
    In a network, only task form models that are inside the given network
    are returned.

    Args:
        task_id (str):
        skip_count (Union[Unset, int]):
        max_items (Union[Unset, int]):
        properties (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TaskFormModelPaging]
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            client=client,
            skip_count=skip_count,
            max_items=max_items,
            properties=properties,
        )
    ).parsed
