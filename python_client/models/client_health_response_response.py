# coding: utf-8

"""
    Swagger

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from python_client.models.client_health_response_score_detail import ClientHealthResponseScoreDetail  # noqa: F401,E501


class ClientHealthResponseResponse(object):
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
        'site_id': 'str',
        'score_detail': 'list[ClientHealthResponseScoreDetail]'
    }

    attribute_map = {
        'site_id': 'siteId',
        'score_detail': 'scoreDetail'
    }

    def __init__(self, site_id=None, score_detail=None):  # noqa: E501
        """ClientHealthResponseResponse - a model defined in Swagger"""  # noqa: E501

        self._site_id = None
        self._score_detail = None
        self.discriminator = None

        if site_id is not None:
            self.site_id = site_id
        if score_detail is not None:
            self.score_detail = score_detail

    @property
    def site_id(self):
        """Gets the site_id of this ClientHealthResponseResponse.  # noqa: E501


        :return: The site_id of this ClientHealthResponseResponse.  # noqa: E501
        :rtype: str
        """
        return self._site_id

    @site_id.setter
    def site_id(self, site_id):
        """Sets the site_id of this ClientHealthResponseResponse.


        :param site_id: The site_id of this ClientHealthResponseResponse.  # noqa: E501
        :type: str
        """

        self._site_id = site_id

    @property
    def score_detail(self):
        """Gets the score_detail of this ClientHealthResponseResponse.  # noqa: E501


        :return: The score_detail of this ClientHealthResponseResponse.  # noqa: E501
        :rtype: list[ClientHealthResponseScoreDetail]
        """
        return self._score_detail

    @score_detail.setter
    def score_detail(self, score_detail):
        """Sets the score_detail of this ClientHealthResponseResponse.


        :param score_detail: The score_detail of this ClientHealthResponseResponse.  # noqa: E501
        :type: list[ClientHealthResponseScoreDetail]
        """

        self._score_detail = score_detail

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ClientHealthResponseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
