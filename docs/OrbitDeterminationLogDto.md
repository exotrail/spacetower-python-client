# OrbitDeterminationLogDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computation_date** | **datetime** |  | [optional] 
**computation_status** | **str** |  | [optional] 
**error_messages** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 

## Example

```python
from fds_api_gen_client.models.orbit_determination_log_dto import OrbitDeterminationLogDto

# TODO update the JSON string below
json = "{}"
# create an instance of OrbitDeterminationLogDto from a JSON string
orbit_determination_log_dto_instance = OrbitDeterminationLogDto.from_json(json)
# print the JSON string representation of the object
print(OrbitDeterminationLogDto.to_json())

# convert the object into a dict
orbit_determination_log_dto_dict = orbit_determination_log_dto_instance.to_dict()
# create an instance of OrbitDeterminationLogDto from a dict
orbit_determination_log_dto_from_dict = OrbitDeterminationLogDto.from_dict(orbit_determination_log_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


