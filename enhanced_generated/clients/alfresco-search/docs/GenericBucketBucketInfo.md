# GenericBucketBucketInfo

Additional information of nested facet

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **str** | The end of range | [optional] 
**end_inclusive** | **bool** | Includes values less than or equal to \&quot;end\&quot; | [optional] 
**start** | **str** | The start of range | [optional] 
**start_inclusive** | **bool** | Includes values greater or equal to \&quot;start\&quot; | [optional] 

## Example

```python
from alfresco_search_client.models.generic_bucket_bucket_info import GenericBucketBucketInfo

# TODO update the JSON string below
json = "{}"
# create an instance of GenericBucketBucketInfo from a JSON string
generic_bucket_bucket_info_instance = GenericBucketBucketInfo.from_json(json)
# print the JSON string representation of the object
print(GenericBucketBucketInfo.to_json())

# convert the object into a dict
generic_bucket_bucket_info_dict = generic_bucket_bucket_info_instance.to_dict()
# create an instance of GenericBucketBucketInfo from a dict
generic_bucket_bucket_info_from_dict = GenericBucketBucketInfo.from_dict(generic_bucket_bucket_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


