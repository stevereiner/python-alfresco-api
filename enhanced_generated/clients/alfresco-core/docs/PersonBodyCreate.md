# PersonBodyCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_names** | **List[str]** |  | [optional] 
**company** | [**Company**](Company.md) |  | [optional] 
**description** | **str** |  | [optional] 
**email** | **str** |  | 
**email_notifications_enabled** | **bool** |  | [optional] [default to True]
**enabled** | **bool** |  | [optional] [default to True]
**first_name** | **str** |  | 
**google_id** | **str** |  | [optional] 
**id** | **str** |  | 
**instant_message_id** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**mobile** | **str** |  | [optional] 
**password** | **str** |  | 
**properties** | **object** |  | [optional] 
**skype_id** | **str** |  | [optional] 
**telephone** | **str** |  | [optional] 
**user_status** | **str** |  | [optional] 

## Example

```python
from alfresco_core_client.models.person_body_create import PersonBodyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of PersonBodyCreate from a JSON string
person_body_create_instance = PersonBodyCreate.from_json(json)
# print the JSON string representation of the object
print(PersonBodyCreate.to_json())

# convert the object into a dict
person_body_create_dict = person_body_create_instance.to_dict()
# create an instance of PersonBodyCreate from a dict
person_body_create_from_dict = PersonBodyCreate.from_dict(person_body_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


