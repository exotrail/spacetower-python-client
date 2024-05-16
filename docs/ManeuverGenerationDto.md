# ManeuverGenerationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delta_eccentricity** | **float** |  | [optional] 
**delta_inclination** | **float** |  | [optional] 
**delta_semi_major_axis** | **float** |  | [optional] 
**id** | **str** |  | [optional] 
**initial_orbit** | **object** |  | [optional] 
**maximum_duration** | **float** |  | [optional] 
**orbital_states_required** | **str** |  | [optional] 
**propagation_context** | [**PropagationContextDto**](PropagationContextDto.md) |  | [optional] 
**quaternion_step** | **float** |  | [optional] 
**spacecraft** | **object** |  | [optional] 
**strategy** | [**ManeuverStrategyDto**](ManeuverStrategyDto.md) |  | [optional] 

## Example

```python
from fds_api_gen_client.models.maneuver_generation_dto import ManeuverGenerationDto

# TODO update the JSON string below
json = "{}"
# create an instance of ManeuverGenerationDto from a JSON string
maneuver_generation_dto_instance = ManeuverGenerationDto.from_json(json)
# print the JSON string representation of the object
print(ManeuverGenerationDto.to_json())

# convert the object into a dict
maneuver_generation_dto_dict = maneuver_generation_dto_instance.to_dict()
# create an instance of ManeuverGenerationDto from a dict
maneuver_generation_dto_from_dict = ManeuverGenerationDto.from_dict(maneuver_generation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


