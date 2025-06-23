from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.variable_body import VariableBody
from ...models.variable_entry import VariableEntry
from ...types import Response


def _get_kwargs(
    process_id: str,
    *,
    body: VariableBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/processes/{process_id}/variables",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, VariableEntry]]:
    if response.status_code == 201:
        response_201 = VariableEntry.from_dict(response.json())

        return response_201
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
    process_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: VariableBody,
) -> Response[Union[Any, VariableEntry]]:
    r"""Create or update variables

     Create or update a variable for a given process.
    If the variable does not exist yet, it will be created.


    **Note:** You can create or update more than one variable by
    specifying a list of variables in the JSON body like this:

    ```JSON
    [
      {
        \"name\": \"string\",
        \"value\": \"string\",
        \"type\": \"string\"
      },
      {
        \"name\": \"string\",
        \"value\": \"string\",
        \"type\": \"string\"
      }
    ]
    ```
    If you specify a list as input, then a paginated list rather than an entry is returned in the
    response body. For example:

    ```JSON
    {
      \"list\": {
        \"pagination\": {
          \"count\": 2,
          \"hasMoreItems\": false,
          \"totalItems\": 2,
          \"skipCount\": 0,
          \"maxItems\": 100
        },
        \"entries\": [
          {
            \"entry\": {
              ...
            }
          },
          {
            \"entry\": {
             ...
            }
          }
        ]
      }
    }
    ```

    Args:
        process_id (str):
        body (VariableBody): An input process variable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VariableEntry]]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    process_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: VariableBody,
) -> Optional[Union[Any, VariableEntry]]:
    r"""Create or update variables

     Create or update a variable for a given process.
    If the variable does not exist yet, it will be created.


    **Note:** You can create or update more than one variable by
    specifying a list of variables in the JSON body like this:

    ```JSON
    [
      {
        \"name\": \"string\",
        \"value\": \"string\",
        \"type\": \"string\"
      },
      {
        \"name\": \"string\",
        \"value\": \"string\",
        \"type\": \"string\"
      }
    ]
    ```
    If you specify a list as input, then a paginated list rather than an entry is returned in the
    response body. For example:

    ```JSON
    {
      \"list\": {
        \"pagination\": {
          \"count\": 2,
          \"hasMoreItems\": false,
          \"totalItems\": 2,
          \"skipCount\": 0,
          \"maxItems\": 100
        },
        \"entries\": [
          {
            \"entry\": {
              ...
            }
          },
          {
            \"entry\": {
             ...
            }
          }
        ]
      }
    }
    ```

    Args:
        process_id (str):
        body (VariableBody): An input process variable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VariableEntry]
    """

    return sync_detailed(
        process_id=process_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    process_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: VariableBody,
) -> Response[Union[Any, VariableEntry]]:
    r"""Create or update variables

     Create or update a variable for a given process.
    If the variable does not exist yet, it will be created.


    **Note:** You can create or update more than one variable by
    specifying a list of variables in the JSON body like this:

    ```JSON
    [
      {
        \"name\": \"string\",
        \"value\": \"string\",
        \"type\": \"string\"
      },
      {
        \"name\": \"string\",
        \"value\": \"string\",
        \"type\": \"string\"
      }
    ]
    ```
    If you specify a list as input, then a paginated list rather than an entry is returned in the
    response body. For example:

    ```JSON
    {
      \"list\": {
        \"pagination\": {
          \"count\": 2,
          \"hasMoreItems\": false,
          \"totalItems\": 2,
          \"skipCount\": 0,
          \"maxItems\": 100
        },
        \"entries\": [
          {
            \"entry\": {
              ...
            }
          },
          {
            \"entry\": {
             ...
            }
          }
        ]
      }
    }
    ```

    Args:
        process_id (str):
        body (VariableBody): An input process variable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, VariableEntry]]
    """

    kwargs = _get_kwargs(
        process_id=process_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    process_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: VariableBody,
) -> Optional[Union[Any, VariableEntry]]:
    r"""Create or update variables

     Create or update a variable for a given process.
    If the variable does not exist yet, it will be created.


    **Note:** You can create or update more than one variable by
    specifying a list of variables in the JSON body like this:

    ```JSON
    [
      {
        \"name\": \"string\",
        \"value\": \"string\",
        \"type\": \"string\"
      },
      {
        \"name\": \"string\",
        \"value\": \"string\",
        \"type\": \"string\"
      }
    ]
    ```
    If you specify a list as input, then a paginated list rather than an entry is returned in the
    response body. For example:

    ```JSON
    {
      \"list\": {
        \"pagination\": {
          \"count\": 2,
          \"hasMoreItems\": false,
          \"totalItems\": 2,
          \"skipCount\": 0,
          \"maxItems\": 100
        },
        \"entries\": [
          {
            \"entry\": {
              ...
            }
          },
          {
            \"entry\": {
             ...
            }
          }
        ]
      }
    }
    ```

    Args:
        process_id (str):
        body (VariableBody): An input process variable.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, VariableEntry]
    """

    return (
        await asyncio_detailed(
            process_id=process_id,
            client=client,
            body=body,
        )
    ).parsed
