# DateIntervalDto

Date intervals where the maneuver is not allowed to be executed

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **str** |  | [optional] 
**start** | **str** |  | [optional] 

## Example

```python
from spacetower_python_client.models.date_interval_dto import DateIntervalDto

# TODO update the JSON string below
json = "{}"
# create an instance of DateIntervalDto from a JSON string
date_interval_dto_instance = DateIntervalDto.from_json(json)
# print the JSON string representation of the object
print(DateIntervalDto.to_json())

# convert the object into a dict
date_interval_dto_dict = date_interval_dto_instance.to_dict()
# create an instance of DateIntervalDto from a dict
date_interval_dto_from_dict = DateIntervalDto.from_dict(date_interval_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


