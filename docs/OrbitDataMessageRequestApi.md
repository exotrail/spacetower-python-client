# spacetower_python_client.OrbitDataMessageRequestApi

All URIs are relative to *http://172.16.3.63*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_oem_request**](OrbitDataMessageRequestApi.md#create_oem_request) | **POST** /orbit-data-message/requests/oem | 
[**delete_orbit_data_message_request**](OrbitDataMessageRequestApi.md#delete_orbit_data_message_request) | **DELETE** /orbit-data-message/requests/{id} | 
[**retrieve_all4**](OrbitDataMessageRequestApi.md#retrieve_all4) | **GET** /orbit-data-message/requests | 
[**retrieve_orbit_data_message_request_by_id**](OrbitDataMessageRequestApi.md#retrieve_orbit_data_message_request_by_id) | **GET** /orbit-data-message/requests/{id} | 


# **create_oem_request**
> object create_oem_request(oem_request_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.oem_request_dto import OemRequestDto
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
    api_instance = spacetower_python_client.OrbitDataMessageRequestApi(api_client)
    oem_request_dto = spacetower_python_client.OemRequestDto() # OemRequestDto | 

    try:
        api_response = api_instance.create_oem_request(oem_request_dto)
        print("The response of OrbitDataMessageRequestApi->create_oem_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitDataMessageRequestApi->create_oem_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oem_request_dto** | [**OemRequestDto**](OemRequestDto.md)|  | 

### Return type

**object**

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

# **delete_orbit_data_message_request**
> delete_orbit_data_message_request(id)



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
    api_instance = spacetower_python_client.OrbitDataMessageRequestApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_orbit_data_message_request(id)
    except Exception as e:
        print("Exception when calling OrbitDataMessageRequestApi->delete_orbit_data_message_request: %s\n" % e)
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

# **retrieve_all4**
> List[object] retrieve_all4()



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
    api_instance = spacetower_python_client.OrbitDataMessageRequestApi(api_client)

    try:
        api_response = api_instance.retrieve_all4()
        print("The response of OrbitDataMessageRequestApi->retrieve_all4:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitDataMessageRequestApi->retrieve_all4: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[object]**

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

# **retrieve_orbit_data_message_request_by_id**
> object retrieve_orbit_data_message_request_by_id(id)



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
    api_instance = spacetower_python_client.OrbitDataMessageRequestApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_orbit_data_message_request_by_id(id)
        print("The response of OrbitDataMessageRequestApi->retrieve_orbit_data_message_request_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitDataMessageRequestApi->retrieve_orbit_data_message_request_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

**object**

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

