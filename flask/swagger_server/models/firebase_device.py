# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class FirebaseDevice(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, uuid: str=None, safes: List[str]=None, cloud_messaging_token: str=None, build_number: int=None, bundle: str=None, device_type: str=None, version: str=None, timestamp: int=None, signatures: List[str]=None):  # noqa: E501
        """FirebaseDevice - a model defined in Swagger

        :param uuid: The uuid of this FirebaseDevice.  # noqa: E501
        :type uuid: str
        :param safes: The safes of this FirebaseDevice.  # noqa: E501
        :type safes: List[str]
        :param cloud_messaging_token: The cloud_messaging_token of this FirebaseDevice.  # noqa: E501
        :type cloud_messaging_token: str
        :param build_number: The build_number of this FirebaseDevice.  # noqa: E501
        :type build_number: int
        :param bundle: The bundle of this FirebaseDevice.  # noqa: E501
        :type bundle: str
        :param device_type: The device_type of this FirebaseDevice.  # noqa: E501
        :type device_type: str
        :param version: The version of this FirebaseDevice.  # noqa: E501
        :type version: str
        :param timestamp: The timestamp of this FirebaseDevice.  # noqa: E501
        :type timestamp: int
        :param signatures: The signatures of this FirebaseDevice.  # noqa: E501
        :type signatures: List[str]
        """
        self.swagger_types = {
            'uuid': str,
            'safes': List[str],
            'cloud_messaging_token': str,
            'build_number': int,
            'bundle': str,
            'device_type': str,
            'version': str,
            'timestamp': int,
            'signatures': List[str]
        }

        self.attribute_map = {
            'uuid': 'uuid',
            'safes': 'safes',
            'cloud_messaging_token': 'cloudMessagingToken',
            'build_number': 'buildNumber',
            'bundle': 'bundle',
            'device_type': 'deviceType',
            'version': 'version',
            'timestamp': 'timestamp',
            'signatures': 'signatures'
        }

        self._uuid = uuid
        self._safes = safes
        self._cloud_messaging_token = cloud_messaging_token
        self._build_number = build_number
        self._bundle = bundle
        self._device_type = device_type
        self._version = version
        self._timestamp = timestamp
        self._signatures = signatures

    @classmethod
    def from_dict(cls, dikt) -> 'FirebaseDevice':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FirebaseDevice of this FirebaseDevice.  # noqa: E501
        :rtype: FirebaseDevice
        """
        return util.deserialize_model(dikt, cls)

    @property
    def uuid(self) -> str:
        """Gets the uuid of this FirebaseDevice.


        :return: The uuid of this FirebaseDevice.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid: str):
        """Sets the uuid of this FirebaseDevice.


        :param uuid: The uuid of this FirebaseDevice.
        :type uuid: str
        """

        self._uuid = uuid

    @property
    def safes(self) -> List[str]:
        """Gets the safes of this FirebaseDevice.


        :return: The safes of this FirebaseDevice.
        :rtype: List[str]
        """
        return self._safes

    @safes.setter
    def safes(self, safes: List[str]):
        """Sets the safes of this FirebaseDevice.


        :param safes: The safes of this FirebaseDevice.
        :type safes: List[str]
        """
        if safes is None:
            raise ValueError("Invalid value for `safes`, must not be `None`")  # noqa: E501

        self._safes = safes

    @property
    def cloud_messaging_token(self) -> str:
        """Gets the cloud_messaging_token of this FirebaseDevice.


        :return: The cloud_messaging_token of this FirebaseDevice.
        :rtype: str
        """
        return self._cloud_messaging_token

    @cloud_messaging_token.setter
    def cloud_messaging_token(self, cloud_messaging_token: str):
        """Sets the cloud_messaging_token of this FirebaseDevice.


        :param cloud_messaging_token: The cloud_messaging_token of this FirebaseDevice.
        :type cloud_messaging_token: str
        """
        if cloud_messaging_token is None:
            raise ValueError("Invalid value for `cloud_messaging_token`, must not be `None`")  # noqa: E501
        if cloud_messaging_token is not None and len(cloud_messaging_token) > 200:
            raise ValueError("Invalid value for `cloud_messaging_token`, length must be less than or equal to `200`")  # noqa: E501
        if cloud_messaging_token is not None and len(cloud_messaging_token) < 100:
            raise ValueError("Invalid value for `cloud_messaging_token`, length must be greater than or equal to `100`")  # noqa: E501

        self._cloud_messaging_token = cloud_messaging_token

    @property
    def build_number(self) -> int:
        """Gets the build_number of this FirebaseDevice.


        :return: The build_number of this FirebaseDevice.
        :rtype: int
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number: int):
        """Sets the build_number of this FirebaseDevice.


        :param build_number: The build_number of this FirebaseDevice.
        :type build_number: int
        """
        if build_number is None:
            raise ValueError("Invalid value for `build_number`, must not be `None`")  # noqa: E501
        if build_number is not None and build_number < 0:  # noqa: E501
            raise ValueError("Invalid value for `build_number`, must be a value greater than or equal to `0`")  # noqa: E501

        self._build_number = build_number

    @property
    def bundle(self) -> str:
        """Gets the bundle of this FirebaseDevice.


        :return: The bundle of this FirebaseDevice.
        :rtype: str
        """
        return self._bundle

    @bundle.setter
    def bundle(self, bundle: str):
        """Sets the bundle of this FirebaseDevice.


        :param bundle: The bundle of this FirebaseDevice.
        :type bundle: str
        """
        if bundle is None:
            raise ValueError("Invalid value for `bundle`, must not be `None`")  # noqa: E501
        if bundle is not None and len(bundle) > 100:
            raise ValueError("Invalid value for `bundle`, length must be less than or equal to `100`")  # noqa: E501
        if bundle is not None and len(bundle) < 1:
            raise ValueError("Invalid value for `bundle`, length must be greater than or equal to `1`")  # noqa: E501

        self._bundle = bundle

    @property
    def device_type(self) -> str:
        """Gets the device_type of this FirebaseDevice.


        :return: The device_type of this FirebaseDevice.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type: str):
        """Sets the device_type of this FirebaseDevice.


        :param device_type: The device_type of this FirebaseDevice.
        :type device_type: str
        """
        allowed_values = ["ANDROID", "IOS", "WEB"]  # noqa: E501
        if device_type not in allowed_values:
            raise ValueError(
                "Invalid value for `device_type` ({0}), must be one of {1}"
                .format(device_type, allowed_values)
            )

        self._device_type = device_type

    @property
    def version(self) -> str:
        """Gets the version of this FirebaseDevice.


        :return: The version of this FirebaseDevice.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version: str):
        """Sets the version of this FirebaseDevice.


        :param version: The version of this FirebaseDevice.
        :type version: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501
        if version is not None and len(version) > 100:
            raise ValueError("Invalid value for `version`, length must be less than or equal to `100`")  # noqa: E501
        if version is not None and len(version) < 1:
            raise ValueError("Invalid value for `version`, length must be greater than or equal to `1`")  # noqa: E501

        self._version = version

    @property
    def timestamp(self) -> int:
        """Gets the timestamp of this FirebaseDevice.


        :return: The timestamp of this FirebaseDevice.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp: int):
        """Sets the timestamp of this FirebaseDevice.


        :param timestamp: The timestamp of this FirebaseDevice.
        :type timestamp: int
        """

        self._timestamp = timestamp

    @property
    def signatures(self) -> List[str]:
        """Gets the signatures of this FirebaseDevice.


        :return: The signatures of this FirebaseDevice.
        :rtype: List[str]
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures: List[str]):
        """Sets the signatures of this FirebaseDevice.


        :param signatures: The signatures of this FirebaseDevice.
        :type signatures: List[str]
        """

        self._signatures = signatures
