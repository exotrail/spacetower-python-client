# BatteryDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**depth_of_discharge** | **float** | x in (0,1), Units: [-] | 
**id** | **str** |  | [optional] 
**initial_charge** | **float** | x in (0,1], Units: [-] | 
**minimum_charge_for_firing** | **float** | x in (0,1), Units: [-] | 
**nominal_capacity** | **float** | Units: [Wh] | 

## Example

```python
from fds_api_gen_client.models.battery_dto import BatteryDto

# TODO update the JSON string below
json = "{}"
# create an instance of BatteryDto from a JSON string
battery_dto_instance = BatteryDto.from_json(json)
# print the JSON string representation of the object
print(BatteryDto.to_json())

# convert the object into a dict
battery_dto_dict = battery_dto_instance.to_dict()
# create an instance of BatteryDto from a dict
battery_dto_from_dict = BatteryDto.from_dict(battery_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


