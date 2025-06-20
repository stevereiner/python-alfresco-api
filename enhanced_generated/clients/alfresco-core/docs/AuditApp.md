# AuditApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**is_enabled** | **bool** |  | [optional] [default to True]
**max_entry_id** | **int** |  | [optional] 
**min_entry_id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from alfresco_core_client.models.audit_app import AuditApp

# TODO update the JSON string below
json = "{}"
# create an instance of AuditApp from a JSON string
audit_app_instance = AuditApp.from_json(json)
# print the JSON string representation of the object
print(AuditApp.to_json())

# convert the object into a dict
audit_app_dict = audit_app_instance.to_dict()
# create an instance of AuditApp from a dict
audit_app_from_dict = AuditApp.from_dict(audit_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


