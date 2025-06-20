# alfresco_core.AuditApi

All URIs are relative to */alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_audit_entries_for_audit_app**](AuditApi.md#delete_audit_entries_for_audit_app) | **DELETE** /audit-applications/{auditApplicationId}/audit-entries | Permanently delete audit entries for an audit application
[**delete_audit_entry**](AuditApi.md#delete_audit_entry) | **DELETE** /audit-applications/{auditApplicationId}/audit-entries/{auditEntryId} | Permanently delete an audit entry
[**get_audit_app**](AuditApi.md#get_audit_app) | **GET** /audit-applications/{auditApplicationId} | Get audit application info
[**get_audit_entry**](AuditApi.md#get_audit_entry) | **GET** /audit-applications/{auditApplicationId}/audit-entries/{auditEntryId} | Get audit entry
[**list_audit_apps**](AuditApi.md#list_audit_apps) | **GET** /audit-applications | List audit applications
[**list_audit_entries_for_audit_app**](AuditApi.md#list_audit_entries_for_audit_app) | **GET** /audit-applications/{auditApplicationId}/audit-entries | List audit entries for an audit application
[**list_audit_entries_for_node**](AuditApi.md#list_audit_entries_for_node) | **GET** /nodes/{nodeId}/audit-entries | List audit entries for a node
[**update_audit_app**](AuditApi.md#update_audit_app) | **PUT** /audit-applications/{auditApplicationId} | Update audit application info

# **delete_audit_entries_for_audit_app**
> delete_audit_entries_for_audit_app(audit_application_id, where)

Permanently delete audit entries for an audit application

**Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.  Permanently delete audit entries for an audit application **auditApplicationId**.  The **where** clause must be specified, either with an inclusive time period or for an inclusive range of ids. The delete is within the context of the given audit application.  For example:  *   ```where=(createdAt BETWEEN ('2017-06-02T12:13:51.593+01:00' , '2017-06-04T10:05:16.536+01:00')``` *   ```where=(id BETWEEN ('1234', '4321')```  You must have admin rights to delete audit information. 

### Example
```python
from __future__ import print_function
import time
import alfresco_core
from alfresco_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_core.AuditApi(alfresco_core.ApiClient(configuration))
audit_application_id = 'audit_application_id_example' # str | The identifier of an audit application.
where = 'where_example' # str | Audit entries to permanently delete for an audit application, given an inclusive time period or range of ids. For example:  *   ```where=(createdAt BETWEEN ('2017-06-02T12:13:51.593+01:00' , '2017-06-04T10:05:16.536+01:00')``` *   ```where=(id BETWEEN ('1234', '4321')``` 

try:
    # Permanently delete audit entries for an audit application
    api_instance.delete_audit_entries_for_audit_app(audit_application_id, where)
except ApiException as e:
    print("Exception when calling AuditApi->delete_audit_entries_for_audit_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_application_id** | **str**| The identifier of an audit application. | 
 **where** | **str**| Audit entries to permanently delete for an audit application, given an inclusive time period or range of ids. For example:  *   &#x60;&#x60;&#x60;where&#x3D;(createdAt BETWEEN (&#x27;2017-06-02T12:13:51.593+01:00&#x27; , &#x27;2017-06-04T10:05:16.536+01:00&#x27;)&#x60;&#x60;&#x60; *   &#x60;&#x60;&#x60;where&#x3D;(id BETWEEN (&#x27;1234&#x27;, &#x27;4321&#x27;)&#x60;&#x60;&#x60;  | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_audit_entry**
> delete_audit_entry(audit_application_id, audit_entry_id)

Permanently delete an audit entry

**Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.  Permanently delete a single audit entry **auditEntryId**.  You must have admin rights to delete audit information. 

### Example
```python
from __future__ import print_function
import time
import alfresco_core
from alfresco_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_core.AuditApi(alfresco_core.ApiClient(configuration))
audit_application_id = 'audit_application_id_example' # str | The identifier of an audit application.
audit_entry_id = 'audit_entry_id_example' # str | The identifier of an audit entry.

try:
    # Permanently delete an audit entry
    api_instance.delete_audit_entry(audit_application_id, audit_entry_id)
except ApiException as e:
    print("Exception when calling AuditApi->delete_audit_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_application_id** | **str**| The identifier of an audit application. | 
 **audit_entry_id** | **str**| The identifier of an audit entry. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_app**
> AuditApp get_audit_app(audit_application_id, fields=fields, include=include)

Get audit application info

**Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.  Get status of an audit application **auditApplicationId**.  You must have admin rights to retrieve audit information.  You can use the **include** parameter to return the minimum and/or maximum audit record id for the application. 

### Example
```python
from __future__ import print_function
import time
import alfresco_core
from alfresco_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_core.AuditApi(alfresco_core.ApiClient(configuration))
audit_application_id = 'audit_application_id_example' # str | The identifier of an audit application.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)
include = ['include_example'] # list[str] | Also include the current minimum and/or maximum audit entry ids for the application. The following optional fields can be requested: * max * min  (optional)

try:
    # Get audit application info
    api_response = api_instance.get_audit_app(audit_application_id, fields=fields, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_audit_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_application_id** | **str**| The identifier of an audit application. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 
 **include** | [**list[str]**](str.md)| Also include the current minimum and/or maximum audit entry ids for the application. The following optional fields can be requested: * max * min  | [optional] 

### Return type

[**AuditApp**](AuditApp.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_audit_entry**
> AuditEntryEntry get_audit_entry(audit_application_id, audit_entry_id, fields=fields)

Get audit entry

**Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.  Gets audit entry **auditEntryId**.  You must have admin rights to access audit information. 

### Example
```python
from __future__ import print_function
import time
import alfresco_core
from alfresco_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_core.AuditApi(alfresco_core.ApiClient(configuration))
audit_application_id = 'audit_application_id_example' # str | The identifier of an audit application.
audit_entry_id = 'audit_entry_id_example' # str | The identifier of an audit entry.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Get audit entry
    api_response = api_instance.get_audit_entry(audit_application_id, audit_entry_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->get_audit_entry: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_application_id** | **str**| The identifier of an audit application. | 
 **audit_entry_id** | **str**| The identifier of an audit entry. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**AuditEntryEntry**](AuditEntryEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_audit_apps**
> AuditAppPaging list_audit_apps(skip_count=skip_count, max_items=max_items, fields=fields)

List audit applications

**Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.  Gets a list of audit applications in this repository.  This list may include pre-configured audit applications, if enabled, such as:  * alfresco-access * CMISChangeLog * Alfresco Tagging Service * Alfresco Sync Service (used by Enterprise Cloud Sync)  You must have admin rights to retrieve audit information. 

### Example
```python
from __future__ import print_function
import time
import alfresco_core
from alfresco_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_core.AuditApi(alfresco_core.ApiClient(configuration))
skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # List audit applications
    api_response = api_instance.list_audit_apps(skip_count=skip_count, max_items=max_items, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->list_audit_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**AuditAppPaging**](AuditAppPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_audit_entries_for_audit_app**
> AuditEntryPaging list_audit_entries_for_audit_app(audit_application_id, skip_count=skip_count, omit_total_items=omit_total_items, order_by=order_by, max_items=max_items, where=where, include=include, fields=fields)

List audit entries for an audit application

**Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.  Gets a list of audit entries for audit application **auditApplicationId**.  You can use the **include** parameter to return additional **values** information.  The list can be filtered by one or more of: * **createdByUser** person id * **createdAt** inclusive time period * **id** inclusive range of ids * **valuesKey** audit entry values contains the exact matching key * **valuesValue** audit entry values contains the exact matching value  The default sort order is **createdAt** ascending, but you can use an optional **ASC** or **DESC** modifier to specify an ascending or descending sort order.  For example, specifying ```orderBy=createdAt DESC``` returns audit entries in descending **createdAt** order.  You must have admin rights to retrieve audit information. 

### Example
```python
from __future__ import print_function
import time
import alfresco_core
from alfresco_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_core.AuditApi(alfresco_core.ApiClient(configuration))
audit_application_id = 'audit_application_id_example' # str | The identifier of an audit application.
skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
omit_total_items = false # bool | A boolean to control if the response provides the total numbers of items in the collection. If not supplied then the default value is false.  (optional) (default to false)
order_by = ['order_by_example'] # list[str] | A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)
max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
where = 'where_example' # str | Optionally filter the list. Here are some examples:  *   ```where=(createdByUser='jbloggs')```  *   ```where=(id BETWEEN ('1234', '4321')```  *   ```where=(createdAt BETWEEN ('2017-06-02T12:13:51.593+01:00' , '2017-06-04T10:05:16.536+01:00')```  *   ```where=(createdByUser='jbloggs' and createdAt BETWEEN ('2017-06-02T12:13:51.593+01:00' , '2017-06-04T10:05:16.536+01:00')```  *   ```where=(valuesKey='/alfresco-access/login/user')```  *   ```where=(valuesKey='/alfresco-access/transaction/action' and valuesValue='DELETE')```  (optional)
include = ['include_example'] # list[str] | Returns additional information about the audit entry. The following optional fields can be requested: * values  (optional)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # List audit entries for an audit application
    api_response = api_instance.list_audit_entries_for_audit_app(audit_application_id, skip_count=skip_count, omit_total_items=omit_total_items, order_by=order_by, max_items=max_items, where=where, include=include, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->list_audit_entries_for_audit_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audit_application_id** | **str**| The identifier of an audit application. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **omit_total_items** | **bool**| A boolean to control if the response provides the total numbers of items in the collection. If not supplied then the default value is false.  | [optional] [default to false]
 **order_by** | [**list[str]**](str.md)| A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  | [optional] 
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **where** | **str**| Optionally filter the list. Here are some examples:  *   &#x60;&#x60;&#x60;where&#x3D;(createdByUser&#x3D;&#x27;jbloggs&#x27;)&#x60;&#x60;&#x60;  *   &#x60;&#x60;&#x60;where&#x3D;(id BETWEEN (&#x27;1234&#x27;, &#x27;4321&#x27;)&#x60;&#x60;&#x60;  *   &#x60;&#x60;&#x60;where&#x3D;(createdAt BETWEEN (&#x27;2017-06-02T12:13:51.593+01:00&#x27; , &#x27;2017-06-04T10:05:16.536+01:00&#x27;)&#x60;&#x60;&#x60;  *   &#x60;&#x60;&#x60;where&#x3D;(createdByUser&#x3D;&#x27;jbloggs&#x27; and createdAt BETWEEN (&#x27;2017-06-02T12:13:51.593+01:00&#x27; , &#x27;2017-06-04T10:05:16.536+01:00&#x27;)&#x60;&#x60;&#x60;  *   &#x60;&#x60;&#x60;where&#x3D;(valuesKey&#x3D;&#x27;/alfresco-access/login/user&#x27;)&#x60;&#x60;&#x60;  *   &#x60;&#x60;&#x60;where&#x3D;(valuesKey&#x3D;&#x27;/alfresco-access/transaction/action&#x27; and valuesValue&#x3D;&#x27;DELETE&#x27;)&#x60;&#x60;&#x60;  | [optional] 
 **include** | [**list[str]**](str.md)| Returns additional information about the audit entry. The following optional fields can be requested: * values  | [optional] 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**AuditEntryPaging**](AuditEntryPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_audit_entries_for_node**
> AuditEntryPaging list_audit_entries_for_node(node_id, skip_count=skip_count, order_by=order_by, max_items=max_items, where=where, include=include, fields=fields)

List audit entries for a node

**Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.  Gets a list of audit entries for node **nodeId**.  The list can be filtered by **createdByUser** and for a given inclusive time period.  The default sort order is **createdAt** ascending, but you can use an optional **ASC** or **DESC** modifier to specify an ascending or descending sort order.  For example, specifying ```orderBy=createdAt DESC``` returns audit entries in descending **createdAt** order.  This relies on the pre-configured 'alfresco-access' audit application. 

### Example
```python
from __future__ import print_function
import time
import alfresco_core
from alfresco_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_core.AuditApi(alfresco_core.ApiClient(configuration))
node_id = 'node_id_example' # str | The identifier of a node.
skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
order_by = ['order_by_example'] # list[str] | A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)
max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
where = 'where_example' # str | Optionally filter the list. Here are some examples:  *   ```where=(createdByUser='-me-')```  *   ```where=(createdAt BETWEEN ('2017-06-02T12:13:51.593+01:00' , '2017-06-04T10:05:16.536+01:00')```  *   ```where=(createdByUser='jbloggs' and createdAt BETWEEN ('2017-06-02T12:13:51.593+01:00' , '2017-06-04T10:05:16.536+01:00')```  (optional)
include = ['include_example'] # list[str] | Returns additional information about the audit entry. The following optional fields can be requested: * values  (optional)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # List audit entries for a node
    api_response = api_instance.list_audit_entries_for_node(node_id, skip_count=skip_count, order_by=order_by, max_items=max_items, where=where, include=include, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->list_audit_entries_for_node: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **node_id** | **str**| The identifier of a node. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **order_by** | [**list[str]**](str.md)| A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  | [optional] 
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **where** | **str**| Optionally filter the list. Here are some examples:  *   &#x60;&#x60;&#x60;where&#x3D;(createdByUser&#x3D;&#x27;-me-&#x27;)&#x60;&#x60;&#x60;  *   &#x60;&#x60;&#x60;where&#x3D;(createdAt BETWEEN (&#x27;2017-06-02T12:13:51.593+01:00&#x27; , &#x27;2017-06-04T10:05:16.536+01:00&#x27;)&#x60;&#x60;&#x60;  *   &#x60;&#x60;&#x60;where&#x3D;(createdByUser&#x3D;&#x27;jbloggs&#x27; and createdAt BETWEEN (&#x27;2017-06-02T12:13:51.593+01:00&#x27; , &#x27;2017-06-04T10:05:16.536+01:00&#x27;)&#x60;&#x60;&#x60;  | [optional] 
 **include** | [**list[str]**](str.md)| Returns additional information about the audit entry. The following optional fields can be requested: * values  | [optional] 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**AuditEntryPaging**](AuditEntryPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_audit_app**
> AuditApp update_audit_app(body, audit_application_id, fields=fields)

Update audit application info

**Note:** this endpoint is available in Alfresco 5.2.2 and newer versions.  Disable or re-enable the audit application **auditApplicationId**.  New audit entries will not be created for a disabled audit application until it is re-enabled (and system-wide auditing is also enabled).  Note, it is still possible to query &/or delete any existing audit entries even if auditing is disabled for the audit application.  You must have admin rights to update audit application. 

### Example
```python
from __future__ import print_function
import time
import alfresco_core
from alfresco_core.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = alfresco_core.AuditApi(alfresco_core.ApiClient(configuration))
body = alfresco_core.AuditBodyUpdate() # AuditBodyUpdate | The audit application to update.
audit_application_id = 'audit_application_id_example' # str | The identifier of an audit application.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Update audit application info
    api_response = api_instance.update_audit_app(body, audit_application_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuditApi->update_audit_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuditBodyUpdate**](AuditBodyUpdate.md)| The audit application to update. | 
 **audit_application_id** | **str**| The identifier of an audit application. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**AuditApp**](AuditApp.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

