# SphericalSpacecraftDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**drag_coefficient** | **float** | Units: [-] | 
**id** | **str** |  | [optional] 
**platform_mass** | **float** | Units: [kg] | 
**reflection_coefficient** | **float** | Units: [-] | [optional] 
**spherical_cross_section** | **float** | Units: [m²] | 

## Example

```python
from spacetower_python_client.models.spherical_spacecraft_dto import SphericalSpacecraftDto

# TODO update the JSON string below
json = "{}"
# create an instance of SphericalSpacecraftDto from a JSON string
spherical_spacecraft_dto_instance = SphericalSpacecraftDto.from_json(json)
# print the JSON string representation of the object
print(SphericalSpacecraftDto.to_json())

# convert the object into a dict
spherical_spacecraft_dto_dict = spherical_spacecraft_dto_instance.to_dict()
# create an instance of SphericalSpacecraftDto from a dict
spherical_spacecraft_dto_from_dict = SphericalSpacecraftDto.from_dict(spherical_spacecraft_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


