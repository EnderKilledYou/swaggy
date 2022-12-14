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


class PortfoliosApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_all_portfolio_systems(self, **kwargs):  # noqa: E501
        """get_all_portfolio_systems  # noqa: E501

        Gets all systems belonging to a portfolio by either system id or portfolio id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_portfolio_systems(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int portfolio_id: ID of the portfolio
        :param int system_id: ID of the system
        :param bool cached: Pull from cached flood control system
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_portfolio_systems_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_portfolio_systems_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_portfolio_systems_with_http_info(self, **kwargs):  # noqa: E501
        """get_all_portfolio_systems  # noqa: E501

        Gets all systems belonging to a portfolio by either system id or portfolio id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_portfolio_systems_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int portfolio_id: ID of the portfolio
        :param int system_id: ID of the system
        :param bool cached: Pull from cached flood control system
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['portfolio_id', 'system_id', 'cached']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_portfolio_systems" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'portfolio_id' in params:
            query_params.append(('portfolioId', params['portfolio_id']))  # noqa: E501
        if 'system_id' in params:
            query_params.append(('systemId', params['system_id']))  # noqa: E501
        if 'cached' in params:
            query_params.append(('cached', params['cached']))  # noqa: E501

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
            '/portfolio-systems', 'GET',
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

    def get_all_portfolios(self, **kwargs):  # noqa: E501
        """get_all_portfolios  # noqa: E501

        Gets all systems portfolios belonging to a user or organization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_portfolios(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int org_id: ID of the organization
        :param bool populated: Only include populated portfolios
        :param bool published: Only include published portfolios
        :return: list[Portfolio1]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_all_portfolios_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_all_portfolios_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_all_portfolios_with_http_info(self, **kwargs):  # noqa: E501
        """get_all_portfolios  # noqa: E501

        Gets all systems portfolios belonging to a user or organization  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_portfolios_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int org_id: ID of the organization
        :param bool populated: Only include populated portfolios
        :param bool published: Only include published portfolios
        :return: list[Portfolio1]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['org_id', 'populated', 'published']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all_portfolios" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'org_id' in params:
            query_params.append(('orgId', params['org_id']))  # noqa: E501
        if 'populated' in params:
            query_params.append(('populated', params['populated']))  # noqa: E501
        if 'published' in params:
            query_params.append(('published', params['published']))  # noqa: E501

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
            '/portfolio', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Portfolio1]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_system_ids(self, id, **kwargs):  # noqa: E501
        """get_system_ids  # noqa: E501

        Gets all system IDs belonging to a portfolio  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_system_ids(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: ID of the portfolio (required)
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_system_ids_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_system_ids_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_system_ids_with_http_info(self, id, **kwargs):  # noqa: E501
        """get_system_ids  # noqa: E501

        Gets all system IDs belonging to a portfolio  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_system_ids_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: ID of the portfolio (required)
        :return: list[int]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_system_ids" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `get_system_ids`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/portfolio-system-ids/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[int]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def portfolio_id_get(self, id, **kwargs):  # noqa: E501
        """portfolio_id_get  # noqa: E501

        Gets a portfolio  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.portfolio_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: ID of portfolio (required)
        :return: Portfolio1
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.portfolio_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.portfolio_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def portfolio_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """portfolio_id_get  # noqa: E501

        Gets a portfolio  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.portfolio_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: ID of portfolio (required)
        :return: Portfolio1
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method portfolio_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `portfolio_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/portfolio/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Portfolio1',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def portfolio_system_id_get(self, id, **kwargs):  # noqa: E501
        """portfolio_system_id_get  # noqa: E501

        Gets a single portfolio system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.portfolio_system_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: ID of the portfolio system (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.portfolio_system_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.portfolio_system_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def portfolio_system_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """portfolio_system_id_get  # noqa: E501

        Gets a single portfolio system  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.portfolio_system_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: ID of the portfolio system (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method portfolio_system_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if self.api_client.client_side_validation and ('id' not in params or
                                                       params['id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `id` when calling `portfolio_system_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/portfolio-system/{id}', 'GET',
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
