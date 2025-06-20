# Version


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aspect_names** | **List[str]** |  | [optional] 
**content** | [**ContentInfo**](ContentInfo.md) |  | [optional] 
**id** | **str** |  | 
**is_file** | **bool** |  | 
**is_folder** | **bool** |  | 
**modified_at** | **datetime** |  | 
**modified_by_user** | [**UserInfo**](UserInfo.md) |  | 
**name** | **str** | The name must not contain spaces or the following special characters: * \&quot; &lt; &gt; \\ / ? : and |. The character . must not be used at the end of the name.  | 
**node_type** | **str** |  | 
**properties** | **object** |  | [optional] 
**version_comment** | **str** |  | [optional] 

## Example

```python
from alfresco_core_client.models.version import Version

# TODO update the JSON string below
json = "{}"
# create an instance of Version from a JSON string
version_instance = Version.from_json(json)
# print the JSON string representation of the object
print(Version.to_json())

# convert the object into a dict
version_dict = version_instance.to_dict()
# create an instance of Version from a dict
version_from_dict = Version.from_dict(version_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


