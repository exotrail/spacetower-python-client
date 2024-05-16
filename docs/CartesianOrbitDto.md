# CartesianOrbitDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | UTC date | 
**frame** | **str** |  | 
**id** | **str** |  | [optional] 
**position_x** | **float** | Position X. Units: [km] | 
**position_y** | **float** | Position Y. Units: [km] | 
**position_z** | **float** | Position Z. Units: [km] | 
**velocity_x** | **float** | Velocity X. Units: [km/s] | 
**velocity_y** | **float** | Velocity Y. Units: [km/s] | 
**velocity_z** | **float** | Velocity Z. Units: [km/s] | 

## Example

```python
from fds_api_gen_client.models.cartesian_orbit_dto import CartesianOrbitDto

# TODO update the JSON string below
json = "{}"
# create an instance of CartesianOrbitDto from a JSON string
cartesian_orbit_dto_instance = CartesianOrbitDto.from_json(json)
# print the JSON string representation of the object
print(CartesianOrbitDto.to_json())

# convert the object into a dict
cartesian_orbit_dto_dict = cartesian_orbit_dto_instance.to_dict()
# create an instance of CartesianOrbitDto from a dict
cartesian_orbit_dto_from_dict = CartesianOrbitDto.from_dict(cartesian_orbit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


