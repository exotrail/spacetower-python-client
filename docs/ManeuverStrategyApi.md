# spacetower_python_client.ManeuverStrategyApi

All URIs are relative to *http://172.16.3.63*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_maneuver_strategy**](ManeuverStrategyApi.md#create_maneuver_strategy) | **POST** /maneuver-strategy | 
[**delete_manoeuvre_strategy**](ManeuverStrategyApi.md#delete_manoeuvre_strategy) | **DELETE** /maneuver-strategy/{id} | 
[**retrieve_all7**](ManeuverStrategyApi.md#retrieve_all7) | **GET** /maneuver-strategies | 
[**retrieve_manoeuvre_strategy_by_id**](ManeuverStrategyApi.md#retrieve_manoeuvre_strategy_by_id) | **GET** /maneuver-strategy/{id} | 


# **create_maneuver_strategy**
> ManeuverStrategyDto create_maneuver_strategy(maneuver_strategy_dto)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.maneuver_strategy_dto import ManeuverStrategyDto
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
    api_instance = spacetower_python_client.ManeuverStrategyApi(api_client)
    maneuver_strategy_dto = spacetower_python_client.ManeuverStrategyDto() # ManeuverStrategyDto | 

    try:
        api_response = api_instance.create_maneuver_strategy(maneuver_strategy_dto)
        print("The response of ManeuverStrategyApi->create_maneuver_strategy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManeuverStrategyApi->create_maneuver_strategy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maneuver_strategy_dto** | [**ManeuverStrategyDto**](ManeuverStrategyDto.md)|  | 

### Return type

[**ManeuverStrategyDto**](ManeuverStrategyDto.md)

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

# **delete_manoeuvre_strategy**
> delete_manoeuvre_strategy(id)



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
    api_instance = spacetower_python_client.ManeuverStrategyApi(api_client)
    id = 'id_example' # str | 

    try:
        api_instance.delete_manoeuvre_strategy(id)
    except Exception as e:
        print("Exception when calling ManeuverStrategyApi->delete_manoeuvre_strategy: %s\n" % e)
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

# **retrieve_all7**
> List[ManeuverStrategyDto] retrieve_all7()



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.maneuver_strategy_dto import ManeuverStrategyDto
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
    api_instance = spacetower_python_client.ManeuverStrategyApi(api_client)

    try:
        api_response = api_instance.retrieve_all7()
        print("The response of ManeuverStrategyApi->retrieve_all7:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManeuverStrategyApi->retrieve_all7: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ManeuverStrategyDto]**](ManeuverStrategyDto.md)

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

# **retrieve_manoeuvre_strategy_by_id**
> ManeuverStrategyDto retrieve_manoeuvre_strategy_by_id(id)



### Example

* Bearer (JWT) Authentication (bearer-key):

```python
import spacetower_python_client
from spacetower_python_client.models.maneuver_strategy_dto import ManeuverStrategyDto
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
    api_instance = spacetower_python_client.ManeuverStrategyApi(api_client)
    id = 'id_example' # str | 

    try:
        api_response = api_instance.retrieve_manoeuvre_strategy_by_id(id)
        print("The response of ManeuverStrategyApi->retrieve_manoeuvre_strategy_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ManeuverStrategyApi->retrieve_manoeuvre_strategy_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ManeuverStrategyDto**](ManeuverStrategyDto.md)

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

