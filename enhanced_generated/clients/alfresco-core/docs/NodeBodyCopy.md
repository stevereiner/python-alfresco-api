# NodeBodyCopy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name must not contain spaces or the following special characters: * \&quot; &lt; &gt; \\ / ? : and |. The character . must not be used at the end of the name.  | [optional] 
**target_parent_id** | **str** |  | 

## Example

```python
from alfresco_core_client.models.node_body_copy import NodeBodyCopy

# TODO update the JSON string below
json = "{}"
# create an instance of NodeBodyCopy from a JSON string
node_body_copy_instance = NodeBodyCopy.from_json(json)
# print the JSON string representation of the object
print(NodeBodyCopy.to_json())

# convert the object into a dict
node_body_copy_dict = node_body_copy_instance.to_dict()
# create an instance of NodeBodyCopy from a dict
node_body_copy_from_dict = NodeBodyCopy.from_dict(node_body_copy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


