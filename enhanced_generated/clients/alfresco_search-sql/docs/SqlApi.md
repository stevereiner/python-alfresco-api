# alfresco_search-sql.SqlApi

All URIs are relative to */alfresco/api/-default-/public/search/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search**](SqlApi.md#search) | **POST** /sql | Alfresco Insight Engine SQL Passthrough

# **search**
> SQLResultSetPaging search(body)

Alfresco Insight Engine SQL Passthrough

**Note**: this endpoint is available in Alfresco 6.0 and newer versions. This will require Insight Engine and will not work with Alfresco Search Services.  **You specify all the parameters in this API in a JSON body**, A basic query looks like this:  ```JSON {   \"stmt\": \"select * from alfresco\",   \"locales\": [\"en_UK\"],   \"timezone\": \"Europe/London\",   \"includeMetadata\":true } ```  **Note:** the minimum possible query parameter required. ```JSON {   \"stmt\": } ``` The expected reponse will appear in the Alfresco format as seen below. ```JSON {   \"list\": {     \"pagination\": {       \"count\": 1,       \"hasMoreItems\": false,       \"totalItems\": 1,       \"skipCount\": 0,       \"maxItems\": 100   },   \"entries\": [{     \"entry\": [       {         \"label\": \"aliases\",         \"value\": \"{\\\"SITE\\\":\\\"site\\\"}\"       },       {         \"label\": \"isMetadata\",         \"value\": \"true\"       },       {         \"label\": \"fields\",         \"value\": \"[\\\"SITE\\\"]\"       }     ]   }]}}   ```   To override the default format set the format to solr.   ```JSON   {     \"stmt\": \"select * from alfresco\",     \"format\": \"solr\"   } ``` This will return Solr's output response. ```JSON {   \"result-set\": {   \"docs\": [     {       \"aliases\": {       \"SITE\": \"site\"     },       \"isMetadata\": true,       \"fields\": [ \"SITE\"]     },     {         \"RESPONSE_TIME\": 23,         \"EOF\": true     }   ]} } ```   You can use the **locales parameter** to filter results based on locale. ```JSON \"locales\": [\"en_UK\", \"en_US\"] ```  To include timezone in the query add the **timezone parameter**. ```JSON \"timezone\": \"Japan\" ```  To include custom filter queries add the **filterQueries parameter**. ```JSON \"filterQueries\": [\"-SITE:swsdp\"] ```  You can use the **includeMetadata parameter** to include addtional  information, this is by default set to false.  ```JSON \"includeMetadata\": \"false\" ``` Please note that if its set to true the first entry will represent the metdata requested   ```JSON  {    \"stmt\": \"select site from alfresco limit 2\",    \"includeMetadata\":true  } ``` The expected response: ```JSON \"entries\": [   {     #First entry holds the Metadata infromation as set by {includeMetadata:true}     \"entry\": [       {         \"label\": \"aliases\",         \"value\": \"{\\\"SITE\\\":\\\"site\\\"}\"        },       {         \"label\": \"isMetadata\",         \"value\": \"true\"       },       {         \"label\": \"fields\",         \"value\": \"[\\\"SITE\\\"]\"       }     ]     #end of Metadata   },   {     #Query result entry value.     \"entry\": [       {         \"label\": \"site\",         \"value\": \"[\\\"test\\\"]\"       }     ]   },   {     \"entry\": [     {       \"label\": \"site\",       \"value\": \"[\\\"test\\\"]\"     }     ]   } ] ``` 

### Example
```python
from __future__ import print_function
import time
import alfresco_search-sql
from alfresco_search-sql.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_search-sql.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_search-sql.SqlApi(alfresco_search-sql.ApiClient(configuration))
body = alfresco_search-sql.SQLSearchRequest() # SQLSearchRequest | Generic query API


try:
    # Alfresco Insight Engine SQL Passthrough
    api_response = api_instance.search(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SqlApi->search: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SQLSearchRequest**](SQLSearchRequest.md)| Generic query API
 | 

### Return type

[**SQLResultSetPaging**](SQLResultSetPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

