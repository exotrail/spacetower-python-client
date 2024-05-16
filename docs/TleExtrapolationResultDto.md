# TleExtrapolationResultDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**orbits** | **List[object]** |  | [optional] 
**tle_extrapolation** | [**TleExtrapolationDto**](TleExtrapolationDto.md) |  | [optional] 

## Example

```python
from fds_api_gen_client.models.tle_extrapolation_result_dto import TleExtrapolationResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of TleExtrapolationResultDto from a JSON string
tle_extrapolation_result_dto_instance = TleExtrapolationResultDto.from_json(json)
# print the JSON string representation of the object
print(TleExtrapolationResultDto.to_json())

# convert the object into a dict
tle_extrapolation_result_dto_dict = tle_extrapolation_result_dto_instance.to_dict()
# create an instance of TleExtrapolationResultDto from a dict
tle_extrapolation_result_dto_from_dict = TleExtrapolationResultDto.from_dict(tle_extrapolation_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


