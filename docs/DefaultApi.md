# swagger_client.DefaultApi

All URIs are relative to *https://levees.sec.usace.army.mil:443/api-local/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_emergency_sponsors**](DefaultApi.md#get_all_emergency_sponsors) | **GET** /emergency-sponsors | 
[**get_all_hsip_data_layers**](DefaultApi.md#get_all_hsip_data_layers) | **GET** /hsip-data | 
[**get_all_sponsor_maintainers**](DefaultApi.md#get_all_sponsor_maintainers) | **GET** /sponsor-maintainers | 
[**get_all_steward_organizations**](DefaultApi.md#get_all_steward_organizations) | **GET** /steward-organizations | 
[**get_all_system_types**](DefaultApi.md#get_all_system_types) | **GET** /system-types | 
[**get_all_what_can_you_do**](DefaultApi.md#get_all_what_can_you_do) | **GET** /what-can-you-do | 
[**get_entity_mappings**](DefaultApi.md#get_entity_mappings) | **GET** /entity-mapping | 
[**hello**](DefaultApi.md#hello) | **GET** /test/hello | 
[**what_can_you_do_id_get**](DefaultApi.md#what_can_you_do_id_get) | **GET** /what-can-you-do/{id} | 


# **get_all_emergency_sponsors**
> list[object] get_all_emergency_sponsors(system_id=system_id, segment_id=segment_id, id=id)



Gets all emergency sponsors

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
id = 56 # int | emergencySponsorId (optional)

try:
    api_response = api_instance.get_all_emergency_sponsors(system_id=system_id, segment_id=segment_id, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_emergency_sponsors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **id** | **int**| emergencySponsorId | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_hsip_data_layers**
> list[object] get_all_hsip_data_layers(system_id)



Gets an array of HSIP Data Layers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
system_id = 56 # int | systemId

try:
    api_response = api_instance.get_all_hsip_data_layers(system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_hsip_data_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_sponsor_maintainers**
> list[object] get_all_sponsor_maintainers()



Gets all SponsorMaintainers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.get_all_sponsor_maintainers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_sponsor_maintainers: %s\n" % e)
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

# **get_all_steward_organizations**
> list[object] get_all_steward_organizations(portfolio=portfolio)



Gets all Steward Organizations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
portfolio = 8.14 # float | get organizations tied to a system (optional)

try:
    api_response = api_instance.get_all_steward_organizations(portfolio=portfolio)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_steward_organizations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio** | **float**| get organizations tied to a system | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_system_types**
> SystemType1 get_all_system_types()



Gets a grouping of system types

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.get_all_system_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_system_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SystemType1**](SystemType1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_what_can_you_do**
> list[object] get_all_what_can_you_do(system_id=system_id)



Gets WhatCanYouDo by systemId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
system_id = 56 # int | systemId (optional)

try:
    api_response = api_instance.get_all_what_can_you_do(system_id=system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_all_what_can_you_do: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entity_mappings**
> object get_entity_mappings()



Returns an entity mapping with properties

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.get_entity_mappings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_entity_mappings: %s\n" % e)
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

# **hello**
> object hello(name=name)



Returns Hello to the caller

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
name = 'name_example' # str | The name of the person to whom to say hello (optional)

try:
    api_response = api_instance.hello(name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->hello: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the person to whom to say hello | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **what_can_you_do_id_get**
> object what_can_you_do_id_get(id)



Gets a WhatCanYouDo

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 56 # int | ID of WhatCanYouDo

try:
    api_response = api_instance.what_can_you_do_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->what_can_you_do_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of WhatCanYouDo | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

