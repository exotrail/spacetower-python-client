# SmoothedKeplerianElementsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**argument_of_perigee** | **float** |  | [optional] 
**argument_of_perigee_standard_deviation** | **float** |  | [optional] 
**eccentricity** | **float** |  | [optional] 
**eccentricity_standard_deviation** | **float** |  | [optional] 
**id** | **str** |  | [optional] 
**inclination** | **float** |  | [optional] 
**inclination_standard_deviation** | **float** |  | [optional] 
**raan** | **float** |  | [optional] 
**raan_standard_deviation** | **float** |  | [optional] 
**semi_major_axis** | **float** |  | [optional] 
**semi_major_axis_standard_deviation** | **float** |  | [optional] 

## Example

```python
from fds_api_gen_client.models.smoothed_keplerian_elements_dto import SmoothedKeplerianElementsDto

# TODO update the JSON string below
json = "{}"
# create an instance of SmoothedKeplerianElementsDto from a JSON string
smoothed_keplerian_elements_dto_instance = SmoothedKeplerianElementsDto.from_json(json)
# print the JSON string representation of the object
print(SmoothedKeplerianElementsDto.to_json())

# convert the object into a dict
smoothed_keplerian_elements_dto_dict = smoothed_keplerian_elements_dto_instance.to_dict()
# create an instance of SmoothedKeplerianElementsDto from a dict
smoothed_keplerian_elements_dto_from_dict = SmoothedKeplerianElementsDto.from_dict(smoothed_keplerian_elements_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


