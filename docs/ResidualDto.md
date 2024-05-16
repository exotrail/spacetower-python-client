# ResidualDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from spacetower_python_client.models.residual_dto import ResidualDto

# TODO update the JSON string below
json = "{}"
# create an instance of ResidualDto from a JSON string
residual_dto_instance = ResidualDto.from_json(json)
# print the JSON string representation of the object
print(ResidualDto.to_json())

# convert the object into a dict
residual_dto_dict = residual_dto_instance.to_dict()
# create an instance of ResidualDto from a dict
residual_dto_from_dict = ResidualDto.from_dict(residual_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


