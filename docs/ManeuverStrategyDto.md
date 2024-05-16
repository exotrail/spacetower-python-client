# ManeuverStrategyDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**number_of_rest_orbits** | **int** | Units: [-] | 
**number_of_shift_orbits** | **int** | Units: [-] | 
**number_of_thrust_orbits** | **int** | Units: [-] | 
**orbital_duty_cycle** | **float** | Units: [%] | [optional] 
**stop_thrust_at_eclipse** | **bool** |  | 
**thrust_arc_definition** | **str** |  | 
**thrust_arc_duration** | **float** | Units: [s] | [optional] 
**thrust_arcs_number** | **str** |  | 
**thrust_arcs_position** | **str** |  | 

## Example

```python
from spacetower_python_client.models.maneuver_strategy_dto import ManeuverStrategyDto

# TODO update the JSON string below
json = "{}"
# create an instance of ManeuverStrategyDto from a JSON string
maneuver_strategy_dto_instance = ManeuverStrategyDto.from_json(json)
# print the JSON string representation of the object
print(ManeuverStrategyDto.to_json())

# convert the object into a dict
maneuver_strategy_dto_dict = maneuver_strategy_dto_instance.to_dict()
# create an instance of ManeuverStrategyDto from a dict
maneuver_strategy_dto_from_dict = ManeuverStrategyDto.from_dict(maneuver_strategy_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


