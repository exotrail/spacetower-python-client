# ElectricalThrusterDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**impulse** | **float** | Units: [Ns] | 
**maximum_thrust_duration** | **float** | Units: [s] | 
**propellant_mass** | **float** | Units: [kg] | 
**stand_by_power** | **float** | Units: [W] | 
**thrust** | **float** | Units: [N] | 
**thruster_axis_in_satellite_frame** | **List[float]** |  | 
**thruster_isp** | **float** | Units: [s] | 
**thruster_power** | **float** | Units: [W] | 
**thruster_total_mass** | **float** | Wet mass. Units: [kg] | 
**warm_up_duration** | **float** | Units: [s] | 
**warm_up_power** | **float** | Units: [W] | 

## Example

```python
from spacetower_python_client.models.electrical_thruster_dto import ElectricalThrusterDto

# TODO update the JSON string below
json = "{}"
# create an instance of ElectricalThrusterDto from a JSON string
electrical_thruster_dto_instance = ElectricalThrusterDto.from_json(json)
# print the JSON string representation of the object
print(ElectricalThrusterDto.to_json())

# convert the object into a dict
electrical_thruster_dto_dict = electrical_thruster_dto_instance.to_dict()
# create an instance of ElectricalThrusterDto from a dict
electrical_thruster_dto_from_dict = ElectricalThrusterDto.from_dict(electrical_thruster_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


