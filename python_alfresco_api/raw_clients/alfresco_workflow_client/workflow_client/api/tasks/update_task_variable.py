from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.variable import Variable
from ...models.variable_entry import VariableEntry
from ...types import Response


def _get_kwargs(
    task_id: str,
    variable_name: str,
    *,
    body: Variable,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/tasks/{task_id}/variables/{variable_name}",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, VariableEntry]]:
    if response.status_code == 200:
        response_200 = VariableEntry.from_dict(response.json())

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
) -> Response[Union[Any, VariableEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    task_id: str,
    variable_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Variable,
) -> Response[Union[Any, VariableEntry]]:
    """Create or update a variable

     Creates or updates a specific variable **variableName** for a given task **taskId**.

    Args:
        task_id (str):
        variable_name (str):
        body (Variable): A task variable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VariableEntry]]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        variable_name=variable_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: str,
    variable_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Variable,
) -> Optional[Union[Any, VariableEntry]]:
    """Create or update a variable

     Creates or updates a specific variable **variableName** for a given task **taskId**.

    Args:
        task_id (str):
        variable_name (str):
        body (Variable): A task variable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VariableEntry]
    """

    return sync_detailed(
        task_id=task_id,
        variable_name=variable_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    task_id: str,
    variable_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Variable,
) -> Response[Union[Any, VariableEntry]]:
    """Create or update a variable

     Creates or updates a specific variable **variableName** for a given task **taskId**.

    Args:
        task_id (str):
        variable_name (str):
        body (Variable): A task variable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VariableEntry]]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        variable_name=variable_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: str,
    variable_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Variable,
) -> Optional[Union[Any, VariableEntry]]:
    """Create or update a variable

     Creates or updates a specific variable **variableName** for a given task **taskId**.

    Args:
        task_id (str):
        variable_name (str):
        body (Variable): A task variable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VariableEntry]
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            variable_name=variable_name,
            client=client,
            body=body,
        )
    ).parsed
