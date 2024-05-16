# FullCovarianceMatrixDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | UTC date | [optional] 
**frame** | **str** | Reference frame | 
**id** | **str** |  | [optional] 
**matrix** | **List[List[float]]** |  | 
**orbit_type** | **str** |  | 

## Example

```python
from spacetower_python_client.models.full_covariance_matrix_dto import FullCovarianceMatrixDto

# TODO update the JSON string below
json = "{}"
# create an instance of FullCovarianceMatrixDto from a JSON string
full_covariance_matrix_dto_instance = FullCovarianceMatrixDto.from_json(json)
# print the JSON string representation of the object
print(FullCovarianceMatrixDto.to_json())

# convert the object into a dict
full_covariance_matrix_dto_dict = full_covariance_matrix_dto_instance.to_dict()
# create an instance of FullCovarianceMatrixDto from a dict
full_covariance_matrix_dto_from_dict = FullCovarianceMatrixDto.from_dict(full_covariance_matrix_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


