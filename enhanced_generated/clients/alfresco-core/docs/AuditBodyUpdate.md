# AuditBodyUpdate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enabled** | **bool** |  | [optional] 

## Example

```python
from alfresco_core_client.models.audit_body_update import AuditBodyUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of AuditBodyUpdate from a JSON string
audit_body_update_instance = AuditBodyUpdate.from_json(json)
# print the JSON string representation of the object
print(AuditBodyUpdate.to_json())

# convert the object into a dict
audit_body_update_dict = audit_body_update_instance.to_dict()
# create an instance of AuditBodyUpdate from a dict
audit_body_update_from_dict = AuditBodyUpdate.from_dict(audit_body_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


