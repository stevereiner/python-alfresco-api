# DownloadEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry** | [**Download**](Download.md) |  | 

## Example

```python
from alfresco_core_client.models.download_entry import DownloadEntry

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadEntry from a JSON string
download_entry_instance = DownloadEntry.from_json(json)
# print the JSON string representation of the object
print(DownloadEntry.to_json())

# convert the object into a dict
download_entry_dict = download_entry_instance.to_dict()
# create an instance of DownloadEntry from a dict
download_entry_from_dict = DownloadEntry.from_dict(download_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


