# KeplerianOrbitDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomaly** | **float** | Units: [deg] | 
**argument_of_perigee** | **float** | Units: [deg] | 
**var_date** | **str** | UTC date | 
**eccentricity** | **float** | Units: [-] | 
**frame** | **str** |  | 
**id** | **str** |  | [optional] 
**inclination** | **float** | Units: [deg] | 
**mean_osc_type** | **str** |  | 
**position_angle_type** | **str** |  | 
**raan** | **float** | Units: [deg] | 
**semi_major_axis** | **float** | Units: [km] | 

## Example

```python
from fds_api_gen_client.models.keplerian_orbit_dto import KeplerianOrbitDto

# TODO update the JSON string below
json = "{}"
# create an instance of KeplerianOrbitDto from a JSON string
keplerian_orbit_dto_instance = KeplerianOrbitDto.from_json(json)
# print the JSON string representation of the object
print(KeplerianOrbitDto.to_json())

# convert the object into a dict
keplerian_orbit_dto_dict = keplerian_orbit_dto_instance.to_dict()
# create an instance of KeplerianOrbitDto from a dict
keplerian_orbit_dto_from_dict = KeplerianOrbitDto.from_dict(keplerian_orbit_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


