# swagger_client.FemaApi

All URIs are relative to *https://levees.sec.usace.army.mil:443/api-local/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_fema_sys_info**](FemaApi.md#get_all_fema_sys_info) | **GET** /fema-fast/sys-info/{id} | 


# **get_all_fema_sys_info**
> list[FemaSystemInfo1] get_all_fema_sys_info(id)



Gets a FemaSystemInfo

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FemaApi()
id = 56 # int | ID of FemaSystemInfo

try:
    api_response = api_instance.get_all_fema_sys_info(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FemaApi->get_all_fema_sys_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of FemaSystemInfo | 

### Return type

[**list[FemaSystemInfo1]**](FemaSystemInfo1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

