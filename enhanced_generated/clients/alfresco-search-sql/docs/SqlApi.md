# alfresco_search_sql_client.SqlApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/search/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SqlApi.md#search) | **POST** /sql | Alfresco Insight Engine SQL Passthrough


# **search**
> SQLResultSetPaging search()

Alfresco Insight Engine SQL Passthrough

**Note**: this endpoint is available in Alfresco 6.0 and newer versions.
This will require Insight Engine and will not work with Alfresco Search Services.

**You specify all the parameters in this API in a JSON body**,
A basic query looks like this:

```JSON
{
  "stmt": "select * from alfresco",
  "locales": ["en_UK"],
  "timezone": "Europe/London",
  "includeMetadata":true
}
```

**Note:** the minimum possible query parameter required.
```JSON
{
  "stmt":
}
```
The expected reponse will appear in the Alfresco format as seen below.
```JSON
{
  "list": {
    "pagination": {
      "count": 1,
      "hasMoreItems": false,
      "totalItems": 1,
      "skipCount": 0,
      "maxItems": 100
  },
  "entries": [{
    "entry": [
      {
        "label": "aliases",
        "value": "{\"SITE\":\"site\"}"
      },
      {
        "label": "isMetadata",
        "value": "true"
      },
      {
        "label": "fields",
        "value": "[\"SITE\"]"
      }
    ]
  }]}}
  ```
  To override the default format set the format to solr.
  ```JSON
  {
    "stmt": "select * from alfresco",
    "format": "solr"
  }
```
This will return Solr's output response.
```JSON
{
  "result-set": {
  "docs": [
    {
      "aliases": {
      "SITE": "site"
    },
      "isMetadata": true,
      "fields": [ "SITE"]
    },
    {
        "RESPONSE_TIME": 23,
        "EOF": true
    }
  ]}
}
```


You can use the **locales parameter** to filter results based on locale.
```JSON
"locales": ["en_UK", "en_US"]
```

To include timezone in the query add the **timezone parameter**.
```JSON
"timezone": "Japan"
```

To include custom filter queries add the **filterQueries parameter**.
```JSON
"filterQueries": ["-SITE:swsdp"]
```

You can use the **includeMetadata parameter** to include addtional  information, this is by default set to false.

```JSON
"includeMetadata": "false"
```
Please note that if its set to true the first entry will represent the metdata requested

 ```JSON
 {
   "stmt": "select site from alfresco limit 2",
   "includeMetadata":true
 }
```
The expected response:
```JSON
"entries": [
  {
    #First entry holds the Metadata infromation as set by {includeMetadata:true}
    "entry": [
      {
        "label": "aliases",
        "value": "{\"SITE\":\"site\"}"

      },
      {
        "label": "isMetadata",
        "value": "true"
      },
      {
        "label": "fields",
        "value": "[\"SITE\"]"
      }
    ]
    #end of Metadata
  },
  {
    #Query result entry value.
    "entry": [
      {
        "label": "site",
        "value": "[\"test\"]"
      }
    ]
  },
  {
    "entry": [
    {
      "label": "site",
      "value": "[\"test\"]"
    }
    ]
  }
]
```


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_search_sql_client
from alfresco_search_sql_client.models.sql_result_set_paging import SQLResultSetPaging
from alfresco_search_sql_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/search/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_search_sql_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/search/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_search_sql_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_search_sql_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_search_sql_client.SqlApi(api_client)

    try:
        # Alfresco Insight Engine SQL Passthrough
        api_response = api_instance.search()
        print("The response of SqlApi->search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SqlApi->search: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SQLResultSetPaging**](SQLResultSetPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

