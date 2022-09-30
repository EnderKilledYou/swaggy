# swagger_client.HomeApi

All URIs are relative to *https://levees.sec.usace.army.mil:443/api-local/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**context_summaries_key_key_value_value_get**](HomeApi.md#context_summaries_key_key_value_value_get) | **GET** /context-summaries/key/{key}/value/{value} | 
[**metadata_get**](HomeApi.md#metadata_get) | **GET** /metadata | 
[**suggestions_post**](HomeApi.md#suggestions_post) | **POST** /suggestions | 


# **context_summaries_key_key_value_value_get**
> ContextSummary1 context_summaries_key_key_value_value_get(key, value, portfolio_id=portfolio_id)



Gets the counts for a given context name and context key

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomeApi()
key = 'key_example' # str | Context key that the count is being returned for
value = 'value_example' # str | Context value that the count is being returned for
portfolio_id = 8.14 # float | limiting portfolio id (optional)

try:
    api_response = api_instance.context_summaries_key_key_value_value_get(key, value, portfolio_id=portfolio_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomeApi->context_summaries_key_key_value_value_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| Context key that the count is being returned for | 
 **value** | **str**| Context value that the count is being returned for | 
 **portfolio_id** | **float**| limiting portfolio id | [optional] 

### Return type

[**ContextSummary1**](ContextSummary1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metadata_get**
> object metadata_get()



Returns metadata about the system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomeApi()

try:
    api_response = api_instance.metadata_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomeApi->metadata_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **suggestions_post**
> object suggestions_post(body)



Provides sugesstions for contexts and system/segment names

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.HomeApi()
body = swagger_client.SearchRequest1() # SearchRequest1 | search request

try:
    api_response = api_instance.suggestions_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HomeApi->suggestions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchRequest1**](SearchRequest1.md)| search request | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

