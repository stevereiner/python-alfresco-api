from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.site_membership_request_body_create import SiteMembershipRequestBodyCreate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: str,
    *,
    body: SiteMembershipRequestBodyCreate,
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
        "url": f"/people/{person_id}/site-membership-requests",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == 400:
        return None
    if response.status_code == 401:
        return None
    if response.status_code == 404:
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
    person_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteMembershipRequestBodyCreate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Any]:
    r"""Create a site membership request

     Create a site membership request for yourself on the site with the identifier of **id**, specified
    in the JSON body.
    The result of the request differs depending on the type of site.

    * For a **public** site, you join the site immediately as a SiteConsumer.
    * For a **moderated** site, your request is added to the site membership request list. The request
    waits for approval from the Site Manager.
    * You cannot request membership of a **private** site. Members are invited by the site
    administrator.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

     **Note:** You can create site membership requests for more than one site by
    specifying a list of sites in the JSON body like this:

    ```JSON
    [
      {
        \"message\": \"Please can you add me\",
        \"id\": \"test-site-1\",
        \"title\": \"Request for test site 1\",
      },
      {
        \"message\": \"Please can you add me\",
        \"id\": \"test-site-2\",
        \"title\": \"Request for test site 2\",
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
        body (SiteMembershipRequestBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
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


async def asyncio_detailed(
    person_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteMembershipRequestBodyCreate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Any]:
    r"""Create a site membership request

     Create a site membership request for yourself on the site with the identifier of **id**, specified
    in the JSON body.
    The result of the request differs depending on the type of site.

    * For a **public** site, you join the site immediately as a SiteConsumer.
    * For a **moderated** site, your request is added to the site membership request list. The request
    waits for approval from the Site Manager.
    * You cannot request membership of a **private** site. Members are invited by the site
    administrator.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

     **Note:** You can create site membership requests for more than one site by
    specifying a list of sites in the JSON body like this:

    ```JSON
    [
      {
        \"message\": \"Please can you add me\",
        \"id\": \"test-site-1\",
        \"title\": \"Request for test site 1\",
      },
      {
        \"message\": \"Please can you add me\",
        \"id\": \"test-site-2\",
        \"title\": \"Request for test site 2\",
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
        body (SiteMembershipRequestBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        person_id=person_id,
        body=body,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
