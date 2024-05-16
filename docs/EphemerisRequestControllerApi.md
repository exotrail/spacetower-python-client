# spacetower_python_client.EphemerisRequestControllerApi

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


```python
import spacetower_python_client
from spacetower_python_client.models.ephemeris_request_dto import EphemerisRequestDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.EphemerisRequestControllerApi(api_client)
    ephemeris_request_dto = spacetower_python_client.EphemerisRequestDto() # EphemerisRequestDto | 

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

No authorization required

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


```python
import spacetower_python_client
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.EphemerisRequestControllerApi(api_client)
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

No authorization required

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


```python
import spacetower_python_client
from spacetower_python_client.models.ephemeris_request_dto import EphemerisRequestDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.EphemerisRequestControllerApi(api_client)
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

No authorization required

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


```python
import spacetower_python_client
from spacetower_python_client.models.ephemeris_request_dto import EphemerisRequestDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.EphemerisRequestControllerApi(api_client)

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

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

