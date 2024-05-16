# ManeuverGenerationCommandDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delta_eccentricity** | **float** | Units: [-] | 
**delta_inclination** | **float** | Units: [deg] | 
**delta_semi_major_axis** | **float** | Units: [km] | 
**id** | **str** |  | [optional] 
**initial_orbit_id** | **str** |  | 
**maximum_duration** | **float** | Units: [s] | 
**orbital_states_required** | **str** |  | 
**propagation_context_id** | **str** |  | 
**quaternion_step** | **float** | Units: [s] | 
**spacecraft_id** | **str** |  | 
**strategy_id** | **str** |  | 

## Example

```python
from fds_api_gen_client.models.maneuver_generation_command_dto import ManeuverGenerationCommandDto

# TODO update the JSON string below
json = "{}"
# create an instance of ManeuverGenerationCommandDto from a JSON string
maneuver_generation_command_dto_instance = ManeuverGenerationCommandDto.from_json(json)
# print the JSON string representation of the object
print(ManeuverGenerationCommandDto.to_json())

# convert the object into a dict
maneuver_generation_command_dto_dict = maneuver_generation_command_dto_instance.to_dict()
# create an instance of ManeuverGenerationCommandDto from a dict
maneuver_generation_command_dto_from_dict = ManeuverGenerationCommandDto.from_dict(maneuver_generation_command_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


