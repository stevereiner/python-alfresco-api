# RequestPivot

A list of pivots.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | A key corresponding to a matching field facet label or stats. | [optional] 
**pivots** | [**List[RequestPivot]**](RequestPivot.md) |  | [optional] 

## Example

```python
from alfresco_search_client.models.request_pivot import RequestPivot

# TODO update the JSON string below
json = "{}"
# create an instance of RequestPivot from a JSON string
request_pivot_instance = RequestPivot.from_json(json)
# print the JSON string representation of the object
print(RequestPivot.to_json())

# convert the object into a dict
request_pivot_dict = request_pivot_instance.to_dict()
# create an instance of RequestPivot from a dict
request_pivot_from_dict = RequestPivot.from_dict(request_pivot_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


