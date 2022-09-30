# swagger_client.PortfoliosApi

All URIs are relative to *https://levees.sec.usace.army.mil:443/api-local/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_portfolio_systems**](PortfoliosApi.md#get_all_portfolio_systems) | **GET** /portfolio-systems | 
[**get_all_portfolios**](PortfoliosApi.md#get_all_portfolios) | **GET** /portfolio | 
[**get_system_ids**](PortfoliosApi.md#get_system_ids) | **GET** /portfolio-system-ids/{id} | 
[**portfolio_id_get**](PortfoliosApi.md#portfolio_id_get) | **GET** /portfolio/{id} | 
[**portfolio_system_id_get**](PortfoliosApi.md#portfolio_system_id_get) | **GET** /portfolio-system/{id} | 


# **get_all_portfolio_systems**
> list[object] get_all_portfolio_systems(portfolio_id=portfolio_id, system_id=system_id, cached=cached)



Gets all systems belonging to a portfolio by either system id or portfolio id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfoliosApi()
portfolio_id = 56 # int | ID of the portfolio (optional)
system_id = 56 # int | ID of the system (optional)
cached = false # bool | Pull from cached flood control system (optional) (default to false)

try:
    api_response = api_instance.get_all_portfolio_systems(portfolio_id=portfolio_id, system_id=system_id, cached=cached)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->get_all_portfolio_systems: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **portfolio_id** | **int**| ID of the portfolio | [optional] 
 **system_id** | **int**| ID of the system | [optional] 
 **cached** | **bool**| Pull from cached flood control system | [optional] [default to false]

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_portfolios**
> list[Portfolio1] get_all_portfolios(org_id=org_id, populated=populated, published=published)



Gets all systems portfolios belonging to a user or organization

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfoliosApi()
org_id = 56 # int | ID of the organization (optional)
populated = false # bool | Only include populated portfolios (optional) (default to false)
published = true # bool | Only include published portfolios (optional) (default to true)

try:
    api_response = api_instance.get_all_portfolios(org_id=org_id, populated=populated, published=published)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->get_all_portfolios: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **org_id** | **int**| ID of the organization | [optional] 
 **populated** | **bool**| Only include populated portfolios | [optional] [default to false]
 **published** | **bool**| Only include published portfolios | [optional] [default to true]

### Return type

[**list[Portfolio1]**](Portfolio1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_system_ids**
> list[int] get_system_ids(id)



Gets all system IDs belonging to a portfolio

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfoliosApi()
id = 56 # int | ID of the portfolio

try:
    api_response = api_instance.get_system_ids(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->get_system_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the portfolio | 

### Return type

**list[int]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_id_get**
> Portfolio1 portfolio_id_get(id)



Gets a portfolio

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfoliosApi()
id = 56 # int | ID of portfolio

try:
    api_response = api_instance.portfolio_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->portfolio_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of portfolio | 

### Return type

[**Portfolio1**](Portfolio1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **portfolio_system_id_get**
> object portfolio_system_id_get(id)



Gets a single portfolio system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.PortfoliosApi()
id = 56 # int | ID of the portfolio system

try:
    api_response = api_instance.portfolio_system_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PortfoliosApi->portfolio_system_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of the portfolio system | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

