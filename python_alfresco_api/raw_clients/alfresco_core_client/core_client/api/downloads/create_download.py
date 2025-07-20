from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.download_body_create import DownloadBodyCreate
from ...models.download_entry import DownloadEntry
from ...types import UNSET, Unset
from typing import cast
from typing import Union



def _get_kwargs(
    *,
    body: DownloadBodyCreate,
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
        "url": "/downloads",
        "params": params,
    }

    _kwargs["json"] = body.to_dict()


    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Union[Any, DownloadEntry]]:
    if response.status_code == 202:
        response_202 = DownloadEntry.from_dict(response.json())



        return response_202
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Union[Any, DownloadEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DownloadBodyCreate,
    fields: Union[Unset, list[str]] = UNSET,

) -> Response[Union[Any, DownloadEntry]]:
    r""" Create a new download

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Creates a new download node asynchronously, the content of which will be the zipped content of the
    **nodeIds** specified in the JSON body like this:

    ```JSON
    {
        \"nodeIds\":
         [
           \"c8bb482a-ff3c-4704-a3a3-de1c83ccd84c\",
           \"cffa62db-aa01-493d-9594-058bc058eeb1\"
         ]
    }
    ```

    **Note:** The content of the download node can be obtained using the **GET
    /nodes/{downloadId}/content** endpoint

    Args:
        fields (Union[Unset, list[str]]):
        body (DownloadBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DownloadEntry]]
     """


    kwargs = _get_kwargs(
        body=body,
fields=fields,

    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)

def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DownloadBodyCreate,
    fields: Union[Unset, list[str]] = UNSET,

) -> Optional[Union[Any, DownloadEntry]]:
    r""" Create a new download

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Creates a new download node asynchronously, the content of which will be the zipped content of the
    **nodeIds** specified in the JSON body like this:

    ```JSON
    {
        \"nodeIds\":
         [
           \"c8bb482a-ff3c-4704-a3a3-de1c83ccd84c\",
           \"cffa62db-aa01-493d-9594-058bc058eeb1\"
         ]
    }
    ```

    **Note:** The content of the download node can be obtained using the **GET
    /nodes/{downloadId}/content** endpoint

    Args:
        fields (Union[Unset, list[str]]):
        body (DownloadBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DownloadEntry]
     """


    return sync_detailed(
        client=client,
body=body,
fields=fields,

    ).parsed

async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DownloadBodyCreate,
    fields: Union[Unset, list[str]] = UNSET,

) -> Response[Union[Any, DownloadEntry]]:
    r""" Create a new download

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Creates a new download node asynchronously, the content of which will be the zipped content of the
    **nodeIds** specified in the JSON body like this:

    ```JSON
    {
        \"nodeIds\":
         [
           \"c8bb482a-ff3c-4704-a3a3-de1c83ccd84c\",
           \"cffa62db-aa01-493d-9594-058bc058eeb1\"
         ]
    }
    ```

    **Note:** The content of the download node can be obtained using the **GET
    /nodes/{downloadId}/content** endpoint

    Args:
        fields (Union[Unset, list[str]]):
        body (DownloadBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, DownloadEntry]]
     """


    kwargs = _get_kwargs(
        body=body,
fields=fields,

    )

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: DownloadBodyCreate,
    fields: Union[Unset, list[str]] = UNSET,

) -> Optional[Union[Any, DownloadEntry]]:
    r""" Create a new download

     **Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.

    Creates a new download node asynchronously, the content of which will be the zipped content of the
    **nodeIds** specified in the JSON body like this:

    ```JSON
    {
        \"nodeIds\":
         [
           \"c8bb482a-ff3c-4704-a3a3-de1c83ccd84c\",
           \"cffa62db-aa01-493d-9594-058bc058eeb1\"
         ]
    }
    ```

    **Note:** The content of the download node can be obtained using the **GET
    /nodes/{downloadId}/content** endpoint

    Args:
        fields (Union[Unset, list[str]]):
        body (DownloadBodyCreate):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, DownloadEntry]
     """


    return (await asyncio_detailed(
        client=client,
body=body,
fields=fields,

    )).parsed
