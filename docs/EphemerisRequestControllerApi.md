# fds_api_gen_client.EphemerisRequestControllerApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ephemeris_request**](EphemerisRequestControllerApi.md#create_ephemeris_request) | **POST** /ephemeris-request | 
[**delete**](EphemerisRequestControllerApi.md#delete) | **DELETE** /ephemeris-request/{id} | 
[**retrieve1**](EphemerisRequestControllerApi.md#retrieve1) | **GET** /ephemeris-request/{id} | 
[**retrieve_all9**](EphemerisRequestControllerApi.md#retrieve_all9) | **GET** /ephemeris-requests | 


# **create_ephemeris_request**
> EphemerisRequestDto create_ephemeris_request(ephemeris_request_dto)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import fds_api_gen_client
from fds_api_gen_client.models.ephemeris_request_dto import EphemerisRequestDto
from fds_api_gen_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fds_api_gen_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-key
configuration = fds_api_gen_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fds_api_gen_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fds_api_gen_client.EphemerisRequestControllerApi(api_client)
    ephemeris_request_dto = fds_api_gen_client.EphemerisRequestDto() # EphemerisRequestDto | 

    try:
        api_response = api_instance.create_ephemeris_request(ephemeris_request_dto)
        print("The response of EphemerisRequestControllerApi->create_ephemeris_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EphemerisRequestControllerApi->create_ephemeris_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ephemeris_request_dto** | [**EphemerisRequestDto**](EphemerisRequestDto.md)|  | 

### Return type

[**EphemerisRequestDto**](EphemerisRequestDto.md)

### Authorization

[bearer-key](../README.md#bearer-key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> delete(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import fds_api_gen_client
from fds_api_gen_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fds_api_gen_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-key
configuration = fds_api_gen_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fds_api_gen_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fds_api_gen_client.EphemerisRequestControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete(id)
    except Exception as e:
        print("Exception when calling EphemerisRequestControllerApi->delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[bearer-key](../README.md#bearer-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve1**
> EphemerisRequestDto retrieve1(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import fds_api_gen_client
from fds_api_gen_client.models.ephemeris_request_dto import EphemerisRequestDto
from fds_api_gen_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fds_api_gen_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-key
configuration = fds_api_gen_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fds_api_gen_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fds_api_gen_client.EphemerisRequestControllerApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve1(id)
        print("The response of EphemerisRequestControllerApi->retrieve1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EphemerisRequestControllerApi->retrieve1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**EphemerisRequestDto**](EphemerisRequestDto.md)

### Authorization

[bearer-key](../README.md#bearer-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retrieve_all9**
> List[EphemerisRequestDto] retrieve_all9()



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import fds_api_gen_client
from fds_api_gen_client.models.ephemeris_request_dto import EphemerisRequestDto
from fds_api_gen_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = fds_api_gen_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-key
configuration = fds_api_gen_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with fds_api_gen_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = fds_api_gen_client.EphemerisRequestControllerApi(api_client)

    try:
        api_response = api_instance.retrieve_all9()
        print("The response of EphemerisRequestControllerApi->retrieve_all9:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EphemerisRequestControllerApi->retrieve_all9: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[EphemerisRequestDto]**](EphemerisRequestDto.md)

### Authorization

[bearer-key](../README.md#bearer-key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
