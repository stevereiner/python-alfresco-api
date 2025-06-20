# ResultNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowable_operations** | **List[str]** |  | [optional] 
**aspect_names** | **List[str]** |  | [optional] 
**content** | [**ContentInfo**](ContentInfo.md) |  | [optional] 
**created_at** | **datetime** |  | 
**created_by_user** | [**UserInfo**](UserInfo.md) |  | 
**id** | **str** |  | 
**is_file** | **bool** |  | 
**is_folder** | **bool** |  | 
**is_link** | **bool** |  | [optional] 
**is_locked** | **bool** |  | [optional] [default to False]
**modified_at** | **datetime** |  | 
**modified_by_user** | [**UserInfo**](UserInfo.md) |  | 
**name** | **str** | The name must not contain spaces or the following special characters: * \&quot; &lt; &gt; \\ / ? : and |. The character . must not be used at the end of the name.  | 
**node_type** | **str** |  | 
**parent_id** | **str** |  | [optional] 
**path** | [**PathInfo**](PathInfo.md) |  | [optional] 
**properties** | **object** |  | [optional] 
**archived_at** | **datetime** |  | [optional] 
**archived_by_user** | [**UserInfo**](UserInfo.md) |  | [optional] 
**search** | [**SearchEntry**](SearchEntry.md) |  | [optional] 
**version_comment** | **str** |  | [optional] 
**version_label** | **str** |  | [optional] 

## Example

```python
from alfresco_search_client.models.result_node import ResultNode

# TODO update the JSON string below
json = "{}"
# create an instance of ResultNode from a JSON string
result_node_instance = ResultNode.from_json(json)
# print the JSON string representation of the object
print(ResultNode.to_json())

# convert the object into a dict
result_node_dict = result_node_instance.to_dict()
# create an instance of ResultNode from a dict
result_node_from_dict = ResultNode.from_dict(result_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


