# swagger_client.RiskApi

All URIs are relative to *https://levees.sec.usace.army.mil:443/api-local/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**consequences_post**](RiskApi.md#consequences_post) | **POST** /consequences | 
[**get_all_risk_driver_mitigations**](RiskApi.md#get_all_risk_driver_mitigations) | **GET** /risk-driver-mitigations | 
[**get_all_risk_drivers**](RiskApi.md#get_all_risk_drivers) | **GET** /risk-drivers | 
[**get_all_risk_process_links**](RiskApi.md#get_all_risk_process_links) | **GET** /risk-processes-link | 
[**get_all_system_screenings**](RiskApi.md#get_all_system_screenings) | **GET** /system/{id}/screenings | 
[**high_level_risk_assessment_id_get**](RiskApi.md#high_level_risk_assessment_id_get) | **GET** /high-level-risk-assessment/{id} | 


# **consequences_post**
> object consequences_post(body)



Creates consequence job results

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RiskApi()
body = swagger_client.Consequence1() # Consequence1 | consequence job

try:
    api_response = api_instance.consequences_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->consequences_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Consequence1**](Consequence1.md)| consequence job | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_risk_driver_mitigations**
> list[RiskDriverMitigation1] get_all_risk_driver_mitigations(system_id=system_id, segment_id=segment_id, id=id)



Gets all risk driver mitigations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RiskApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
id = 56 # int | riskDriverMitigationId (optional)

try:
    api_response = api_instance.get_all_risk_driver_mitigations(system_id=system_id, segment_id=segment_id, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->get_all_risk_driver_mitigations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **id** | **int**| riskDriverMitigationId | [optional] 

### Return type

[**list[RiskDriverMitigation1]**](RiskDriverMitigation1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_risk_drivers**
> list[RiskDriver1] get_all_risk_drivers(system_id=system_id, segment_id=segment_id, id=id)



Gets all risk drivers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RiskApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
id = 56 # int | riskDriverId (optional)

try:
    api_response = api_instance.get_all_risk_drivers(system_id=system_id, segment_id=segment_id, id=id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->get_all_risk_drivers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **id** | **int**| riskDriverId | [optional] 

### Return type

[**list[RiskDriver1]**](RiskDriver1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_risk_process_links**
> list[object] get_all_risk_process_links(system_id=system_id)



Gets all risk process links mitigations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RiskApi()
system_id = 56 # int | systemId (optional)

try:
    api_response = api_instance.get_all_risk_process_links(system_id=system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->get_all_risk_process_links: %s\n" % e)
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

# **get_all_system_screenings**
> list[object] get_all_system_screenings(id)



Returns the screenings levee system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RiskApi()
id = 56 # int | ID of levee system

try:
    api_response = api_instance.get_all_system_screenings(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->get_all_system_screenings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of levee system | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **high_level_risk_assessment_id_get**
> HighLevelRiskAssessment1 high_level_risk_assessment_id_get(id)



Gets a high level risk assessment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.RiskApi()
id = 56 # int | ID of high level risk assessment

try:
    api_response = api_instance.high_level_risk_assessment_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RiskApi->high_level_risk_assessment_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of high level risk assessment | 

### Return type

[**HighLevelRiskAssessment1**](HighLevelRiskAssessment1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

