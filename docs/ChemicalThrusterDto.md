# ChemicalThrusterDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**impulse** | **float** | Units: [Ns] | 
**maximum_thrust_duration** | **float** | Units: [s] | 
**propellant_mass** | **float** | Units: [kg] | 
**thrust** | **float** | Units: [N] | 
**thruster_axis_in_satellite_frame** | **List[float]** |  | 
**thruster_isp** | **float** | Units: [s] | 
**thruster_total_mass** | **float** | Wet mass. Units: [kg] | 
**warm_up_duration** | **float** | Units: [s] | 

## Example

```python
from fds_api_gen_client.models.chemical_thruster_dto import ChemicalThrusterDto

# TODO update the JSON string below
json = "{}"
# create an instance of ChemicalThrusterDto from a JSON string
chemical_thruster_dto_instance = ChemicalThrusterDto.from_json(json)
# print the JSON string representation of the object
print(ChemicalThrusterDto.to_json())

# convert the object into a dict
chemical_thruster_dto_dict = chemical_thruster_dto_instance.to_dict()
# create an instance of ChemicalThrusterDto from a dict
chemical_thruster_dto_from_dict = ChemicalThrusterDto.from_dict(chemical_thruster_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


