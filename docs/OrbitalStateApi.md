# spacetower_python_client.OrbitalStateApi

All URIs are relative to *http://172.16.3.63*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_orbital_state**](OrbitalStateApi.md#create_orbital_state) | **POST** /orbital-state | 
[**delete_orbital_state**](OrbitalStateApi.md#delete_orbital_state) | **DELETE** /orbital-state/{id} | 
[**retrieve_all3**](OrbitalStateApi.md#retrieve_all3) | **GET** /orbital-states | 
[**retrieve_orbital_state_by_id**](OrbitalStateApi.md#retrieve_orbital_state_by_id) | **GET** /orbital-state/{id} | 


# **create_orbital_state**
> OrbitalStateDto create_orbital_state(orbital_state_creation_request_dto)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.orbital_state_creation_request_dto import OrbitalStateCreationRequestDto
from spacetower_python_client.models.orbital_state_dto import OrbitalStateDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://172.16.3.63
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://172.16.3.63"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-key
configuration = spacetower_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.OrbitalStateApi(api_client)
    orbital_state_creation_request_dto = spacetower_python_client.OrbitalStateCreationRequestDto() # OrbitalStateCreationRequestDto | 

    try:
        api_response = api_instance.create_orbital_state(orbital_state_creation_request_dto)
        print("The response of OrbitalStateApi->create_orbital_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitalStateApi->create_orbital_state: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **orbital_state_creation_request_dto** | [**OrbitalStateCreationRequestDto**](OrbitalStateCreationRequestDto.md)|  | 

### Return type

[**OrbitalStateDto**](OrbitalStateDto.md)

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

# **delete_orbital_state**
> delete_orbital_state(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://172.16.3.63
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://172.16.3.63"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-key
configuration = spacetower_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.OrbitalStateApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_orbital_state(id)
    except Exception as e:
        print("Exception when calling OrbitalStateApi->delete_orbital_state: %s\n" % e)
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

# **retrieve_all3**
> List[OrbitalStateDto] retrieve_all3()



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.orbital_state_dto import OrbitalStateDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://172.16.3.63
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://172.16.3.63"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-key
configuration = spacetower_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.OrbitalStateApi(api_client)

    try:
        api_response = api_instance.retrieve_all3()
        print("The response of OrbitalStateApi->retrieve_all3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitalStateApi->retrieve_all3: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[OrbitalStateDto]**](OrbitalStateDto.md)

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

# **retrieve_orbital_state_by_id**
> OrbitalStateDto retrieve_orbital_state_by_id(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.orbital_state_dto import OrbitalStateDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://172.16.3.63
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://172.16.3.63"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearer-key
configuration = spacetower_python_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.OrbitalStateApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_orbital_state_by_id(id)
        print("The response of OrbitalStateApi->retrieve_orbital_state_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitalStateApi->retrieve_orbital_state_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**OrbitalStateDto**](OrbitalStateDto.md)

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

