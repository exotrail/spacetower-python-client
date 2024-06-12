# spacetower_python_client.PropagationContextApi

All URIs are relative to *http://172.16.3.63*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_propagation_context**](PropagationContextApi.md#create_propagation_context) | **POST** /propagation-context | 
[**delete_propagation_context**](PropagationContextApi.md#delete_propagation_context) | **DELETE** /propagation-context/{id} | 
[**retrieve_all_contexts**](PropagationContextApi.md#retrieve_all_contexts) | **GET** /propagation-contexts | 
[**retrieve_context**](PropagationContextApi.md#retrieve_context) | **GET** /propagation-context/{id} | 


# **create_propagation_context**
> PropagationContextDto create_propagation_context(propagation_context_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.propagation_context_dto import PropagationContextDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://172.16.3.63
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://172.16.3.63"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.PropagationContextApi(api_client)
    propagation_context_dto = spacetower_python_client.PropagationContextDto() # PropagationContextDto | 

    try:
        api_response = api_instance.create_propagation_context(propagation_context_dto)
        print("The response of PropagationContextApi->create_propagation_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropagationContextApi->create_propagation_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **propagation_context_dto** | [**PropagationContextDto**](PropagationContextDto.md)|  | 

### Return type

[**PropagationContextDto**](PropagationContextDto.md)

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

# **delete_propagation_context**
> delete_propagation_context(id)



### Example


```python
import spacetower_python_client
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://172.16.3.63
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://172.16.3.63"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.PropagationContextApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_propagation_context(id)
    except Exception as e:
        print("Exception when calling PropagationContextApi->delete_propagation_context: %s\n" % e)
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

# **retrieve_all_contexts**
> List[PropagationContextDto] retrieve_all_contexts()



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.propagation_context_dto import PropagationContextDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://172.16.3.63
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://172.16.3.63"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.PropagationContextApi(api_client)

    try:
        api_response = api_instance.retrieve_all_contexts()
        print("The response of PropagationContextApi->retrieve_all_contexts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropagationContextApi->retrieve_all_contexts: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[PropagationContextDto]**](PropagationContextDto.md)

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

# **retrieve_context**
> PropagationContextDto retrieve_context(id)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.propagation_context_dto import PropagationContextDto
from spacetower_python_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://172.16.3.63
# See configuration.py for a list of all supported configuration parameters.
configuration = spacetower_python_client.Configuration(
    host = "http://172.16.3.63"
)


# Enter a context with an instance of the API client
with spacetower_python_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = spacetower_python_client.PropagationContextApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_context(id)
        print("The response of PropagationContextApi->retrieve_context:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PropagationContextApi->retrieve_context: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**PropagationContextDto**](PropagationContextDto.md)

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

