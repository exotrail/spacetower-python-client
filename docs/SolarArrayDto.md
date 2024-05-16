# SolarArrayDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**maximum_power** | **float** | Units: [W] | [optional] 
**satellite_faces** | **List[str]** |  | [optional] 
**solar_array_axis_in_satellite_frame** | **List[float]** |  | [optional] 
**solar_array_definition_type** | **str** |  | 
**solar_array_efficiency** | **float** | x in (0,1), Units: [-] | 
**solar_array_normal_in_satellite_frame** | **List[float]** |  | 
**solar_array_type** | **str** |  | 
**surface** | **float** | Units: [m²] | [optional] 

## Example

```python
from fds_api_gen_client.models.solar_array_dto import SolarArrayDto

# TODO update the JSON string below
json = "{}"
# create an instance of SolarArrayDto from a JSON string
solar_array_dto_instance = SolarArrayDto.from_json(json)
# print the JSON string representation of the object
print(SolarArrayDto.to_json())

# convert the object into a dict
solar_array_dto_dict = solar_array_dto_instance.to_dict()
# create an instance of SolarArrayDto from a dict
solar_array_dto_from_dict = SolarArrayDto.from_dict(solar_array_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


