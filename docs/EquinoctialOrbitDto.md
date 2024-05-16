# EquinoctialOrbitDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | UTC date | 
**eccentricity_vector_x** | **float** | Eccentricity vector X. Units: [-] | 
**eccentricity_vector_y** | **float** | Eccentricity vector Y. Units: [-] | 
**equinoctial_longitude** | **float** | Units: [deg] | 
**frame** | **str** |  | 
**id** | **str** |  | [optional] 
**inclination_vector_x** | **float** | Inclination vector X. Units: [-] | 
**inclination_vector_y** | **float** | Inclination vector Y. Units: [-] | 
**mean_osc_type** | **str** |  | 
**position_angle_type** | **str** |  | 
**semi_major_axis** | **float** | Units: [km] | 

## Example

```python
from spacetower_python_client.models.equinoctial_orbit_dto import EquinoctialOrbitDto

# TODO update the JSON string below
json = "{}"
# create an instance of EquinoctialOrbitDto from a JSON string
equinoctial_orbit_dto_instance = EquinoctialOrbitDto.from_json(json)
# print the JSON string representation of the object
print(EquinoctialOrbitDto.to_json())

# convert the object into a dict
equinoctial_orbit_dto_dict = equinoctial_orbit_dto_instance.to_dict()
# create an instance of EquinoctialOrbitDto from a dict
equinoctial_orbit_dto_from_dict = EquinoctialOrbitDto.from_dict(equinoctial_orbit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


