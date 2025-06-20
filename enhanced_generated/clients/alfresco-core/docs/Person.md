# Person


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_names** | **List[str]** |  | [optional] 
**avatar_id** | **str** |  | [optional] 
**capabilities** | [**Capabilities**](Capabilities.md) |  | [optional] 
**company** | [**Company**](Company.md) |  | [optional] 
**description** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**email** | **str** |  | 
**email_notifications_enabled** | **bool** |  | [optional] [default to True]
**enabled** | **bool** |  | [default to True]
**first_name** | **str** |  | 
**google_id** | **str** |  | [optional] 
**id** | **str** |  | 
**instant_message_id** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**mobile** | **str** |  | [optional] 
**properties** | **object** |  | [optional] 
**skype_id** | **str** |  | [optional] 
**status_updated_at** | **datetime** |  | [optional] 
**telephone** | **str** |  | [optional] 
**user_status** | **str** |  | [optional] 

## Example

```python
from alfresco_core_client.models.person import Person

# TODO update the JSON string below
json = "{}"
# create an instance of Person from a JSON string
person_instance = Person.from_json(json)
# print the JSON string representation of the object
print(Person.to_json())

# convert the object into a dict
person_dict = person_instance.to_dict()
# create an instance of Person from a dict
person_from_dict = Person.from_dict(person_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


