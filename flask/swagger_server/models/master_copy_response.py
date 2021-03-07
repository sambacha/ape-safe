# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MasterCopyResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, address: str=None, version: str=None):  # noqa: E501
        """MasterCopyResponse - a model defined in Swagger

        :param address: The address of this MasterCopyResponse.  # noqa: E501
        :type address: str
        :param version: The version of this MasterCopyResponse.  # noqa: E501
        :type version: str
        """
        self.swagger_types = {
            'address': str,
            'version': str
        }

        self.attribute_map = {
            'address': 'address',
            'version': 'version'
        }

        self._address = address
        self._version = version

    @classmethod
    def from_dict(cls, dikt) -> 'MasterCopyResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MasterCopyResponse of this MasterCopyResponse.  # noqa: E501
        :rtype: MasterCopyResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self) -> str:
        """Gets the address of this MasterCopyResponse.


        :return: The address of this MasterCopyResponse.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this MasterCopyResponse.


        :param address: The address of this MasterCopyResponse.
        :type address: str
        """
        if address is None:
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def version(self) -> str:
        """Gets the version of this MasterCopyResponse.


        :return: The version of this MasterCopyResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this MasterCopyResponse.


        :param version: The version of this MasterCopyResponse.
        :type version: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if version is not None and len(version) < 1:
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501

        self._version = version