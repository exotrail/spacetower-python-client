# spacetower_python_client.ThrusterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_chemical_thruster**](ThrusterApi.md#create_chemical_thruster) | **POST** /thruster/chemical | 
[**create_electrical_thruster**](ThrusterApi.md#create_electrical_thruster) | **POST** /thruster/electrical | 
[**delete_thruster**](ThrusterApi.md#delete_thruster) | **DELETE** /thruster/{id} | 
[**retrieve_all_thrusters**](ThrusterApi.md#retrieve_all_thrusters) | **GET** /thrusters | 
[**retrieve_thruster**](ThrusterApi.md#retrieve_thruster) | **GET** /thruster/{id} | 


# **create_chemical_thruster**
> object create_chemical_thruster(chemical_thruster_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.chemical_thruster_dto import ChemicalThrusterDto
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
    api_instance = spacetower_python_client.ThrusterApi(api_client)
    chemical_thruster_dto = spacetower_python_client.ChemicalThrusterDto() # ChemicalThrusterDto | 

    try:
        api_response = api_instance.create_chemical_thruster(chemical_thruster_dto)
        print("The response of ThrusterApi->create_chemical_thruster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThrusterApi->create_chemical_thruster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **chemical_thruster_dto** | [**ChemicalThrusterDto**](ChemicalThrusterDto.md)|  | 

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

# **create_electrical_thruster**
> object create_electrical_thruster(electrical_thruster_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.electrical_thruster_dto import ElectricalThrusterDto
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
    api_instance = spacetower_python_client.ThrusterApi(api_client)
    electrical_thruster_dto = spacetower_python_client.ElectricalThrusterDto() # ElectricalThrusterDto | 

    try:
        api_response = api_instance.create_electrical_thruster(electrical_thruster_dto)
        print("The response of ThrusterApi->create_electrical_thruster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThrusterApi->create_electrical_thruster: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **electrical_thruster_dto** | [**ElectricalThrusterDto**](ElectricalThrusterDto.md)|  | 

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

# **delete_thruster**
> delete_thruster(id)



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
    api_instance = spacetower_python_client.ThrusterApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_thruster(id)
    except Exception as e:
        print("Exception when calling ThrusterApi->delete_thruster: %s\n" % e)
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

# **retrieve_all_thrusters**
> List[object] retrieve_all_thrusters()



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
    api_instance = spacetower_python_client.ThrusterApi(api_client)

    try:
        api_response = api_instance.retrieve_all_thrusters()
        print("The response of ThrusterApi->retrieve_all_thrusters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThrusterApi->retrieve_all_thrusters: %s\n" % e)
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

# **retrieve_thruster**
> object retrieve_thruster(id)



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
    api_instance = spacetower_python_client.ThrusterApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_thruster(id)
        print("The response of ThrusterApi->retrieve_thruster:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThrusterApi->retrieve_thruster: %s\n" % e)
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

