from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    where: Union[Unset, str] = UNSET,
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    include: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["where"] = where

    params["skipCount"] = skip_count

    params["maxItems"] = max_items

    json_include: Union[Unset, list[str]] = UNSET
    if not isinstance(include, Unset):
        json_include = include

    params["include"] = json_include

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/aspects",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 401:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    where: Union[Unset, str] = UNSET,
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    include: Union[Unset, list[str]] = UNSET,
) -> Response[Any]:
    r"""List aspects

     **Note:** This is available in Alfresco 7.0.0 and newer versions.

    Gets a list of aspects from the data dictionary. The System aspects will be ignored by default.
    ```JSON
    {
      \"list\": {
        \"pagination\": {
          \"count\": 0,
          \"hasMoreItems\": true,
          \"totalItems\": 0,
          \"skipCount\": 0,
          \"maxItems\": 0
        },
        \"entries\": [
          {
            \"entry\": {
              \"associations\": [],
              \"mandatoryAspects\": [],
              \"includedInSupertypeQuery\": true,
              \"description\": \"Titled\",
              \"isContainer\": false,
              \"model\": {
                  \"id\": \"cm:contentmodel\",
                  \"author\": \"Alfresco\",
                  \"description\": \"Alfresco Content Domain Model\",
                  \"namespaceUri\": \"http://www.alfresco.org/model/content/1.0\",
                  \"namespacePrefix\": \"cm\"
              },
              \"id\": \"cm:titled\",
              \"title\": \"Titled\",
              \"properties\": [
                {
                  \"id\": \"cm:title\",
                  \"title\": \"Title\",
                  \"description\": \"Content Title\",
                  \"dataType\": \"d:mltext\",
                  \"isMultiValued\": false,
                  \"isMandatory\": false,
                  \"isMandatoryEnforced\": false,
                  \"isProtected\": false
                },
                {
                  ...
                }
              ]
            }
          },
          {
            \"entry\": {
              ...
            }
          },
          {
            \"entry\": {
              ...
            }
          },
        ]
      }
    }
    ```

    Args:
        where (Union[Unset, str]):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        include (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        where=where,
        skip_count=skip_count,
        max_items=max_items,
        include=include,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    where: Union[Unset, str] = UNSET,
    skip_count: Union[Unset, int] = 0,
    max_items: Union[Unset, int] = 100,
    include: Union[Unset, list[str]] = UNSET,
) -> Response[Any]:
    r"""List aspects

     **Note:** This is available in Alfresco 7.0.0 and newer versions.

    Gets a list of aspects from the data dictionary. The System aspects will be ignored by default.
    ```JSON
    {
      \"list\": {
        \"pagination\": {
          \"count\": 0,
          \"hasMoreItems\": true,
          \"totalItems\": 0,
          \"skipCount\": 0,
          \"maxItems\": 0
        },
        \"entries\": [
          {
            \"entry\": {
              \"associations\": [],
              \"mandatoryAspects\": [],
              \"includedInSupertypeQuery\": true,
              \"description\": \"Titled\",
              \"isContainer\": false,
              \"model\": {
                  \"id\": \"cm:contentmodel\",
                  \"author\": \"Alfresco\",
                  \"description\": \"Alfresco Content Domain Model\",
                  \"namespaceUri\": \"http://www.alfresco.org/model/content/1.0\",
                  \"namespacePrefix\": \"cm\"
              },
              \"id\": \"cm:titled\",
              \"title\": \"Titled\",
              \"properties\": [
                {
                  \"id\": \"cm:title\",
                  \"title\": \"Title\",
                  \"description\": \"Content Title\",
                  \"dataType\": \"d:mltext\",
                  \"isMultiValued\": false,
                  \"isMandatory\": false,
                  \"isMandatoryEnforced\": false,
                  \"isProtected\": false
                },
                {
                  ...
                }
              ]
            }
          },
          {
            \"entry\": {
              ...
            }
          },
          {
            \"entry\": {
              ...
            }
          },
        ]
      }
    }
    ```

    Args:
        where (Union[Unset, str]):
        skip_count (Union[Unset, int]):  Default: 0.
        max_items (Union[Unset, int]):  Default: 100.
        include (Union[Unset, list[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        where=where,
        skip_count=skip_count,
        max_items=max_items,
        include=include,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
