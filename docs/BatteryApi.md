# spacetower_python_client.BatteryApi

All URIs are relative to *http://172.16.3.63*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_battery**](BatteryApi.md#create_battery) | **POST** /battery | 
[**delete_battery**](BatteryApi.md#delete_battery) | **DELETE** /battery/{id} | 
[**retrieve_all_batteries**](BatteryApi.md#retrieve_all_batteries) | **GET** /batteries | 
[**retrieve_battery**](BatteryApi.md#retrieve_battery) | **GET** /battery/{id} | 


# **create_battery**
> BatteryDto create_battery(battery_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.battery_dto import BatteryDto
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
    api_instance = spacetower_python_client.BatteryApi(api_client)
    battery_dto = spacetower_python_client.BatteryDto() # BatteryDto | 

    try:
        api_response = api_instance.create_battery(battery_dto)
        print("The response of BatteryApi->create_battery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatteryApi->create_battery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **battery_dto** | [**BatteryDto**](BatteryDto.md)|  | 

### Return type

[**BatteryDto**](BatteryDto.md)

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

# **delete_battery**
> delete_battery(id)



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
    api_instance = spacetower_python_client.BatteryApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_battery(id)
    except Exception as e:
        print("Exception when calling BatteryApi->delete_battery: %s\n" % e)
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

# **retrieve_all_batteries**
> List[BatteryDto] retrieve_all_batteries()



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.battery_dto import BatteryDto
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
    api_instance = spacetower_python_client.BatteryApi(api_client)

    try:
        api_response = api_instance.retrieve_all_batteries()
        print("The response of BatteryApi->retrieve_all_batteries:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatteryApi->retrieve_all_batteries: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[BatteryDto]**](BatteryDto.md)

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

# **retrieve_battery**
> BatteryDto retrieve_battery(id)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.battery_dto import BatteryDto
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
    api_instance = spacetower_python_client.BatteryApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_battery(id)
        print("The response of BatteryApi->retrieve_battery:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BatteryApi->retrieve_battery: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**BatteryDto**](BatteryDto.md)

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

