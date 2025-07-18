from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.result_set_paging import ResultSetPaging
from ...models.search_request import SearchRequest
from ...types import Response


def _get_kwargs(
    *,
    body: SearchRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/search",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ResultSetPaging]:
    if response.status_code == 200:
        response_200 = ResultSetPaging.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ResultSetPaging]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SearchRequest,
) -> Response[ResultSetPaging]:
    r"""Searches Alfresco

     **Note**: this endpoint is available in Alfresco 5.2 and newer versions.

    **You specify all the parameters in this API in a JSON body**, URL parameters are not supported.
    A basic query looks like this:

    ```JSON
    {
      \"query\": {
        \"query\": \"foo\"
      }
    }
    ```

    **Note:** These are the minimum possible query parameters.

    The default search language is **afts** ([Alfresco Full Text
    Search](http://docs.alfresco.com/5.1/concepts/rm-searchsyntax-intro.html)), but you can also specify
    **cmis**, and **lucene**.

    A basic CMIS query looks like this:

    ```JSON
    {
      \"query\": {
        \"query\": \"select * from cmis:folder\",
        \"language\": \"cmis\"
      }
    }
    ```

    By default, **results are limited to the first 100.**
    Results can be restricted using \"paging\". For example:
    ```JSON
    \"paging\": {
      \"maxItems\": \"50\",
      \"skipCount\": \"28\"
    }
    ```
    This example would ensure that results are **limited by Final Size**, skipping the first 28 results
    and returning the next 50.

    Alternatively, you can limit the results by using the **limits JSON body parameter**. For example,
    ```JSON
    \"limits\": {
      \"permissionEvaluationTime\": 20000,
      \"permissionEvaluationCount\": 2000
    }
    ```

    You can use the **include JSON body parameter** to return additional information.
    This works in the same way as in the /nodes/{nodeId}/children method in the core API. For example:
    ```JSON
    \"include\": [\"aspectNames\", \"properties\", \"isLink\"]
    ```

    You can use the **fields JSON body parameter** to restrict the fields returned within a response if,
    for example, you want to save on overall bandwidth.
    This works in the same way as in the /nodes/{nodeId}/children method in the core API. For example:
    ```JSON
    \"fields\": [\"id\", \"name\", \"search\"]
    ```

    You can sort the results using the **sort JSON body parameter**, for example:
    ```JSON
    \"sort\": [{\"type\":\"FIELD\", \"field\":\"cm:description\", \"ascending\":\"true\"}]
    ```
    **Note:** the **sort** parameter is not supported for CMIS queries.

    By default, search uses the **\"nodes\" location**, which is the **content store known as
    workspace://SpacesStore**.
    To change the scope to another location you can use the **locations JSON body parameter**.
    You can specify either **nodes** (the default), **versions** or **deleted-nodes**. For example:
    ```JSON
    \"scope\": {
        \"locations\": [\"deleted-nodes\"]
    }
    ```
    You can specify templates using the **templates JSON body parameter**, for example:
    ```JSON
    \"templates\": [{\"name\": \"_PERSON\",\"template\": \"|%firstName OR |%lastName OR |%userName\"},
                  {\"name\": \"mytemplate\",\"template\": \"%cm:content\"}]
    ```

    **Note: Spell checking only works on Search Services (Solr 6) if you have already enabled
    suggestions.**

    For **spell checking** you can use a query like this:
    ```JSON
    {
      \"query\": {
        \"query\": \"cm:title:alfrezco\"
      },
      \"spellcheck\": {\"query\": \"alfrezco\"}
    }
    ```

    If you are already specifying \"userQuery\" then the following may be easier and produces the same
    result :
    ```JSON
    {
      \"query\": {
        \"query\": \"cm:title:alfrezco\",
        \"userQuery\": \"alfrezco\"
      },
      \"spellcheck\": {}
    }
    ```

    The spellcheck response includes a spellCheck context like this:
    ```JSON
    \"context\": {
      \"spellCheck\": {
        \"type\": \"searchInsteadFor\",
        \"suggestions\": [\"alfresco\"]
      }
    },
    ```

    To specify defaults, you  use a **defaults JSON body parameter**, for example:
    ```JSON
    \"defaults\": {
      \"textAttributes\": [
        \"cm:content\", \"cm:name\"
      ],
      \"defaultFTSOperator\": \"AND\",
      \"defaultFTSFieldOperator\": \"OR\",
      \"namespace\": \"cm\",
      \"defaultFieldName\": \"PATH\"
    }
    ```

    You can specify several filter queries using the **filterQueries JSON body parameter**, for example:
    ```JSON
    \"filterQueries\": [{\"query\": \"TYPE:'cm:folder'\"},{\"query\": \"cm:creator:mjackson\"}]
    ```

    You can specify several facet queries using the **facetQueries JSON body parameter**, for example:
    ```JSON
    \"facetQueries\": [{\"query\": \"created:2016\",\"label\": \"CreatedThisYear\"}]
    ```
    The response will contain a matching \"context\" section, the \"label\" will match the facet query.
    ```JSON
    \"context\": {
      \"facetQueries\": [
        {\"label\": \"CreatedThisYear\",\"count\": 3}
      ]
    },
    ```

    A complete query for facetting via the content.size field looks this:
    ```JSON
    {
      \"query\": {
        \"query\": \"presentation\",
        \"language\": \"afts\"
      },
        \"facetQueries\": [
            {\"query\": \"content.size:[0 TO 10240]\", \"label\": \"xtra small\"},
            {\"query\": \"content.size:[10240 TO 102400]\", \"label\": \"small\"},
            {\"query\": \"content.size:[102400 TO 1048576]\", \"label\": \"medium\"},
            {\"query\": \"content.size:[1048576 TO 16777216]\", \"label\": \"large\"},
            {\"query\": \"content.size:[16777216 TO 134217728]\", \"label\": \"xtra large\"},
            {\"query\": \"content.size:[134217728 TO MAX]\", \"label\": \"XX large\"}
      ],
        \"facetFields\": {\"facets\": [{\"field\": \"'content.size'\"}]}
    }
    ```

    The response will contain a matching \"context\" section, the \"label\" will match the facet query.
    ```JSON
    \"context\": {
      \"facetQueries\": [
        { \"label\": \"small\",\"count\": 2 },
        { \"label\": \"large\",\"count\": 0 },
        { \"label\": \"xtra small\",\"count\": 5 },
        { \"label\": \"xtra large\",\"count\": 56},
        { \"label\": \"medium\",\"count\": 4 },
        { \"label\": \"XX large\", \"count\": 1 }
      ]
    },
    ```

    You can specify several facet fields using the **facetFields JSON body parameter**, for example:
    ```JSON
    \"facetFields\": {\"facets\": [{\"field\": \"creator\", \"mincount\": 1}, {\"field\": \"modifier\",
    \"mincount\": 1}]}
    ```
    The response will contain a matching \"context\" section, the \"label\" will match the facet field.
    ```JSON
    \"context\": {
       \"facetsFields\": [
         {  \"label\": \"creator\",
            \"buckets\": [
              { \"label\": \"System\", \"count\": 75 },
              { \"label\": \"mjackson\", \"count\": 5 }
            ]},
         {  \"label\": \"modifier\",
            \"buckets\": [
              { \"label\": \"System\", \"count\": 72 },
              { \"label\": \"mjackson\", \"count\": 5 },
              { \"label\": \"admin\", \"count\": 3 }
            ]}
       ]
    },
    ```

    Grouping facet queries that go together can be done by specifying the group label in the fact
    queries as follow:
    ```JSON
        {
            \"query\": {
                \"query\": \"presentation\"
            },
            \"facetQueries\": [
                {\"query\": \"content.size:[0 TO 102400]\", \"label\": \"small\", \"group\":\"foo\"},
                {\"query\": \"content.size:[102400 TO 1048576]\", \"label\":
    \"medium\",\"group\":\"foo\"},
                {\"query\": \"content.size:[1048576 TO 16777216]\", \"label\":
    \"large\",\"group\":\"foo\"}
            ]
        }
    ```
    The above query returns the results a faceted field grouped under the label foo:
    ```JSON
    {
        \"context\": {\"facetsFields\": [{
            \"label\": \"foo\",
            \"buckets\": [
                {
                    \"count\": 109,
                    \"label\": \"small\",
                    \"filterQuery\": \"content.size:[0 TO 102400]\"
                },
                {
                    \"count\": 0,
                    \"label\": \"large\",
                    \"filterQuery\": \"content.size:[1048576 TO 16777216]\"
                },
                {
                    \"count\": 0,
                    \"label\": \"medium\",
                    \"filterQuery\": \"content.size:[102400 TO 1048576]\"
                }
            ]
        }]
    }
    ```
    Range Faceting is supported by the **ranges JSON body parameter**, for example:
    ```JSON
        {
            \"query\": {
                \"query\": \"presentation\"
            },
            \"ranges\": [
            {
                \"field\": \"content.size\",
                 \"start\": \"0\",
                 \"end\": \"100\",
                 \"gap\": \"20\",
                 \"hardend\": true
            },
            {
                \"field\": \"created\",
                \"start\": \"2015-09-29T10:45:15.729Z\",
                \"end\": \"2016-09-29T10:45:15.729Z\",
                \"gap\": \"+100DAY\"
            }]
        }
    ```
    An example query for **search highlighting** could look like this:
    ```JSON
    {
      \"query\": {
        \"query\": \"description:workflow\",
        \"userQuery\":\"workflow\"
      },
      \"highlight\": {
        \"prefix\": \"¿\",
        \"postfix\": \"?\",
        \"mergeContiguous\": true,
        \"fields\": [
          {
            \"field\": \"cm:title\"
          },
          {
            \"field\": \"description\",
            \"prefix\": \"(\",
            \"postfix\": \")\"
          }

        ]
      }
    }
    ```
    The example above changes the highlighting prefix and postfix from the default `<em>` for all fields
    to ¿? and just for the \"description\" field to ().
    The hightlight information is added in each node entry response; here is an example partial
    response:
    ```
    \"entry\": {
            \"createdAt\": \"2016-10-12T15:24:31.202+0000\",
            \"isFolder\": true,
            \"search\": {
              \"score\": 1,
              \"highlight\": [
                {
                  \"field\": \"cm:title\",
                  \"snippets\": [
                    \"Customized ¿Workflow? Process Definitions\"
                  ]
                },
                {
                  \"field\": \"description\",
                  \"snippets\": [
                    \"Customized (Workflow) Process Definitions\"
                  ]
                }
              ]
          },
    ```
    **Note**: after the migration to Swagger UI 3, this API definition was triggering some warnings,
    more info in [this StackOverflow Q&A](https://stackoverflow.com/q/65584131/1654265).

    Args:
        body (SearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResultSetPaging]
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
    body: SearchRequest,
) -> Optional[ResultSetPaging]:
    r"""Searches Alfresco

     **Note**: this endpoint is available in Alfresco 5.2 and newer versions.

    **You specify all the parameters in this API in a JSON body**, URL parameters are not supported.
    A basic query looks like this:

    ```JSON
    {
      \"query\": {
        \"query\": \"foo\"
      }
    }
    ```

    **Note:** These are the minimum possible query parameters.

    The default search language is **afts** ([Alfresco Full Text
    Search](http://docs.alfresco.com/5.1/concepts/rm-searchsyntax-intro.html)), but you can also specify
    **cmis**, and **lucene**.

    A basic CMIS query looks like this:

    ```JSON
    {
      \"query\": {
        \"query\": \"select * from cmis:folder\",
        \"language\": \"cmis\"
      }
    }
    ```

    By default, **results are limited to the first 100.**
    Results can be restricted using \"paging\". For example:
    ```JSON
    \"paging\": {
      \"maxItems\": \"50\",
      \"skipCount\": \"28\"
    }
    ```
    This example would ensure that results are **limited by Final Size**, skipping the first 28 results
    and returning the next 50.

    Alternatively, you can limit the results by using the **limits JSON body parameter**. For example,
    ```JSON
    \"limits\": {
      \"permissionEvaluationTime\": 20000,
      \"permissionEvaluationCount\": 2000
    }
    ```

    You can use the **include JSON body parameter** to return additional information.
    This works in the same way as in the /nodes/{nodeId}/children method in the core API. For example:
    ```JSON
    \"include\": [\"aspectNames\", \"properties\", \"isLink\"]
    ```

    You can use the **fields JSON body parameter** to restrict the fields returned within a response if,
    for example, you want to save on overall bandwidth.
    This works in the same way as in the /nodes/{nodeId}/children method in the core API. For example:
    ```JSON
    \"fields\": [\"id\", \"name\", \"search\"]
    ```

    You can sort the results using the **sort JSON body parameter**, for example:
    ```JSON
    \"sort\": [{\"type\":\"FIELD\", \"field\":\"cm:description\", \"ascending\":\"true\"}]
    ```
    **Note:** the **sort** parameter is not supported for CMIS queries.

    By default, search uses the **\"nodes\" location**, which is the **content store known as
    workspace://SpacesStore**.
    To change the scope to another location you can use the **locations JSON body parameter**.
    You can specify either **nodes** (the default), **versions** or **deleted-nodes**. For example:
    ```JSON
    \"scope\": {
        \"locations\": [\"deleted-nodes\"]
    }
    ```
    You can specify templates using the **templates JSON body parameter**, for example:
    ```JSON
    \"templates\": [{\"name\": \"_PERSON\",\"template\": \"|%firstName OR |%lastName OR |%userName\"},
                  {\"name\": \"mytemplate\",\"template\": \"%cm:content\"}]
    ```

    **Note: Spell checking only works on Search Services (Solr 6) if you have already enabled
    suggestions.**

    For **spell checking** you can use a query like this:
    ```JSON
    {
      \"query\": {
        \"query\": \"cm:title:alfrezco\"
      },
      \"spellcheck\": {\"query\": \"alfrezco\"}
    }
    ```

    If you are already specifying \"userQuery\" then the following may be easier and produces the same
    result :
    ```JSON
    {
      \"query\": {
        \"query\": \"cm:title:alfrezco\",
        \"userQuery\": \"alfrezco\"
      },
      \"spellcheck\": {}
    }
    ```

    The spellcheck response includes a spellCheck context like this:
    ```JSON
    \"context\": {
      \"spellCheck\": {
        \"type\": \"searchInsteadFor\",
        \"suggestions\": [\"alfresco\"]
      }
    },
    ```

    To specify defaults, you  use a **defaults JSON body parameter**, for example:
    ```JSON
    \"defaults\": {
      \"textAttributes\": [
        \"cm:content\", \"cm:name\"
      ],
      \"defaultFTSOperator\": \"AND\",
      \"defaultFTSFieldOperator\": \"OR\",
      \"namespace\": \"cm\",
      \"defaultFieldName\": \"PATH\"
    }
    ```

    You can specify several filter queries using the **filterQueries JSON body parameter**, for example:
    ```JSON
    \"filterQueries\": [{\"query\": \"TYPE:'cm:folder'\"},{\"query\": \"cm:creator:mjackson\"}]
    ```

    You can specify several facet queries using the **facetQueries JSON body parameter**, for example:
    ```JSON
    \"facetQueries\": [{\"query\": \"created:2016\",\"label\": \"CreatedThisYear\"}]
    ```
    The response will contain a matching \"context\" section, the \"label\" will match the facet query.
    ```JSON
    \"context\": {
      \"facetQueries\": [
        {\"label\": \"CreatedThisYear\",\"count\": 3}
      ]
    },
    ```

    A complete query for facetting via the content.size field looks this:
    ```JSON
    {
      \"query\": {
        \"query\": \"presentation\",
        \"language\": \"afts\"
      },
        \"facetQueries\": [
            {\"query\": \"content.size:[0 TO 10240]\", \"label\": \"xtra small\"},
            {\"query\": \"content.size:[10240 TO 102400]\", \"label\": \"small\"},
            {\"query\": \"content.size:[102400 TO 1048576]\", \"label\": \"medium\"},
            {\"query\": \"content.size:[1048576 TO 16777216]\", \"label\": \"large\"},
            {\"query\": \"content.size:[16777216 TO 134217728]\", \"label\": \"xtra large\"},
            {\"query\": \"content.size:[134217728 TO MAX]\", \"label\": \"XX large\"}
      ],
        \"facetFields\": {\"facets\": [{\"field\": \"'content.size'\"}]}
    }
    ```

    The response will contain a matching \"context\" section, the \"label\" will match the facet query.
    ```JSON
    \"context\": {
      \"facetQueries\": [
        { \"label\": \"small\",\"count\": 2 },
        { \"label\": \"large\",\"count\": 0 },
        { \"label\": \"xtra small\",\"count\": 5 },
        { \"label\": \"xtra large\",\"count\": 56},
        { \"label\": \"medium\",\"count\": 4 },
        { \"label\": \"XX large\", \"count\": 1 }
      ]
    },
    ```

    You can specify several facet fields using the **facetFields JSON body parameter**, for example:
    ```JSON
    \"facetFields\": {\"facets\": [{\"field\": \"creator\", \"mincount\": 1}, {\"field\": \"modifier\",
    \"mincount\": 1}]}
    ```
    The response will contain a matching \"context\" section, the \"label\" will match the facet field.
    ```JSON
    \"context\": {
       \"facetsFields\": [
         {  \"label\": \"creator\",
            \"buckets\": [
              { \"label\": \"System\", \"count\": 75 },
              { \"label\": \"mjackson\", \"count\": 5 }
            ]},
         {  \"label\": \"modifier\",
            \"buckets\": [
              { \"label\": \"System\", \"count\": 72 },
              { \"label\": \"mjackson\", \"count\": 5 },
              { \"label\": \"admin\", \"count\": 3 }
            ]}
       ]
    },
    ```

    Grouping facet queries that go together can be done by specifying the group label in the fact
    queries as follow:
    ```JSON
        {
            \"query\": {
                \"query\": \"presentation\"
            },
            \"facetQueries\": [
                {\"query\": \"content.size:[0 TO 102400]\", \"label\": \"small\", \"group\":\"foo\"},
                {\"query\": \"content.size:[102400 TO 1048576]\", \"label\":
    \"medium\",\"group\":\"foo\"},
                {\"query\": \"content.size:[1048576 TO 16777216]\", \"label\":
    \"large\",\"group\":\"foo\"}
            ]
        }
    ```
    The above query returns the results a faceted field grouped under the label foo:
    ```JSON
    {
        \"context\": {\"facetsFields\": [{
            \"label\": \"foo\",
            \"buckets\": [
                {
                    \"count\": 109,
                    \"label\": \"small\",
                    \"filterQuery\": \"content.size:[0 TO 102400]\"
                },
                {
                    \"count\": 0,
                    \"label\": \"large\",
                    \"filterQuery\": \"content.size:[1048576 TO 16777216]\"
                },
                {
                    \"count\": 0,
                    \"label\": \"medium\",
                    \"filterQuery\": \"content.size:[102400 TO 1048576]\"
                }
            ]
        }]
    }
    ```
    Range Faceting is supported by the **ranges JSON body parameter**, for example:
    ```JSON
        {
            \"query\": {
                \"query\": \"presentation\"
            },
            \"ranges\": [
            {
                \"field\": \"content.size\",
                 \"start\": \"0\",
                 \"end\": \"100\",
                 \"gap\": \"20\",
                 \"hardend\": true
            },
            {
                \"field\": \"created\",
                \"start\": \"2015-09-29T10:45:15.729Z\",
                \"end\": \"2016-09-29T10:45:15.729Z\",
                \"gap\": \"+100DAY\"
            }]
        }
    ```
    An example query for **search highlighting** could look like this:
    ```JSON
    {
      \"query\": {
        \"query\": \"description:workflow\",
        \"userQuery\":\"workflow\"
      },
      \"highlight\": {
        \"prefix\": \"¿\",
        \"postfix\": \"?\",
        \"mergeContiguous\": true,
        \"fields\": [
          {
            \"field\": \"cm:title\"
          },
          {
            \"field\": \"description\",
            \"prefix\": \"(\",
            \"postfix\": \")\"
          }

        ]
      }
    }
    ```
    The example above changes the highlighting prefix and postfix from the default `<em>` for all fields
    to ¿? and just for the \"description\" field to ().
    The hightlight information is added in each node entry response; here is an example partial
    response:
    ```
    \"entry\": {
            \"createdAt\": \"2016-10-12T15:24:31.202+0000\",
            \"isFolder\": true,
            \"search\": {
              \"score\": 1,
              \"highlight\": [
                {
                  \"field\": \"cm:title\",
                  \"snippets\": [
                    \"Customized ¿Workflow? Process Definitions\"
                  ]
                },
                {
                  \"field\": \"description\",
                  \"snippets\": [
                    \"Customized (Workflow) Process Definitions\"
                  ]
                }
              ]
          },
    ```
    **Note**: after the migration to Swagger UI 3, this API definition was triggering some warnings,
    more info in [this StackOverflow Q&A](https://stackoverflow.com/q/65584131/1654265).

    Args:
        body (SearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResultSetPaging
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SearchRequest,
) -> Response[ResultSetPaging]:
    r"""Searches Alfresco

     **Note**: this endpoint is available in Alfresco 5.2 and newer versions.

    **You specify all the parameters in this API in a JSON body**, URL parameters are not supported.
    A basic query looks like this:

    ```JSON
    {
      \"query\": {
        \"query\": \"foo\"
      }
    }
    ```

    **Note:** These are the minimum possible query parameters.

    The default search language is **afts** ([Alfresco Full Text
    Search](http://docs.alfresco.com/5.1/concepts/rm-searchsyntax-intro.html)), but you can also specify
    **cmis**, and **lucene**.

    A basic CMIS query looks like this:

    ```JSON
    {
      \"query\": {
        \"query\": \"select * from cmis:folder\",
        \"language\": \"cmis\"
      }
    }
    ```

    By default, **results are limited to the first 100.**
    Results can be restricted using \"paging\". For example:
    ```JSON
    \"paging\": {
      \"maxItems\": \"50\",
      \"skipCount\": \"28\"
    }
    ```
    This example would ensure that results are **limited by Final Size**, skipping the first 28 results
    and returning the next 50.

    Alternatively, you can limit the results by using the **limits JSON body parameter**. For example,
    ```JSON
    \"limits\": {
      \"permissionEvaluationTime\": 20000,
      \"permissionEvaluationCount\": 2000
    }
    ```

    You can use the **include JSON body parameter** to return additional information.
    This works in the same way as in the /nodes/{nodeId}/children method in the core API. For example:
    ```JSON
    \"include\": [\"aspectNames\", \"properties\", \"isLink\"]
    ```

    You can use the **fields JSON body parameter** to restrict the fields returned within a response if,
    for example, you want to save on overall bandwidth.
    This works in the same way as in the /nodes/{nodeId}/children method in the core API. For example:
    ```JSON
    \"fields\": [\"id\", \"name\", \"search\"]
    ```

    You can sort the results using the **sort JSON body parameter**, for example:
    ```JSON
    \"sort\": [{\"type\":\"FIELD\", \"field\":\"cm:description\", \"ascending\":\"true\"}]
    ```
    **Note:** the **sort** parameter is not supported for CMIS queries.

    By default, search uses the **\"nodes\" location**, which is the **content store known as
    workspace://SpacesStore**.
    To change the scope to another location you can use the **locations JSON body parameter**.
    You can specify either **nodes** (the default), **versions** or **deleted-nodes**. For example:
    ```JSON
    \"scope\": {
        \"locations\": [\"deleted-nodes\"]
    }
    ```
    You can specify templates using the **templates JSON body parameter**, for example:
    ```JSON
    \"templates\": [{\"name\": \"_PERSON\",\"template\": \"|%firstName OR |%lastName OR |%userName\"},
                  {\"name\": \"mytemplate\",\"template\": \"%cm:content\"}]
    ```

    **Note: Spell checking only works on Search Services (Solr 6) if you have already enabled
    suggestions.**

    For **spell checking** you can use a query like this:
    ```JSON
    {
      \"query\": {
        \"query\": \"cm:title:alfrezco\"
      },
      \"spellcheck\": {\"query\": \"alfrezco\"}
    }
    ```

    If you are already specifying \"userQuery\" then the following may be easier and produces the same
    result :
    ```JSON
    {
      \"query\": {
        \"query\": \"cm:title:alfrezco\",
        \"userQuery\": \"alfrezco\"
      },
      \"spellcheck\": {}
    }
    ```

    The spellcheck response includes a spellCheck context like this:
    ```JSON
    \"context\": {
      \"spellCheck\": {
        \"type\": \"searchInsteadFor\",
        \"suggestions\": [\"alfresco\"]
      }
    },
    ```

    To specify defaults, you  use a **defaults JSON body parameter**, for example:
    ```JSON
    \"defaults\": {
      \"textAttributes\": [
        \"cm:content\", \"cm:name\"
      ],
      \"defaultFTSOperator\": \"AND\",
      \"defaultFTSFieldOperator\": \"OR\",
      \"namespace\": \"cm\",
      \"defaultFieldName\": \"PATH\"
    }
    ```

    You can specify several filter queries using the **filterQueries JSON body parameter**, for example:
    ```JSON
    \"filterQueries\": [{\"query\": \"TYPE:'cm:folder'\"},{\"query\": \"cm:creator:mjackson\"}]
    ```

    You can specify several facet queries using the **facetQueries JSON body parameter**, for example:
    ```JSON
    \"facetQueries\": [{\"query\": \"created:2016\",\"label\": \"CreatedThisYear\"}]
    ```
    The response will contain a matching \"context\" section, the \"label\" will match the facet query.
    ```JSON
    \"context\": {
      \"facetQueries\": [
        {\"label\": \"CreatedThisYear\",\"count\": 3}
      ]
    },
    ```

    A complete query for facetting via the content.size field looks this:
    ```JSON
    {
      \"query\": {
        \"query\": \"presentation\",
        \"language\": \"afts\"
      },
        \"facetQueries\": [
            {\"query\": \"content.size:[0 TO 10240]\", \"label\": \"xtra small\"},
            {\"query\": \"content.size:[10240 TO 102400]\", \"label\": \"small\"},
            {\"query\": \"content.size:[102400 TO 1048576]\", \"label\": \"medium\"},
            {\"query\": \"content.size:[1048576 TO 16777216]\", \"label\": \"large\"},
            {\"query\": \"content.size:[16777216 TO 134217728]\", \"label\": \"xtra large\"},
            {\"query\": \"content.size:[134217728 TO MAX]\", \"label\": \"XX large\"}
      ],
        \"facetFields\": {\"facets\": [{\"field\": \"'content.size'\"}]}
    }
    ```

    The response will contain a matching \"context\" section, the \"label\" will match the facet query.
    ```JSON
    \"context\": {
      \"facetQueries\": [
        { \"label\": \"small\",\"count\": 2 },
        { \"label\": \"large\",\"count\": 0 },
        { \"label\": \"xtra small\",\"count\": 5 },
        { \"label\": \"xtra large\",\"count\": 56},
        { \"label\": \"medium\",\"count\": 4 },
        { \"label\": \"XX large\", \"count\": 1 }
      ]
    },
    ```

    You can specify several facet fields using the **facetFields JSON body parameter**, for example:
    ```JSON
    \"facetFields\": {\"facets\": [{\"field\": \"creator\", \"mincount\": 1}, {\"field\": \"modifier\",
    \"mincount\": 1}]}
    ```
    The response will contain a matching \"context\" section, the \"label\" will match the facet field.
    ```JSON
    \"context\": {
       \"facetsFields\": [
         {  \"label\": \"creator\",
            \"buckets\": [
              { \"label\": \"System\", \"count\": 75 },
              { \"label\": \"mjackson\", \"count\": 5 }
            ]},
         {  \"label\": \"modifier\",
            \"buckets\": [
              { \"label\": \"System\", \"count\": 72 },
              { \"label\": \"mjackson\", \"count\": 5 },
              { \"label\": \"admin\", \"count\": 3 }
            ]}
       ]
    },
    ```

    Grouping facet queries that go together can be done by specifying the group label in the fact
    queries as follow:
    ```JSON
        {
            \"query\": {
                \"query\": \"presentation\"
            },
            \"facetQueries\": [
                {\"query\": \"content.size:[0 TO 102400]\", \"label\": \"small\", \"group\":\"foo\"},
                {\"query\": \"content.size:[102400 TO 1048576]\", \"label\":
    \"medium\",\"group\":\"foo\"},
                {\"query\": \"content.size:[1048576 TO 16777216]\", \"label\":
    \"large\",\"group\":\"foo\"}
            ]
        }
    ```
    The above query returns the results a faceted field grouped under the label foo:
    ```JSON
    {
        \"context\": {\"facetsFields\": [{
            \"label\": \"foo\",
            \"buckets\": [
                {
                    \"count\": 109,
                    \"label\": \"small\",
                    \"filterQuery\": \"content.size:[0 TO 102400]\"
                },
                {
                    \"count\": 0,
                    \"label\": \"large\",
                    \"filterQuery\": \"content.size:[1048576 TO 16777216]\"
                },
                {
                    \"count\": 0,
                    \"label\": \"medium\",
                    \"filterQuery\": \"content.size:[102400 TO 1048576]\"
                }
            ]
        }]
    }
    ```
    Range Faceting is supported by the **ranges JSON body parameter**, for example:
    ```JSON
        {
            \"query\": {
                \"query\": \"presentation\"
            },
            \"ranges\": [
            {
                \"field\": \"content.size\",
                 \"start\": \"0\",
                 \"end\": \"100\",
                 \"gap\": \"20\",
                 \"hardend\": true
            },
            {
                \"field\": \"created\",
                \"start\": \"2015-09-29T10:45:15.729Z\",
                \"end\": \"2016-09-29T10:45:15.729Z\",
                \"gap\": \"+100DAY\"
            }]
        }
    ```
    An example query for **search highlighting** could look like this:
    ```JSON
    {
      \"query\": {
        \"query\": \"description:workflow\",
        \"userQuery\":\"workflow\"
      },
      \"highlight\": {
        \"prefix\": \"¿\",
        \"postfix\": \"?\",
        \"mergeContiguous\": true,
        \"fields\": [
          {
            \"field\": \"cm:title\"
          },
          {
            \"field\": \"description\",
            \"prefix\": \"(\",
            \"postfix\": \")\"
          }

        ]
      }
    }
    ```
    The example above changes the highlighting prefix and postfix from the default `<em>` for all fields
    to ¿? and just for the \"description\" field to ().
    The hightlight information is added in each node entry response; here is an example partial
    response:
    ```
    \"entry\": {
            \"createdAt\": \"2016-10-12T15:24:31.202+0000\",
            \"isFolder\": true,
            \"search\": {
              \"score\": 1,
              \"highlight\": [
                {
                  \"field\": \"cm:title\",
                  \"snippets\": [
                    \"Customized ¿Workflow? Process Definitions\"
                  ]
                },
                {
                  \"field\": \"description\",
                  \"snippets\": [
                    \"Customized (Workflow) Process Definitions\"
                  ]
                }
              ]
          },
    ```
    **Note**: after the migration to Swagger UI 3, this API definition was triggering some warnings,
    more info in [this StackOverflow Q&A](https://stackoverflow.com/q/65584131/1654265).

    Args:
        body (SearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ResultSetPaging]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: SearchRequest,
) -> Optional[ResultSetPaging]:
    r"""Searches Alfresco

     **Note**: this endpoint is available in Alfresco 5.2 and newer versions.

    **You specify all the parameters in this API in a JSON body**, URL parameters are not supported.
    A basic query looks like this:

    ```JSON
    {
      \"query\": {
        \"query\": \"foo\"
      }
    }
    ```

    **Note:** These are the minimum possible query parameters.

    The default search language is **afts** ([Alfresco Full Text
    Search](http://docs.alfresco.com/5.1/concepts/rm-searchsyntax-intro.html)), but you can also specify
    **cmis**, and **lucene**.

    A basic CMIS query looks like this:

    ```JSON
    {
      \"query\": {
        \"query\": \"select * from cmis:folder\",
        \"language\": \"cmis\"
      }
    }
    ```

    By default, **results are limited to the first 100.**
    Results can be restricted using \"paging\". For example:
    ```JSON
    \"paging\": {
      \"maxItems\": \"50\",
      \"skipCount\": \"28\"
    }
    ```
    This example would ensure that results are **limited by Final Size**, skipping the first 28 results
    and returning the next 50.

    Alternatively, you can limit the results by using the **limits JSON body parameter**. For example,
    ```JSON
    \"limits\": {
      \"permissionEvaluationTime\": 20000,
      \"permissionEvaluationCount\": 2000
    }
    ```

    You can use the **include JSON body parameter** to return additional information.
    This works in the same way as in the /nodes/{nodeId}/children method in the core API. For example:
    ```JSON
    \"include\": [\"aspectNames\", \"properties\", \"isLink\"]
    ```

    You can use the **fields JSON body parameter** to restrict the fields returned within a response if,
    for example, you want to save on overall bandwidth.
    This works in the same way as in the /nodes/{nodeId}/children method in the core API. For example:
    ```JSON
    \"fields\": [\"id\", \"name\", \"search\"]
    ```

    You can sort the results using the **sort JSON body parameter**, for example:
    ```JSON
    \"sort\": [{\"type\":\"FIELD\", \"field\":\"cm:description\", \"ascending\":\"true\"}]
    ```
    **Note:** the **sort** parameter is not supported for CMIS queries.

    By default, search uses the **\"nodes\" location**, which is the **content store known as
    workspace://SpacesStore**.
    To change the scope to another location you can use the **locations JSON body parameter**.
    You can specify either **nodes** (the default), **versions** or **deleted-nodes**. For example:
    ```JSON
    \"scope\": {
        \"locations\": [\"deleted-nodes\"]
    }
    ```
    You can specify templates using the **templates JSON body parameter**, for example:
    ```JSON
    \"templates\": [{\"name\": \"_PERSON\",\"template\": \"|%firstName OR |%lastName OR |%userName\"},
                  {\"name\": \"mytemplate\",\"template\": \"%cm:content\"}]
    ```

    **Note: Spell checking only works on Search Services (Solr 6) if you have already enabled
    suggestions.**

    For **spell checking** you can use a query like this:
    ```JSON
    {
      \"query\": {
        \"query\": \"cm:title:alfrezco\"
      },
      \"spellcheck\": {\"query\": \"alfrezco\"}
    }
    ```

    If you are already specifying \"userQuery\" then the following may be easier and produces the same
    result :
    ```JSON
    {
      \"query\": {
        \"query\": \"cm:title:alfrezco\",
        \"userQuery\": \"alfrezco\"
      },
      \"spellcheck\": {}
    }
    ```

    The spellcheck response includes a spellCheck context like this:
    ```JSON
    \"context\": {
      \"spellCheck\": {
        \"type\": \"searchInsteadFor\",
        \"suggestions\": [\"alfresco\"]
      }
    },
    ```

    To specify defaults, you  use a **defaults JSON body parameter**, for example:
    ```JSON
    \"defaults\": {
      \"textAttributes\": [
        \"cm:content\", \"cm:name\"
      ],
      \"defaultFTSOperator\": \"AND\",
      \"defaultFTSFieldOperator\": \"OR\",
      \"namespace\": \"cm\",
      \"defaultFieldName\": \"PATH\"
    }
    ```

    You can specify several filter queries using the **filterQueries JSON body parameter**, for example:
    ```JSON
    \"filterQueries\": [{\"query\": \"TYPE:'cm:folder'\"},{\"query\": \"cm:creator:mjackson\"}]
    ```

    You can specify several facet queries using the **facetQueries JSON body parameter**, for example:
    ```JSON
    \"facetQueries\": [{\"query\": \"created:2016\",\"label\": \"CreatedThisYear\"}]
    ```
    The response will contain a matching \"context\" section, the \"label\" will match the facet query.
    ```JSON
    \"context\": {
      \"facetQueries\": [
        {\"label\": \"CreatedThisYear\",\"count\": 3}
      ]
    },
    ```

    A complete query for facetting via the content.size field looks this:
    ```JSON
    {
      \"query\": {
        \"query\": \"presentation\",
        \"language\": \"afts\"
      },
        \"facetQueries\": [
            {\"query\": \"content.size:[0 TO 10240]\", \"label\": \"xtra small\"},
            {\"query\": \"content.size:[10240 TO 102400]\", \"label\": \"small\"},
            {\"query\": \"content.size:[102400 TO 1048576]\", \"label\": \"medium\"},
            {\"query\": \"content.size:[1048576 TO 16777216]\", \"label\": \"large\"},
            {\"query\": \"content.size:[16777216 TO 134217728]\", \"label\": \"xtra large\"},
            {\"query\": \"content.size:[134217728 TO MAX]\", \"label\": \"XX large\"}
      ],
        \"facetFields\": {\"facets\": [{\"field\": \"'content.size'\"}]}
    }
    ```

    The response will contain a matching \"context\" section, the \"label\" will match the facet query.
    ```JSON
    \"context\": {
      \"facetQueries\": [
        { \"label\": \"small\",\"count\": 2 },
        { \"label\": \"large\",\"count\": 0 },
        { \"label\": \"xtra small\",\"count\": 5 },
        { \"label\": \"xtra large\",\"count\": 56},
        { \"label\": \"medium\",\"count\": 4 },
        { \"label\": \"XX large\", \"count\": 1 }
      ]
    },
    ```

    You can specify several facet fields using the **facetFields JSON body parameter**, for example:
    ```JSON
    \"facetFields\": {\"facets\": [{\"field\": \"creator\", \"mincount\": 1}, {\"field\": \"modifier\",
    \"mincount\": 1}]}
    ```
    The response will contain a matching \"context\" section, the \"label\" will match the facet field.
    ```JSON
    \"context\": {
       \"facetsFields\": [
         {  \"label\": \"creator\",
            \"buckets\": [
              { \"label\": \"System\", \"count\": 75 },
              { \"label\": \"mjackson\", \"count\": 5 }
            ]},
         {  \"label\": \"modifier\",
            \"buckets\": [
              { \"label\": \"System\", \"count\": 72 },
              { \"label\": \"mjackson\", \"count\": 5 },
              { \"label\": \"admin\", \"count\": 3 }
            ]}
       ]
    },
    ```

    Grouping facet queries that go together can be done by specifying the group label in the fact
    queries as follow:
    ```JSON
        {
            \"query\": {
                \"query\": \"presentation\"
            },
            \"facetQueries\": [
                {\"query\": \"content.size:[0 TO 102400]\", \"label\": \"small\", \"group\":\"foo\"},
                {\"query\": \"content.size:[102400 TO 1048576]\", \"label\":
    \"medium\",\"group\":\"foo\"},
                {\"query\": \"content.size:[1048576 TO 16777216]\", \"label\":
    \"large\",\"group\":\"foo\"}
            ]
        }
    ```
    The above query returns the results a faceted field grouped under the label foo:
    ```JSON
    {
        \"context\": {\"facetsFields\": [{
            \"label\": \"foo\",
            \"buckets\": [
                {
                    \"count\": 109,
                    \"label\": \"small\",
                    \"filterQuery\": \"content.size:[0 TO 102400]\"
                },
                {
                    \"count\": 0,
                    \"label\": \"large\",
                    \"filterQuery\": \"content.size:[1048576 TO 16777216]\"
                },
                {
                    \"count\": 0,
                    \"label\": \"medium\",
                    \"filterQuery\": \"content.size:[102400 TO 1048576]\"
                }
            ]
        }]
    }
    ```
    Range Faceting is supported by the **ranges JSON body parameter**, for example:
    ```JSON
        {
            \"query\": {
                \"query\": \"presentation\"
            },
            \"ranges\": [
            {
                \"field\": \"content.size\",
                 \"start\": \"0\",
                 \"end\": \"100\",
                 \"gap\": \"20\",
                 \"hardend\": true
            },
            {
                \"field\": \"created\",
                \"start\": \"2015-09-29T10:45:15.729Z\",
                \"end\": \"2016-09-29T10:45:15.729Z\",
                \"gap\": \"+100DAY\"
            }]
        }
    ```
    An example query for **search highlighting** could look like this:
    ```JSON
    {
      \"query\": {
        \"query\": \"description:workflow\",
        \"userQuery\":\"workflow\"
      },
      \"highlight\": {
        \"prefix\": \"¿\",
        \"postfix\": \"?\",
        \"mergeContiguous\": true,
        \"fields\": [
          {
            \"field\": \"cm:title\"
          },
          {
            \"field\": \"description\",
            \"prefix\": \"(\",
            \"postfix\": \")\"
          }

        ]
      }
    }
    ```
    The example above changes the highlighting prefix and postfix from the default `<em>` for all fields
    to ¿? and just for the \"description\" field to ().
    The hightlight information is added in each node entry response; here is an example partial
    response:
    ```
    \"entry\": {
            \"createdAt\": \"2016-10-12T15:24:31.202+0000\",
            \"isFolder\": true,
            \"search\": {
              \"score\": 1,
              \"highlight\": [
                {
                  \"field\": \"cm:title\",
                  \"snippets\": [
                    \"Customized ¿Workflow? Process Definitions\"
                  ]
                },
                {
                  \"field\": \"description\",
                  \"snippets\": [
                    \"Customized (Workflow) Process Definitions\"
                  ]
                }
              ]
          },
    ```
    **Note**: after the migration to Swagger UI 3, this API definition was triggering some warnings,
    more info in [this StackOverflow Q&A](https://stackoverflow.com/q/65584131/1654265).

    Args:
        body (SearchRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ResultSetPaging
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
