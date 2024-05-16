# fds_api_gen_client.TokenApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_token**](TokenApi.md#get_token) | **POST** /token | 


# **get_token**
> JwtMessage get_token(account_credentials)



### Example


```python
import fds_api_gen_client
from fds_api_gen_client.models.account_credentials import AccountCredentials
from fds_api_gen_client.models.jwt_message import JwtMessage
from fds_api_gen_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fds_api_gen_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with fds_api_gen_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fds_api_gen_client.TokenApi(api_client)
    account_credentials = fds_api_gen_client.AccountCredentials() # AccountCredentials | 

    try:
        api_response = api_instance.get_token(account_credentials)
        print("The response of TokenApi->get_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TokenApi->get_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_credentials** | [**AccountCredentials**](AccountCredentials.md)|  | 

### Return type

[**JwtMessage**](JwtMessage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

