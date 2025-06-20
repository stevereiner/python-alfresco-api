# Node

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowable_operations** | **list[str]** |  | [optional] 
**aspect_names** | **list[str]** |  | [optional] 
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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

