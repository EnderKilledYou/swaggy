# swagger_client.AgencyApi

All URIs are relative to *https://levees.sec.usace.army.mil:443/api-local/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agency_id_get**](AgencyApi.md#agency_id_get) | **GET** /agency/{id} | 
[**get_all_agencies**](AgencyApi.md#get_all_agencies) | **GET** /agency | 
[**get_all_agency_organizations**](AgencyApi.md#get_all_agency_organizations) | **GET** /agency-organization/{id} | 


# **agency_id_get**
> object agency_id_get(id)



Gets an agency

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AgencyApi()
id = 56 # int | ID of agency

try:
    api_response = api_instance.agency_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgencyApi->agency_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of agency | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_agencies**
> list[object] get_all_agencies()



Gets all agencies

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AgencyApi()

try:
    api_response = api_instance.get_all_agencies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgencyApi->get_all_agencies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_agency_organizations**
> list[object] get_all_agency_organizations(id)



Gets All organization ids belonging to an agency

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AgencyApi()
id = 56 # int | ID of the agency

try:
    api_response = api_instance.get_all_agency_organizations(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgencyApi->get_all_agency_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the agency | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

