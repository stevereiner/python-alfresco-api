# Download


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_added** | **int** | number of bytes added so far in the zip | [optional] [default to 0]
**files_added** | **int** | number of files added so far in the zip | [optional] [default to 0]
**id** | **str** | the id of the download node | [optional] 
**status** | **str** | the current status of the download node creation | [optional] [default to 'PENDING']
**total_bytes** | **int** | the total number of bytes to be added in the zip | [optional] [default to 0]
**total_files** | **int** | the total number of files to be added in the zip | [optional] [default to 0]

## Example

```python
from alfresco_core_client.models.download import Download

# TODO update the JSON string below
json = "{}"
# create an instance of Download from a JSON string
download_instance = Download.from_json(json)
# print the JSON string representation of the object
print(Download.to_json())

# convert the object into a dict
download_dict = download_instance.to_dict()
# create an instance of Download from a dict
download_from_dict = Download.from_dict(download_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


