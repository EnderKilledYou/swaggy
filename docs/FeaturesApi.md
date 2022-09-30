# swagger_client.FeaturesApi

All URIs are relative to *https://levees.sec.usace.army.mil:443/api-local/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**boreholes_id_get**](FeaturesApi.md#boreholes_id_get) | **GET** /boreholes/{id} | 
[**centerlines_id_get**](FeaturesApi.md#centerlines_id_get) | **GET** /centerlines/{id} | 
[**channels_id_get**](FeaturesApi.md#channels_id_get) | **GET** /channels/{id} | 
[**closure_structures_id_get**](FeaturesApi.md#closure_structures_id_get) | **GET** /closure-structures/{id} | 
[**cross_sections_id_get**](FeaturesApi.md#cross_sections_id_get) | **GET** /cross-sections/{id} | 
[**floodwalls_id_get**](FeaturesApi.md#floodwalls_id_get) | **GET** /floodwalls/{id} | 
[**frm_lines_id_get**](FeaturesApi.md#frm_lines_id_get) | **GET** /frm-lines/{id} | 
[**geometries_type_id_get**](FeaturesApi.md#geometries_type_id_get) | **GET** /geometries/{type}/{id} | 
[**get_alignment_line**](FeaturesApi.md#get_alignment_line) | **GET** /alignment-lines/{id} | 
[**get_all_alignment_lines**](FeaturesApi.md#get_all_alignment_lines) | **GET** /alignment-lines | 
[**get_all_boreholes**](FeaturesApi.md#get_all_boreholes) | **GET** /boreholes | 
[**get_all_channels**](FeaturesApi.md#get_all_channels) | **GET** /channels | 
[**get_all_closure_structures**](FeaturesApi.md#get_all_closure_structures) | **GET** /closure-structures | 
[**get_all_cross_sections**](FeaturesApi.md#get_all_cross_sections) | **GET** /cross-sections | 
[**get_all_floodwalls**](FeaturesApi.md#get_all_floodwalls) | **GET** /floodwalls | 
[**get_all_frm_lines**](FeaturesApi.md#get_all_frm_lines) | **GET** /frm-lines | 
[**get_all_gravity_drains**](FeaturesApi.md#get_all_gravity_drains) | **GET** /gravity-drains | 
[**get_all_levee_centerlines**](FeaturesApi.md#get_all_levee_centerlines) | **GET** /centerlines | 
[**get_all_levee_crossings**](FeaturesApi.md#get_all_levee_crossings) | **GET** /levee-crossings | 
[**get_all_levee_stations**](FeaturesApi.md#get_all_levee_stations) | **GET** /levee-stations | 
[**get_all_leveed_areas**](FeaturesApi.md#get_all_leveed_areas) | **GET** /leveed-areas | 
[**get_all_piezometers**](FeaturesApi.md#get_all_piezometers) | **GET** /piezometers | 
[**get_all_pipe_gates**](FeaturesApi.md#get_all_pipe_gates) | **GET** /pipe-gates | 
[**get_all_pipes**](FeaturesApi.md#get_all_pipes) | **GET** /pipes | 
[**get_all_pump_stations**](FeaturesApi.md#get_all_pump_stations) | **GET** /pump-stations | 
[**get_all_relief_wells**](FeaturesApi.md#get_all_relief_wells) | **GET** /relief-wells | 
[**get_all_toedrains**](FeaturesApi.md#get_all_toedrains) | **GET** /toedrains | 
[**get_geo_json_feature_collection**](FeaturesApi.md#get_geo_json_feature_collection) | **GET** /leveed-areas-{systemId}.geojson | 
[**get_geo_json_feature_collection_0**](FeaturesApi.md#get_geo_json_feature_collection_0) | **GET** /levee-stations-{segmentId}.geojson | 
[**get_some**](FeaturesApi.md#get_some) | **GET** /geometries/query | 
[**gravity_drains_id_get**](FeaturesApi.md#gravity_drains_id_get) | **GET** /gravity-drains/{id} | 
[**levee_crossings_id_get**](FeaturesApi.md#levee_crossings_id_get) | **GET** /levee-crossings/{id} | 
[**levee_stations_id_get**](FeaturesApi.md#levee_stations_id_get) | **GET** /levee-stations/{id} | 
[**leveed_areas_id_get**](FeaturesApi.md#leveed_areas_id_get) | **GET** /leveed-areas/{id} | 
[**piezometers_id_get**](FeaturesApi.md#piezometers_id_get) | **GET** /piezometers/{id} | 
[**pipe_gates_id_get**](FeaturesApi.md#pipe_gates_id_get) | **GET** /pipe-gates/{id} | 
[**pipes_id_get**](FeaturesApi.md#pipes_id_get) | **GET** /pipes/{id} | 
[**pump_stations_id_get**](FeaturesApi.md#pump_stations_id_get) | **GET** /pump-stations/{id} | 
[**relief_wells_id_get**](FeaturesApi.md#relief_wells_id_get) | **GET** /relief-wells/{id} | 
[**toedrains_id_get**](FeaturesApi.md#toedrains_id_get) | **GET** /toedrains/{id} | 


# **boreholes_id_get**
> Borehole2 boreholes_id_get(id)



Gets a Borehole

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of Borehole

try:
    api_response = api_instance.boreholes_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->boreholes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Borehole | 

### Return type

[**Borehole2**](Borehole2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **centerlines_id_get**
> Centerline1 centerlines_id_get(id)



Gets a Centerline

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of Centerline

try:
    api_response = api_instance.centerlines_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->centerlines_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Centerline | 

### Return type

[**Centerline1**](Centerline1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **channels_id_get**
> Channel1 channels_id_get(id)



Gets a Channel

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of Channel

try:
    api_response = api_instance.channels_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->channels_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Channel | 

### Return type

[**Channel1**](Channel1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **closure_structures_id_get**
> ClosureStructure1 closure_structures_id_get(id)



Gets a ClosureStructure

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of ClosureStructure

try:
    api_response = api_instance.closure_structures_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->closure_structures_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of ClosureStructure | 

### Return type

[**ClosureStructure1**](ClosureStructure1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cross_sections_id_get**
> CrossSection1 cross_sections_id_get(id)



Gets a CrossSection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of CrossSection

try:
    api_response = api_instance.cross_sections_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->cross_sections_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of CrossSection | 

### Return type

[**CrossSection1**](CrossSection1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **floodwalls_id_get**
> Floodwall1 floodwalls_id_get(id)



Gets a Floodwall

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of Floodwall

try:
    api_response = api_instance.floodwalls_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->floodwalls_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Floodwall | 

### Return type

[**Floodwall1**](Floodwall1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **frm_lines_id_get**
> FrmLine1 frm_lines_id_get(id)



Gets a FrmLine

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of FrmLine

try:
    api_response = api_instance.frm_lines_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->frm_lines_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of FrmLine | 

### Return type

[**FrmLine1**](FrmLine1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geometries_type_id_get**
> object geometries_type_id_get(type, id, format=format, props=props)



Gets a geometry from a valid feature ID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
type = 'type_example' # str | The id of the geometry
id = 56 # int | The id of the geometry
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)
props = false # bool | Include identifying properties (optional) (default to false)

try:
    api_response = api_instance.geometries_type_id_get(type, id, format=format, props=props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->geometries_type_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The id of the geometry | 
 **id** | **int**| The id of the geometry | 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]
 **props** | **bool**| Include identifying properties | [optional] [default to false]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alignment_line**
> HsipLayer1 get_alignment_line(id)



Gets a Alignment Line

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of Alignment Line

try:
    api_response = api_instance.get_alignment_line(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_alignment_line: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Alignment Line | 

### Return type

[**HsipLayer1**](HsipLayer1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_alignment_lines**
> list[HsipLayer1] get_all_alignment_lines(system_id=system_id, segment_id=segment_id, embed=embed)



Gets all Alignment Lines

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
embed = 'embed_example' # str | link to embed (optional)

try:
    api_response = api_instance.get_all_alignment_lines(system_id=system_id, segment_id=segment_id, embed=embed)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_alignment_lines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **embed** | **str**| link to embed | [optional] 

### Return type

[**list[HsipLayer1]**](HsipLayer1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_boreholes**
> list[Borehole1] get_all_boreholes(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)



Gets all Boreholes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
embed = 'embed_example' # str | link to embed (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)
props = false # bool | Include identifying properties (optional) (default to false)

try:
    api_response = api_instance.get_all_boreholes(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_boreholes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **embed** | **str**| link to embed | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]
 **props** | **bool**| Include identifying properties | [optional] [default to false]

### Return type

[**list[Borehole1]**](Borehole1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_channels**
> list[Channel1] get_all_channels(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)



Gets all Channels

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
embed = 'embed_example' # str | link to embed (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)
props = false # bool | Include identifying properties (optional) (default to false)

try:
    api_response = api_instance.get_all_channels(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **embed** | **str**| link to embed | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]
 **props** | **bool**| Include identifying properties | [optional] [default to false]

### Return type

[**list[Channel1]**](Channel1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_closure_structures**
> list[ClosureStructure1] get_all_closure_structures(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)



Gets all ClosureStructures

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
embed = 'embed_example' # str | link to embed (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)
props = false # bool | Include identifying properties (optional) (default to false)

try:
    api_response = api_instance.get_all_closure_structures(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_closure_structures: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **embed** | **str**| link to embed | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]
 **props** | **bool**| Include identifying properties | [optional] [default to false]

### Return type

[**list[ClosureStructure1]**](ClosureStructure1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_cross_sections**
> list[CrossSection1] get_all_cross_sections(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)



Gets all CrossSections

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
embed = 'embed_example' # str | link to embed (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)
props = false # bool | Include identifying properties (optional) (default to false)

try:
    api_response = api_instance.get_all_cross_sections(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_cross_sections: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **embed** | **str**| link to embed | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]
 **props** | **bool**| Include identifying properties | [optional] [default to false]

### Return type

[**list[CrossSection1]**](CrossSection1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_floodwalls**
> list[Floodwall1] get_all_floodwalls(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)



Gets all Floodwalls

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
embed = 'embed_example' # str | link to embed (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)
props = false # bool | Include identifying properties (optional) (default to false)

try:
    api_response = api_instance.get_all_floodwalls(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_floodwalls: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **embed** | **str**| link to embed | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]
 **props** | **bool**| Include identifying properties | [optional] [default to false]

### Return type

[**list[Floodwall1]**](Floodwall1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_frm_lines**
> list[FrmLine1] get_all_frm_lines(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)



Gets all FRM Lines

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
embed = 'embed_example' # str | link to embed (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)
props = false # bool | Include identifying properties (optional) (default to false)

try:
    api_response = api_instance.get_all_frm_lines(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_frm_lines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **embed** | **str**| link to embed | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]
 **props** | **bool**| Include identifying properties | [optional] [default to false]

### Return type

[**list[FrmLine1]**](FrmLine1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_gravity_drains**
> list[GravityDrain1] get_all_gravity_drains(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)



Gets all GravityDrains

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
embed = 'embed_example' # str | link to embed (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)
props = false # bool | Include identifying properties (optional) (default to false)

try:
    api_response = api_instance.get_all_gravity_drains(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_gravity_drains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **embed** | **str**| link to embed | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]
 **props** | **bool**| Include identifying properties | [optional] [default to false]

### Return type

[**list[GravityDrain1]**](GravityDrain1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_levee_centerlines**
> list[Centerline1] get_all_levee_centerlines(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)



Gets all LeveeCenterlines

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
embed = 'embed_example' # str | link to embed (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)
props = false # bool | Include identifying properties (optional) (default to false)

try:
    api_response = api_instance.get_all_levee_centerlines(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_levee_centerlines: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **embed** | **str**| link to embed | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]
 **props** | **bool**| Include identifying properties | [optional] [default to false]

### Return type

[**list[Centerline1]**](Centerline1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_levee_crossings**
> list[LeveeCrossing1] get_all_levee_crossings(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)



Gets all LeveeCrossings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
embed = 'embed_example' # str | link to embed (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)
props = false # bool | Include identifying properties (optional) (default to false)

try:
    api_response = api_instance.get_all_levee_crossings(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_levee_crossings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **embed** | **str**| link to embed | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]
 **props** | **bool**| Include identifying properties | [optional] [default to false]

### Return type

[**list[LeveeCrossing1]**](LeveeCrossing1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_levee_stations**
> list[LeveeStation1] get_all_levee_stations(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)



Gets all LeveeStations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
embed = 'embed_example' # str | link to embed (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)
props = false # bool | Include identifying properties (optional) (default to false)

try:
    api_response = api_instance.get_all_levee_stations(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_levee_stations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **embed** | **str**| link to embed | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]
 **props** | **bool**| Include identifying properties | [optional] [default to false]

### Return type

[**list[LeveeStation1]**](LeveeStation1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_leveed_areas**
> list[LeveedArea1] get_all_leveed_areas(system_id=system_id, embed=embed, format=format)



Gets all LeveedAreas

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
embed = 'embed_example' # str | link to embed (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)

try:
    api_response = api_instance.get_all_leveed_areas(system_id=system_id, embed=embed, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_leveed_areas: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **embed** | **str**| link to embed | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]

### Return type

[**list[LeveedArea1]**](LeveedArea1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_piezometers**
> list[Piezometer1] get_all_piezometers(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)



Gets all Piezometers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
embed = 'embed_example' # str | link to embed (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)
props = false # bool | Include identifying properties (optional) (default to false)

try:
    api_response = api_instance.get_all_piezometers(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_piezometers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **embed** | **str**| link to embed | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]
 **props** | **bool**| Include identifying properties | [optional] [default to false]

### Return type

[**list[Piezometer1]**](Piezometer1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_pipe_gates**
> list[PipeGate1] get_all_pipe_gates(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)



Gets all Pipe Gates

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
embed = 'embed_example' # str | link to embed (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)
props = false # bool | Include identifying properties (optional) (default to false)

try:
    api_response = api_instance.get_all_pipe_gates(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_pipe_gates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **embed** | **str**| link to embed | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]
 **props** | **bool**| Include identifying properties | [optional] [default to false]

### Return type

[**list[PipeGate1]**](PipeGate1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_pipes**
> list[Pipe1] get_all_pipes(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)



Gets all Pipes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
embed = 'embed_example' # str | link to embed (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)
props = false # bool | Include identifying properties (optional) (default to false)

try:
    api_response = api_instance.get_all_pipes(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_pipes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **embed** | **str**| link to embed | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]
 **props** | **bool**| Include identifying properties | [optional] [default to false]

### Return type

[**list[Pipe1]**](Pipe1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_pump_stations**
> list[PumpStation1] get_all_pump_stations(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)



Gets all PumpStations

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
embed = 'embed_example' # str | link to embed (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)
props = false # bool | Include identifying properties (optional) (default to false)

try:
    api_response = api_instance.get_all_pump_stations(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_pump_stations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **embed** | **str**| link to embed | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]
 **props** | **bool**| Include identifying properties | [optional] [default to false]

### Return type

[**list[PumpStation1]**](PumpStation1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_relief_wells**
> list[ReliefWell1] get_all_relief_wells(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)



Gets all ReliefWells

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
embed = 'embed_example' # str | link to embed (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)
props = false # bool | Include identifying properties (optional) (default to false)

try:
    api_response = api_instance.get_all_relief_wells(system_id=system_id, segment_id=segment_id, embed=embed, format=format, props=props)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_relief_wells: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **embed** | **str**| link to embed | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]
 **props** | **bool**| Include identifying properties | [optional] [default to false]

### Return type

[**list[ReliefWell1]**](ReliefWell1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_toedrains**
> list[object] get_all_toedrains(system_id=system_id, segment_id=segment_id, embed=embed, format=format)



Gets all Toedrains

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | systemId (optional)
segment_id = 56 # int | segmentId (optional)
embed = 'embed_example' # str | link to embed (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)

try:
    api_response = api_instance.get_all_toedrains(system_id=system_id, segment_id=segment_id, embed=embed, format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_all_toedrains: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| systemId | [optional] 
 **segment_id** | **int**| segmentId | [optional] 
 **embed** | **str**| link to embed | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_geo_json_feature_collection**
> object get_geo_json_feature_collection(system_id)



Gets all leveed areas belonging to system as a geojson feature collection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
system_id = 56 # int | system_id

try:
    api_response = api_instance.get_geo_json_feature_collection(system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_geo_json_feature_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| system_id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_geo_json_feature_collection_0**
> object get_geo_json_feature_collection_0(segment_id)



Gets all levee stations belonging to segment as a geojson feature collection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
segment_id = 56 # int | segment_id

try:
    api_response = api_instance.get_geo_json_feature_collection_0(segment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_geo_json_feature_collection_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **segment_id** | **int**| segment_id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_some**
> object get_some(type, segment_id=segment_id, system_id=system_id, format=format, props=props, coll=coll)



Gets geometries by type and system/segment Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
type = 'type_example' # str | The type (or class) of the geometry in spinal case (e.g. pump-station)
segment_id = 56 # int | The segment id of the geometry (one of systemId or segmentId is required) (optional)
system_id = 56 # int | The system id of the geometry (one of systemId or segmentId is required) (optional)
format = 'topo' # str | JSON geometry format (topo, geo). Default is topo (optional) (default to topo)
props = false # bool | Include identifying properties (id, name, class) (optional) (default to false)
coll = false # bool | Return response as a FeatureCollection (optional) (default to false)

try:
    api_response = api_instance.get_some(type, segment_id=segment_id, system_id=system_id, format=format, props=props, coll=coll)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->get_some: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| The type (or class) of the geometry in spinal case (e.g. pump-station) | 
 **segment_id** | **int**| The segment id of the geometry (one of systemId or segmentId is required) | [optional] 
 **system_id** | **int**| The system id of the geometry (one of systemId or segmentId is required) | [optional] 
 **format** | **str**| JSON geometry format (topo, geo). Default is topo | [optional] [default to topo]
 **props** | **bool**| Include identifying properties (id, name, class) | [optional] [default to false]
 **coll** | **bool**| Return response as a FeatureCollection | [optional] [default to false]

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gravity_drains_id_get**
> GravityDrain1 gravity_drains_id_get(id)



Gets a GravityDrain

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of GravityDrain

try:
    api_response = api_instance.gravity_drains_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->gravity_drains_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of GravityDrain | 

### Return type

[**GravityDrain1**](GravityDrain1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **levee_crossings_id_get**
> LeveeCrossing1 levee_crossings_id_get(id)



Gets a LeveeCrossing

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of LeveeCrossing

try:
    api_response = api_instance.levee_crossings_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->levee_crossings_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of LeveeCrossing | 

### Return type

[**LeveeCrossing1**](LeveeCrossing1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **levee_stations_id_get**
> LeveeStation1 levee_stations_id_get(id)



Gets a LeveeStation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of LeveeStation

try:
    api_response = api_instance.levee_stations_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->levee_stations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of LeveeStation | 

### Return type

[**LeveeStation1**](LeveeStation1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **leveed_areas_id_get**
> LeveedArea1 leveed_areas_id_get(id)



Gets a LeveedArea

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of LeveedArea

try:
    api_response = api_instance.leveed_areas_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->leveed_areas_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of LeveedArea | 

### Return type

[**LeveedArea1**](LeveedArea1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **piezometers_id_get**
> Piezometer1 piezometers_id_get(id)



Gets a Piezometer

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of Piezometer

try:
    api_response = api_instance.piezometers_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->piezometers_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Piezometer | 

### Return type

[**Piezometer1**](Piezometer1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipe_gates_id_get**
> PipeGate1 pipe_gates_id_get(id)



Gets a PipeGate

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of PipeGate

try:
    api_response = api_instance.pipe_gates_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->pipe_gates_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of PipeGate | 

### Return type

[**PipeGate1**](PipeGate1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipes_id_get**
> Pipe1 pipes_id_get(id)



Gets a Pipe

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of Pipe

try:
    api_response = api_instance.pipes_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->pipes_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Pipe | 

### Return type

[**Pipe1**](Pipe1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pump_stations_id_get**
> PumpStation1 pump_stations_id_get(id)



Gets a PumpStation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of PumpStation

try:
    api_response = api_instance.pump_stations_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->pump_stations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of PumpStation | 

### Return type

[**PumpStation1**](PumpStation1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **relief_wells_id_get**
> ReliefWell1 relief_wells_id_get(id)



Gets a ReliefWell

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of ReliefWell

try:
    api_response = api_instance.relief_wells_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->relief_wells_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of ReliefWell | 

### Return type

[**ReliefWell1**](ReliefWell1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toedrains_id_get**
> object toedrains_id_get(id)



Gets a Toedrain

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.FeaturesApi()
id = 56 # int | ID of Toedrain

try:
    api_response = api_instance.toedrains_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FeaturesApi->toedrains_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID of Toedrain | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

