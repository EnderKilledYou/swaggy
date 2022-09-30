# swagger_client.DashboardApi

All URIs are relative to *https://levees.sec.usace.army.mil:443/api-local/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_dashboards**](DashboardApi.md#get_all_dashboards) | **GET** /dashboards | 
[**get_all_hierarchies**](DashboardApi.md#get_all_hierarchies) | **GET** /context-hierarchy | 
[**get_all_widgets**](DashboardApi.md#get_all_widgets) | **GET** /widgets | 
[**metrics_accreditation_status_get**](DashboardApi.md#metrics_accreditation_status_get) | **GET** /metrics/accreditation-status | 
[**metrics_authorization_status_get**](DashboardApi.md#metrics_authorization_status_get) | **GET** /metrics/authorization-status | 
[**metrics_construction_history_get**](DashboardApi.md#metrics_construction_history_get) | **GET** /metrics/construction-history | 
[**metrics_inspection_history_get**](DashboardApi.md#metrics_inspection_history_get) | **GET** /metrics/inspection-history | 
[**metrics_inspection_rating_get**](DashboardApi.md#metrics_inspection_rating_get) | **GET** /metrics/inspection-rating | 
[**metrics_lsac_history_get**](DashboardApi.md#metrics_lsac_history_get) | **GET** /metrics/lsac-history | 
[**metrics_lsac_rating_get**](DashboardApi.md#metrics_lsac_rating_get) | **GET** /metrics/lsac-rating | 
[**metrics_risk_characteristics_get**](DashboardApi.md#metrics_risk_characteristics_get) | **GET** /metrics/risk-characteristics | 


# **get_all_dashboards**
> list[Dashboard1] get_all_dashboards()



Gets user and organization shared dashboards

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardApi()

try:
    api_response = api_instance.get_all_dashboards()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->get_all_dashboards: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Dashboard1]**](Dashboard1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_hierarchies**
> ContextHierarchy1 get_all_hierarchies()



Returns context hierarchy for the dashboards

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardApi()

try:
    api_response = api_instance.get_all_hierarchies()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->get_all_hierarchies: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ContextHierarchy1**](ContextHierarchy1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_widgets**
> list[object] get_all_widgets(dashboard_id=dashboard_id)



Gets all widgets

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardApi()
dashboard_id = 56 # int | dashboard_id (optional)

try:
    api_response = api_instance.get_all_widgets(dashboard_id=dashboard_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->get_all_widgets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dashboard_id** | **int**| dashboard_id | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_accreditation_status_get**
> list[AdvancedField1] metrics_accreditation_status_get(_in=_in, is_usace=is_usace)



Gets the accreditation status metrics for a given context

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardApi()
_in = '_in_example' # str | @state:illinois|missouri (optional)
is_usace = false # bool | Limit dashboard to only USACE systems (optional) (default to false)

try:
    api_response = api_instance.metrics_accreditation_status_get(_in=_in, is_usace=is_usace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->metrics_accreditation_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_in** | **str**| @state:illinois|missouri | [optional] 
 **is_usace** | **bool**| Limit dashboard to only USACE systems | [optional] [default to false]

### Return type

[**list[AdvancedField1]**](AdvancedField1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_authorization_status_get**
> list[AdvancedField1] metrics_authorization_status_get(_in=_in, is_usace=is_usace)



Gets the authorization status metrics for a given context

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardApi()
_in = '_in_example' # str | @state:illinois|missouri (optional)
is_usace = false # bool | Limit dashboard to only USACE systems (optional) (default to false)

try:
    api_response = api_instance.metrics_authorization_status_get(_in=_in, is_usace=is_usace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->metrics_authorization_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_in** | **str**| @state:illinois|missouri | [optional] 
 **is_usace** | **bool**| Limit dashboard to only USACE systems | [optional] [default to false]

### Return type

[**list[AdvancedField1]**](AdvancedField1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_construction_history_get**
> list[AdvancedField1] metrics_construction_history_get(_in=_in, is_usace=is_usace)



Gets the construction history metrics for a given context

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardApi()
_in = '_in_example' # str | @state:illinois|missouri (optional)
is_usace = false # bool | Limit dashboard to only USACE systems (optional) (default to false)

try:
    api_response = api_instance.metrics_construction_history_get(_in=_in, is_usace=is_usace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->metrics_construction_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_in** | **str**| @state:illinois|missouri | [optional] 
 **is_usace** | **bool**| Limit dashboard to only USACE systems | [optional] [default to false]

### Return type

[**list[AdvancedField1]**](AdvancedField1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_inspection_history_get**
> list[AdvancedField1] metrics_inspection_history_get(_in=_in, _as=_as, is_usace=is_usace)



Gets the inspection history metrics for a given context

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardApi()
_in = '_in_example' # str | @state:illinois|missouri (optional)
_as = 'Routine' # str | return items as.  e.g. ?as=Routine (optional) (default to Routine)
is_usace = false # bool | Limit dashboard to only USACE systems (optional) (default to false)

try:
    api_response = api_instance.metrics_inspection_history_get(_in=_in, _as=_as, is_usace=is_usace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->metrics_inspection_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_in** | **str**| @state:illinois|missouri | [optional] 
 **_as** | **str**| return items as.  e.g. ?as&#x3D;Routine | [optional] [default to Routine]
 **is_usace** | **bool**| Limit dashboard to only USACE systems | [optional] [default to false]

### Return type

[**list[AdvancedField1]**](AdvancedField1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_inspection_rating_get**
> list[AdvancedField1] metrics_inspection_rating_get(_in=_in, _as=_as, is_usace=is_usace)



Gets the inspection rating metrics for a given context

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardApi()
_in = '_in_example' # str | @state:illinois|missouri (optional)
_as = 'Routine' # str | return items as.  e.g. ?as=Routine (optional) (default to Routine)
is_usace = false # bool | Limit dashboard to only USACE systems (optional) (default to false)

try:
    api_response = api_instance.metrics_inspection_rating_get(_in=_in, _as=_as, is_usace=is_usace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->metrics_inspection_rating_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_in** | **str**| @state:illinois|missouri | [optional] 
 **_as** | **str**| return items as.  e.g. ?as&#x3D;Routine | [optional] [default to Routine]
 **is_usace** | **bool**| Limit dashboard to only USACE systems | [optional] [default to false]

### Return type

[**list[AdvancedField1]**](AdvancedField1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_lsac_history_get**
> list[AdvancedField1] metrics_lsac_history_get(_in=_in, is_usace=is_usace)



Gets the LSAC history metrics for a given context

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardApi()
_in = '_in_example' # str | @state:illinois|missouri (optional)
is_usace = false # bool | Limit dashboard to only USACE systems (optional) (default to false)

try:
    api_response = api_instance.metrics_lsac_history_get(_in=_in, is_usace=is_usace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->metrics_lsac_history_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_in** | **str**| @state:illinois|missouri | [optional] 
 **is_usace** | **bool**| Limit dashboard to only USACE systems | [optional] [default to false]

### Return type

[**list[AdvancedField1]**](AdvancedField1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_lsac_rating_get**
> list[AdvancedField1] metrics_lsac_rating_get(_in=_in, is_usace=is_usace, is_system=is_system)



Gets the LSAC Rating count metrics for a given context

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardApi()
_in = '_in_example' # str | @state:illinois|missouri (optional)
is_usace = false # bool | Limit dashboard to only USACE systems (optional) (default to false)
is_system = true # bool | Limit dashboard to only systems (optional) (default to true)

try:
    api_response = api_instance.metrics_lsac_rating_get(_in=_in, is_usace=is_usace, is_system=is_system)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->metrics_lsac_rating_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_in** | **str**| @state:illinois|missouri | [optional] 
 **is_usace** | **bool**| Limit dashboard to only USACE systems | [optional] [default to false]
 **is_system** | **bool**| Limit dashboard to only systems | [optional] [default to true]

### Return type

[**list[AdvancedField1]**](AdvancedField1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **metrics_risk_characteristics_get**
> list[AdvancedField1] metrics_risk_characteristics_get(_in=_in, is_usace=is_usace)



Gets the risk characteristics metrics for a given context

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DashboardApi()
_in = '_in_example' # str | @state:illinois|missouri (optional)
is_usace = false # bool | Limit dashboard to only USACE systems (optional) (default to false)

try:
    api_response = api_instance.metrics_risk_characteristics_get(_in=_in, is_usace=is_usace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DashboardApi->metrics_risk_characteristics_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_in** | **str**| @state:illinois|missouri | [optional] 
 **is_usace** | **bool**| Limit dashboard to only USACE systems | [optional] [default to false]

### Return type

[**list[AdvancedField1]**](AdvancedField1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

