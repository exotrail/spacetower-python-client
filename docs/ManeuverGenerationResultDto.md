# ManeuverGenerationResultDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**log** | [**ManeuverGenerationLogDto**](ManeuverGenerationLogDto.md) |  | [optional] 
**report** | [**ManeuverGenerationReportDto**](ManeuverGenerationReportDto.md) |  | [optional] 
**request** | [**ManeuverGenerationOutputDto**](ManeuverGenerationOutputDto.md) |  | [optional] 
**roadmap** | **object** |  | [optional] 

## Example

```python
from fds_api_gen_client.models.maneuver_generation_result_dto import ManeuverGenerationResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of ManeuverGenerationResultDto from a JSON string
maneuver_generation_result_dto_instance = ManeuverGenerationResultDto.from_json(json)
# print the JSON string representation of the object
print(ManeuverGenerationResultDto.to_json())

# convert the object into a dict
maneuver_generation_result_dto_dict = maneuver_generation_result_dto_instance.to_dict()
# create an instance of ManeuverGenerationResultDto from a dict
maneuver_generation_result_dto_from_dict = ManeuverGenerationResultDto.from_dict(maneuver_generation_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


