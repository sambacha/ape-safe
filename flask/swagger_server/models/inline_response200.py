# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, next: str=None, previous: str=None, results: List[AnalyticsMultisigTxsBySafeResponse]=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param count: The count of this InlineResponse200.  # noqa: E501
        :type count: int
        :param next: The next of this InlineResponse200.  # noqa: E501
        :type next: str
        :param previous: The previous of this InlineResponse200.  # noqa: E501
        :type previous: str
        :param results: The results of this InlineResponse200.  # noqa: E501
        :type results: List[AnalyticsMultisigTxsBySafeResponse]
        """
        self.swagger_types = {
            'count': int,
            'next': str,
            'previous': str,
            'results': List[AnalyticsMultisigTxsBySafeResponse]
        }

        self.attribute_map = {
            'count': 'count',
            'next': 'next',
            'previous': 'previous',
            'results': 'results'
        }

        self._count = count
        self._next = next
        self._previous = previous
        self._results = results

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self) -> int:
        """Gets the count of this InlineResponse200.


        :return: The count of this InlineResponse200.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int):
        """Sets the count of this InlineResponse200.


        :param count: The count of this InlineResponse200.
        :type count: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def next(self) -> str:
        """Gets the next of this InlineResponse200.


        :return: The next of this InlineResponse200.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next: str):
        """Sets the next of this InlineResponse200.


        :param next: The next of this InlineResponse200.
        :type next: str
        """

        self._next = next

    @property
    def previous(self) -> str:
        """Gets the previous of this InlineResponse200.


        :return: The previous of this InlineResponse200.
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous: str):
        """Sets the previous of this InlineResponse200.


        :param previous: The previous of this InlineResponse200.
        :type previous: str
        """

        self._previous = previous

    @property
    def results(self) -> List[AnalyticsMultisigTxsBySafeResponse]:
        """Gets the results of this InlineResponse200.


        :return: The results of this InlineResponse200.
        :rtype: List[AnalyticsMultisigTxsBySafeResponse]
        """
        return self._results

    @results.setter
    def results(self, results: List[AnalyticsMultisigTxsBySafeResponse]):
        """Sets the results of this InlineResponse200.


        :param results: The results of this InlineResponse200.
        :type results: List[AnalyticsMultisigTxsBySafeResponse]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results