# OrbitalStateCreationRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**covariance_matrix_id** | **str** |  | [optional] 
**orbit_id** | **str** | Orbit ID (osculating or mean) is mandatory if no TLE is provided. | [optional] 
**propagation_context_id** | **str** |  | 
**spacecraft_id** | **str** |  | 
**tle** | [**TLE**](TLE.md) |  | [optional] 

## Example

```python
from fds_api_gen_client.models.orbital_state_creation_request_dto import OrbitalStateCreationRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrbitalStateCreationRequestDto from a JSON string
orbital_state_creation_request_dto_instance = OrbitalStateCreationRequestDto.from_json(json)
# print the JSON string representation of the object
print(OrbitalStateCreationRequestDto.to_json())

# convert the object into a dict
orbital_state_creation_request_dto_dict = orbital_state_creation_request_dto_instance.to_dict()
# create an instance of OrbitalStateCreationRequestDto from a dict
orbital_state_creation_request_dto_from_dict = OrbitalStateCreationRequestDto.from_dict(orbital_state_creation_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


