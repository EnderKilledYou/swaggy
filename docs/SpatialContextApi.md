# swagger_client.SpatialContextApi

All URIs are relative to *https://levees.sec.usace.army.mil:443/api-local/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_contexts_param**](SpatialContextApi.md#get_all_contexts_param) | **GET** /spatial-context | 


# **get_all_contexts_param**
> list[object] get_all_contexts_param(system_id=system_id, segment_id=segment_id, type=type)



Gets all Contexts for a system/segments

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SpatialContextApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
type = 'ALL' # str | type of context (optional) (default to ALL)

try:
    api_response = api_instance.get_all_contexts_param(system_id=system_id, segment_id=segment_id, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SpatialContextApi->get_all_contexts_param: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **type** | **str**| type of context | [optional] [default to ALL]

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

