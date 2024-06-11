# spacetower_python_client.OrbitDeterminationConfigurationApi

All URIs are relative to *http://172.16.3.63*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_ukf_orbit_determination_configuration**](OrbitDeterminationConfigurationApi.md#create_ukf_orbit_determination_configuration) | **POST** /od-configuration/ukf | 
[**delete_ukf_orbit_determination_configuration**](OrbitDeterminationConfigurationApi.md#delete_ukf_orbit_determination_configuration) | **DELETE** /od-configuration/{id} | 
[**retrieve_all_orbit_determination_configurations**](OrbitDeterminationConfigurationApi.md#retrieve_all_orbit_determination_configurations) | **GET** /od-configurations | 
[**retrieve_orbit_determination_configuration_by_id**](OrbitDeterminationConfigurationApi.md#retrieve_orbit_determination_configuration_by_id) | **GET** /od-configuration/{id} | 


# **create_ukf_orbit_determination_configuration**
> CreateUkfOrbitDeterminationConfiguration200Response create_ukf_orbit_determination_configuration(ukf_orbit_determination_configuration_dto)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.create_ukf_orbit_determination_configuration200_response import CreateUkfOrbitDeterminationConfiguration200Response
from spacetower_python_client.models.ukf_orbit_determination_configuration_dto import UkfOrbitDeterminationConfigurationDto
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
    api_instance = spacetower_python_client.OrbitDeterminationConfigurationApi(api_client)
    ukf_orbit_determination_configuration_dto = spacetower_python_client.UkfOrbitDeterminationConfigurationDto() # UkfOrbitDeterminationConfigurationDto | 

    try:
        api_response = api_instance.create_ukf_orbit_determination_configuration(ukf_orbit_determination_configuration_dto)
        print("The response of OrbitDeterminationConfigurationApi->create_ukf_orbit_determination_configuration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitDeterminationConfigurationApi->create_ukf_orbit_determination_configuration: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ukf_orbit_determination_configuration_dto** | [**UkfOrbitDeterminationConfigurationDto**](UkfOrbitDeterminationConfigurationDto.md)|  | 

### Return type

[**CreateUkfOrbitDeterminationConfiguration200Response**](CreateUkfOrbitDeterminationConfiguration200Response.md)

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

# **delete_ukf_orbit_determination_configuration**
> delete_ukf_orbit_determination_configuration(id)



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
    api_instance = spacetower_python_client.OrbitDeterminationConfigurationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_ukf_orbit_determination_configuration(id)
    except Exception as e:
        print("Exception when calling OrbitDeterminationConfigurationApi->delete_ukf_orbit_determination_configuration: %s\n" % e)
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

# **retrieve_all_orbit_determination_configurations**
> List[CreateUkfOrbitDeterminationConfiguration200Response] retrieve_all_orbit_determination_configurations()



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.create_ukf_orbit_determination_configuration200_response import CreateUkfOrbitDeterminationConfiguration200Response
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
    api_instance = spacetower_python_client.OrbitDeterminationConfigurationApi(api_client)

    try:
        api_response = api_instance.retrieve_all_orbit_determination_configurations()
        print("The response of OrbitDeterminationConfigurationApi->retrieve_all_orbit_determination_configurations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitDeterminationConfigurationApi->retrieve_all_orbit_determination_configurations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CreateUkfOrbitDeterminationConfiguration200Response]**](CreateUkfOrbitDeterminationConfiguration200Response.md)

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

# **retrieve_orbit_determination_configuration_by_id**
> CreateUkfOrbitDeterminationConfiguration200Response retrieve_orbit_determination_configuration_by_id(id)



### Example


```python
import spacetower_python_client
from spacetower_python_client.models.create_ukf_orbit_determination_configuration200_response import CreateUkfOrbitDeterminationConfiguration200Response
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
    api_instance = spacetower_python_client.OrbitDeterminationConfigurationApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_orbit_determination_configuration_by_id(id)
        print("The response of OrbitDeterminationConfigurationApi->retrieve_orbit_determination_configuration_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrbitDeterminationConfigurationApi->retrieve_orbit_determination_configuration_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CreateUkfOrbitDeterminationConfiguration200Response**](CreateUkfOrbitDeterminationConfiguration200Response.md)

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

