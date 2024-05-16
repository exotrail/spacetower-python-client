# BoxSpacecraftInputDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**battery_id** | **str** |  | 
**drag_coefficient** | **float** | Units: [-] | 
**id** | **str** |  | [optional] 
**max_angular_acceleration** | **float** | Units: [deg/s²] | 
**max_angular_velocity** | **float** | Units: [deg/s] | 
**platform_mass** | **float** |  | 
**reflection_coefficient** | **float** | Units: [-] | [optional] 
**solar_array_id** | **str** |  | 
**spacecraft_length_x** | **float** | Units: [m] | 
**spacecraft_length_y** | **float** | Units: [m] | 
**spacecraft_length_z** | **float** | Units: [m] | 
**thruster_id** | **str** |  | 

## Example

```python
from spacetower_python_client.models.box_spacecraft_input_dto import BoxSpacecraftInputDto

# TODO update the JSON string below
json = "{}"
# create an instance of BoxSpacecraftInputDto from a JSON string
box_spacecraft_input_dto_instance = BoxSpacecraftInputDto.from_json(json)
# print the JSON string representation of the object
print(BoxSpacecraftInputDto.to_json())

# convert the object into a dict
box_spacecraft_input_dto_dict = box_spacecraft_input_dto_instance.to_dict()
# create an instance of BoxSpacecraftInputDto from a dict
box_spacecraft_input_dto_from_dict = BoxSpacecraftInputDto.from_dict(box_spacecraft_input_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


