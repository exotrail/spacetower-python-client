# ManeuverGenerationReportDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_thrust_duration** | **float** |  | [optional] 
**final_duty_cycle** | **float** |  | [optional] 
**number_of_period** | **float** |  | [optional] 
**orbital_states** | [**List[OrbitalStateDto]**](OrbitalStateDto.md) |  | [optional] 
**simulation_duration** | **float** |  | [optional] 
**thruster_duty_cycle** | **float** |  | [optional] 
**total_burns_duration** | **float** |  | [optional] 
**total_consumption** | **float** |  | [optional] 
**total_delta_v** | **float** |  | [optional] 
**total_impulse** | **float** |  | [optional] 
**total_number_of_burns** | **int** |  | [optional] 
**total_warmup_duty_cycle** | **float** |  | [optional] 

## Example

```python
from spacetower_python_client.models.maneuver_generation_report_dto import ManeuverGenerationReportDto

# TODO update the JSON string below
json = "{}"
# create an instance of ManeuverGenerationReportDto from a JSON string
maneuver_generation_report_dto_instance = ManeuverGenerationReportDto.from_json(json)
# print the JSON string representation of the object
print(ManeuverGenerationReportDto.to_json())

# convert the object into a dict
maneuver_generation_report_dto_dict = maneuver_generation_report_dto_instance.to_dict()
# create an instance of ManeuverGenerationReportDto from a dict
maneuver_generation_report_dto_from_dict = ManeuverGenerationReportDto.from_dict(maneuver_generation_report_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


