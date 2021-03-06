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


class FlowAnalysisRequest(object):
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
        'control_path': 'bool',
        'dest_ip': 'str',
        'dest_port': 'str',
        'inclusions': 'list[str]',
        'periodic_refresh': 'bool',
        'protocol': 'str',
        'source_ip': 'str',
        'source_port': 'str'
    }

    attribute_map = {
        'control_path': 'controlPath',
        'dest_ip': 'destIP',
        'dest_port': 'destPort',
        'inclusions': 'inclusions',
        'periodic_refresh': 'periodicRefresh',
        'protocol': 'protocol',
        'source_ip': 'sourceIP',
        'source_port': 'sourcePort'
    }

    def __init__(self, control_path=None, dest_ip=None, dest_port=None, inclusions=None, periodic_refresh=None, protocol=None, source_ip=None, source_port=None):  # noqa: E501
        """FlowAnalysisRequest - a model defined in Swagger"""  # noqa: E501

        self._control_path = None
        self._dest_ip = None
        self._dest_port = None
        self._inclusions = None
        self._periodic_refresh = None
        self._protocol = None
        self._source_ip = None
        self._source_port = None
        self.discriminator = None

        if control_path is not None:
            self.control_path = control_path
        if dest_ip is not None:
            self.dest_ip = dest_ip
        if dest_port is not None:
            self.dest_port = dest_port
        if inclusions is not None:
            self.inclusions = inclusions
        if periodic_refresh is not None:
            self.periodic_refresh = periodic_refresh
        if protocol is not None:
            self.protocol = protocol
        if source_ip is not None:
            self.source_ip = source_ip
        if source_port is not None:
            self.source_port = source_port

    @property
    def control_path(self):
        """Gets the control_path of this FlowAnalysisRequest.  # noqa: E501


        :return: The control_path of this FlowAnalysisRequest.  # noqa: E501
        :rtype: bool
        """
        return self._control_path

    @control_path.setter
    def control_path(self, control_path):
        """Sets the control_path of this FlowAnalysisRequest.


        :param control_path: The control_path of this FlowAnalysisRequest.  # noqa: E501
        :type: bool
        """

        self._control_path = control_path

    @property
    def dest_ip(self):
        """Gets the dest_ip of this FlowAnalysisRequest.  # noqa: E501


        :return: The dest_ip of this FlowAnalysisRequest.  # noqa: E501
        :rtype: str
        """
        return self._dest_ip

    @dest_ip.setter
    def dest_ip(self, dest_ip):
        """Sets the dest_ip of this FlowAnalysisRequest.


        :param dest_ip: The dest_ip of this FlowAnalysisRequest.  # noqa: E501
        :type: str
        """

        self._dest_ip = dest_ip

    @property
    def dest_port(self):
        """Gets the dest_port of this FlowAnalysisRequest.  # noqa: E501


        :return: The dest_port of this FlowAnalysisRequest.  # noqa: E501
        :rtype: str
        """
        return self._dest_port

    @dest_port.setter
    def dest_port(self, dest_port):
        """Sets the dest_port of this FlowAnalysisRequest.


        :param dest_port: The dest_port of this FlowAnalysisRequest.  # noqa: E501
        :type: str
        """

        self._dest_port = dest_port

    @property
    def inclusions(self):
        """Gets the inclusions of this FlowAnalysisRequest.  # noqa: E501


        :return: The inclusions of this FlowAnalysisRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._inclusions

    @inclusions.setter
    def inclusions(self, inclusions):
        """Sets the inclusions of this FlowAnalysisRequest.


        :param inclusions: The inclusions of this FlowAnalysisRequest.  # noqa: E501
        :type: list[str]
        """

        self._inclusions = inclusions

    @property
    def periodic_refresh(self):
        """Gets the periodic_refresh of this FlowAnalysisRequest.  # noqa: E501


        :return: The periodic_refresh of this FlowAnalysisRequest.  # noqa: E501
        :rtype: bool
        """
        return self._periodic_refresh

    @periodic_refresh.setter
    def periodic_refresh(self, periodic_refresh):
        """Sets the periodic_refresh of this FlowAnalysisRequest.


        :param periodic_refresh: The periodic_refresh of this FlowAnalysisRequest.  # noqa: E501
        :type: bool
        """

        self._periodic_refresh = periodic_refresh

    @property
    def protocol(self):
        """Gets the protocol of this FlowAnalysisRequest.  # noqa: E501


        :return: The protocol of this FlowAnalysisRequest.  # noqa: E501
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this FlowAnalysisRequest.


        :param protocol: The protocol of this FlowAnalysisRequest.  # noqa: E501
        :type: str
        """

        self._protocol = protocol

    @property
    def source_ip(self):
        """Gets the source_ip of this FlowAnalysisRequest.  # noqa: E501


        :return: The source_ip of this FlowAnalysisRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_ip

    @source_ip.setter
    def source_ip(self, source_ip):
        """Sets the source_ip of this FlowAnalysisRequest.


        :param source_ip: The source_ip of this FlowAnalysisRequest.  # noqa: E501
        :type: str
        """

        self._source_ip = source_ip

    @property
    def source_port(self):
        """Gets the source_port of this FlowAnalysisRequest.  # noqa: E501


        :return: The source_port of this FlowAnalysisRequest.  # noqa: E501
        :rtype: str
        """
        return self._source_port

    @source_port.setter
    def source_port(self, source_port):
        """Sets the source_port of this FlowAnalysisRequest.


        :param source_port: The source_port of this FlowAnalysisRequest.  # noqa: E501
        :type: str
        """

        self._source_port = source_port

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
        if not isinstance(other, FlowAnalysisRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
