# coding: utf-8

"""
    NLD2 API

    The <b>NLD2 API</b> is a complete, programmable interface to all National Levee Database functionality. The NLD2 API is a RESTful web service, using standard technologies like HTTP verbs, headers, and status codes.<br/><br/>The <a href=\"/#/\" target=\"_blank\">National Levee Database website</a> is built on this API, and all of its services are available for integration into your application. To get started, we recommend exploring the website to learn about the functionality that is available and then using the OpenAPI specification below to try connecting to the test/hello endpoint.<br/><br/>Currently, you can develop your application with the public API. For more advanced features, you may need an NLD account and specific government clearance, depending on the nature of the data. If you need assistance, please email us at <a href=\"mailto:NLD@usace.army.mil\">NLD@usace.army.mil</a> or call us at <a href=\"tel:18775383387\">1-877-LEVEEUS</a> (1-877-538-3387).  # noqa: E501

    OpenAPI spec version: 3.26.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SystemsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_system_p2_names(self, system_id, **kwargs):  # noqa: E501
        """get_all_system_p2_names  # noqa: E501

        Gets all System P2 Names  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_system_p2_names(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int system_id: fc_system_id (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_system_p2_names_with_http_info(system_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_all_system_p2_names_with_http_info(system_id, **kwargs)  # noqa: E501
            return data

    def get_all_system_p2_names_with_http_info(self, system_id, **kwargs):  # noqa: E501
        """get_all_system_p2_names  # noqa: E501

        Gets all System P2 Names  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_system_p2_names_with_http_info(system_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int system_id: fc_system_id (required)
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['system_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_system_p2_names" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'system_id' is set
        if self.api_client.client_side_validation and ('system_id' not in params or
                                                       params['system_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `system_id` when calling `get_all_system_p2_names`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'system_id' in params:
            query_params.append(('systemId', params['system_id']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/systems/p2-names', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def names(self, **kwargs):  # noqa: E501
        """names  # noqa: E501

        Gets a map of system names provided a list of ids as a query parameter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.names(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] ids: list of systems ids for which to retrieve names
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.names_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.names_with_http_info(**kwargs)  # noqa: E501
            return data

    def names_with_http_info(self, **kwargs):  # noqa: E501
        """names  # noqa: E501

        Gets a map of system names provided a list of ids as a query parameter  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.names_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[int] ids: list of systems ids for which to retrieve names
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['ids']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method names" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'ids' in params:
            query_params.append(('ids', params['ids']))  # noqa: E501
            collection_formats['ids'] = 'multi'  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/systems/names', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def query(self, **kwargs):  # noqa: E501
        """query  # noqa: E501

        Finds Systems using redisearch syntax by type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str _as: return items as.  e.g. ?as=borehole
        :param str bh: borehole
        :param str cl: centerline
        :param str cs: closure-structure
        :param str sy: flood-control-system
        :param str syarray: flood-control-system array values
        :param str fw: floodwall
        :param str gd: gravity-drain
        :param str _in: @state:illinois|missouri
        :param str lc: levee-crossing
        :param str la: leveed-area
        :param bool md: return metadata only
        :param str nr: DEPRECATED, use sy=@coords:[lon lat radius unit] where unit == mi || ft || km || m
        :param str pz: piezometer
        :param str pi: pipe
        :param str pg: pipe-gate
        :param str ps: pump-station
        :param str rw: relief-well
        :param str ri: risk
        :param str rs: rip-status
        :param str sg: segment
        :param str gi: segment-inspection
        :param str yi: system-inspection
        :param list[str] _return: return only these fields
        :param str fsi: fema-system-info
        :param str frm: frm-line
        :param str cha: channel
        :return: list[FloodControlSystem1]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.query_with_http_info(**kwargs)  # noqa: E501
            return data

    def query_with_http_info(self, **kwargs):  # noqa: E501
        """query  # noqa: E501

        Finds Systems using redisearch syntax by type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str _as: return items as.  e.g. ?as=borehole
        :param str bh: borehole
        :param str cl: centerline
        :param str cs: closure-structure
        :param str sy: flood-control-system
        :param str syarray: flood-control-system array values
        :param str fw: floodwall
        :param str gd: gravity-drain
        :param str _in: @state:illinois|missouri
        :param str lc: levee-crossing
        :param str la: leveed-area
        :param bool md: return metadata only
        :param str nr: DEPRECATED, use sy=@coords:[lon lat radius unit] where unit == mi || ft || km || m
        :param str pz: piezometer
        :param str pi: pipe
        :param str pg: pipe-gate
        :param str ps: pump-station
        :param str rw: relief-well
        :param str ri: risk
        :param str rs: rip-status
        :param str sg: segment
        :param str gi: segment-inspection
        :param str yi: system-inspection
        :param list[str] _return: return only these fields
        :param str fsi: fema-system-info
        :param str frm: frm-line
        :param str cha: channel
        :return: list[FloodControlSystem1]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['_as', 'bh', 'cl', 'cs', 'sy', 'syarray', 'fw', 'gd', '_in', 'lc', 'la', 'md', 'nr', 'pz', 'pi', 'pg', 'ps', 'rw', 'ri', 'rs', 'sg', 'gi', 'yi', '_return', 'fsi', 'frm', 'cha']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if '_as' in params:
            query_params.append(('as', params['_as']))  # noqa: E501
        if 'bh' in params:
            query_params.append(('bh', params['bh']))  # noqa: E501
        if 'cl' in params:
            query_params.append(('cl', params['cl']))  # noqa: E501
        if 'cs' in params:
            query_params.append(('cs', params['cs']))  # noqa: E501
        if 'sy' in params:
            query_params.append(('sy', params['sy']))  # noqa: E501
        if 'syarray' in params:
            query_params.append(('syarray', params['syarray']))  # noqa: E501
        if 'fw' in params:
            query_params.append(('fw', params['fw']))  # noqa: E501
        if 'gd' in params:
            query_params.append(('gd', params['gd']))  # noqa: E501
        if '_in' in params:
            query_params.append(('in', params['_in']))  # noqa: E501
        if 'lc' in params:
            query_params.append(('lc', params['lc']))  # noqa: E501
        if 'la' in params:
            query_params.append(('la', params['la']))  # noqa: E501
        if 'md' in params:
            query_params.append(('md', params['md']))  # noqa: E501
        if 'nr' in params:
            query_params.append(('nr', params['nr']))  # noqa: E501
        if 'pz' in params:
            query_params.append(('pz', params['pz']))  # noqa: E501
        if 'pi' in params:
            query_params.append(('pi', params['pi']))  # noqa: E501
        if 'pg' in params:
            query_params.append(('pg', params['pg']))  # noqa: E501
        if 'ps' in params:
            query_params.append(('ps', params['ps']))  # noqa: E501
        if 'rw' in params:
            query_params.append(('rw', params['rw']))  # noqa: E501
        if 'ri' in params:
            query_params.append(('ri', params['ri']))  # noqa: E501
        if 'rs' in params:
            query_params.append(('rs', params['rs']))  # noqa: E501
        if 'sg' in params:
            query_params.append(('sg', params['sg']))  # noqa: E501
        if 'gi' in params:
            query_params.append(('gi', params['gi']))  # noqa: E501
        if 'yi' in params:
            query_params.append(('yi', params['yi']))  # noqa: E501
        if '_return' in params:
            query_params.append(('return', params['_return']))  # noqa: E501
            collection_formats['return'] = 'multi'  # noqa: E501
        if 'fsi' in params:
            query_params.append(('fsi', params['fsi']))  # noqa: E501
        if 'frm' in params:
            query_params.append(('frm', params['frm']))  # noqa: E501
        if 'cha' in params:
            query_params.append(('cha', params['cha']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/systems/query', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[FloodControlSystem1]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
