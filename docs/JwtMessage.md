# JwtMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | 

## Example

```python
from fds_api_gen_client.models.jwt_message import JwtMessage

# TODO update the JSON string below
json = "{}"
# create an instance of JwtMessage from a JSON string
jwt_message_instance = JwtMessage.from_json(json)
# print the JSON string representation of the object
print(JwtMessage.to_json())

# convert the object into a dict
jwt_message_dict = jwt_message_instance.to_dict()
# create an instance of JwtMessage from a dict
jwt_message_from_dict = JwtMessage.from_dict(jwt_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


