# swagger_client.SystemsApi

All URIs are relative to *https://levees.sec.usace.army.mil:443/api-local/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_system_p2_names**](SystemsApi.md#get_all_system_p2_names) | **GET** /systems/p2-names | 
[**names**](SystemsApi.md#names) | **GET** /systems/names | 
[**query**](SystemsApi.md#query) | **GET** /systems/query | 


# **get_all_system_p2_names**
> list[object] get_all_system_p2_names(system_id)



Gets all System P2 Names

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemsApi()
system_id = 56 # int | fc_system_id

try:
    api_response = api_instance.get_all_system_p2_names(system_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemsApi->get_all_system_p2_names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system_id** | **int**| fc_system_id | 

### Return type

**list[object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **names**
> object names(ids=ids)



Gets a map of system names provided a list of ids as a query parameter

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemsApi()
ids = [56] # list[int] | list of systems ids for which to retrieve names (optional)

try:
    api_response = api_instance.names(ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemsApi->names: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**list[int]**](int.md)| list of systems ids for which to retrieve names | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query**
> list[FloodControlSystem1] query(_as=_as, bh=bh, cl=cl, cs=cs, sy=sy, syarray=syarray, fw=fw, gd=gd, _in=_in, lc=lc, la=la, md=md, nr=nr, pz=pz, pi=pi, pg=pg, ps=ps, rw=rw, ri=ri, rs=rs, sg=sg, gi=gi, yi=yi, _return=_return, fsi=fsi, frm=frm, cha=cha)



Finds Systems using redisearch syntax by type

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.SystemsApi()
_as = 'system' # str | return items as.  e.g. ?as=borehole (optional) (default to system)
bh = 'bh_example' # str | borehole (optional)
cl = 'cl_example' # str | centerline (optional)
cs = 'cs_example' # str | closure-structure (optional)
sy = 'sy_example' # str | flood-control-system (optional)
syarray = 'syarray_example' # str | flood-control-system array values (optional)
fw = 'fw_example' # str | floodwall (optional)
gd = 'gd_example' # str | gravity-drain (optional)
_in = '_in_example' # str | @state:illinois|missouri (optional)
lc = 'lc_example' # str | levee-crossing (optional)
la = 'la_example' # str | leveed-area (optional)
md = false # bool | return metadata only (optional) (default to false)
nr = 'nr_example' # str | DEPRECATED, use sy=@coords:[lon lat radius unit] where unit == mi || ft || km || m (optional)
pz = 'pz_example' # str | piezometer (optional)
pi = 'pi_example' # str | pipe (optional)
pg = 'pg_example' # str | pipe-gate (optional)
ps = 'ps_example' # str | pump-station (optional)
rw = 'rw_example' # str | relief-well (optional)
ri = 'ri_example' # str | risk (optional)
rs = 'rs_example' # str | rip-status (optional)
sg = 'sg_example' # str | segment (optional)
gi = 'gi_example' # str | segment-inspection (optional)
yi = 'yi_example' # str | system-inspection (optional)
_return = ['_return_example'] # list[str] | return only these fields (optional)
fsi = 'fsi_example' # str | fema-system-info (optional)
frm = 'frm_example' # str | frm-line (optional)
cha = 'cha_example' # str | channel (optional)

try:
    api_response = api_instance.query(_as=_as, bh=bh, cl=cl, cs=cs, sy=sy, syarray=syarray, fw=fw, gd=gd, _in=_in, lc=lc, la=la, md=md, nr=nr, pz=pz, pi=pi, pg=pg, ps=ps, rw=rw, ri=ri, rs=rs, sg=sg, gi=gi, yi=yi, _return=_return, fsi=fsi, frm=frm, cha=cha)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SystemsApi->query: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_as** | **str**| return items as.  e.g. ?as&#x3D;borehole | [optional] [default to system]
 **bh** | **str**| borehole | [optional] 
 **cl** | **str**| centerline | [optional] 
 **cs** | **str**| closure-structure | [optional] 
 **sy** | **str**| flood-control-system | [optional] 
 **syarray** | **str**| flood-control-system array values | [optional] 
 **fw** | **str**| floodwall | [optional] 
 **gd** | **str**| gravity-drain | [optional] 
 **_in** | **str**| @state:illinois|missouri | [optional] 
 **lc** | **str**| levee-crossing | [optional] 
 **la** | **str**| leveed-area | [optional] 
 **md** | **bool**| return metadata only | [optional] [default to false]
 **nr** | **str**| DEPRECATED, use sy&#x3D;@coords:[lon lat radius unit] where unit &#x3D;&#x3D; mi || ft || km || m | [optional] 
 **pz** | **str**| piezometer | [optional] 
 **pi** | **str**| pipe | [optional] 
 **pg** | **str**| pipe-gate | [optional] 
 **ps** | **str**| pump-station | [optional] 
 **rw** | **str**| relief-well | [optional] 
 **ri** | **str**| risk | [optional] 
 **rs** | **str**| rip-status | [optional] 
 **sg** | **str**| segment | [optional] 
 **gi** | **str**| segment-inspection | [optional] 
 **yi** | **str**| system-inspection | [optional] 
 **_return** | [**list[str]**](str.md)| return only these fields | [optional] 
 **fsi** | **str**| fema-system-info | [optional] 
 **frm** | **str**| frm-line | [optional] 
 **cha** | **str**| channel | [optional] 

### Return type

[**list[FloodControlSystem1]**](FloodControlSystem1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

