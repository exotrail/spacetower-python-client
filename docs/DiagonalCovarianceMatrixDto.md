# DiagonalCovarianceMatrixDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** | UTC date | [optional] 
**diagonal** | **List[float]** |  | 
**frame** | **str** | Reference frame | 
**id** | **str** |  | [optional] 
**orbit_type** | **str** |  | 

## Example

```python
from spacetower_python_client.models.diagonal_covariance_matrix_dto import DiagonalCovarianceMatrixDto

# TODO update the JSON string below
json = "{}"
# create an instance of DiagonalCovarianceMatrixDto from a JSON string
diagonal_covariance_matrix_dto_instance = DiagonalCovarianceMatrixDto.from_json(json)
# print the JSON string representation of the object
print(DiagonalCovarianceMatrixDto.to_json())

# convert the object into a dict
diagonal_covariance_matrix_dto_dict = diagonal_covariance_matrix_dto_instance.to_dict()
# create an instance of DiagonalCovarianceMatrixDto from a dict
diagonal_covariance_matrix_dto_from_dict = DiagonalCovarianceMatrixDto.from_dict(diagonal_covariance_matrix_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


