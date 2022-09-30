# swagger_client.DownloadApi

All URIs are relative to *https://levees.sec.usace.army.mil:443/api-local/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_dataset_csv_zip_post**](DownloadApi.md#download_dataset_csv_zip_post) | **POST** /download/dataset/csv.zip | 
[**download_dataset_earth_zip_post**](DownloadApi.md#download_dataset_earth_zip_post) | **POST** /download/dataset/earth.zip | 
[**download_dataset_geojson_zip_post**](DownloadApi.md#download_dataset_geojson_zip_post) | **POST** /download/dataset/geojson.zip | 
[**download_dataset_shapefile_zip_post**](DownloadApi.md#download_dataset_shapefile_zip_post) | **POST** /download/dataset/shapefile.zip | 
[**download_hsip_counts_id_csv_get**](DownloadApi.md#download_hsip_counts_id_csv_get) | **GET** /download/hsip-counts-{id}.csv | 
[**download_risk_processes_csv_get**](DownloadApi.md#download_risk_processes_csv_get) | **GET** /download/risk-processes.csv | 
[**download_system_name_history_csv_get**](DownloadApi.md#download_system_name_history_csv_get) | **GET** /download/system-name-history.csv | 
[**get_all_hsip_layers**](DownloadApi.md#get_all_hsip_layers) | **GET** /download/hsip-layers-{id}.zip | 
[**get_download_blob**](DownloadApi.md#get_download_blob) | **GET** /download/attachments/{id} | 


# **download_dataset_csv_zip_post**
> file download_dataset_csv_zip_post(body, full=full)



Returns the features of levee system(s) as a zip file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadApi()
body = [swagger_client.list[int]()] # list[int] | ID of levee system(s)
full = true # bool | add all avaliable features to zip (optional)

try:
    api_response = api_instance.download_dataset_csv_zip_post(body, full=full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadApi->download_dataset_csv_zip_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[int]**| ID of levee system(s) | 
 **full** | **bool**| add all avaliable features to zip | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_dataset_earth_zip_post**
> file download_dataset_earth_zip_post(body, full=full)



Returns the kml of levee system(s) as a zip file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadApi()
body = [swagger_client.list[int]()] # list[int] | ID of levee system(s)
full = true # bool | add all avaliable features to zip (optional)

try:
    api_response = api_instance.download_dataset_earth_zip_post(body, full=full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadApi->download_dataset_earth_zip_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[int]**| ID of levee system(s) | 
 **full** | **bool**| add all avaliable features to zip | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_dataset_geojson_zip_post**
> file download_dataset_geojson_zip_post(body, full=full)



Returns the geojson of levee system(s) as a zip file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadApi()
body = [swagger_client.list[int]()] # list[int] | ID of levee system(s)
full = true # bool | add all avaliable features to zip (optional)

try:
    api_response = api_instance.download_dataset_geojson_zip_post(body, full=full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadApi->download_dataset_geojson_zip_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[int]**| ID of levee system(s) | 
 **full** | **bool**| add all avaliable features to zip | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_dataset_shapefile_zip_post**
> file download_dataset_shapefile_zip_post(body, full=full)



Returns the shapefile zip of levee system(s) as a zip file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadApi()
body = [swagger_client.list[int]()] # list[int] | ID of levee system(s)
full = true # bool | add all avaliable features to zip (optional)

try:
    api_response = api_instance.download_dataset_shapefile_zip_post(body, full=full)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadApi->download_dataset_shapefile_zip_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **list[int]**| ID of levee system(s) | 
 **full** | **bool**| add all avaliable features to zip | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_hsip_counts_id_csv_get**
> file download_hsip_counts_id_csv_get(id)



Returns the HSIP counts for a given system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadApi()
id = 56 # int | ID of system

try:
    api_response = api_instance.download_hsip_counts_id_csv_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadApi->download_hsip_counts_id_csv_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of system | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_risk_processes_csv_get**
> file download_risk_processes_csv_get()



Returns the CSV list of all risk processes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadApi()

try:
    api_response = api_instance.download_risk_processes_csv_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadApi->download_risk_processes_csv_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_system_name_history_csv_get**
> file download_system_name_history_csv_get(begin_date=begin_date, end_date=end_date)



Returns the system name history

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadApi()
begin_date = 'begin_date_example' # str | 20-FEB-2018 (optional)
end_date = 'end_date_example' # str | 20-FEB-2018 (optional)

try:
    api_response = api_instance.download_system_name_history_csv_get(begin_date=begin_date, end_date=end_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadApi->download_system_name_history_csv_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **begin_date** | **str**| 20-FEB-2018 | [optional] 
 **end_date** | **str**| 20-FEB-2018 | [optional] 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_hsip_layers**
> list[HsipLayer1] get_all_hsip_layers(id)



Gets HsipLayer zip of shp files

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadApi()
id = 56 # int | ID of system

try:
    api_response = api_instance.get_all_hsip_layers(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadApi->get_all_hsip_layers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of system | 

### Return type

[**list[HsipLayer1]**](HsipLayer1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_download_blob**
> file get_download_blob(id)



Gets an Attachment File

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DownloadApi()
id = 56 # int | ID of Attachment

try:
    api_response = api_instance.get_download_blob(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DownloadApi->get_download_blob: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attachment | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

