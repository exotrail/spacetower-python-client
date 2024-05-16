# spacetower_python_client.SpacecraftApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_box_spacecraft**](SpacecraftApi.md#create_box_spacecraft) | **POST** /spacecraft/box | 
[**create_spherical_spacecraft**](SpacecraftApi.md#create_spherical_spacecraft) | **POST** /spacecraft/spherical | 
[**delete_spacecraft**](SpacecraftApi.md#delete_spacecraft) | **DELETE** /spacecraft/{id} | 
[**retrieve_all**](SpacecraftApi.md#retrieve_all) | **GET** /spacecrafts | 
[**retrieve_spacecraft**](SpacecraftApi.md#retrieve_spacecraft) | **GET** /spacecraft/{id} | 


# **create_box_spacecraft**
> object create_box_spacecraft(box_spacecraft_input_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.box_spacecraft_input_dto import BoxSpacecraftInputDto
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
    api_instance = spacetower_python_client.SpacecraftApi(api_client)
    box_spacecraft_input_dto = spacetower_python_client.BoxSpacecraftInputDto() # BoxSpacecraftInputDto | 

    try:
        api_response = api_instance.create_box_spacecraft(box_spacecraft_input_dto)
        print("The response of SpacecraftApi->create_box_spacecraft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpacecraftApi->create_box_spacecraft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **box_spacecraft_input_dto** | [**BoxSpacecraftInputDto**](BoxSpacecraftInputDto.md)|  | 

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

# **create_spherical_spacecraft**
> object create_spherical_spacecraft(spherical_spacecraft_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.spherical_spacecraft_dto import SphericalSpacecraftDto
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
    api_instance = spacetower_python_client.SpacecraftApi(api_client)
    spherical_spacecraft_dto = spacetower_python_client.SphericalSpacecraftDto() # SphericalSpacecraftDto | 

    try:
        api_response = api_instance.create_spherical_spacecraft(spherical_spacecraft_dto)
        print("The response of SpacecraftApi->create_spherical_spacecraft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpacecraftApi->create_spherical_spacecraft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **spherical_spacecraft_dto** | [**SphericalSpacecraftDto**](SphericalSpacecraftDto.md)|  | 

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

# **delete_spacecraft**
> delete_spacecraft(id)



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
    api_instance = spacetower_python_client.SpacecraftApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_spacecraft(id)
    except Exception as e:
        print("Exception when calling SpacecraftApi->delete_spacecraft: %s\n" % e)
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

# **retrieve_all**
> List[object] retrieve_all()



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
    api_instance = spacetower_python_client.SpacecraftApi(api_client)

    try:
        api_response = api_instance.retrieve_all()
        print("The response of SpacecraftApi->retrieve_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpacecraftApi->retrieve_all: %s\n" % e)
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

# **retrieve_spacecraft**
> object retrieve_spacecraft(id)



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
    api_instance = spacetower_python_client.SpacecraftApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_spacecraft(id)
        print("The response of SpacecraftApi->retrieve_spacecraft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SpacecraftApi->retrieve_spacecraft: %s\n" % e)
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

