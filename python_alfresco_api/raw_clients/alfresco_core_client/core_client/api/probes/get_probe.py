from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.probe_entry import ProbeEntry
from ...types import Response


def _get_kwargs(
    probe_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/probes/{probe_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, ProbeEntry]]:
    if response.status_code == 200:
        response_200 = ProbeEntry.from_dict(response.json())

        return response_200
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 503:
        response_503 = cast(Any, None)
        return response_503
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, ProbeEntry]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    probe_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ProbeEntry]]:
    """Check readiness and liveness of the repository

     **Note:** this endpoint is available in Alfresco 6.0 and newer versions.

    Returns a status of 200 to indicate success and 503 for failure.

    The readiness probe is normally only used to check repository startup.

    The liveness probe should then be used to check the repository is still responding to requests.

    **Note:** No authentication is required to call this endpoint.

    Args:
        probe_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProbeEntry]]
    """

    kwargs = _get_kwargs(
        probe_id=probe_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    probe_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ProbeEntry]]:
    """Check readiness and liveness of the repository

     **Note:** this endpoint is available in Alfresco 6.0 and newer versions.

    Returns a status of 200 to indicate success and 503 for failure.

    The readiness probe is normally only used to check repository startup.

    The liveness probe should then be used to check the repository is still responding to requests.

    **Note:** No authentication is required to call this endpoint.

    Args:
        probe_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProbeEntry]
    """

    return sync_detailed(
        probe_id=probe_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    probe_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, ProbeEntry]]:
    """Check readiness and liveness of the repository

     **Note:** this endpoint is available in Alfresco 6.0 and newer versions.

    Returns a status of 200 to indicate success and 503 for failure.

    The readiness probe is normally only used to check repository startup.

    The liveness probe should then be used to check the repository is still responding to requests.

    **Note:** No authentication is required to call this endpoint.

    Args:
        probe_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProbeEntry]]
    """

    kwargs = _get_kwargs(
        probe_id=probe_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    probe_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, ProbeEntry]]:
    """Check readiness and liveness of the repository

     **Note:** this endpoint is available in Alfresco 6.0 and newer versions.

    Returns a status of 200 to indicate success and 503 for failure.

    The readiness probe is normally only used to check repository startup.

    The liveness probe should then be used to check the repository is still responding to requests.

    **Note:** No authentication is required to call this endpoint.

    Args:
        probe_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProbeEntry]
    """

    return (
        await asyncio_detailed(
            probe_id=probe_id,
            client=client,
        )
    ).parsed
