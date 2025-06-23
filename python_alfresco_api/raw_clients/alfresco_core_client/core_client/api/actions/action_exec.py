from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.action_body_exec import ActionBodyExec
from ...models.action_exec_result_entry import ActionExecResultEntry
from ...types import Response


def _get_kwargs(
    *,
    body: ActionBodyExec,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/action-executions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ActionExecResultEntry, Any]]:
    if response.status_code == 202:
        response_202 = ActionExecResultEntry.from_dict(response.json())

        return response_202
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
) -> Response[Union[ActionExecResultEntry, Any]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ActionBodyExec,
) -> Response[Union[ActionExecResultEntry, Any]]:
    r"""Execute an action

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Executes an action

    An action may be executed against a node specified by **targetId**. For example:

    ```
    {
      \"actionDefinitionId\": \"copy\",
      \"targetId\": \"4c4b3c43-f18b-43ff-af84-751f16f1ddfd\",
      \"params\": {
        \"destination-folder\": \"34219f79-66fa-4ebf-b371-118598af898c\"
      }
    }
    ```

    Performing a POST with the request body shown above will result in the node identified by
    ```targetId```
    being copied to the destination folder specified in the ```params``` object by the key
    ```destination-folder```.

    **targetId** is optional, however, currently **targetId** must be a valid node ID.
    In the future, actions may be executed against different entity types or
    executed without the need for the context of an entity.


    Parameters supplied to the action within the ```params``` object will be converted to the expected
    type,
    where possible using the DefaultTypeConverter class. In addition:

    * Node IDs may be supplied in their short form (implicit workspace://SpacesStore prefix)
    * Aspect names may be supplied using their short form, e.g. cm:versionable or cm:auditable

    In this example, we add the aspect ```cm:versionable``` to a node using the QName resolution
    mentioned above:

    ```
    {
      \"actionDefinitionId\": \"add-features\",
      \"targetId\": \"16349e3f-2977-44d1-93f2-73c12b8083b5\",
      \"params\": {
        \"aspect-name\": \"cm:versionable\"
      }
    }
    ```

    The ```actionDefinitionId``` is the ```id``` of an action definition as returned by
    the _list actions_ operations (e.g. GET /action-definitions).

    The action will be executed **asynchronously** with a `202` HTTP response signifying that
    the request has been accepted successfully. The response body contains the unique ID of the action
    pending execution. The ID may be used, for example to correlate an execution with output in the
    server logs.

    Args:
        body (ActionBodyExec):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionExecResultEntry, Any]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ActionBodyExec,
) -> Optional[Union[ActionExecResultEntry, Any]]:
    r"""Execute an action

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Executes an action

    An action may be executed against a node specified by **targetId**. For example:

    ```
    {
      \"actionDefinitionId\": \"copy\",
      \"targetId\": \"4c4b3c43-f18b-43ff-af84-751f16f1ddfd\",
      \"params\": {
        \"destination-folder\": \"34219f79-66fa-4ebf-b371-118598af898c\"
      }
    }
    ```

    Performing a POST with the request body shown above will result in the node identified by
    ```targetId```
    being copied to the destination folder specified in the ```params``` object by the key
    ```destination-folder```.

    **targetId** is optional, however, currently **targetId** must be a valid node ID.
    In the future, actions may be executed against different entity types or
    executed without the need for the context of an entity.


    Parameters supplied to the action within the ```params``` object will be converted to the expected
    type,
    where possible using the DefaultTypeConverter class. In addition:

    * Node IDs may be supplied in their short form (implicit workspace://SpacesStore prefix)
    * Aspect names may be supplied using their short form, e.g. cm:versionable or cm:auditable

    In this example, we add the aspect ```cm:versionable``` to a node using the QName resolution
    mentioned above:

    ```
    {
      \"actionDefinitionId\": \"add-features\",
      \"targetId\": \"16349e3f-2977-44d1-93f2-73c12b8083b5\",
      \"params\": {
        \"aspect-name\": \"cm:versionable\"
      }
    }
    ```

    The ```actionDefinitionId``` is the ```id``` of an action definition as returned by
    the _list actions_ operations (e.g. GET /action-definitions).

    The action will be executed **asynchronously** with a `202` HTTP response signifying that
    the request has been accepted successfully. The response body contains the unique ID of the action
    pending execution. The ID may be used, for example to correlate an execution with output in the
    server logs.

    Args:
        body (ActionBodyExec):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActionExecResultEntry, Any]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ActionBodyExec,
) -> Response[Union[ActionExecResultEntry, Any]]:
    r"""Execute an action

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Executes an action

    An action may be executed against a node specified by **targetId**. For example:

    ```
    {
      \"actionDefinitionId\": \"copy\",
      \"targetId\": \"4c4b3c43-f18b-43ff-af84-751f16f1ddfd\",
      \"params\": {
        \"destination-folder\": \"34219f79-66fa-4ebf-b371-118598af898c\"
      }
    }
    ```

    Performing a POST with the request body shown above will result in the node identified by
    ```targetId```
    being copied to the destination folder specified in the ```params``` object by the key
    ```destination-folder```.

    **targetId** is optional, however, currently **targetId** must be a valid node ID.
    In the future, actions may be executed against different entity types or
    executed without the need for the context of an entity.


    Parameters supplied to the action within the ```params``` object will be converted to the expected
    type,
    where possible using the DefaultTypeConverter class. In addition:

    * Node IDs may be supplied in their short form (implicit workspace://SpacesStore prefix)
    * Aspect names may be supplied using their short form, e.g. cm:versionable or cm:auditable

    In this example, we add the aspect ```cm:versionable``` to a node using the QName resolution
    mentioned above:

    ```
    {
      \"actionDefinitionId\": \"add-features\",
      \"targetId\": \"16349e3f-2977-44d1-93f2-73c12b8083b5\",
      \"params\": {
        \"aspect-name\": \"cm:versionable\"
      }
    }
    ```

    The ```actionDefinitionId``` is the ```id``` of an action definition as returned by
    the _list actions_ operations (e.g. GET /action-definitions).

    The action will be executed **asynchronously** with a `202` HTTP response signifying that
    the request has been accepted successfully. The response body contains the unique ID of the action
    pending execution. The ID may be used, for example to correlate an execution with output in the
    server logs.

    Args:
        body (ActionBodyExec):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActionExecResultEntry, Any]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ActionBodyExec,
) -> Optional[Union[ActionExecResultEntry, Any]]:
    r"""Execute an action

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Executes an action

    An action may be executed against a node specified by **targetId**. For example:

    ```
    {
      \"actionDefinitionId\": \"copy\",
      \"targetId\": \"4c4b3c43-f18b-43ff-af84-751f16f1ddfd\",
      \"params\": {
        \"destination-folder\": \"34219f79-66fa-4ebf-b371-118598af898c\"
      }
    }
    ```

    Performing a POST with the request body shown above will result in the node identified by
    ```targetId```
    being copied to the destination folder specified in the ```params``` object by the key
    ```destination-folder```.

    **targetId** is optional, however, currently **targetId** must be a valid node ID.
    In the future, actions may be executed against different entity types or
    executed without the need for the context of an entity.


    Parameters supplied to the action within the ```params``` object will be converted to the expected
    type,
    where possible using the DefaultTypeConverter class. In addition:

    * Node IDs may be supplied in their short form (implicit workspace://SpacesStore prefix)
    * Aspect names may be supplied using their short form, e.g. cm:versionable or cm:auditable

    In this example, we add the aspect ```cm:versionable``` to a node using the QName resolution
    mentioned above:

    ```
    {
      \"actionDefinitionId\": \"add-features\",
      \"targetId\": \"16349e3f-2977-44d1-93f2-73c12b8083b5\",
      \"params\": {
        \"aspect-name\": \"cm:versionable\"
      }
    }
    ```

    The ```actionDefinitionId``` is the ```id``` of an action definition as returned by
    the _list actions_ operations (e.g. GET /action-definitions).

    The action will be executed **asynchronously** with a `202` HTTP response signifying that
    the request has been accepted successfully. The response body contains the unique ID of the action
    pending execution. The ID may be used, for example to correlate an execution with output in the
    server logs.

    Args:
        body (ActionBodyExec):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActionExecResultEntry, Any]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
