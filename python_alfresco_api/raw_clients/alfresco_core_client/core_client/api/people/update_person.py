from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.person_body_update import PersonBodyUpdate
from ...models.person_entry import PersonEntry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    person_id: str,
    *,
    body: PersonBodyUpdate,
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
        "method": "put",
        "url": f"/people/{person_id}",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, PersonEntry]]:
    if response.status_code == 200:
        response_200 = PersonEntry.from_dict(response.json())

        return response_200
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
    if response.status_code == 422:
        response_422 = cast(Any, None)
        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, PersonEntry]]:
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
    body: PersonBodyUpdate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, PersonEntry]]:
    r"""Update person

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Update the given person's details.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

    If applicable, the given person's login access can also be optionally disabled or re-enabled.

    You must have admin rights to update a person — unless updating your own details.

    If you are changing your password, as a non-admin user, then the existing password must also
    be supplied (using the oldPassword field in addition to the new password value).

    Admin users cannot be disabled by setting enabled to false.

    Non-admin users may not disable themselves.

    You can set custom properties when you update a person:
    ```JSON
    {
      \"firstName\": \"Alice\",
      \"properties\":
      {
        \"my:property\": \"The value\"
      }
    }
    ```
    **Note:** setting properties of type d:content and d:category are not supported.

    Args:
        person_id (str):
        fields (Union[Unset, list[str]]):
        body (PersonBodyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PersonEntry]]
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
    body: PersonBodyUpdate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, PersonEntry]]:
    r"""Update person

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Update the given person's details.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

    If applicable, the given person's login access can also be optionally disabled or re-enabled.

    You must have admin rights to update a person — unless updating your own details.

    If you are changing your password, as a non-admin user, then the existing password must also
    be supplied (using the oldPassword field in addition to the new password value).

    Admin users cannot be disabled by setting enabled to false.

    Non-admin users may not disable themselves.

    You can set custom properties when you update a person:
    ```JSON
    {
      \"firstName\": \"Alice\",
      \"properties\":
      {
        \"my:property\": \"The value\"
      }
    }
    ```
    **Note:** setting properties of type d:content and d:category are not supported.

    Args:
        person_id (str):
        fields (Union[Unset, list[str]]):
        body (PersonBodyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PersonEntry]
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
    body: PersonBodyUpdate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Union[Any, PersonEntry]]:
    r"""Update person

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Update the given person's details.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

    If applicable, the given person's login access can also be optionally disabled or re-enabled.

    You must have admin rights to update a person — unless updating your own details.

    If you are changing your password, as a non-admin user, then the existing password must also
    be supplied (using the oldPassword field in addition to the new password value).

    Admin users cannot be disabled by setting enabled to false.

    Non-admin users may not disable themselves.

    You can set custom properties when you update a person:
    ```JSON
    {
      \"firstName\": \"Alice\",
      \"properties\":
      {
        \"my:property\": \"The value\"
      }
    }
    ```
    **Note:** setting properties of type d:content and d:category are not supported.

    Args:
        person_id (str):
        fields (Union[Unset, list[str]]):
        body (PersonBodyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, PersonEntry]]
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
    body: PersonBodyUpdate,
    fields: Union[Unset, list[str]] = UNSET,
) -> Optional[Union[Any, PersonEntry]]:
    r"""Update person

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Update the given person's details.

    You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

    If applicable, the given person's login access can also be optionally disabled or re-enabled.

    You must have admin rights to update a person — unless updating your own details.

    If you are changing your password, as a non-admin user, then the existing password must also
    be supplied (using the oldPassword field in addition to the new password value).

    Admin users cannot be disabled by setting enabled to false.

    Non-admin users may not disable themselves.

    You can set custom properties when you update a person:
    ```JSON
    {
      \"firstName\": \"Alice\",
      \"properties\":
      {
        \"my:property\": \"The value\"
      }
    }
    ```
    **Note:** setting properties of type d:content and d:category are not supported.

    Args:
        person_id (str):
        fields (Union[Unset, list[str]]):
        body (PersonBodyUpdate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, PersonEntry]
    """

    return (
        await asyncio_detailed(
            person_id=person_id,
            client=client,
            body=body,
            fields=fields,
        )
    ).parsed
