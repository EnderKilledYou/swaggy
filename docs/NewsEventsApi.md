# swagger_client.NewsEventsApi

All URIs are relative to *https://levees.sec.usace.army.mil:443/api-local/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_id_get**](NewsEventsApi.md#events_id_get) | **GET** /events/{id} | 
[**get_all_events**](NewsEventsApi.md#get_all_events) | **GET** /events | 
[**get_all_news_articles**](NewsEventsApi.md#get_all_news_articles) | **GET** /news | 
[**news_id_get**](NewsEventsApi.md#news_id_get) | **GET** /news/{id} | 


# **events_id_get**
> object events_id_get(id)



Gets an event article

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NewsEventsApi()
id = 56 # int | ID of event article

try:
    api_response = api_instance.events_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsEventsApi->events_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of event article | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_events**
> list[object] get_all_events()



Gets all event articles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NewsEventsApi()

try:
    api_response = api_instance.get_all_events()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsEventsApi->get_all_events: %s\n" % e)
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

# **get_all_news_articles**
> list[object] get_all_news_articles(user_id=user_id)



Gets all news articles

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NewsEventsApi()
user_id = 56 # int | userId (optional)

try:
    api_response = api_instance.get_all_news_articles(user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsEventsApi->get_all_news_articles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| userId | [optional] 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **news_id_get**
> object news_id_get(id)



Gets a news article

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.NewsEventsApi()
id = 56 # int | ID of news article

try:
    api_response = api_instance.news_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NewsEventsApi->news_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of news article | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

