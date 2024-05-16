# FiringActionDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firing_attitude** | **str** |  | 
**firing_duration** | **float** | Units: [s] | 
**id** | **str** |  | [optional] 
**post_firing_attitude** | **str** |  | 
**start_firing** | **str** | UTC date | 
**warm_up_attitude** | **str** |  | [optional] 
**warm_up_duration** | **float** | Units: [s] | 

## Example

```python
from fds_api_gen_client.models.firing_action_dto import FiringActionDto

# TODO update the JSON string below
json = "{}"
# create an instance of FiringActionDto from a JSON string
firing_action_dto_instance = FiringActionDto.from_json(json)
# print the JSON string representation of the object
print(FiringActionDto.to_json())

# convert the object into a dict
firing_action_dto_dict = firing_action_dto_instance.to_dict()
# create an instance of FiringActionDto from a dict
firing_action_dto_from_dict = FiringActionDto.from_dict(firing_action_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


