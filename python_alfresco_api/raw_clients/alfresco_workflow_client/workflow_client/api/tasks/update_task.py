from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.task_body import TaskBody
from ...models.task_entry import TaskEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    task_id: str,
    *,
    body: TaskBody,
    select: Union[Unset, int] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["select"] = select

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "put",
        "url": f"/tasks/{task_id}",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, TaskEntry]]:
    if response.status_code == 200:
        response_200 = TaskEntry.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, TaskEntry]]:
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
    body: TaskBody,
    select: Union[Unset, int] = UNSET,
) -> Response[Union[Any, TaskEntry]]:
    r"""Update a task

     Updates the state of the task **taskId**.

    To perform a task action the authenticated user must be the assignee  or
    a candidate. If networks is enabled, the task action is only
    performed  if the task is inside the given network.

    In non-network deployments, administrators can perform all operations
    on  tasks. In network deployments, network administrators can see all
    tasks  in their network and perform all operations on tasks in their
    network.

    You use the **select** parameter in the URL to specify a comma-separated list of
    properties in the
    task that you want to update. Use the JSON body to specify the new values for those
    properties.

    So for example to change the state of task **123** to **completed**, use
    this URL
    http://localhost:8080/alfresco/api/-default-/public/workflow/versions/1/tasks/123?select=state, and
    provide this request body:

    ```JSON
    {
      \"state\": \"completed\"
    }
    ```
    State Transitions
    =================

    Clients can invoke actions by assigning an allowed value to the state property of a task.
    The select parameter can be used to allow for a partial update of the resource.
    Alfresco will check for illegal state transitions and return an HTTP Bad Request (Response 400)
    if an illegal state transition is attempted.
    There are five state transitions, completing, claiming, unclaiming, delegating, resolving.

    Completing a task
    -----------------

    If variables are included in the JSON body, they will be set in the task and then the process will
    continue.

    To complete a task, the authenticated user must be the assignee of the task, the owner of the task,
    or have started the process.

    In non-network deployments, administrators can perform this task operation on all tasks.
    In network deployments, network administrators can perform this action on all tasks in their
    network.

    Here's an example PUT request

    ```
    /tasks/123?select=state,variables
    ```
    Here's is a corresponding PUT request body:

    ```JSON
    {
      “state : “completed”,
      “variables” : [
      {
        \"name\" : \"bpm_priority\",
        \"type\" : \"d_int\",
        \"value\" : 1,
        \"scope\" : \"global\"
      }
     ]
    }
    ```

    Claiming a task
    -----------------

    To claim a task, the authenticated user must be the assignee of the task,
    the owner of the task, or have started the process.

    Here's an example PUT request

    ```
    /tasks/123?select=state
    ```
    Here's a corresponding PUT request body:

    ```JSON
    {
      “state : “claimed”
    }
    ```

    Unclaiming a task
    -----------------

    This removes the current assignee of the task.

    To unclaim a task, the authenticated user must be the assignee of the task,
    the owner of the task, or have started the process.

    Here's an example PUT request

    ```
    /tasks/123?select=state
    ```
    Here's a corresponding PUT request body:

    ```JSON
    {
      “state : “unclaimed”
    }
    ```

    Delegating a task
    -----------------

    This delegates the task from the owner to an assignee.
    The result is the same as if the assignee had claimed the task,
    but the task can then be resolved and the owner will
    become the assignee again.

    To delegate a task, the authenticated user must be the
    assignee of the task and the assignee must be different from the owner.

    Here's an example PUT request

    ```
    /tasks/123?select=state,assignee
    ```
    Here's a corresponding PUT request body:

    ```JSON
    {
      “state : “delegated”,
      “assignee : “Kermit”
    }
    ```
    Resolving a task
    -----------------

    This returns a delegated task back to the owner.
    In order to delegate a task, the authenticated user
    must be the assignee of the task and the assignee must
    be different from the owner.

    To resolve a task, the authenticated user must be
    the assignee of the task, the owner of the task,
    or have started the process.

    Here's an example PUT request

    ```
    /tasks/123?select=state
    ```
    Here's a corresponding PUT request body:

    ```JSON
    {
      “state : “resolved”
    }
    ```

    Args:
        task_id (str):
        select (Union[Unset, int]):
        body (TaskBody): Input body to update a specific task.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TaskEntry]]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        body=body,
        select=select,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TaskBody,
    select: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, TaskEntry]]:
    r"""Update a task

     Updates the state of the task **taskId**.

    To perform a task action the authenticated user must be the assignee  or
    a candidate. If networks is enabled, the task action is only
    performed  if the task is inside the given network.

    In non-network deployments, administrators can perform all operations
    on  tasks. In network deployments, network administrators can see all
    tasks  in their network and perform all operations on tasks in their
    network.

    You use the **select** parameter in the URL to specify a comma-separated list of
    properties in the
    task that you want to update. Use the JSON body to specify the new values for those
    properties.

    So for example to change the state of task **123** to **completed**, use
    this URL
    http://localhost:8080/alfresco/api/-default-/public/workflow/versions/1/tasks/123?select=state, and
    provide this request body:

    ```JSON
    {
      \"state\": \"completed\"
    }
    ```
    State Transitions
    =================

    Clients can invoke actions by assigning an allowed value to the state property of a task.
    The select parameter can be used to allow for a partial update of the resource.
    Alfresco will check for illegal state transitions and return an HTTP Bad Request (Response 400)
    if an illegal state transition is attempted.
    There are five state transitions, completing, claiming, unclaiming, delegating, resolving.

    Completing a task
    -----------------

    If variables are included in the JSON body, they will be set in the task and then the process will
    continue.

    To complete a task, the authenticated user must be the assignee of the task, the owner of the task,
    or have started the process.

    In non-network deployments, administrators can perform this task operation on all tasks.
    In network deployments, network administrators can perform this action on all tasks in their
    network.

    Here's an example PUT request

    ```
    /tasks/123?select=state,variables
    ```
    Here's is a corresponding PUT request body:

    ```JSON
    {
      “state : “completed”,
      “variables” : [
      {
        \"name\" : \"bpm_priority\",
        \"type\" : \"d_int\",
        \"value\" : 1,
        \"scope\" : \"global\"
      }
     ]
    }
    ```

    Claiming a task
    -----------------

    To claim a task, the authenticated user must be the assignee of the task,
    the owner of the task, or have started the process.

    Here's an example PUT request

    ```
    /tasks/123?select=state
    ```
    Here's a corresponding PUT request body:

    ```JSON
    {
      “state : “claimed”
    }
    ```

    Unclaiming a task
    -----------------

    This removes the current assignee of the task.

    To unclaim a task, the authenticated user must be the assignee of the task,
    the owner of the task, or have started the process.

    Here's an example PUT request

    ```
    /tasks/123?select=state
    ```
    Here's a corresponding PUT request body:

    ```JSON
    {
      “state : “unclaimed”
    }
    ```

    Delegating a task
    -----------------

    This delegates the task from the owner to an assignee.
    The result is the same as if the assignee had claimed the task,
    but the task can then be resolved and the owner will
    become the assignee again.

    To delegate a task, the authenticated user must be the
    assignee of the task and the assignee must be different from the owner.

    Here's an example PUT request

    ```
    /tasks/123?select=state,assignee
    ```
    Here's a corresponding PUT request body:

    ```JSON
    {
      “state : “delegated”,
      “assignee : “Kermit”
    }
    ```
    Resolving a task
    -----------------

    This returns a delegated task back to the owner.
    In order to delegate a task, the authenticated user
    must be the assignee of the task and the assignee must
    be different from the owner.

    To resolve a task, the authenticated user must be
    the assignee of the task, the owner of the task,
    or have started the process.

    Here's an example PUT request

    ```
    /tasks/123?select=state
    ```
    Here's a corresponding PUT request body:

    ```JSON
    {
      “state : “resolved”
    }
    ```

    Args:
        task_id (str):
        select (Union[Unset, int]):
        body (TaskBody): Input body to update a specific task.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TaskEntry]
    """

    return sync_detailed(
        task_id=task_id,
        client=client,
        body=body,
        select=select,
    ).parsed


async def asyncio_detailed(
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TaskBody,
    select: Union[Unset, int] = UNSET,
) -> Response[Union[Any, TaskEntry]]:
    r"""Update a task

     Updates the state of the task **taskId**.

    To perform a task action the authenticated user must be the assignee  or
    a candidate. If networks is enabled, the task action is only
    performed  if the task is inside the given network.

    In non-network deployments, administrators can perform all operations
    on  tasks. In network deployments, network administrators can see all
    tasks  in their network and perform all operations on tasks in their
    network.

    You use the **select** parameter in the URL to specify a comma-separated list of
    properties in the
    task that you want to update. Use the JSON body to specify the new values for those
    properties.

    So for example to change the state of task **123** to **completed**, use
    this URL
    http://localhost:8080/alfresco/api/-default-/public/workflow/versions/1/tasks/123?select=state, and
    provide this request body:

    ```JSON
    {
      \"state\": \"completed\"
    }
    ```
    State Transitions
    =================

    Clients can invoke actions by assigning an allowed value to the state property of a task.
    The select parameter can be used to allow for a partial update of the resource.
    Alfresco will check for illegal state transitions and return an HTTP Bad Request (Response 400)
    if an illegal state transition is attempted.
    There are five state transitions, completing, claiming, unclaiming, delegating, resolving.

    Completing a task
    -----------------

    If variables are included in the JSON body, they will be set in the task and then the process will
    continue.

    To complete a task, the authenticated user must be the assignee of the task, the owner of the task,
    or have started the process.

    In non-network deployments, administrators can perform this task operation on all tasks.
    In network deployments, network administrators can perform this action on all tasks in their
    network.

    Here's an example PUT request

    ```
    /tasks/123?select=state,variables
    ```
    Here's is a corresponding PUT request body:

    ```JSON
    {
      “state : “completed”,
      “variables” : [
      {
        \"name\" : \"bpm_priority\",
        \"type\" : \"d_int\",
        \"value\" : 1,
        \"scope\" : \"global\"
      }
     ]
    }
    ```

    Claiming a task
    -----------------

    To claim a task, the authenticated user must be the assignee of the task,
    the owner of the task, or have started the process.

    Here's an example PUT request

    ```
    /tasks/123?select=state
    ```
    Here's a corresponding PUT request body:

    ```JSON
    {
      “state : “claimed”
    }
    ```

    Unclaiming a task
    -----------------

    This removes the current assignee of the task.

    To unclaim a task, the authenticated user must be the assignee of the task,
    the owner of the task, or have started the process.

    Here's an example PUT request

    ```
    /tasks/123?select=state
    ```
    Here's a corresponding PUT request body:

    ```JSON
    {
      “state : “unclaimed”
    }
    ```

    Delegating a task
    -----------------

    This delegates the task from the owner to an assignee.
    The result is the same as if the assignee had claimed the task,
    but the task can then be resolved and the owner will
    become the assignee again.

    To delegate a task, the authenticated user must be the
    assignee of the task and the assignee must be different from the owner.

    Here's an example PUT request

    ```
    /tasks/123?select=state,assignee
    ```
    Here's a corresponding PUT request body:

    ```JSON
    {
      “state : “delegated”,
      “assignee : “Kermit”
    }
    ```
    Resolving a task
    -----------------

    This returns a delegated task back to the owner.
    In order to delegate a task, the authenticated user
    must be the assignee of the task and the assignee must
    be different from the owner.

    To resolve a task, the authenticated user must be
    the assignee of the task, the owner of the task,
    or have started the process.

    Here's an example PUT request

    ```
    /tasks/123?select=state
    ```
    Here's a corresponding PUT request body:

    ```JSON
    {
      “state : “resolved”
    }
    ```

    Args:
        task_id (str):
        select (Union[Unset, int]):
        body (TaskBody): Input body to update a specific task.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TaskEntry]]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        body=body,
        select=select,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TaskBody,
    select: Union[Unset, int] = UNSET,
) -> Optional[Union[Any, TaskEntry]]:
    r"""Update a task

     Updates the state of the task **taskId**.

    To perform a task action the authenticated user must be the assignee  or
    a candidate. If networks is enabled, the task action is only
    performed  if the task is inside the given network.

    In non-network deployments, administrators can perform all operations
    on  tasks. In network deployments, network administrators can see all
    tasks  in their network and perform all operations on tasks in their
    network.

    You use the **select** parameter in the URL to specify a comma-separated list of
    properties in the
    task that you want to update. Use the JSON body to specify the new values for those
    properties.

    So for example to change the state of task **123** to **completed**, use
    this URL
    http://localhost:8080/alfresco/api/-default-/public/workflow/versions/1/tasks/123?select=state, and
    provide this request body:

    ```JSON
    {
      \"state\": \"completed\"
    }
    ```
    State Transitions
    =================

    Clients can invoke actions by assigning an allowed value to the state property of a task.
    The select parameter can be used to allow for a partial update of the resource.
    Alfresco will check for illegal state transitions and return an HTTP Bad Request (Response 400)
    if an illegal state transition is attempted.
    There are five state transitions, completing, claiming, unclaiming, delegating, resolving.

    Completing a task
    -----------------

    If variables are included in the JSON body, they will be set in the task and then the process will
    continue.

    To complete a task, the authenticated user must be the assignee of the task, the owner of the task,
    or have started the process.

    In non-network deployments, administrators can perform this task operation on all tasks.
    In network deployments, network administrators can perform this action on all tasks in their
    network.

    Here's an example PUT request

    ```
    /tasks/123?select=state,variables
    ```
    Here's is a corresponding PUT request body:

    ```JSON
    {
      “state : “completed”,
      “variables” : [
      {
        \"name\" : \"bpm_priority\",
        \"type\" : \"d_int\",
        \"value\" : 1,
        \"scope\" : \"global\"
      }
     ]
    }
    ```

    Claiming a task
    -----------------

    To claim a task, the authenticated user must be the assignee of the task,
    the owner of the task, or have started the process.

    Here's an example PUT request

    ```
    /tasks/123?select=state
    ```
    Here's a corresponding PUT request body:

    ```JSON
    {
      “state : “claimed”
    }
    ```

    Unclaiming a task
    -----------------

    This removes the current assignee of the task.

    To unclaim a task, the authenticated user must be the assignee of the task,
    the owner of the task, or have started the process.

    Here's an example PUT request

    ```
    /tasks/123?select=state
    ```
    Here's a corresponding PUT request body:

    ```JSON
    {
      “state : “unclaimed”
    }
    ```

    Delegating a task
    -----------------

    This delegates the task from the owner to an assignee.
    The result is the same as if the assignee had claimed the task,
    but the task can then be resolved and the owner will
    become the assignee again.

    To delegate a task, the authenticated user must be the
    assignee of the task and the assignee must be different from the owner.

    Here's an example PUT request

    ```
    /tasks/123?select=state,assignee
    ```
    Here's a corresponding PUT request body:

    ```JSON
    {
      “state : “delegated”,
      “assignee : “Kermit”
    }
    ```
    Resolving a task
    -----------------

    This returns a delegated task back to the owner.
    In order to delegate a task, the authenticated user
    must be the assignee of the task and the assignee must
    be different from the owner.

    To resolve a task, the authenticated user must be
    the assignee of the task, the owner of the task,
    or have started the process.

    Here's an example PUT request

    ```
    /tasks/123?select=state
    ```
    Here's a corresponding PUT request body:

    ```JSON
    {
      “state : “resolved”
    }
    ```

    Args:
        task_id (str):
        select (Union[Unset, int]):
        body (TaskBody): Input body to update a specific task.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TaskEntry]
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            client=client,
            body=body,
            select=select,
        )
    ).parsed
