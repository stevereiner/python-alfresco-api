# RequestTemplatesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The template name | [optional] 
**template** | **str** | The template | [optional] 

## Example

```python
from alfresco_search_client.models.request_templates_inner import RequestTemplatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of RequestTemplatesInner from a JSON string
request_templates_inner_instance = RequestTemplatesInner.from_json(json)
# print the JSON string representation of the object
print(RequestTemplatesInner.to_json())

# convert the object into a dict
request_templates_inner_dict = request_templates_inner_instance.to_dict()
# create an instance of RequestTemplatesInner from a dict
request_templates_inner_from_dict = RequestTemplatesInner.from_dict(request_templates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


