# coding: utf-8

"""
    NLD2 API

    The <b>NLD2 API</b> is a complete, programmable interface to all National Levee Database functionality. The NLD2 API is a RESTful web service, using standard technologies like HTTP verbs, headers, and status codes.<br/><br/>The <a href=\"/#/\" target=\"_blank\">National Levee Database website</a> is built on this API, and all of its services are available for integration into your application. To get started, we recommend exploring the website to learn about the functionality that is available and then using the OpenAPI specification below to try connecting to the test/hello endpoint.<br/><br/>Currently, you can develop your application with the public API. For more advanced features, you may need an NLD account and specific government clearance, depending on the nature of the data. If you need assistance, please email us at <a href=\"mailto:NLD@usace.army.mil\">NLD@usace.army.mil</a> or call us at <a href=\"tel:18775383387\">1-877-LEVEEUS</a> (1-877-538-3387).  # noqa: E501

    OpenAPI spec version: 3.26.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from swagger_client.configuration import Configuration


class FemaSystemInfo(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'geometry': 'object',
        'huc8': 'list[str]',
        'congdist': 'list[str]'
    }

    attribute_map = {
        'geometry': 'geometry',
        'huc8': 'huc8',
        'congdist': 'congdist'
    }

    def __init__(self, geometry=None, huc8=None, congdist=None, _configuration=None):  # noqa: E501
        """FemaSystemInfo - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._geometry = None
        self._huc8 = None
        self._congdist = None
        self.discriminator = None

        if geometry is not None:
            self.geometry = geometry
        if huc8 is not None:
            self.huc8 = huc8
        if congdist is not None:
            self.congdist = congdist

    @property
    def geometry(self):
        """Gets the geometry of this FemaSystemInfo.  # noqa: E501


        :return: The geometry of this FemaSystemInfo.  # noqa: E501
        :rtype: object
        """
        return self._geometry

    @geometry.setter
    def geometry(self, geometry):
        """Sets the geometry of this FemaSystemInfo.


        :param geometry: The geometry of this FemaSystemInfo.  # noqa: E501
        :type: object
        """

        self._geometry = geometry

    @property
    def huc8(self):
        """Gets the huc8 of this FemaSystemInfo.  # noqa: E501


        :return: The huc8 of this FemaSystemInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._huc8

    @huc8.setter
    def huc8(self, huc8):
        """Sets the huc8 of this FemaSystemInfo.


        :param huc8: The huc8 of this FemaSystemInfo.  # noqa: E501
        :type: list[str]
        """

        self._huc8 = huc8

    @property
    def congdist(self):
        """Gets the congdist of this FemaSystemInfo.  # noqa: E501


        :return: The congdist of this FemaSystemInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._congdist

    @congdist.setter
    def congdist(self, congdist):
        """Sets the congdist of this FemaSystemInfo.


        :param congdist: The congdist of this FemaSystemInfo.  # noqa: E501
        :type: list[str]
        """

        self._congdist = congdist

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(FemaSystemInfo, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, FemaSystemInfo):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FemaSystemInfo):
            return True

        return self.to_dict() != other.to_dict()
