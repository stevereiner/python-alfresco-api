from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.sql_result_set_paging import SQLResultSetPaging
from ...models.sql_search_request import SQLSearchRequest
from ...types import Response


def _get_kwargs(
    *,
    body: SQLSearchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/sql",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SQLResultSetPaging]:
    if response.status_code == 200:
        response_200 = SQLResultSetPaging.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SQLResultSetPaging]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SQLSearchRequest,
) -> Response[SQLResultSetPaging]:
    r"""Alfresco Insight Engine SQL Passthrough

     **Note**: this endpoint is available in Alfresco 6.0 and newer versions.
    This will require Insight Engine and will not work with Alfresco Search Services.

    **You specify all the parameters in this API in a JSON body**,
    A basic query looks like this:

    ```JSON
    {
      \"stmt\": \"select * from alfresco\",
      \"locales\": [\"en_UK\"],
      \"timezone\": \"Europe/London\",
      \"includeMetadata\":true
    }
    ```

    **Note:** the minimum possible query parameter required.
    ```JSON
    {
      \"stmt\":
    }
    ```
    The expected reponse will appear in the Alfresco format as seen below.
    ```JSON
    {
      \"list\": {
        \"pagination\": {
          \"count\": 1,
          \"hasMoreItems\": false,
          \"totalItems\": 1,
          \"skipCount\": 0,
          \"maxItems\": 100
      },
      \"entries\": [{
        \"entry\": [
          {
            \"label\": \"aliases\",
            \"value\": \"{\\"SITE\\":\\"site\\"}\"
          },
          {
            \"label\": \"isMetadata\",
            \"value\": \"true\"
          },
          {
            \"label\": \"fields\",
            \"value\": \"[\\"SITE\\"]\"
          }
        ]
      }]}}
      ```
      To override the default format set the format to solr.
      ```JSON
      {
        \"stmt\": \"select * from alfresco\",
        \"format\": \"solr\"
      }
    ```
    This will return Solr's output response.
    ```JSON
    {
      \"result-set\": {
      \"docs\": [
        {
          \"aliases\": {
          \"SITE\": \"site\"
        },
          \"isMetadata\": true,
          \"fields\": [ \"SITE\"]
        },
        {
            \"RESPONSE_TIME\": 23,
            \"EOF\": true
        }
      ]}
    }
    ```


    You can use the **locales parameter** to filter results based on locale.
    ```JSON
    \"locales\": [\"en_UK\", \"en_US\"]
    ```

    To include timezone in the query add the **timezone parameter**.
    ```JSON
    \"timezone\": \"Japan\"
    ```

    To include custom filter queries add the **filterQueries parameter**.
    ```JSON
    \"filterQueries\": [\"-SITE:swsdp\"]
    ```

    You can use the **includeMetadata parameter** to include addtional  information, this is by default
    set to false.

    ```JSON
    \"includeMetadata\": \"false\"
    ```
    Please note that if its set to true the first entry will represent the metdata requested

     ```JSON
     {
       \"stmt\": \"select site from alfresco limit 2\",
       \"includeMetadata\":true
     }
    ```
    The expected response:
    ```JSON
    \"entries\": [
      {
        #First entry holds the Metadata infromation as set by {includeMetadata:true}
        \"entry\": [
          {
            \"label\": \"aliases\",
            \"value\": \"{\\"SITE\\":\\"site\\"}\"

          },
          {
            \"label\": \"isMetadata\",
            \"value\": \"true\"
          },
          {
            \"label\": \"fields\",
            \"value\": \"[\\"SITE\\"]\"
          }
        ]
        #end of Metadata
      },
      {
        #Query result entry value.
        \"entry\": [
          {
            \"label\": \"site\",
            \"value\": \"[\\"test\\"]\"
          }
        ]
      },
      {
        \"entry\": [
        {
          \"label\": \"site\",
          \"value\": \"[\\"test\\"]\"
        }
        ]
      }
    ]
    ```

    Args:
        body (SQLSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SQLResultSetPaging]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SQLSearchRequest,
) -> Optional[SQLResultSetPaging]:
    r"""Alfresco Insight Engine SQL Passthrough

     **Note**: this endpoint is available in Alfresco 6.0 and newer versions.
    This will require Insight Engine and will not work with Alfresco Search Services.

    **You specify all the parameters in this API in a JSON body**,
    A basic query looks like this:

    ```JSON
    {
      \"stmt\": \"select * from alfresco\",
      \"locales\": [\"en_UK\"],
      \"timezone\": \"Europe/London\",
      \"includeMetadata\":true
    }
    ```

    **Note:** the minimum possible query parameter required.
    ```JSON
    {
      \"stmt\":
    }
    ```
    The expected reponse will appear in the Alfresco format as seen below.
    ```JSON
    {
      \"list\": {
        \"pagination\": {
          \"count\": 1,
          \"hasMoreItems\": false,
          \"totalItems\": 1,
          \"skipCount\": 0,
          \"maxItems\": 100
      },
      \"entries\": [{
        \"entry\": [
          {
            \"label\": \"aliases\",
            \"value\": \"{\\"SITE\\":\\"site\\"}\"
          },
          {
            \"label\": \"isMetadata\",
            \"value\": \"true\"
          },
          {
            \"label\": \"fields\",
            \"value\": \"[\\"SITE\\"]\"
          }
        ]
      }]}}
      ```
      To override the default format set the format to solr.
      ```JSON
      {
        \"stmt\": \"select * from alfresco\",
        \"format\": \"solr\"
      }
    ```
    This will return Solr's output response.
    ```JSON
    {
      \"result-set\": {
      \"docs\": [
        {
          \"aliases\": {
          \"SITE\": \"site\"
        },
          \"isMetadata\": true,
          \"fields\": [ \"SITE\"]
        },
        {
            \"RESPONSE_TIME\": 23,
            \"EOF\": true
        }
      ]}
    }
    ```


    You can use the **locales parameter** to filter results based on locale.
    ```JSON
    \"locales\": [\"en_UK\", \"en_US\"]
    ```

    To include timezone in the query add the **timezone parameter**.
    ```JSON
    \"timezone\": \"Japan\"
    ```

    To include custom filter queries add the **filterQueries parameter**.
    ```JSON
    \"filterQueries\": [\"-SITE:swsdp\"]
    ```

    You can use the **includeMetadata parameter** to include addtional  information, this is by default
    set to false.

    ```JSON
    \"includeMetadata\": \"false\"
    ```
    Please note that if its set to true the first entry will represent the metdata requested

     ```JSON
     {
       \"stmt\": \"select site from alfresco limit 2\",
       \"includeMetadata\":true
     }
    ```
    The expected response:
    ```JSON
    \"entries\": [
      {
        #First entry holds the Metadata infromation as set by {includeMetadata:true}
        \"entry\": [
          {
            \"label\": \"aliases\",
            \"value\": \"{\\"SITE\\":\\"site\\"}\"

          },
          {
            \"label\": \"isMetadata\",
            \"value\": \"true\"
          },
          {
            \"label\": \"fields\",
            \"value\": \"[\\"SITE\\"]\"
          }
        ]
        #end of Metadata
      },
      {
        #Query result entry value.
        \"entry\": [
          {
            \"label\": \"site\",
            \"value\": \"[\\"test\\"]\"
          }
        ]
      },
      {
        \"entry\": [
        {
          \"label\": \"site\",
          \"value\": \"[\\"test\\"]\"
        }
        ]
      }
    ]
    ```

    Args:
        body (SQLSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SQLResultSetPaging
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SQLSearchRequest,
) -> Response[SQLResultSetPaging]:
    r"""Alfresco Insight Engine SQL Passthrough

     **Note**: this endpoint is available in Alfresco 6.0 and newer versions.
    This will require Insight Engine and will not work with Alfresco Search Services.

    **You specify all the parameters in this API in a JSON body**,
    A basic query looks like this:

    ```JSON
    {
      \"stmt\": \"select * from alfresco\",
      \"locales\": [\"en_UK\"],
      \"timezone\": \"Europe/London\",
      \"includeMetadata\":true
    }
    ```

    **Note:** the minimum possible query parameter required.
    ```JSON
    {
      \"stmt\":
    }
    ```
    The expected reponse will appear in the Alfresco format as seen below.
    ```JSON
    {
      \"list\": {
        \"pagination\": {
          \"count\": 1,
          \"hasMoreItems\": false,
          \"totalItems\": 1,
          \"skipCount\": 0,
          \"maxItems\": 100
      },
      \"entries\": [{
        \"entry\": [
          {
            \"label\": \"aliases\",
            \"value\": \"{\\"SITE\\":\\"site\\"}\"
          },
          {
            \"label\": \"isMetadata\",
            \"value\": \"true\"
          },
          {
            \"label\": \"fields\",
            \"value\": \"[\\"SITE\\"]\"
          }
        ]
      }]}}
      ```
      To override the default format set the format to solr.
      ```JSON
      {
        \"stmt\": \"select * from alfresco\",
        \"format\": \"solr\"
      }
    ```
    This will return Solr's output response.
    ```JSON
    {
      \"result-set\": {
      \"docs\": [
        {
          \"aliases\": {
          \"SITE\": \"site\"
        },
          \"isMetadata\": true,
          \"fields\": [ \"SITE\"]
        },
        {
            \"RESPONSE_TIME\": 23,
            \"EOF\": true
        }
      ]}
    }
    ```


    You can use the **locales parameter** to filter results based on locale.
    ```JSON
    \"locales\": [\"en_UK\", \"en_US\"]
    ```

    To include timezone in the query add the **timezone parameter**.
    ```JSON
    \"timezone\": \"Japan\"
    ```

    To include custom filter queries add the **filterQueries parameter**.
    ```JSON
    \"filterQueries\": [\"-SITE:swsdp\"]
    ```

    You can use the **includeMetadata parameter** to include addtional  information, this is by default
    set to false.

    ```JSON
    \"includeMetadata\": \"false\"
    ```
    Please note that if its set to true the first entry will represent the metdata requested

     ```JSON
     {
       \"stmt\": \"select site from alfresco limit 2\",
       \"includeMetadata\":true
     }
    ```
    The expected response:
    ```JSON
    \"entries\": [
      {
        #First entry holds the Metadata infromation as set by {includeMetadata:true}
        \"entry\": [
          {
            \"label\": \"aliases\",
            \"value\": \"{\\"SITE\\":\\"site\\"}\"

          },
          {
            \"label\": \"isMetadata\",
            \"value\": \"true\"
          },
          {
            \"label\": \"fields\",
            \"value\": \"[\\"SITE\\"]\"
          }
        ]
        #end of Metadata
      },
      {
        #Query result entry value.
        \"entry\": [
          {
            \"label\": \"site\",
            \"value\": \"[\\"test\\"]\"
          }
        ]
      },
      {
        \"entry\": [
        {
          \"label\": \"site\",
          \"value\": \"[\\"test\\"]\"
        }
        ]
      }
    ]
    ```

    Args:
        body (SQLSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SQLResultSetPaging]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SQLSearchRequest,
) -> Optional[SQLResultSetPaging]:
    r"""Alfresco Insight Engine SQL Passthrough

     **Note**: this endpoint is available in Alfresco 6.0 and newer versions.
    This will require Insight Engine and will not work with Alfresco Search Services.

    **You specify all the parameters in this API in a JSON body**,
    A basic query looks like this:

    ```JSON
    {
      \"stmt\": \"select * from alfresco\",
      \"locales\": [\"en_UK\"],
      \"timezone\": \"Europe/London\",
      \"includeMetadata\":true
    }
    ```

    **Note:** the minimum possible query parameter required.
    ```JSON
    {
      \"stmt\":
    }
    ```
    The expected reponse will appear in the Alfresco format as seen below.
    ```JSON
    {
      \"list\": {
        \"pagination\": {
          \"count\": 1,
          \"hasMoreItems\": false,
          \"totalItems\": 1,
          \"skipCount\": 0,
          \"maxItems\": 100
      },
      \"entries\": [{
        \"entry\": [
          {
            \"label\": \"aliases\",
            \"value\": \"{\\"SITE\\":\\"site\\"}\"
          },
          {
            \"label\": \"isMetadata\",
            \"value\": \"true\"
          },
          {
            \"label\": \"fields\",
            \"value\": \"[\\"SITE\\"]\"
          }
        ]
      }]}}
      ```
      To override the default format set the format to solr.
      ```JSON
      {
        \"stmt\": \"select * from alfresco\",
        \"format\": \"solr\"
      }
    ```
    This will return Solr's output response.
    ```JSON
    {
      \"result-set\": {
      \"docs\": [
        {
          \"aliases\": {
          \"SITE\": \"site\"
        },
          \"isMetadata\": true,
          \"fields\": [ \"SITE\"]
        },
        {
            \"RESPONSE_TIME\": 23,
            \"EOF\": true
        }
      ]}
    }
    ```


    You can use the **locales parameter** to filter results based on locale.
    ```JSON
    \"locales\": [\"en_UK\", \"en_US\"]
    ```

    To include timezone in the query add the **timezone parameter**.
    ```JSON
    \"timezone\": \"Japan\"
    ```

    To include custom filter queries add the **filterQueries parameter**.
    ```JSON
    \"filterQueries\": [\"-SITE:swsdp\"]
    ```

    You can use the **includeMetadata parameter** to include addtional  information, this is by default
    set to false.

    ```JSON
    \"includeMetadata\": \"false\"
    ```
    Please note that if its set to true the first entry will represent the metdata requested

     ```JSON
     {
       \"stmt\": \"select site from alfresco limit 2\",
       \"includeMetadata\":true
     }
    ```
    The expected response:
    ```JSON
    \"entries\": [
      {
        #First entry holds the Metadata infromation as set by {includeMetadata:true}
        \"entry\": [
          {
            \"label\": \"aliases\",
            \"value\": \"{\\"SITE\\":\\"site\\"}\"

          },
          {
            \"label\": \"isMetadata\",
            \"value\": \"true\"
          },
          {
            \"label\": \"fields\",
            \"value\": \"[\\"SITE\\"]\"
          }
        ]
        #end of Metadata
      },
      {
        #Query result entry value.
        \"entry\": [
          {
            \"label\": \"site\",
            \"value\": \"[\\"test\\"]\"
          }
        ]
      },
      {
        \"entry\": [
        {
          \"label\": \"site\",
          \"value\": \"[\\"test\\"]\"
        }
        ]
      }
    ]
    ```

    Args:
        body (SQLSearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SQLResultSetPaging
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
