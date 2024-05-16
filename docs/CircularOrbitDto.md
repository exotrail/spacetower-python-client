# CircularOrbitDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**argument_of_latitude** | **float** | Units: [deg] | 
**var_date** | **str** | UTC date | 
**eccentricity_vector_x** | **float** | Eccentricity vector X. Units: [-] | 
**eccentricity_vector_y** | **float** | Eccentricity vector Y. Units: [-] | 
**frame** | **str** |  | 
**id** | **str** |  | [optional] 
**inclination** | **float** | Units: [deg] | 
**mean_osc_type** | **str** |  | 
**position_angle_type** | **str** |  | 
**raan** | **float** | Units: [deg] | 
**semi_major_axis** | **float** | Units: [km] | 

## Example

```python
from spacetower_python_client.models.circular_orbit_dto import CircularOrbitDto

# TODO update the JSON string below
json = "{}"
# create an instance of CircularOrbitDto from a JSON string
circular_orbit_dto_instance = CircularOrbitDto.from_json(json)
# print the JSON string representation of the object
print(CircularOrbitDto.to_json())

# convert the object into a dict
circular_orbit_dto_dict = circular_orbit_dto_instance.to_dict()
# create an instance of CircularOrbitDto from a dict
circular_orbit_dto_from_dict = CircularOrbitDto.from_dict(circular_orbit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


