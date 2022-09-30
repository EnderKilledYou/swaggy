# swagger_client.SegmentsApi

All URIs are relative to *https://levees.sec.usace.army.mil:443/api-local/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_segment_p2_names**](SegmentsApi.md#get_all_segment_p2_names) | **GET** /segments/p2-names | 
[**get_all_segment_sponsors**](SegmentsApi.md#get_all_segment_sponsors) | **GET** /segments/{segmentId}/sponsorships | 
[**get_all_segments**](SegmentsApi.md#get_all_segments) | **GET** /segments | 
[**segments_id_get**](SegmentsApi.md#segments_id_get) | **GET** /segments/{id} | 


# **get_all_segment_p2_names**
> list[object] get_all_segment_p2_names(segment_id)



Gets all Segment P2 Names

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SegmentsApi()
segment_id = 56 # int | fc_segment_id

try:
    api_response = api_instance.get_all_segment_p2_names(segment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->get_all_segment_p2_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **int**| fc_segment_id | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_segment_sponsors**
> list[SegmentSponsor1] get_all_segment_sponsors(segment_id)



Gets all SegmentSponsors

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SegmentsApi()
segment_id = 56 # int | fc_segment_id

try:
    api_response = api_instance.get_all_segment_sponsors(segment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->get_all_segment_sponsors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **int**| fc_segment_id | 

### Return type

[**list[SegmentSponsor1]**](SegmentSponsor1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_segments**
> list[Segment1] get_all_segments(system_id=system_id, embed=embed)



Gets all Segments

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SegmentsApi()
system_id = 56 # int | systemId (optional)
embed = 'embed_example' # str | link to embed (optional)

try:
    api_response = api_instance.get_all_segments(system_id=system_id, embed=embed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->get_all_segments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **embed** | **str**| link to embed | [optional] 

### Return type

[**list[Segment1]**](Segment1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **segments_id_get**
> Segment1 segments_id_get(id)



Gets a Segment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SegmentsApi()
id = 56 # int | ID of Segment

try:
    api_response = api_instance.segments_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->segments_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Segment | 

### Return type

[**Segment1**](Segment1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

