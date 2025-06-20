# GenericMetric

A metric used in faceting

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The type of metric, e.g. count | [optional] 
**value** | **object** | The metric value, e.g. {\&quot;count\&quot;: 34}  | [optional] 

## Example

```python
from alfresco_search_client.models.generic_metric import GenericMetric

# TODO update the JSON string below
json = "{}"
# create an instance of GenericMetric from a JSON string
generic_metric_instance = GenericMetric.from_json(json)
# print the JSON string representation of the object
print(GenericMetric.to_json())

# convert the object into a dict
generic_metric_dict = generic_metric_instance.to_dict()
# create an instance of GenericMetric from a dict
generic_metric_from_dict = GenericMetric.from_dict(generic_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


