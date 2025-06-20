# PathElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from alfresco_search_client.models.path_element import PathElement

# TODO update the JSON string below
json = "{}"
# create an instance of PathElement from a JSON string
path_element_instance = PathElement.from_json(json)
# print the JSON string representation of the object
print(PathElement.to_json())

# convert the object into a dict
path_element_dict = path_element_instance.to_dict()
# create an instance of PathElement from a dict
path_element_from_dict = PathElement.from_dict(path_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


