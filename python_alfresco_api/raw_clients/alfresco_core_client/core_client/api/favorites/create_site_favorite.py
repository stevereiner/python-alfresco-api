from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.favorite_site_body_create import FavoriteSiteBodyCreate
from ...models.favorite_site_entry import FavoriteSiteEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: str,
    *,
    body: FavoriteSiteBodyCreate,
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
        "url": f"/people/{person_id}/favorite-sites",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, FavoriteSiteEntry]]:
    if response.status_code == 201:
        response_201 = FavoriteSiteEntry.from_dict(response.json())

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
    if response.status_code == 409:
        response_409 = cast(Any, None)
        return response_409
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, FavoriteSiteEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    person_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: FavoriteSiteBodyCreate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, FavoriteSiteEntry]]:
    r"""Create a site favorite

     **Note:** this endpoint is deprecated as of Alfresco 4.2, and will be removed in the future.
    Use `/people/{personId}/favorites` instead.

    Create a site favorite for person **personId**.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

     **Note:** You can favorite more than one site by
    specifying a list of sites in the JSON body like this:

    ```JSON
    [
      {
        \"id\": \"test-site-1\"
      },
      {
        \"id\": \"test-site-2\"
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
        person_id (str):
        fields (Union[Unset, list[str]]):
        body (FavoriteSiteBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FavoriteSiteEntry]]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        body=body,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    person_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: FavoriteSiteBodyCreate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, FavoriteSiteEntry]]:
    r"""Create a site favorite

     **Note:** this endpoint is deprecated as of Alfresco 4.2, and will be removed in the future.
    Use `/people/{personId}/favorites` instead.

    Create a site favorite for person **personId**.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

     **Note:** You can favorite more than one site by
    specifying a list of sites in the JSON body like this:

    ```JSON
    [
      {
        \"id\": \"test-site-1\"
      },
      {
        \"id\": \"test-site-2\"
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
        person_id (str):
        fields (Union[Unset, list[str]]):
        body (FavoriteSiteBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FavoriteSiteEntry]
    """

    return sync_detailed(
        person_id=person_id,
        client=client,
        body=body,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    person_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: FavoriteSiteBodyCreate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, FavoriteSiteEntry]]:
    r"""Create a site favorite

     **Note:** this endpoint is deprecated as of Alfresco 4.2, and will be removed in the future.
    Use `/people/{personId}/favorites` instead.

    Create a site favorite for person **personId**.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

     **Note:** You can favorite more than one site by
    specifying a list of sites in the JSON body like this:

    ```JSON
    [
      {
        \"id\": \"test-site-1\"
      },
      {
        \"id\": \"test-site-2\"
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
        person_id (str):
        fields (Union[Unset, list[str]]):
        body (FavoriteSiteBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, FavoriteSiteEntry]]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        body=body,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    person_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: FavoriteSiteBodyCreate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, FavoriteSiteEntry]]:
    r"""Create a site favorite

     **Note:** this endpoint is deprecated as of Alfresco 4.2, and will be removed in the future.
    Use `/people/{personId}/favorites` instead.

    Create a site favorite for person **personId**.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

     **Note:** You can favorite more than one site by
    specifying a list of sites in the JSON body like this:

    ```JSON
    [
      {
        \"id\": \"test-site-1\"
      },
      {
        \"id\": \"test-site-2\"
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
        person_id (str):
        fields (Union[Unset, list[str]]):
        body (FavoriteSiteBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, FavoriteSiteEntry]
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            body=body,
            fields=fields,
        )
    ).parsed
