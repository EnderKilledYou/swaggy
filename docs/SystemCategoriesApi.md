# swagger_client.SystemCategoriesApi

All URIs are relative to *https://levees.sec.usace.army.mil:443/api-local/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**system_categories_fed_nonfed_get**](SystemCategoriesApi.md#system_categories_fed_nonfed_get) | **GET** /system-categories/fed-nonfed | 
[**system_categories_inspection_rating_get**](SystemCategoriesApi.md#system_categories_inspection_rating_get) | **GET** /system-categories/inspection-rating | 
[**system_categories_rip_status_get**](SystemCategoriesApi.md#system_categories_rip_status_get) | **GET** /system-categories/rip-status | 
[**system_categories_usace_nonusace_get**](SystemCategoriesApi.md#system_categories_usace_nonusace_get) | **GET** /system-categories/usace-nonusace | 


# **system_categories_fed_nonfed_get**
> object system_categories_fed_nonfed_get()



Gets all system Ids grouped by fed/non-fed categorical indicators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemCategoriesApi()

try:
    api_response = api_instance.system_categories_fed_nonfed_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemCategoriesApi->system_categories_fed_nonfed_get: %s\n" % e)
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

# **system_categories_inspection_rating_get**
> object system_categories_inspection_rating_get()



Gets all system Ids grouped by fed/non-fed categorical indicators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemCategoriesApi()

try:
    api_response = api_instance.system_categories_inspection_rating_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemCategoriesApi->system_categories_inspection_rating_get: %s\n" % e)
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

# **system_categories_rip_status_get**
> object system_categories_rip_status_get()



Gets all system Ids grouped by fed/non-fed categorical indicators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemCategoriesApi()

try:
    api_response = api_instance.system_categories_rip_status_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemCategoriesApi->system_categories_rip_status_get: %s\n" % e)
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

# **system_categories_usace_nonusace_get**
> object system_categories_usace_nonusace_get()



Gets all system Ids grouped by fed/non-fed categorical indicators

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemCategoriesApi()

try:
    api_response = api_instance.system_categories_usace_nonusace_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemCategoriesApi->system_categories_usace_nonusace_get: %s\n" % e)
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

