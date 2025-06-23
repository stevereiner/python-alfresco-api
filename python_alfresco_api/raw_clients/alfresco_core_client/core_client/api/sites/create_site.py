from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.site_body_create import SiteBodyCreate
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: SiteBodyCreate,
    skip_configuration: Union[Unset, bool] = False,
    skip_add_to_favorites: Union[Unset, bool] = False,
    fields: Union[Unset, list[str]] = UNSET,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["skipConfiguration"] = skip_configuration

    params["skipAddToFavorites"] = skip_add_to_favorites

    json_fields: Union[Unset, list[str]] = UNSET
    if not isinstance(fields, Unset):
        json_fields = fields

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sites",
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
    if response.status_code == 409:
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
    body: SiteBodyCreate,
    skip_configuration: Union[Unset, bool] = False,
    skip_add_to_favorites: Union[Unset, bool] = False,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Any]:
    r"""Create a site

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Creates a default site with the given details.  Unless explicitly specified, the site id will be
    generated
    from the site title. The site id must be unique and only contain alphanumeric and/or dash
    characters.

    Note: the id of a site cannot be updated once the site has been created.

    For example, to create a public site called \"Marketing\" the following body could be used:
    ```JSON
    {
      \"title\": \"Marketing\",
      \"visibility\": \"PUBLIC\"
    }
    ```

    The creation of the (surf) configuration files required by Share can be skipped via the
    **skipConfiguration** query parameter.

    **Note:** if skipped then such a site will **not** work within Share.

    The addition of the site to the user's site favorites can be skipped via the **skipAddToFavorites**
    query parameter.

    The creator will be added as a member with Site Manager role.

    When you create a site, a container called **documentLibrary** is created for you in the new site.
    This container is the root folder for content stored in the site.

    Args:
        skip_configuration (Union[Unset, bool]):  Default: False.
        skip_add_to_favorites (Union[Unset, bool]):  Default: False.
        fields (Union[Unset, list[str]]):
        body (SiteBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        skip_configuration=skip_configuration,
        skip_add_to_favorites=skip_add_to_favorites,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SiteBodyCreate,
    skip_configuration: Union[Unset, bool] = False,
    skip_add_to_favorites: Union[Unset, bool] = False,
    fields: Union[Unset, list[str]] = UNSET,
) -> Response[Any]:
    r"""Create a site

     **Note:** this endpoint is available in Alfresco 5.2 and newer versions.

    Creates a default site with the given details.  Unless explicitly specified, the site id will be
    generated
    from the site title. The site id must be unique and only contain alphanumeric and/or dash
    characters.

    Note: the id of a site cannot be updated once the site has been created.

    For example, to create a public site called \"Marketing\" the following body could be used:
    ```JSON
    {
      \"title\": \"Marketing\",
      \"visibility\": \"PUBLIC\"
    }
    ```

    The creation of the (surf) configuration files required by Share can be skipped via the
    **skipConfiguration** query parameter.

    **Note:** if skipped then such a site will **not** work within Share.

    The addition of the site to the user's site favorites can be skipped via the **skipAddToFavorites**
    query parameter.

    The creator will be added as a member with Site Manager role.

    When you create a site, a container called **documentLibrary** is created for you in the new site.
    This container is the root folder for content stored in the site.

    Args:
        skip_configuration (Union[Unset, bool]):  Default: False.
        skip_add_to_favorites (Union[Unset, bool]):  Default: False.
        fields (Union[Unset, list[str]]):
        body (SiteBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
        skip_configuration=skip_configuration,
        skip_add_to_favorites=skip_add_to_favorites,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
