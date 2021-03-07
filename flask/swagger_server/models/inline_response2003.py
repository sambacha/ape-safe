# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse2003(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, count: int=None, next: str=None, previous: str=None, results: List[SafeDelegateResponse]=None):  # noqa: E501
        """InlineResponse2003 - a model defined in Swagger

        :param count: The count of this InlineResponse2003.  # noqa: E501
        :type count: int
        :param next: The next of this InlineResponse2003.  # noqa: E501
        :type next: str
        :param previous: The previous of this InlineResponse2003.  # noqa: E501
        :type previous: str
        :param results: The results of this InlineResponse2003.  # noqa: E501
        :type results: List[SafeDelegateResponse]
        """
        self.swagger_types = {
            'count': int,
            'next': str,
            'previous': str,
            'results': List[SafeDelegateResponse]
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
    def from_dict(cls, dikt) -> 'InlineResponse2003':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200_3 of this InlineResponse2003.  # noqa: E501
        :rtype: InlineResponse2003
        """
        return util.deserialize_model(dikt, cls)

    @property
    def count(self) -> int:
        """Gets the count of this InlineResponse2003.


        :return: The count of this InlineResponse2003.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int):
        """Sets the count of this InlineResponse2003.


        :param count: The count of this InlineResponse2003.
        :type count: int
        """
        if count is None:
            raise ValueError("Invalid value for `count`, must not be `None`")  # noqa: E501

        self._count = count

    @property
    def next(self) -> str:
        """Gets the next of this InlineResponse2003.


        :return: The next of this InlineResponse2003.
        :rtype: str
        """
        return self._next

    @next.setter
    def next(self, next: str):
        """Sets the next of this InlineResponse2003.


        :param next: The next of this InlineResponse2003.
        :type next: str
        """

        self._next = next

    @property
    def previous(self) -> str:
        """Gets the previous of this InlineResponse2003.


        :return: The previous of this InlineResponse2003.
        :rtype: str
        """
        return self._previous

    @previous.setter
    def previous(self, previous: str):
        """Sets the previous of this InlineResponse2003.


        :param previous: The previous of this InlineResponse2003.
        :type previous: str
        """

        self._previous = previous

    @property
    def results(self) -> List[SafeDelegateResponse]:
        """Gets the results of this InlineResponse2003.


        :return: The results of this InlineResponse2003.
        :rtype: List[SafeDelegateResponse]
        """
        return self._results

    @results.setter
    def results(self, results: List[SafeDelegateResponse]):
        """Sets the results of this InlineResponse2003.


        :param results: The results of this InlineResponse2003.
        :type results: List[SafeDelegateResponse]
        """
        if results is None:
            raise ValueError("Invalid value for `results`, must not be `None`")  # noqa: E501

        self._results = results
