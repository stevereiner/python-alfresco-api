# DirectAccessUrlBodyCreate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **datetime** |  | [optional] 
**valid_for** | **int** | The length of time in seconds that the url is valid for.  | [optional] 

## Example

```python
from alfresco_core_client.models.direct_access_url_body_create import DirectAccessUrlBodyCreate

# TODO update the JSON string below
json = "{}"
# create an instance of DirectAccessUrlBodyCreate from a JSON string
direct_access_url_body_create_instance = DirectAccessUrlBodyCreate.from_json(json)
# print the JSON string representation of the object
print(DirectAccessUrlBodyCreate.to_json())

# convert the object into a dict
direct_access_url_body_create_dict = direct_access_url_body_create_instance.to_dict()
# create an instance of DirectAccessUrlBodyCreate from a dict
direct_access_url_body_create_from_dict = DirectAccessUrlBodyCreate.from_dict(direct_access_url_body_create_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


