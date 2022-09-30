# swagger_client.SystemLegacyApi

All URIs are relative to *https://levees.sec.usace.army.mil:443/api-local/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deprecated_api_system_id_features_leveed_areas_get**](SystemLegacyApi.md#deprecated_api_system_id_features_leveed_areas_get) | **GET** /deprecated/api/system/{id}/features/leveed-areas | 
[**get_all_high_level_risk_assessments_by_id**](SystemLegacyApi.md#get_all_high_level_risk_assessments_by_id) | **GET** /system/{id}/high-level-risk-assessments | 
[**system_advanced_fields_get**](SystemLegacyApi.md#system_advanced_fields_get) | **GET** /system/advancedFields | 
[**system_field_values_field_get**](SystemLegacyApi.md#system_field_values_field_get) | **GET** /system/fieldValues/{field} | 
[**system_id_detail_get**](SystemLegacyApi.md#system_id_detail_get) | **GET** /system/{id}/detail | 
[**system_id_embankment_sections_get**](SystemLegacyApi.md#system_id_embankment_sections_get) | **GET** /system/{id}/embankment-sections | 
[**system_id_fema_segments_get**](SystemLegacyApi.md#system_id_fema_segments_get) | **GET** /system/{id}/fema-segments | 
[**system_id_route_get**](SystemLegacyApi.md#system_id_route_get) | **GET** /system/{id}/route | 
[**system_suggestions_post**](SystemLegacyApi.md#system_suggestions_post) | **POST** /system/suggestions | 
[**system_systems_post**](SystemLegacyApi.md#system_systems_post) | **POST** /system/systems | 


# **deprecated_api_system_id_features_leveed_areas_get**
> object deprecated_api_system_id_features_leveed_areas_get(id)



Returns the leveed areas of a levee system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemLegacyApi()
id = 56 # int | ID of levee system

try:
    api_response = api_instance.deprecated_api_system_id_features_leveed_areas_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLegacyApi->deprecated_api_system_id_features_leveed_areas_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of levee system | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_high_level_risk_assessments_by_id**
> list[HighLevelRiskAssessment1] get_all_high_level_risk_assessments_by_id(id)



Returns the high level risk assessments of a levee system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemLegacyApi()
id = 56 # int | ID of levee system

try:
    api_response = api_instance.get_all_high_level_risk_assessments_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLegacyApi->get_all_high_level_risk_assessments_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of levee system | 

### Return type

[**list[HighLevelRiskAssessment1]**](HighLevelRiskAssessment1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_advanced_fields_get**
> object system_advanced_fields_get()



Returns information about levee fields available for advanced searches

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemLegacyApi()

try:
    api_response = api_instance.system_advanced_fields_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLegacyApi->system_advanced_fields_get: %s\n" % e)
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

# **system_field_values_field_get**
> object system_field_values_field_get(field)



Returns possible values for lookup fields

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemLegacyApi()
field = 'field_example' # str | field name

try:
    api_response = api_instance.system_field_values_field_get(field)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLegacyApi->system_field_values_field_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **field** | **str**| field name | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_id_detail_get**
> object system_id_detail_get(id)



Returns the details of a levee system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemLegacyApi()
id = 56 # int | ID of levee system

try:
    api_response = api_instance.system_id_detail_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLegacyApi->system_id_detail_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of levee system | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_id_embankment_sections_get**
> object system_id_embankment_sections_get(id)



Returns the embankment-section data of levee segment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemLegacyApi()
id = 56 # int | ID of levee system

try:
    api_response = api_instance.system_id_embankment_sections_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLegacyApi->system_id_embankment_sections_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of levee system | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_id_fema_segments_get**
> object system_id_fema_segments_get(id)



Returns the segments of a levee system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemLegacyApi()
id = 56 # int | ID of levee system

try:
    api_response = api_instance.system_id_fema_segments_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLegacyApi->system_id_fema_segments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of levee system | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_id_route_get**
> object system_id_route_get(id)



Returns the route line of a levee system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemLegacyApi()
id = 56 # int | ID of levee system

try:
    api_response = api_instance.system_id_route_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLegacyApi->system_id_route_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of levee system | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_suggestions_post**
> object system_suggestions_post(body)



Provides sugesstions for contexts and system/segment names

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemLegacyApi()
body = swagger_client.SearchRequest2() # SearchRequest2 | search request

try:
    api_response = api_instance.system_suggestions_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLegacyApi->system_suggestions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchRequest2**](SearchRequest2.md)| search request | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **system_systems_post**
> FloodControlSystem1 system_systems_post(body)



Gets details for specific levee systems

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemLegacyApi()
body = swagger_client.IdsRequest1() # IdsRequest1 | ID of levee system(s)

try:
    api_response = api_instance.system_systems_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemLegacyApi->system_systems_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdsRequest1**](IdsRequest1.md)| ID of levee system(s) | 

### Return type

[**FloodControlSystem1**](FloodControlSystem1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

