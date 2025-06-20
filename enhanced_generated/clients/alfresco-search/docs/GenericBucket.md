# GenericBucket

A bucket of facet results

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket_info** | [**GenericBucketBucketInfo**](GenericBucketBucketInfo.md) |  | [optional] 
**display** | **object** | An optional field for additional display information | [optional] 
**facets** | **List[object]** | Additional list of nested facets | [optional] 
**filter_query** | **str** | The filter query you can use to apply this facet | [optional] 
**label** | **str** | The bucket label | [optional] 
**metrics** | [**List[GenericMetric]**](GenericMetric.md) | An array of buckets and values | [optional] 

## Example

```python
from alfresco_search_client.models.generic_bucket import GenericBucket

# TODO update the JSON string below
json = "{}"
# create an instance of GenericBucket from a JSON string
generic_bucket_instance = GenericBucket.from_json(json)
# print the JSON string representation of the object
print(GenericBucket.to_json())

# convert the object into a dict
generic_bucket_dict = generic_bucket_instance.to_dict()
# create an instance of GenericBucket from a dict
generic_bucket_from_dict = GenericBucket.from_dict(generic_bucket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


