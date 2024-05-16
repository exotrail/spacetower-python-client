# OutlierManagerSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outlier_manager_scale** | **float** | Number of standard deviations for outlier detection | 
**outliers_manager_warmup** | **int** | Number of warmup iterations or number of measurement without outlier rejection | 

## Example

```python
from spacetower_python_client.models.outlier_manager_settings_dto import OutlierManagerSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of OutlierManagerSettingsDto from a JSON string
outlier_manager_settings_dto_instance = OutlierManagerSettingsDto.from_json(json)
# print the JSON string representation of the object
print(OutlierManagerSettingsDto.to_json())

# convert the object into a dict
outlier_manager_settings_dto_dict = outlier_manager_settings_dto_instance.to_dict()
# create an instance of OutlierManagerSettingsDto from a dict
outlier_manager_settings_dto_from_dict = OutlierManagerSettingsDto.from_dict(outlier_manager_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


