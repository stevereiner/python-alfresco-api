from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.tag_body import TagBody
from ...models.tag_entry import TagEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    node_id: str,
    *,
    body: TagBody,
    fields: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/nodes/{node_id}/tags",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, TagEntry]]:
    if response.status_code == 201:
        response_201 = TagEntry.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 405:
        response_405 = cast(Any, None)
        return response_405
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, TagEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TagBody,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, TagEntry]]:
    r"""Create a tag for a node

     Creates a tag on the node **nodeId**. You specify the tag in a JSON body like this:

    ```JSON
    {
      \"tag\":\"test-tag-1\"
    }
    ```

    **Note:** You can create more than one tag by
    specifying a list of tags in the JSON body like this:

    ```JSON
    [
      {
        \"tag\":\"test-tag-1\"
      },
      {
        \"tag\":\"test-tag-2\"
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
        node_id (str):
        fields (Union[Unset, list[str]]):
        body (TagBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TagEntry]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        body=body,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TagBody,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, TagEntry]]:
    r"""Create a tag for a node

     Creates a tag on the node **nodeId**. You specify the tag in a JSON body like this:

    ```JSON
    {
      \"tag\":\"test-tag-1\"
    }
    ```

    **Note:** You can create more than one tag by
    specifying a list of tags in the JSON body like this:

    ```JSON
    [
      {
        \"tag\":\"test-tag-1\"
      },
      {
        \"tag\":\"test-tag-2\"
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
        node_id (str):
        fields (Union[Unset, list[str]]):
        body (TagBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TagEntry]
    """

    return sync_detailed(
        node_id=node_id,
        client=client,
        body=body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TagBody,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, TagEntry]]:
    r"""Create a tag for a node

     Creates a tag on the node **nodeId**. You specify the tag in a JSON body like this:

    ```JSON
    {
      \"tag\":\"test-tag-1\"
    }
    ```

    **Note:** You can create more than one tag by
    specifying a list of tags in the JSON body like this:

    ```JSON
    [
      {
        \"tag\":\"test-tag-1\"
      },
      {
        \"tag\":\"test-tag-2\"
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
        node_id (str):
        fields (Union[Unset, list[str]]):
        body (TagBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, TagEntry]]
    """

    kwargs = _get_kwargs(
        node_id=node_id,
        body=body,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    node_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: TagBody,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, TagEntry]]:
    r"""Create a tag for a node

     Creates a tag on the node **nodeId**. You specify the tag in a JSON body like this:

    ```JSON
    {
      \"tag\":\"test-tag-1\"
    }
    ```

    **Note:** You can create more than one tag by
    specifying a list of tags in the JSON body like this:

    ```JSON
    [
      {
        \"tag\":\"test-tag-1\"
      },
      {
        \"tag\":\"test-tag-2\"
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
        node_id (str):
        fields (Union[Unset, list[str]]):
        body (TagBody):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, TagEntry]
    """

    return (
        await asyncio_detailed(
            node_id=node_id,
            client=client,
            body=body,
            fields=fields,
        )
    ).parsed
