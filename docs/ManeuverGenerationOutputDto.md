# ManeuverGenerationOutputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delta_eccentricity** | **float** |  | [optional] 
**delta_inclination** | **float** |  | [optional] 
**delta_semi_major_axis** | **float** |  | [optional] 
**id** | **str** |  | [optional] 
**initial_orbital_state** | [**OrbitalStateDto**](OrbitalStateDto.md) |  | [optional] 
**maximum_duration** | **float** |  | [optional] 
**quaternion_step** | **float** |  | [optional] 
**required_output_orbital_states** | **str** |  | [optional] 
**strategy** | [**ManeuverStrategyDto**](ManeuverStrategyDto.md) |  | [optional] 

## Example

```python
from fds_api_gen_client.models.maneuver_generation_output_dto import ManeuverGenerationOutputDto

# TODO update the JSON string below
json = "{}"
# create an instance of ManeuverGenerationOutputDto from a JSON string
maneuver_generation_output_dto_instance = ManeuverGenerationOutputDto.from_json(json)
# print the JSON string representation of the object
print(ManeuverGenerationOutputDto.to_json())

# convert the object into a dict
maneuver_generation_output_dto_dict = maneuver_generation_output_dto_instance.to_dict()
# create an instance of ManeuverGenerationOutputDto from a dict
maneuver_generation_output_dto_from_dict = ManeuverGenerationOutputDto.from_dict(maneuver_generation_output_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


