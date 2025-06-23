from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.item_body import ItemBody
from ...models.item_paging import ItemPaging
from ...types import Response


def _get_kwargs(
    task_id: str,
    *,
    body: ItemBody,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/tasks/{task_id}/items",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ItemPaging]]:
    if response.status_code == 201:
        response_201 = ItemPaging.from_dict(response.json())

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
) -> Response[Union[Any, ItemPaging]]:
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
    body: ItemBody,
) -> Response[Union[Any, ItemPaging]]:
    r"""Create an item

     Creates an item for a given task **taskId**.

    If the item  already is part of that task the request will have no effect.

    **Note:** You can create more than one item by
    specifying a list of items in the JSON body like this:

    ```JSON
    [
      {
         \"id\": \"1ff9da1a-ee2f-4b9c-8c34-44665e844444\"
      },
      {
         \"id\": \"1ff9da1a-ee2f-4b9c-8c34-44665e855555\"
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
        task_id (str):
        body (ItemBody): The **nodeId** of the item

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ItemPaging]]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ItemBody,
) -> Optional[Union[Any, ItemPaging]]:
    r"""Create an item

     Creates an item for a given task **taskId**.

    If the item  already is part of that task the request will have no effect.

    **Note:** You can create more than one item by
    specifying a list of items in the JSON body like this:

    ```JSON
    [
      {
         \"id\": \"1ff9da1a-ee2f-4b9c-8c34-44665e844444\"
      },
      {
         \"id\": \"1ff9da1a-ee2f-4b9c-8c34-44665e855555\"
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
        task_id (str):
        body (ItemBody): The **nodeId** of the item

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ItemPaging]
    """

    return sync_detailed(
        task_id=task_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ItemBody,
) -> Response[Union[Any, ItemPaging]]:
    r"""Create an item

     Creates an item for a given task **taskId**.

    If the item  already is part of that task the request will have no effect.

    **Note:** You can create more than one item by
    specifying a list of items in the JSON body like this:

    ```JSON
    [
      {
         \"id\": \"1ff9da1a-ee2f-4b9c-8c34-44665e844444\"
      },
      {
         \"id\": \"1ff9da1a-ee2f-4b9c-8c34-44665e855555\"
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
        task_id (str):
        body (ItemBody): The **nodeId** of the item

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ItemPaging]]
    """

    kwargs = _get_kwargs(
        task_id=task_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    task_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: ItemBody,
) -> Optional[Union[Any, ItemPaging]]:
    r"""Create an item

     Creates an item for a given task **taskId**.

    If the item  already is part of that task the request will have no effect.

    **Note:** You can create more than one item by
    specifying a list of items in the JSON body like this:

    ```JSON
    [
      {
         \"id\": \"1ff9da1a-ee2f-4b9c-8c34-44665e844444\"
      },
      {
         \"id\": \"1ff9da1a-ee2f-4b9c-8c34-44665e855555\"
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
        task_id (str):
        body (ItemBody): The **nodeId** of the item

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ItemPaging]
    """

    return (
        await asyncio_detailed(
            task_id=task_id,
            client=client,
            body=body,
        )
    ).parsed
