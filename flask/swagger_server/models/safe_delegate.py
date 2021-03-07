# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SafeDelegate(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, safe: str=None, delegate: str=None, signature: str=None, label: str=None):  # noqa: E501
        """SafeDelegate - a model defined in Swagger

        :param safe: The safe of this SafeDelegate.  # noqa: E501
        :type safe: str
        :param delegate: The delegate of this SafeDelegate.  # noqa: E501
        :type delegate: str
        :param signature: The signature of this SafeDelegate.  # noqa: E501
        :type signature: str
        :param label: The label of this SafeDelegate.  # noqa: E501
        :type label: str
        """
        self.swagger_types = {
            'safe': str,
            'delegate': str,
            'signature': str,
            'label': str
        }

        self.attribute_map = {
            'safe': 'safe',
            'delegate': 'delegate',
            'signature': 'signature',
            'label': 'label'
        }

        self._safe = safe
        self._delegate = delegate
        self._signature = signature
        self._label = label

    @classmethod
    def from_dict(cls, dikt) -> 'SafeDelegate':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SafeDelegate of this SafeDelegate.  # noqa: E501
        :rtype: SafeDelegate
        """
        return util.deserialize_model(dikt, cls)

    @property
    def safe(self) -> str:
        """Gets the safe of this SafeDelegate.


        :return: The safe of this SafeDelegate.
        :rtype: str
        """
        return self._safe

    @safe.setter
    def safe(self, safe: str):
        """Sets the safe of this SafeDelegate.


        :param safe: The safe of this SafeDelegate.
        :type safe: str
        """
        if safe is None:
            raise ValueError("Invalid value for `safe`, must not be `None`")  # noqa: E501

        self._safe = safe

    @property
    def delegate(self) -> str:
        """Gets the delegate of this SafeDelegate.


        :return: The delegate of this SafeDelegate.
        :rtype: str
        """
        return self._delegate

    @delegate.setter
    def delegate(self, delegate: str):
        """Sets the delegate of this SafeDelegate.


        :param delegate: The delegate of this SafeDelegate.
        :type delegate: str
        """
        if delegate is None:
            raise ValueError("Invalid value for `delegate`, must not be `None`")  # noqa: E501

        self._delegate = delegate

    @property
    def signature(self) -> str:
        """Gets the signature of this SafeDelegate.


        :return: The signature of this SafeDelegate.
        :rtype: str
        """
        return self._signature

    @signature.setter
    def signature(self, signature: str):
        """Sets the signature of this SafeDelegate.


        :param signature: The signature of this SafeDelegate.
        :type signature: str
        """
        if signature is None:
            raise ValueError("Invalid value for `signature`, must not be `None`")  # noqa: E501

        self._signature = signature

    @property
    def label(self) -> str:
        """Gets the label of this SafeDelegate.


        :return: The label of this SafeDelegate.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label: str):
        """Sets the label of this SafeDelegate.


        :param label: The label of this SafeDelegate.
        :type label: str
        """
        if label is None:
            raise ValueError("Invalid value for `label`, must not be `None`")  # noqa: E501
        if label is not None and len(label) > 50:
            raise ValueError("Invalid value for `label`, length must be less than or equal to `50`")  # noqa: E501
        if label is not None and len(label) < 1:
            raise ValueError("Invalid value for `label`, length must be greater than or equal to `1`")  # noqa: E501

        self._label = label