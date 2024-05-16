# ManeuverGenerationLogDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computation_date** | **datetime** |  | [optional] 
**computation_status** | **str** |  | [optional] 
**error_messages** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from fds_api_gen_client.models.maneuver_generation_log_dto import ManeuverGenerationLogDto

# TODO update the JSON string below
json = "{}"
# create an instance of ManeuverGenerationLogDto from a JSON string
maneuver_generation_log_dto_instance = ManeuverGenerationLogDto.from_json(json)
# print the JSON string representation of the object
print(ManeuverGenerationLogDto.to_json())

# convert the object into a dict
maneuver_generation_log_dto_dict = maneuver_generation_log_dto_instance.to_dict()
# create an instance of ManeuverGenerationLogDto from a dict
maneuver_generation_log_dto_from_dict = ManeuverGenerationLogDto.from_dict(maneuver_generation_log_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


