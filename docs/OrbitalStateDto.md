# OrbitalStateDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**covariance_matrix_id** | **str** |  | [optional] 
**creation_date** | **str** |  | [optional] 
**fitted_tle** | [**TLE**](TLE.md) |  | [optional] 
**id** | **str** |  | [optional] 
**mean_orbit_id** | **str** | Mean orbit data computed with the DSST propagator. | [optional] 
**osculating_orbit_id** | **str** |  | [optional] 
**propagation_context_id** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**spacecraft_id** | **str** |  | [optional] 

## Example

```python
from fds_api_gen_client.models.orbital_state_dto import OrbitalStateDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrbitalStateDto from a JSON string
orbital_state_dto_instance = OrbitalStateDto.from_json(json)
# print the JSON string representation of the object
print(OrbitalStateDto.to_json())

# convert the object into a dict
orbital_state_dto_dict = orbital_state_dto_instance.to_dict()
# create an instance of OrbitalStateDto from a dict
orbital_state_dto_from_dict = OrbitalStateDto.from_dict(orbital_state_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


