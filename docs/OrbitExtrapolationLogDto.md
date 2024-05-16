# OrbitExtrapolationLogDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computation_date** | **datetime** |  | [optional] 
**computation_status** | **str** |  | [optional] 
**error_messages** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from spacetower_python_client.models.orbit_extrapolation_log_dto import OrbitExtrapolationLogDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrbitExtrapolationLogDto from a JSON string
orbit_extrapolation_log_dto_instance = OrbitExtrapolationLogDto.from_json(json)
# print the JSON string representation of the object
print(OrbitExtrapolationLogDto.to_json())

# convert the object into a dict
orbit_extrapolation_log_dto_dict = orbit_extrapolation_log_dto_instance.to_dict()
# create an instance of OrbitExtrapolationLogDto from a dict
orbit_extrapolation_log_dto_from_dict = OrbitExtrapolationLogDto.from_dict(orbit_extrapolation_log_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


