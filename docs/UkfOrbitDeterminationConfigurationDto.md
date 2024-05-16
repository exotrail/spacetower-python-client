# UkfOrbitDeterminationConfigurationDto


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
from fds_api_gen_client.models.ukf_orbit_determination_configuration_dto import UkfOrbitDeterminationConfigurationDto

# TODO update the JSON string below
json = "{}"
# create an instance of UkfOrbitDeterminationConfigurationDto from a JSON string
ukf_orbit_determination_configuration_dto_instance = UkfOrbitDeterminationConfigurationDto.from_json(json)
# print the JSON string representation of the object
print(UkfOrbitDeterminationConfigurationDto.to_json())

# convert the object into a dict
ukf_orbit_determination_configuration_dto_dict = ukf_orbit_determination_configuration_dto_instance.to_dict()
# create an instance of UkfOrbitDeterminationConfigurationDto from a dict
ukf_orbit_determination_configuration_dto_from_dict = UkfOrbitDeterminationConfigurationDto.from_dict(ukf_orbit_determination_configuration_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


