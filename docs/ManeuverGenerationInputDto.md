# ManeuverGenerationInputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delta_eccentricity** | **float** | Units: [-] | 
**delta_inclination** | **float** | Units: [deg] | 
**delta_semi_major_axis** | **float** | Units: [km] | 
**initial_orbital_state_id** | **str** |  | 
**maximum_duration** | **float** | Units: [s] | 
**no_firing_date_intervals** | [**List[DateIntervalDto]**](DateIntervalDto.md) | Date intervals where the maneuver is not allowed to be executed | [optional] 
**quaternion_step** | **float** | Units: [s] | 
**required_output_orbital_states** | **str** |  | [optional] 
**strategy_id** | **str** |  | 

## Example

```python
from spacetower_python_client.models.maneuver_generation_input_dto import ManeuverGenerationInputDto

# TODO update the JSON string below
json = "{}"
# create an instance of ManeuverGenerationInputDto from a JSON string
maneuver_generation_input_dto_instance = ManeuverGenerationInputDto.from_json(json)
# print the JSON string representation of the object
print(ManeuverGenerationInputDto.to_json())

# convert the object into a dict
maneuver_generation_input_dto_dict = maneuver_generation_input_dto_instance.to_dict()
# create an instance of ManeuverGenerationInputDto from a dict
maneuver_generation_input_dto_from_dict = ManeuverGenerationInputDto.from_dict(maneuver_generation_input_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


