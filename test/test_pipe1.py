# coding: utf-8

"""
    NLD2 API

    The <b>NLD2 API</b> is a complete, programmable interface to all National Levee Database functionality. The NLD2 API is a RESTful web service, using standard technologies like HTTP verbs, headers, and status codes.<br/><br/>The <a href=\"/#/\" target=\"_blank\">National Levee Database website</a> is built on this API, and all of its services are available for integration into your application. To get started, we recommend exploring the website to learn about the functionality that is available and then using the OpenAPI specification below to try connecting to the test/hello endpoint.<br/><br/>Currently, you can develop your application with the public API. For more advanced features, you may need an NLD account and specific government clearance, depending on the nature of the data. If you need assistance, please email us at <a href=\"mailto:NLD@usace.army.mil\">NLD@usace.army.mil</a> or call us at <a href=\"tel:18775383387\">1-877-LEVEEUS</a> (1-877-538-3387).  # noqa: E501

    OpenAPI spec version: 3.26.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.models.pipe1 import Pipe1  # noqa: E501
from swagger_client.rest import ApiException


class TestPipe1(unittest.TestCase):
    """Pipe1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPipe1(self):
        """Test Pipe1"""
        # FIXME: construct object with mandatory attributes with example values
        # model = swagger_client.models.pipe1.Pipe1()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
