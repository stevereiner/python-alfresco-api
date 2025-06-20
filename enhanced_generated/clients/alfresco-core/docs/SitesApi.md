# alfresco_core_client.SitesApi

All URIs are relative to *http://localhost/alfresco/api/-default-/public/alfresco/versions/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_site_membership_request**](SitesApi.md#approve_site_membership_request) | **POST** /sites/{siteId}/site-membership-requests/{inviteeId}/approve | Approve a site membership request
[**create_site**](SitesApi.md#create_site) | **POST** /sites | Create a site
[**create_site_group_membership**](SitesApi.md#create_site_group_membership) | **POST** /sites/{siteId}/group-members | Create a site membership for group
[**create_site_membership**](SitesApi.md#create_site_membership) | **POST** /sites/{siteId}/members | Create a site membership
[**create_site_membership_request_for_person**](SitesApi.md#create_site_membership_request_for_person) | **POST** /people/{personId}/site-membership-requests | Create a site membership request
[**delete_site**](SitesApi.md#delete_site) | **DELETE** /sites/{siteId} | Delete a site
[**delete_site_group_membership**](SitesApi.md#delete_site_group_membership) | **DELETE** /sites/{siteId}/group-members/{groupId} | Delete a group membership for site
[**delete_site_membership**](SitesApi.md#delete_site_membership) | **DELETE** /sites/{siteId}/members/{personId} | Delete a site membership
[**delete_site_membership_for_person**](SitesApi.md#delete_site_membership_for_person) | **DELETE** /people/{personId}/sites/{siteId} | Delete a site membership
[**delete_site_membership_request_for_person**](SitesApi.md#delete_site_membership_request_for_person) | **DELETE** /people/{personId}/site-membership-requests/{siteId} | Delete a site membership request
[**get_site**](SitesApi.md#get_site) | **GET** /sites/{siteId} | Get a site
[**get_site_container**](SitesApi.md#get_site_container) | **GET** /sites/{siteId}/containers/{containerId} | Get a site container
[**get_site_group_membership**](SitesApi.md#get_site_group_membership) | **GET** /sites/{siteId}/group-members/{groupId} | Get information about site membership of group
[**get_site_membership**](SitesApi.md#get_site_membership) | **GET** /sites/{siteId}/members/{personId} | Get a site membership
[**get_site_membership_for_person**](SitesApi.md#get_site_membership_for_person) | **GET** /people/{personId}/sites/{siteId} | Get a site membership
[**get_site_membership_request_for_person**](SitesApi.md#get_site_membership_request_for_person) | **GET** /people/{personId}/site-membership-requests/{siteId} | Get a site membership request
[**get_site_membership_requests**](SitesApi.md#get_site_membership_requests) | **GET** /site-membership-requests | Get site membership requests
[**list_site_containers**](SitesApi.md#list_site_containers) | **GET** /sites/{siteId}/containers | List site containers
[**list_site_groups**](SitesApi.md#list_site_groups) | **GET** /sites/{siteId}/group-members | List group membership for site
[**list_site_membership_requests_for_person**](SitesApi.md#list_site_membership_requests_for_person) | **GET** /people/{personId}/site-membership-requests | List site membership requests
[**list_site_memberships**](SitesApi.md#list_site_memberships) | **GET** /sites/{siteId}/members | List site memberships
[**list_site_memberships_for_person**](SitesApi.md#list_site_memberships_for_person) | **GET** /people/{personId}/sites | List site memberships
[**list_sites**](SitesApi.md#list_sites) | **GET** /sites | List sites
[**reject_site_membership_request**](SitesApi.md#reject_site_membership_request) | **POST** /sites/{siteId}/site-membership-requests/{inviteeId}/reject | Reject a site membership request
[**update_site**](SitesApi.md#update_site) | **PUT** /sites/{siteId} | Update a site
[**update_site_group_membership**](SitesApi.md#update_site_group_membership) | **PUT** /sites/{siteId}/group-members/{groupId} | Update site membership of group
[**update_site_membership**](SitesApi.md#update_site_membership) | **PUT** /sites/{siteId}/members/{personId} | Update a site membership
[**update_site_membership_request_for_person**](SitesApi.md#update_site_membership_request_for_person) | **PUT** /people/{personId}/site-membership-requests/{siteId} | Update a site membership request


# **approve_site_membership_request**
> approve_site_membership_request(site_id, invitee_id, site_membership_approval_body=site_membership_approval_body)

Approve a site membership request

Approve a site membership request.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_membership_approval_body import SiteMembershipApprovalBody
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_id = 'site_id_example' # str | The identifier of a site.
    invitee_id = 'invitee_id_example' # str | The invitee user name.
    site_membership_approval_body = alfresco_core_client.SiteMembershipApprovalBody() # SiteMembershipApprovalBody | Accepting a request to join, optionally, allows assignment of a role to the user.  (optional)

    try:
        # Approve a site membership request
        api_instance.approve_site_membership_request(site_id, invitee_id, site_membership_approval_body=site_membership_approval_body)
    except Exception as e:
        print("Exception when calling SitesApi->approve_site_membership_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The identifier of a site. | 
 **invitee_id** | **str**| The invitee user name. | 
 **site_membership_approval_body** | [**SiteMembershipApprovalBody**](SiteMembershipApprovalBody.md)| Accepting a request to join, optionally, allows assignment of a role to the user.  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **siteId** or **inviteeId** is invalid  |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have permission to approve membership request |  -  |
**404** | **siteId** or **inviteeId** does not exist  |  -  |
**422** | Integrity exception or not allowed to approve membership request.  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_site**
> SiteEntry create_site(site_body_create, skip_configuration=skip_configuration, skip_add_to_favorites=skip_add_to_favorites, fields=fields)

Create a site

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Creates a default site with the given details.  Unless explicitly specified, the site id will be generated
from the site title. The site id must be unique and only contain alphanumeric and/or dash characters.

Note: the id of a site cannot be updated once the site has been created.

For example, to create a public site called "Marketing" the following body could be used:
```JSON
{
  "title": "Marketing",
  "visibility": "PUBLIC"
}
```

The creation of the (surf) configuration files required by Share can be skipped via the **skipConfiguration** query parameter.

**Note:** if skipped then such a site will **not** work within Share.

The addition of the site to the user's site favorites can be skipped via the **skipAddToFavorites** query parameter.

The creator will be added as a member with Site Manager role.

When you create a site, a container called **documentLibrary** is created for you in the new site.
This container is the root folder for content stored in the site.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_body_create import SiteBodyCreate
from alfresco_core_client.models.site_entry import SiteEntry
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_body_create = alfresco_core_client.SiteBodyCreate() # SiteBodyCreate | The site details
    skip_configuration = False # bool | Flag to indicate whether the Share-specific (surf) configuration files for the site should not be created. (optional) (default to False)
    skip_add_to_favorites = False # bool | Flag to indicate whether the site should not be added to the user's site favorites. (optional) (default to False)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Create a site
        api_response = api_instance.create_site(site_body_create, skip_configuration=skip_configuration, skip_add_to_favorites=skip_add_to_favorites, fields=fields)
        print("The response of SitesApi->create_site:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->create_site: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_body_create** | [**SiteBodyCreate**](SiteBodyCreate.md)| The site details | 
 **skip_configuration** | **bool**| Flag to indicate whether the Share-specific (surf) configuration files for the site should not be created. | [optional] [default to False]
 **skip_add_to_favorites** | **bool**| Flag to indicate whether the site should not be added to the user&#39;s site favorites. | [optional] [default to False]
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteEntry**](SiteEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | Invalid parameter: **id**, **title**, or **description** exceed the maximum length; or **id** contains invalid characters; or **siteBodyCreate** invalid  |  -  |
**401** | Authentication failed |  -  |
**409** | Site with the given identifier already exists |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_site_group_membership**
> SiteGroupEntry create_site_group_membership(site_id, site_membership_body_create, fields=fields)

Create a site membership for group

**Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.

Creates a site membership for group **groupId** on site **siteId**.
You can set the **role** to one of four types:
* SiteConsumer
* SiteCollaborator
* SiteContributor
* SiteManager
**Note:** You can create more than one site membership by
specifying a list of group in the JSON body like this:

```JSON
  [
   {
     "role": "SiteConsumer",
     "id": "authorityId"
   },
   {
     "role": "SiteConsumer",
     "id": "authorityId"
   }
  ]
```
If you specify a list as input, then a paginated list rather than an entry is returned in the response body. For example:
```JSON
  {
    "list": {
      "pagination": {
        "count": 2,
        "hasMoreItems": false,
        "totalItems": 2,
        "skipCount": 0,
        "maxItems": 100
      },
      "entries": [
        {
          "entry": {
            ...
          }
        },
        {
          "entry": {
            ...
          }
        }
      ]
    }
  }
```


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_group_entry import SiteGroupEntry
from alfresco_core_client.models.site_membership_body_create import SiteMembershipBodyCreate
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_id = 'site_id_example' # str | The identifier of a site.
    site_membership_body_create = alfresco_core_client.SiteMembershipBodyCreate() # SiteMembershipBodyCreate | The group to add and their role
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Create a site membership for group
        api_response = api_instance.create_site_group_membership(site_id, site_membership_body_create, fields=fields)
        print("The response of SitesApi->create_site_group_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->create_site_group_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The identifier of a site. | 
 **site_membership_body_create** | [**SiteMembershipBodyCreate**](SiteMembershipBodyCreate.md)| The group to add and their role | 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteGroupEntry**](SiteGroupEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | Invalid parameter: value of **role** or **id** is invalid or **siteMembershipBodyCreate** invalid  |  -  |
**401** | Authentication failed |  -  |
**403** | User does not have permission to invite a Group |  -  |
**404** | **siteId** or **groupId** does not exist  |  -  |
**409** | Group with this **id** is already a member |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_site_membership**
> SiteMemberEntry create_site_membership(site_id, site_membership_body_create, fields=fields)

Create a site membership

Creates a site membership for person **personId** on site **siteId**.

You can set the **role** to one of four types:

* SiteConsumer
* SiteCollaborator
* SiteContributor
* SiteManager

**Note:** You can create more than one site membership by
specifying a list of people in the JSON body like this:

```JSON
[
  {
    "role": "SiteConsumer",
    "id": "joe"
  },
  {
    "role": "SiteConsumer",
    "id": "fred"
  }
]
```
If you specify a list as input, then a paginated list rather than an entry is returned in the response body. For example:

```JSON
{
  "list": {
    "pagination": {
      "count": 2,
      "hasMoreItems": false,
      "totalItems": 2,
      "skipCount": 0,
      "maxItems": 100
    },
    "entries": [
      {
        "entry": {
          ...
        }
      },
      {
        "entry": {
          ...
        }
      }
    ]
  }
}
```


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_member_entry import SiteMemberEntry
from alfresco_core_client.models.site_membership_body_create import SiteMembershipBodyCreate
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_id = 'site_id_example' # str | The identifier of a site.
    site_membership_body_create = alfresco_core_client.SiteMembershipBodyCreate() # SiteMembershipBodyCreate | The person to add and their role
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Create a site membership
        api_response = api_instance.create_site_membership(site_id, site_membership_body_create, fields=fields)
        print("The response of SitesApi->create_site_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->create_site_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The identifier of a site. | 
 **site_membership_body_create** | [**SiteMembershipBodyCreate**](SiteMembershipBodyCreate.md)| The person to add and their role | 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteMemberEntry**](SiteMemberEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | Invalid parameter: value of **role** or **id** is invalid or **siteMembershipBodyCreate** invalid  |  -  |
**401** | Authentication failed |  -  |
**403** | User does not have permission to invite a person |  -  |
**404** | **siteId** or **personId** does not exist  |  -  |
**409** | Person with this **id** is already a member |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_site_membership_request_for_person**
> SiteMembershipRequestEntry create_site_membership_request_for_person(person_id, site_membership_request_body_create, fields=fields)

Create a site membership request

Create a site membership request for yourself on the site with the identifier of **id**, specified in the JSON body.
The result of the request differs depending on the type of site.

* For a **public** site, you join the site immediately as a SiteConsumer.
* For a **moderated** site, your request is added to the site membership request list. The request waits for approval from the Site Manager.
* You cannot request membership of a **private** site. Members are invited by the site administrator.

You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

 **Note:** You can create site membership requests for more than one site by
specifying a list of sites in the JSON body like this:

```JSON
[
  {
    "message": "Please can you add me",
    "id": "test-site-1",
    "title": "Request for test site 1",
  },
  {
    "message": "Please can you add me",
    "id": "test-site-2",
    "title": "Request for test site 2",
  }
]
```
If you specify a list as input, then a paginated list rather than an entry is returned in the response body. For example:

```JSON
{
  "list": {
    "pagination": {
      "count": 2,
      "hasMoreItems": false,
      "totalItems": 2,
      "skipCount": 0,
      "maxItems": 100
    },
    "entries": [
      {
        "entry": {
          ...
        }
      },
      {
        "entry": {
          ...
        }
      }
    ]
  }
}
```


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_membership_request_body_create import SiteMembershipRequestBodyCreate
from alfresco_core_client.models.site_membership_request_entry import SiteMembershipRequestEntry
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    person_id = 'person_id_example' # str | The identifier of a person.
    site_membership_request_body_create = alfresco_core_client.SiteMembershipRequestBodyCreate() # SiteMembershipRequestBodyCreate | Site membership request details
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Create a site membership request
        api_response = api_instance.create_site_membership_request_for_person(person_id, site_membership_request_body_create, fields=fields)
        print("The response of SitesApi->create_site_membership_request_for_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->create_site_membership_request_for_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **site_membership_request_body_create** | [**SiteMembershipRequestBodyCreate**](SiteMembershipRequestBodyCreate.md)| Site membership request details | 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteMembershipRequestEntry**](SiteMembershipRequestEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | Invalid parameter: **id** is invalid, or the user is already invited, or **siteMembershipRequestBodyCreate** invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **personId** or **id** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site**
> delete_site(site_id, permanent=permanent)

Delete a site

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Deletes the site with **siteId**.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_id = 'site_id_example' # str | The identifier of a site.
    permanent = False # bool | Flag to indicate whether the site should be permanently deleted i.e. bypass the trashcan. (optional) (default to False)

    try:
        # Delete a site
        api_instance.delete_site(site_id, permanent=permanent)
    except Exception as e:
        print("Exception when calling SitesApi->delete_site: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The identifier of a site. | 
 **permanent** | **bool**| Flag to indicate whether the site should be permanently deleted i.e. bypass the trashcan. | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful response |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have permission to delete the site that is visible to them. |  -  |
**404** | **siteId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_group_membership**
> delete_site_group_membership(site_id, group_id)

Delete a group membership for site

**Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.

Deletes group **groupId** as a member of site **siteId**.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_id = 'site_id_example' # str | The identifier of a site.
    group_id = 'group_id_example' # str | The identifier of a group.

    try:
        # Delete a group membership for site
        api_instance.delete_site_group_membership(site_id, group_id)
    except Exception as e:
        print("Exception when calling SitesApi->delete_site_group_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The identifier of a site. | 
 **group_id** | **str**| The identifier of a group. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful response |  -  |
**401** | Authentication failed |  -  |
**404** | **siteId** or **groupId** does not exist  |  -  |
**422** | Integrity exception (eg. last site member must be a site manager) or not allowed to delete groupId |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_membership**
> delete_site_membership(site_id, person_id)

Delete a site membership

Deletes person **personId** as a member of site **siteId**.

You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_id = 'site_id_example' # str | The identifier of a site.
    person_id = 'person_id_example' # str | The identifier of a person.

    try:
        # Delete a site membership
        api_instance.delete_site_membership(site_id, person_id)
    except Exception as e:
        print("Exception when calling SitesApi->delete_site_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The identifier of a site. | 
 **person_id** | **str**| The identifier of a person. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful response |  -  |
**401** | Authentication failed |  -  |
**404** | **siteId** or **personId** does not exist  |  -  |
**422** | Integrity exception (eg. last site member must be a site manager) or not allowed to delete member |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_membership_for_person**
> delete_site_membership_for_person(person_id, site_id)

Delete a site membership

Deletes person **personId** as a member of site **siteId**.

You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    person_id = 'person_id_example' # str | The identifier of a person.
    site_id = 'site_id_example' # str | The identifier of a site.

    try:
        # Delete a site membership
        api_instance.delete_site_membership_for_person(person_id, site_id)
    except Exception as e:
        print("Exception when calling SitesApi->delete_site_membership_for_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **site_id** | **str**| The identifier of a site. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful response |  -  |
**401** | Authentication failed |  -  |
**404** | **personId** or **siteId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_site_membership_request_for_person**
> delete_site_membership_request_for_person(person_id, site_id)

Delete a site membership request

Deletes the site membership request to site **siteId** for person **personId**.

You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    person_id = 'person_id_example' # str | The identifier of a person.
    site_id = 'site_id_example' # str | The identifier of a site.

    try:
        # Delete a site membership request
        api_instance.delete_site_membership_request_for_person(person_id, site_id)
    except Exception as e:
        print("Exception when calling SitesApi->delete_site_membership_request_for_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **site_id** | **str**| The identifier of a site. | 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successful response |  -  |
**401** | Authentication failed |  -  |
**404** | **personId** or **siteId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site**
> SiteEntry get_site(site_id, relations=relations, fields=fields)

Get a site

Gets information for site **siteId**.

You can use the **relations** parameter to include one or more related
entities in a single response and so reduce network traffic.

The entity types in Alfresco are organized in a tree structure.
The **sites** entity has two children, **containers** and **members**.
The following relations parameter returns all the container and member
objects related to the site **siteId**:

```
containers,members
```


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_entry import SiteEntry
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_id = 'site_id_example' # str | The identifier of a site.
    relations = ['relations_example'] # List[str] | Use the relations parameter to include one or more related entities in a single response. (optional)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Get a site
        api_response = api_instance.get_site(site_id, relations=relations, fields=fields)
        print("The response of SitesApi->get_site:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->get_site: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The identifier of a site. | 
 **relations** | [**List[str]**](str.md)| Use the relations parameter to include one or more related entities in a single response. | [optional] 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteEntry**](SiteEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Authentication failed |  -  |
**404** | **siteId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_container**
> SiteContainerEntry get_site_container(site_id, container_id, fields=fields)

Get a site container

Gets information on the container **containerId** in site **siteId**.

### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_container_entry import SiteContainerEntry
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_id = 'site_id_example' # str | The identifier of a site.
    container_id = 'container_id_example' # str | The unique identifier of a site container.
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Get a site container
        api_response = api_instance.get_site_container(site_id, container_id, fields=fields)
        print("The response of SitesApi->get_site_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->get_site_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The identifier of a site. | 
 **container_id** | **str**| The unique identifier of a site container. | 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteContainerEntry**](SiteContainerEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Authentication failed |  -  |
**404** | **siteId** or **containerId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_group_membership**
> SiteGroupEntry get_site_group_membership(site_id, group_id, fields=fields)

Get information about site membership of group

**Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.

Gets site membership information for group **groupId** on site **siteId**.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_group_entry import SiteGroupEntry
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_id = 'site_id_example' # str | The identifier of a site.
    group_id = 'group_id_example' # str | The identifier of a group.
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Get information about site membership of group
        api_response = api_instance.get_site_group_membership(site_id, group_id, fields=fields)
        print("The response of SitesApi->get_site_group_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->get_site_group_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The identifier of a site. | 
 **group_id** | **str**| The identifier of a group. | 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteGroupEntry**](SiteGroupEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Authentication failed |  -  |
**404** | **siteId** or **groupId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_membership**
> SiteMemberEntry get_site_membership(site_id, person_id, fields=fields)

Get a site membership

Gets site membership information for person **personId** on site **siteId**.

You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_member_entry import SiteMemberEntry
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_id = 'site_id_example' # str | The identifier of a site.
    person_id = 'person_id_example' # str | The identifier of a person.
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Get a site membership
        api_response = api_instance.get_site_membership(site_id, person_id, fields=fields)
        print("The response of SitesApi->get_site_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->get_site_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The identifier of a site. | 
 **person_id** | **str**| The identifier of a person. | 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteMemberEntry**](SiteMemberEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Authentication failed |  -  |
**404** | **siteId** or **personId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_membership_for_person**
> SiteRoleEntry get_site_membership_for_person(person_id, site_id)

Get a site membership

Gets site membership information for person **personId** on site **siteId**.

You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_role_entry import SiteRoleEntry
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    person_id = 'person_id_example' # str | The identifier of a person.
    site_id = 'site_id_example' # str | The identifier of a site.

    try:
        # Get a site membership
        api_response = api_instance.get_site_membership_for_person(person_id, site_id)
        print("The response of SitesApi->get_site_membership_for_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->get_site_membership_for_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **site_id** | **str**| The identifier of a site. | 

### Return type

[**SiteRoleEntry**](SiteRoleEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Authentication failed |  -  |
**404** | **personId** or **siteId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_membership_request_for_person**
> SiteMembershipRequestEntry get_site_membership_request_for_person(person_id, site_id, fields=fields)

Get a site membership request

Gets the site membership request for site **siteId** for person **personId**, if one exists.

You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_membership_request_entry import SiteMembershipRequestEntry
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    person_id = 'person_id_example' # str | The identifier of a person.
    site_id = 'site_id_example' # str | The identifier of a site.
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Get a site membership request
        api_response = api_instance.get_site_membership_request_for_person(person_id, site_id, fields=fields)
        print("The response of SitesApi->get_site_membership_request_for_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->get_site_membership_request_for_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **site_id** | **str**| The identifier of a site. | 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteMembershipRequestEntry**](SiteMembershipRequestEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Authentication failed |  -  |
**404** | **personId** or **siteId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_site_membership_requests**
> SiteMembershipRequestWithPersonPaging get_site_membership_requests(skip_count=skip_count, max_items=max_items, where=where, fields=fields)

Get site membership requests

Get the list of site membership requests the user can action.

You can use the **where** parameter to filter the returned site membership requests by **siteId**. For example:

```
(siteId=mySite)
```

The **where** parameter can also be used to filter by ***personId***. For example:

```
where=(personId=person)
```

This may be combined with the siteId filter, as shown below:

```
where=(siteId=mySite AND personId=person))
```


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_membership_request_with_person_paging import SiteMembershipRequestWithPersonPaging
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    where = 'where_example' # str | A string to restrict the returned objects by using a predicate. (optional)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Get site membership requests
        api_response = api_instance.get_site_membership_requests(skip_count=skip_count, max_items=max_items, where=where, fields=fields)
        print("The response of SitesApi->get_site_membership_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->get_site_membership_requests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **where** | **str**| A string to restrict the returned objects by using a predicate. | [optional] 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteMembershipRequestWithPersonPaging**](SiteMembershipRequestWithPersonPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **maxItems** or **skipCount** is invalid  |  -  |
**401** | Authentication failed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_site_containers**
> SiteContainerPaging list_site_containers(site_id, skip_count=skip_count, max_items=max_items, fields=fields)

List site containers

Gets a list of containers for the site **siteId**.

### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_container_paging import SiteContainerPaging
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_id = 'site_id_example' # str | The identifier of a site.
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # List site containers
        api_response = api_instance.list_site_containers(site_id, skip_count=skip_count, max_items=max_items, fields=fields)
        print("The response of SitesApi->list_site_containers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->list_site_containers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The identifier of a site. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteContainerPaging**](SiteContainerPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **maxItems** or **skipCount** is invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **siteId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_site_groups**
> SiteGroupPaging list_site_groups(site_id, skip_count=skip_count, max_items=max_items, fields=fields)

List group membership for site

**Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.

Gets a list of group membership for site **siteId**.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_group_paging import SiteGroupPaging
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_id = 'site_id_example' # str | The identifier of a site.
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # List group membership for site
        api_response = api_instance.list_site_groups(site_id, skip_count=skip_count, max_items=max_items, fields=fields)
        print("The response of SitesApi->list_site_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->list_site_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The identifier of a site. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteGroupPaging**](SiteGroupPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **maxItems** or **skipCount** is invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **siteId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_site_membership_requests_for_person**
> SiteMembershipRequestPaging list_site_membership_requests_for_person(person_id, skip_count=skip_count, max_items=max_items, fields=fields)

List site membership requests

Gets a list of the current site membership requests for person **personId**.

You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_membership_request_paging import SiteMembershipRequestPaging
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    person_id = 'person_id_example' # str | The identifier of a person.
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # List site membership requests
        api_response = api_instance.list_site_membership_requests_for_person(person_id, skip_count=skip_count, max_items=max_items, fields=fields)
        print("The response of SitesApi->list_site_membership_requests_for_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->list_site_membership_requests_for_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteMembershipRequestPaging**](SiteMembershipRequestPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **maxItems** or **skipCount** is invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **personId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_site_memberships**
> SiteMemberPaging list_site_memberships(site_id, skip_count=skip_count, max_items=max_items, fields=fields, where=where)

List site memberships

Gets a list of site memberships for site **siteId**.

### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_member_paging import SiteMemberPaging
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_id = 'site_id_example' # str | The identifier of a site.
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)
    where = 'where_example' # str | Optionally filter the list. *   ```where=(isMemberOfGroup=false|true)```  (optional)

    try:
        # List site memberships
        api_response = api_instance.list_site_memberships(site_id, skip_count=skip_count, max_items=max_items, fields=fields, where=where)
        print("The response of SitesApi->list_site_memberships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->list_site_memberships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The identifier of a site. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 
 **where** | **str**| Optionally filter the list. *   &#x60;&#x60;&#x60;where&#x3D;(isMemberOfGroup&#x3D;false|true)&#x60;&#x60;&#x60;  | [optional] 

### Return type

[**SiteMemberPaging**](SiteMemberPaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **maxItems** or **skipCount** is invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **siteId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_site_memberships_for_person**
> SiteRolePaging list_site_memberships_for_person(person_id, skip_count=skip_count, max_items=max_items, order_by=order_by, relations=relations, fields=fields, where=where)

List site memberships

Gets a list of site membership information for person **personId**.

You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

You can use the **where** parameter to filter the returned sites by **visibility** or site **preset**.

Example to filter by **visibility**, use any one of:

```
(visibility='PRIVATE')
(visibility='PUBLIC')
(visibility='MODERATED')
```

Example to filter by site **preset**:

```
(preset='site-dashboard')
```

The default sort order for the returned list is for sites to be sorted by ascending title.
You can override the default by using the **orderBy** parameter. You can specify one or more of the following fields in the **orderBy** parameter:
* id
* title
* role


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_role_paging import SiteRolePaging
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    person_id = 'person_id_example' # str | The identifier of a person.
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    order_by = ['order_by_example'] # List[str] | A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)
    relations = ['relations_example'] # List[str] | Use the relations parameter to include one or more related entities in a single response. (optional)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)
    where = 'where_example' # str | A string to restrict the returned objects by using a predicate. (optional)

    try:
        # List site memberships
        api_response = api_instance.list_site_memberships_for_person(person_id, skip_count=skip_count, max_items=max_items, order_by=order_by, relations=relations, fields=fields, where=where)
        print("The response of SitesApi->list_site_memberships_for_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->list_site_memberships_for_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **order_by** | [**List[str]**](str.md)| A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  | [optional] 
 **relations** | [**List[str]**](str.md)| Use the relations parameter to include one or more related entities in a single response. | [optional] 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 
 **where** | **str**| A string to restrict the returned objects by using a predicate. | [optional] 

### Return type

[**SiteRolePaging**](SiteRolePaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **maxItems**, **skipCount**, **orderBy**, or **where** is invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **personId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sites**
> SitePaging list_sites(skip_count=skip_count, max_items=max_items, order_by=order_by, relations=relations, fields=fields, where=where)

List sites

Gets a list of sites in this repository.

You can use the **where** parameter to filter the returned sites by **visibility** or site **preset**.

Example to filter by **visibility**, use any one of:

```
(visibility='PRIVATE')
(visibility='PUBLIC')
(visibility='MODERATED')
```

Example to filter by site **preset**:

```
(preset='site-dashboard')
```

The default sort order for the returned list is for sites to be sorted by ascending title.
You can override the default by using the **orderBy** parameter. You can specify one or more of the following fields in the **orderBy** parameter:
* id
* title
* description

You can use the **relations** parameter to include one or more related
entities in a single response and so reduce network traffic.

The entity types in Alfresco are organized in a tree structure.
The **sites** entity has two children, **containers** and **members**.
The following relations parameter returns all the container and member
objects related to each site:

```
containers,members
```


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_paging import SitePaging
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    skip_count = 0 # int | The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  (optional) (default to 0)
    max_items = 100 # int | The maximum number of items to return in the list. If not supplied then the default value is 100.  (optional) (default to 100)
    order_by = ['order_by_example'] # List[str] | A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  (optional)
    relations = ['relations_example'] # List[str] | Use the relations parameter to include one or more related entities in a single response. (optional)
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)
    where = 'where_example' # str | A string to restrict the returned objects by using a predicate. (optional)

    try:
        # List sites
        api_response = api_instance.list_sites(skip_count=skip_count, max_items=max_items, order_by=order_by, relations=relations, fields=fields, where=where)
        print("The response of SitesApi->list_sites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->list_sites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **skip_count** | **int**| The number of entities that exist in the collection before those included in this list. If not supplied then the default value is 0.  | [optional] [default to 0]
 **max_items** | **int**| The maximum number of items to return in the list. If not supplied then the default value is 100.  | [optional] [default to 100]
 **order_by** | [**List[str]**](str.md)| A string to control the order of the entities returned in a list. You can use the **orderBy** parameter to sort the list by one or more fields.  Each field has a default sort order, which is normally ascending order. Read the API method implementation notes above to check if any fields used in this method have a descending default search order.  To sort the entities in a specific order, you can use the **ASC** and **DESC** keywords for any field.  | [optional] 
 **relations** | [**List[str]**](str.md)| Use the relations parameter to include one or more related entities in a single response. | [optional] 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 
 **where** | **str**| A string to restrict the returned objects by using a predicate. | [optional] 

### Return type

[**SitePaging**](SitePaging.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **maxItems**, **skipCount**, **orderBy**, or **where** is invalid  |  -  |
**401** | Authentication failed |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_site_membership_request**
> reject_site_membership_request(site_id, invitee_id, site_membership_rejection_body=site_membership_rejection_body)

Reject a site membership request

Reject a site membership request.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_membership_rejection_body import SiteMembershipRejectionBody
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_id = 'site_id_example' # str | The identifier of a site.
    invitee_id = 'invitee_id_example' # str | The invitee user name.
    site_membership_rejection_body = alfresco_core_client.SiteMembershipRejectionBody() # SiteMembershipRejectionBody | Rejecting a request to join, optionally, allows the inclusion of comment.  (optional)

    try:
        # Reject a site membership request
        api_instance.reject_site_membership_request(site_id, invitee_id, site_membership_rejection_body=site_membership_rejection_body)
    except Exception as e:
        print("Exception when calling SitesApi->reject_site_membership_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The identifier of a site. | 
 **invitee_id** | **str**| The invitee user name. | 
 **site_membership_rejection_body** | [**SiteMembershipRejectionBody**](SiteMembershipRejectionBody.md)| Rejecting a request to join, optionally, allows the inclusion of comment.  | [optional] 

### Return type

void (empty response body)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: value of **siteId** or **inviteeId** is invalid  |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have permission to reject membership request |  -  |
**404** | **siteId** or **inviteeId** does not exist  |  -  |
**422** | Integrity exception or not allowed to reject membership request.  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site**
> SiteEntry update_site(site_id, site_body_update, fields=fields)

Update a site

**Note:** this endpoint is available in Alfresco 5.2 and newer versions.

Update the details for the given site **siteId**. Site Manager or otherwise a
(site) admin can update title, description or visibility.

Note: the id of a site cannot be updated once the site has been created.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_body_update import SiteBodyUpdate
from alfresco_core_client.models.site_entry import SiteEntry
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_id = 'site_id_example' # str | The identifier of a site.
    site_body_update = alfresco_core_client.SiteBodyUpdate() # SiteBodyUpdate | The site information to update.
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Update a site
        api_response = api_instance.update_site(site_id, site_body_update, fields=fields)
        print("The response of SitesApi->update_site:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->update_site: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The identifier of a site. | 
 **site_body_update** | [**SiteBodyUpdate**](SiteBodyUpdate.md)| The site information to update. | 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteEntry**](SiteEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **siteBodyUpdate** invalid  |  -  |
**401** | Authentication failed |  -  |
**403** | Current user does not have permission to update the site that is visible to them. |  -  |
**404** | **siteId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_group_membership**
> SiteGroupEntry update_site_group_membership(site_id, group_id, site_membership_body_update, fields=fields)

Update site membership of group

**Note:** this endpoint is available in Alfresco 7.0.0 and newer versions.

Update the membership of person **groupId** in site **siteId**.
You can set the **role** to one of four types:
* SiteConsumer
* SiteCollaborator
* SiteContributor
* SiteManager


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_group_entry import SiteGroupEntry
from alfresco_core_client.models.site_membership_body_update import SiteMembershipBodyUpdate
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_id = 'site_id_example' # str | The identifier of a site.
    group_id = 'group_id_example' # str | The identifier of a group.
    site_membership_body_update = alfresco_core_client.SiteMembershipBodyUpdate() # SiteMembershipBodyUpdate | The groupId new role
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Update site membership of group
        api_response = api_instance.update_site_group_membership(site_id, group_id, site_membership_body_update, fields=fields)
        print("The response of SitesApi->update_site_group_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->update_site_group_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The identifier of a site. | 
 **group_id** | **str**| The identifier of a group. | 
 **site_membership_body_update** | [**SiteMembershipBodyUpdate**](SiteMembershipBodyUpdate.md)| The groupId new role | 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteGroupEntry**](SiteGroupEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **role** does not exist or **siteMembershipBodyUpdate** invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **siteId** or **groupId** does not exist  |  -  |
**422** | Integrity exception (eg. last site member must be a site manager) or not allowed to update group |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_membership**
> SiteMemberEntry update_site_membership(site_id, person_id, site_membership_body_update, fields=fields)

Update a site membership

Update the membership of person **personId** in site **siteId**.

You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.

You can set the **role** to one of four types:

* SiteConsumer
* SiteCollaborator
* SiteContributor
* SiteManager


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_member_entry import SiteMemberEntry
from alfresco_core_client.models.site_membership_body_update import SiteMembershipBodyUpdate
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    site_id = 'site_id_example' # str | The identifier of a site.
    person_id = 'person_id_example' # str | The identifier of a person.
    site_membership_body_update = alfresco_core_client.SiteMembershipBodyUpdate() # SiteMembershipBodyUpdate | The persons new role
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Update a site membership
        api_response = api_instance.update_site_membership(site_id, person_id, site_membership_body_update, fields=fields)
        print("The response of SitesApi->update_site_membership:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->update_site_membership: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **site_id** | **str**| The identifier of a site. | 
 **person_id** | **str**| The identifier of a person. | 
 **site_membership_body_update** | [**SiteMembershipBodyUpdate**](SiteMembershipBodyUpdate.md)| The persons new role | 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteMemberEntry**](SiteMemberEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **role** does not exist or **siteMembershipBodyUpdate** invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **siteId** or **personId** does not exist  |  -  |
**422** | Integrity exception (eg. last site member must be a site manager) or not allowed to update member |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_site_membership_request_for_person**
> SiteMembershipRequestEntry update_site_membership_request_for_person(person_id, site_id, site_membership_request_body_update, fields=fields)

Update a site membership request

Updates the message for the site membership request to site **siteId** for person **personId**.

You can use the `-me-` string in place of `<personId>` to specify the currently authenticated user.


### Example

* Basic Authentication (basicAuth):

```python
import alfresco_core_client
from alfresco_core_client.models.site_membership_request_body_update import SiteMembershipRequestBodyUpdate
from alfresco_core_client.models.site_membership_request_entry import SiteMembershipRequestEntry
from alfresco_core_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost/alfresco/api/-default-/public/alfresco/versions/1
# See configuration.py for a list of all supported configuration parameters.
configuration = alfresco_core_client.Configuration(
    host = "http://localhost/alfresco/api/-default-/public/alfresco/versions/1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = alfresco_core_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with alfresco_core_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = alfresco_core_client.SitesApi(api_client)
    person_id = 'person_id_example' # str | The identifier of a person.
    site_id = 'site_id_example' # str | The identifier of a site.
    site_membership_request_body_update = alfresco_core_client.SiteMembershipRequestBodyUpdate() # SiteMembershipRequestBodyUpdate | The new message to display
    fields = ['fields_example'] # List[str] | A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  (optional)

    try:
        # Update a site membership request
        api_response = api_instance.update_site_membership_request_for_person(person_id, site_id, site_membership_request_body_update, fields=fields)
        print("The response of SitesApi->update_site_membership_request_for_person:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SitesApi->update_site_membership_request_for_person: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **person_id** | **str**| The identifier of a person. | 
 **site_id** | **str**| The identifier of a site. | 
 **site_membership_request_body_update** | [**SiteMembershipRequestBodyUpdate**](SiteMembershipRequestBodyUpdate.md)| The new message to display | 
 **fields** | [**List[str]**](str.md)| A list of field names.  You can use this parameter to restrict the fields returned within a response if, for example, you want to save on overall bandwidth.  The list applies to a returned individual entity or entries within a collection.  If the API method also supports the **include** parameter, then the fields specified in the **include** parameter are returned in addition to those specified in the **fields** parameter.  | [optional] 

### Return type

[**SiteMembershipRequestEntry**](SiteMembershipRequestEntry.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid parameter: **id** is invalid or **siteMembershipRequestBodyUpdate** invalid  |  -  |
**401** | Authentication failed |  -  |
**404** | **personId** or **siteId** does not exist  |  -  |
**0** | Unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

