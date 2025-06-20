# alfresco_core.GroupsApi

All URIs are relative to */alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_group**](GroupsApi.md#create_group) | **POST** /groups | Create a group
[**create_group_membership**](GroupsApi.md#create_group_membership) | **POST** /groups/{groupId}/members | Create a group membership
[**delete_group**](GroupsApi.md#delete_group) | **DELETE** /groups/{groupId} | Delete a group
[**delete_group_membership**](GroupsApi.md#delete_group_membership) | **DELETE** /groups/{groupId}/members/{groupMemberId} | Delete a group membership
[**get_group**](GroupsApi.md#get_group) | **GET** /groups/{groupId} | Get group details
[**list_group_memberships**](GroupsApi.md#list_group_memberships) | **GET** /groups/{groupId}/members | List memberships of a group
[**list_group_memberships_for_person**](GroupsApi.md#list_group_memberships_for_person) | **GET** /people/{personId}/groups | List group memberships
[**list_groups**](GroupsApi.md#list_groups) | **GET** /groups | List groups
[**update_group**](GroupsApi.md#update_group) | **PUT** /groups/{groupId} | Update group details

# **create_group**
> GroupEntry create_group(body, include=include, fields=fields)

Create a group

**Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.  Create a group.  The group id must start with \"GROUP\\_\". If this is omitted it will be added automatically. This format is also returned when listing groups or group memberships. It should be noted that the other group-related operations also expect the id to start with \"GROUP\\_\".  If one or more parentIds are specified then the group will be created and become a member of each of the specified parent groups.  If no parentIds are specified then the group will be created as a root group.  The group will be created in the **APP.DEFAULT** and **AUTH.ALF** zones.  You must have admin rights to create a group. 

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
api_instance = alfresco_core.GroupsApi(alfresco_core.ApiClient(configuration))
body = alfresco_core.GroupBodyCreate() # GroupBodyCreate | The group to create.
include = ['include_example'] # list[str] | Returns additional information about the group. The following optional fields can be requested: * parentIds * zones  (optional)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Create a group
    api_response = api_instance.create_group(body, include=include, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupBodyCreate**](GroupBodyCreate.md)| The group to create. | 
 **include** | [**list[str]**](str.md)| Returns additional information about the group. The following optional fields can be requested: * parentIds * zones  | [optional] 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**GroupEntry**](GroupEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_group_membership**
> GroupMemberEntry create_group_membership(body, group_id, fields=fields)

Create a group membership

**Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.  Create a group membership (for an existing person or group) within a group **groupId**.  If the added group was previously a root group then it becomes a non-root group since it now has a parent.  It is an error to specify an **id** that does not exist.  You must have admin rights to create a group membership. 

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
api_instance = alfresco_core.GroupsApi(alfresco_core.ApiClient(configuration))
body = alfresco_core.GroupMembershipBodyCreate() # GroupMembershipBodyCreate | The group membership to add (person or sub-group).
group_id = 'group_id_example' # str | The identifier of a group.
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Create a group membership
    api_response = api_instance.create_group_membership(body, group_id, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->create_group_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupMembershipBodyCreate**](GroupMembershipBodyCreate.md)| The group membership to add (person or sub-group). | 
 **group_id** | **str**| The identifier of a group. | 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**GroupMemberEntry**](GroupMemberEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group**
> delete_group(group_id, cascade=cascade)

Delete a group

**Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.  Delete group **groupId**.  The option to cascade delete applies this recursively to any hierarchy of group members. In this case, removing a group member does not delete the person or sub-group itself. If a removed sub-group no longer has any parent groups then it becomes a root group.  You must have admin rights to delete a group. 

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
api_instance = alfresco_core.GroupsApi(alfresco_core.ApiClient(configuration))
group_id = 'group_id_example' # str | The identifier of a group.
cascade = false # bool | If **true** then the delete will be applied in cascade to sub-groups.  (optional) (default to false)

try:
    # Delete a group
    api_instance.delete_group(group_id, cascade=cascade)
except ApiException as e:
    print("Exception when calling GroupsApi->delete_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The identifier of a group. | 
 **cascade** | **bool**| If **true** then the delete will be applied in cascade to sub-groups.  | [optional] [default to false]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_group_membership**
> delete_group_membership(group_id, group_member_id)

Delete a group membership

**Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.  Delete group member **groupMemberId** (person or sub-group) from group **groupId**.  Removing a group member does not delete the person or sub-group itself.  If a removed sub-group no longer has any parent groups then it becomes a root group.  You must have admin rights to delete a group membership. 

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
api_instance = alfresco_core.GroupsApi(alfresco_core.ApiClient(configuration))
group_id = 'group_id_example' # str | The identifier of a group.
group_member_id = 'group_member_id_example' # str | The identifier of a person or group.

try:
    # Delete a group membership
    api_instance.delete_group_membership(group_id, group_member_id)
except ApiException as e:
    print("Exception when calling GroupsApi->delete_group_membership: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The identifier of a group. | 
 **group_member_id** | **str**| The identifier of a person or group. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_group**
> GroupEntry get_group(group_id, include=include, fields=fields)

Get group details

**Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.  Get details for group **groupId**.  You can use the **include** parameter to return additional information. 

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
api_instance = alfresco_core.GroupsApi(alfresco_core.ApiClient(configuration))
group_id = 'group_id_example' # str | The identifier of a group.
include = ['include_example'] # list[str] | Returns additional information about the group. The following optional fields can be requested: * parentIds * zones  (optional)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Get group details
    api_response = api_instance.get_group(group_id, include=include, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->get_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The identifier of a group. | 
 **include** | [**list[str]**](str.md)| Returns additional information about the group. The following optional fields can be requested: * parentIds * zones  | [optional] 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**GroupEntry**](GroupEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_memberships**
> GroupMemberPaging list_group_memberships(group_id, skip_count=skip_count, max_items=max_items, order_by=order_by, where=where, fields=fields)

List memberships of a group

**Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.  Gets a list of the group memberships for the group **groupId**.  You can use the **where** parameter to filter the returned groups by **memberType**.  Example to filter by **memberType**, use any one of:  ``` (memberType='GROUP') (memberType='PERSON') ```  The default sort order for the returned list is for group members to be sorted by ascending displayName. You can override the default by using the **orderBy** parameter. You can specify one of the following fields in the **orderBy** parameter: * id * displayName 

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
api_instance = alfresco_core.GroupsApi(alfresco_core.ApiClient(configuration))
group_id = 'group_id_example' # str | The identifier of a group.
skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
order_by = ['order_by_example'] # list[str] | A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)
where = 'where_example' # str | A string to restrict the returned objects by using a predicate. (optional)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # List memberships of a group
    api_response = api_instance.list_group_memberships(group_id, skip_count=skip_count, max_items=max_items, order_by=order_by, where=where, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->list_group_memberships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**| The identifier of a group. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **order_by** | [**list[str]**](str.md)| A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  | [optional] 
 **where** | **str**| A string to restrict the returned objects by using a predicate. | [optional] 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**GroupMemberPaging**](GroupMemberPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_group_memberships_for_person**
> GroupPaging list_group_memberships_for_person(person_id, skip_count=skip_count, max_items=max_items, order_by=order_by, include=include, where=where, fields=fields)

List group memberships

**Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.   Gets a list of group membership information for person **personId**.   You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.   You can use the **include** parameter to return additional information.   You can use the **where** parameter to filter the returned groups by **isRoot**. For example, the following **where**  clause will return just the root groups:   ```  (isRoot=true)  ```   The **where** parameter can also be used to filter by ***zone***. This may be combined with isRoot to narrow  a result set even further. For example, the following where clause will only return groups belonging to the  `MY.ZONE` zone.   ```  where=(zones in ('MY.ZONE'))  ```   This may be combined with the isRoot filter, as shown below:   ```  where=(isRoot=false AND zones in ('MY.ZONE'))  ```   ***Note:*** restrictions include  * `AND` is the only supported operator when combining `isRoot` and `zones` filters  * Only one zone is supported by the filter  * The quoted zone name must be placed in parenthesis — a 400 error will result if these are omitted.    The default sort order for the returned list is for groups to be sorted by ascending displayName.  You can override the default by using the **orderBy** parameter. You can specify one or more of the following fields in the **orderBy** parameter:  * id  * displayName 

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
api_instance = alfresco_core.GroupsApi(alfresco_core.ApiClient(configuration))
person_id = 'person_id_example' # str | The identifier of a person.
skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
order_by = ['order_by_example'] # list[str] | A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)
include = ['include_example'] # list[str] | Returns additional information about the group. The following optional fields can be requested: * parentIds * zones  (optional)
where = 'where_example' # str | A string to restrict the returned objects by using a predicate. (optional)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # List group memberships
    api_response = api_instance.list_group_memberships_for_person(person_id, skip_count=skip_count, max_items=max_items, order_by=order_by, include=include, where=where, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->list_group_memberships_for_person: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **order_by** | [**list[str]**](str.md)| A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  | [optional] 
 **include** | [**list[str]**](str.md)| Returns additional information about the group. The following optional fields can be requested: * parentIds * zones  | [optional] 
 **where** | **str**| A string to restrict the returned objects by using a predicate. | [optional] 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**GroupPaging**](GroupPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_groups**
> GroupPaging list_groups(skip_count=skip_count, max_items=max_items, order_by=order_by, include=include, where=where, fields=fields)

List groups

**Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.  Gets a list of groups.  You can use the **include** parameter to return additional information.  You can use the **where** parameter to filter the returned groups by **isRoot**. For example, the following **where** clause will return just the root groups:  ``` (isRoot=true) ```  The **where** parameter can also be used to filter by ***zone*** and ***displayName***. They may be combined with isRoot to narrow a result set even further.  For example, the following where clause will only return groups belonging to the `MY.ZONE` zone.  ``` where=(zones in ('MY.ZONE')) ```  This may be combined with the isRoot filter, as shown below:  ``` where=(isRoot=false AND zones in ('MY.ZONE')) ``` The following where clause will only return groups with displayName `MY.GROUP.NAME`.   ``` where=(displayName in ('MY.GROUP.NAME')) ``` This may be combined with the isRoot and zones filter, as shown below:  ``` where=(isRoot=false AND displayName in ('MY.GROUP.NAME')) ```  ``` where=(zones in ('MY.ZONE') AND displayName in ('MY.GROUP.NAME')) ```  ``` where=(isRoot=false AND zones in ('MY.ZONE') AND displayName in ('MY.GROUP.NAME')) ```  ***Note:*** restrictions include * `AND` is the only supported operator when combining `isRoot`, `zones` and `displayName` filters * Only one zone is supported by the filter * Only one displayName is supported by the filter * The quoted zone name and displayName must be placed in parenthesis — a 400 error will result if these are omitted.  The default sort order for the returned list is for groups to be sorted by ascending displayName. You can override the default by using the **orderBy** parameter. You can specify one of the following fields in the **orderBy** parameter: * id * displayName 

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
api_instance = alfresco_core.GroupsApi(alfresco_core.ApiClient(configuration))
skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
order_by = ['order_by_example'] # list[str] | A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)
include = ['include_example'] # list[str] | Returns additional information about the group. The following optional fields can be requested: * parentIds * zones  (optional)
where = 'where_example' # str | A string to restrict the returned objects by using a predicate. (optional)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # List groups
    api_response = api_instance.list_groups(skip_count=skip_count, max_items=max_items, order_by=order_by, include=include, where=where, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->list_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **order_by** | [**list[str]**](str.md)| A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  | [optional] 
 **include** | [**list[str]**](str.md)| Returns additional information about the group. The following optional fields can be requested: * parentIds * zones  | [optional] 
 **where** | **str**| A string to restrict the returned objects by using a predicate. | [optional] 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**GroupPaging**](GroupPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_group**
> GroupEntry update_group(body, group_id, include=include, fields=fields)

Update group details

**Note:** this endpoint is available in Alfresco 5.2.1 and newer versions.  Update details (displayName) for group **groupId**.  You must have admin rights to update a group. 

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
api_instance = alfresco_core.GroupsApi(alfresco_core.ApiClient(configuration))
body = alfresco_core.GroupBodyUpdate() # GroupBodyUpdate | The group information to update.
group_id = 'group_id_example' # str | The identifier of a group.
include = ['include_example'] # list[str] | Returns additional information about the group. The following optional fields can be requested: * parentIds * zones  (optional)
fields = ['fields_example'] # list[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

try:
    # Update group details
    api_response = api_instance.update_group(body, group_id, include=include, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupBodyUpdate**](GroupBodyUpdate.md)| The group information to update. | 
 **group_id** | **str**| The identifier of a group. | 
 **include** | [**list[str]**](str.md)| Returns additional information about the group. The following optional fields can be requested: * parentIds * zones  | [optional] 
 **fields** | [**list[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**GroupEntry**](GroupEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

