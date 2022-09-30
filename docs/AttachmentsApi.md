# swagger_client.AttachmentsApi

All URIs are relative to *https://levees.sec.usace.army.mil:443/api-local/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachments_id_get**](AttachmentsApi.md#attachments_id_get) | **GET** /attachments/{id} | 
[**get_all_attachments**](AttachmentsApi.md#get_all_attachments) | **GET** /attachments | 


# **attachments_id_get**
> Attachment1 attachments_id_get(id)



Gets an Attachment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttachmentsApi()
id = 56 # int | ID of Attachment

try:
    api_response = api_instance.attachments_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->attachments_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Attachment | 

### Return type

[**Attachment1**](Attachment1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_attachments**
> list[Attachment1] get_all_attachments(system_id=system_id, segment_id=segment_id, system_inspection_id=system_inspection_id, segment_inspection_id=segment_inspection_id, contclass_id=contclass_id, reference=reference)



Gets all attachments associated with a systemId or segmentId

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AttachmentsApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
system_inspection_id = 56 # int | systemInspectionId (optional)
segment_inspection_id = 56 # int | segmentInspectionId (optional)
contclass_id = 56 # int | contClassId (optional)
reference = true # bool | reference (optional)

try:
    api_response = api_instance.get_all_attachments(system_id=system_id, segment_id=segment_id, system_inspection_id=system_inspection_id, segment_inspection_id=segment_inspection_id, contclass_id=contclass_id, reference=reference)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AttachmentsApi->get_all_attachments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **system_inspection_id** | **int**| systemInspectionId | [optional] 
 **segment_inspection_id** | **int**| segmentInspectionId | [optional] 
 **contclass_id** | **int**| contClassId | [optional] 
 **reference** | **bool**| reference | [optional] 

### Return type

[**list[Attachment1]**](Attachment1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

