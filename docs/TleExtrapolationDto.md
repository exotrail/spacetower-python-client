# TleExtrapolationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dates** | **List[str]** |  | 
**initial_tle** | [**TLE**](TLE.md) |  | 

## Example

```python
from fds_api_gen_client.models.tle_extrapolation_dto import TleExtrapolationDto

# TODO update the JSON string below
json = "{}"
# create an instance of TleExtrapolationDto from a JSON string
tle_extrapolation_dto_instance = TleExtrapolationDto.from_json(json)
# print the JSON string representation of the object
print(TleExtrapolationDto.to_json())

# convert the object into a dict
tle_extrapolation_dto_dict = tle_extrapolation_dto_instance.to_dict()
# create an instance of TleExtrapolationDto from a dict
tle_extrapolation_dto_from_dict = TleExtrapolationDto.from_dict(tle_extrapolation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


