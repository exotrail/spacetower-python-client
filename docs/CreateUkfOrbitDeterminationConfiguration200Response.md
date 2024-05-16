# CreateUkfOrbitDeterminationConfiguration200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alpha** | **float** | Defines the spread of the sigma points. Typical values from 1E-4 to 1E-1 | 
**beta** | **float** | Incorporates knowledge about the distribution of the state vector. Beta &#x3D; 2 is optimal for Gaussian distributions | 
**id** | **str** |  | [optional] 
**kappa** | **float** | Secondary scaling parameter. Usually set to 0 | 
**noise_provider_type** | **str** | Model for the state noise dynamics | 
**outlier_manager_settings** | [**OutlierManagerSettingsDto**](OutlierManagerSettingsDto.md) |  | [optional] 
**process_noise_matrix_id** | **str** | UUID of the covariance matrix for the state noise distribution | 

## Example

```python
from fds_api_gen_client.models.create_ukf_orbit_determination_configuration200_response import CreateUkfOrbitDeterminationConfiguration200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUkfOrbitDeterminationConfiguration200Response from a JSON string
create_ukf_orbit_determination_configuration200_response_instance = CreateUkfOrbitDeterminationConfiguration200Response.from_json(json)
# print the JSON string representation of the object
print(CreateUkfOrbitDeterminationConfiguration200Response.to_json())

# convert the object into a dict
create_ukf_orbit_determination_configuration200_response_dict = create_ukf_orbit_determination_configuration200_response_instance.to_dict()
# create an instance of CreateUkfOrbitDeterminationConfiguration200Response from a dict
create_ukf_orbit_determination_configuration200_response_from_dict = CreateUkfOrbitDeterminationConfiguration200Response.from_dict(create_ukf_orbit_determination_configuration200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


