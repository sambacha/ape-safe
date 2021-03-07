# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class TransferResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, type: str=None, execution_date: datetime=None, block_number: int=None, transaction_hash: str=None, to: str=None, value: str=None, token_id: str=None, token_address: str=None, _from: str=None):  # noqa: E501
        """TransferResponse - a model defined in Swagger

        :param type: The type of this TransferResponse.  # noqa: E501
        :type type: str
        :param execution_date: The execution_date of this TransferResponse.  # noqa: E501
        :type execution_date: datetime
        :param block_number: The block_number of this TransferResponse.  # noqa: E501
        :type block_number: int
        :param transaction_hash: The transaction_hash of this TransferResponse.  # noqa: E501
        :type transaction_hash: str
        :param to: The to of this TransferResponse.  # noqa: E501
        :type to: str
        :param value: The value of this TransferResponse.  # noqa: E501
        :type value: str
        :param token_id: The token_id of this TransferResponse.  # noqa: E501
        :type token_id: str
        :param token_address: The token_address of this TransferResponse.  # noqa: E501
        :type token_address: str
        :param _from: The _from of this TransferResponse.  # noqa: E501
        :type _from: str
        """
        self.swagger_types = {
            'type': str,
            'execution_date': datetime,
            'block_number': int,
            'transaction_hash': str,
            'to': str,
            'value': str,
            'token_id': str,
            'token_address': str,
            '_from': str
        }

        self.attribute_map = {
            'type': 'type',
            'execution_date': 'executionDate',
            'block_number': 'blockNumber',
            'transaction_hash': 'transactionHash',
            'to': 'to',
            'value': 'value',
            'token_id': 'tokenId',
            'token_address': 'tokenAddress',
            '_from': 'from'
        }

        self._type = type
        self._execution_date = execution_date
        self._block_number = block_number
        self._transaction_hash = transaction_hash
        self._to = to
        self._value = value
        self._token_id = token_id
        self._token_address = token_address
        self.__from = _from

    @classmethod
    def from_dict(cls, dikt) -> 'TransferResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TransferResponse of this TransferResponse.  # noqa: E501
        :rtype: TransferResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this TransferResponse.


        :return: The type of this TransferResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this TransferResponse.


        :param type: The type of this TransferResponse.
        :type type: str
        """

        self._type = type

    @property
    def execution_date(self) -> datetime:
        """Gets the execution_date of this TransferResponse.


        :return: The execution_date of this TransferResponse.
        :rtype: datetime
        """
        return self._execution_date

    @execution_date.setter
    def execution_date(self, execution_date: datetime):
        """Sets the execution_date of this TransferResponse.


        :param execution_date: The execution_date of this TransferResponse.
        :type execution_date: datetime
        """
        if execution_date is None:
            raise ValueError("Invalid value for `execution_date`, must not be `None`")  # noqa: E501

        self._execution_date = execution_date

    @property
    def block_number(self) -> int:
        """Gets the block_number of this TransferResponse.


        :return: The block_number of this TransferResponse.
        :rtype: int
        """
        return self._block_number

    @block_number.setter
    def block_number(self, block_number: int):
        """Sets the block_number of this TransferResponse.


        :param block_number: The block_number of this TransferResponse.
        :type block_number: int
        """
        if block_number is None:
            raise ValueError("Invalid value for `block_number`, must not be `None`")  # noqa: E501

        self._block_number = block_number

    @property
    def transaction_hash(self) -> str:
        """Gets the transaction_hash of this TransferResponse.


        :return: The transaction_hash of this TransferResponse.
        :rtype: str
        """
        return self._transaction_hash

    @transaction_hash.setter
    def transaction_hash(self, transaction_hash: str):
        """Sets the transaction_hash of this TransferResponse.


        :param transaction_hash: The transaction_hash of this TransferResponse.
        :type transaction_hash: str
        """
        if transaction_hash is None:
            raise ValueError("Invalid value for `transaction_hash`, must not be `None`")  # noqa: E501

        self._transaction_hash = transaction_hash

    @property
    def to(self) -> str:
        """Gets the to of this TransferResponse.


        :return: The to of this TransferResponse.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to: str):
        """Sets the to of this TransferResponse.


        :param to: The to of this TransferResponse.
        :type to: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def value(self) -> str:
        """Gets the value of this TransferResponse.


        :return: The value of this TransferResponse.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this TransferResponse.


        :param value: The value of this TransferResponse.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if value is not None and len(value) < 1:
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  # noqa: E501

        self._value = value

    @property
    def token_id(self) -> str:
        """Gets the token_id of this TransferResponse.


        :return: The token_id of this TransferResponse.
        :rtype: str
        """
        return self._token_id

    @token_id.setter
    def token_id(self, token_id: str):
        """Sets the token_id of this TransferResponse.


        :param token_id: The token_id of this TransferResponse.
        :type token_id: str
        """
        if token_id is None:
            raise ValueError("Invalid value for `token_id`, must not be `None`")  # noqa: E501
        if token_id is not None and len(token_id) < 1:
            raise ValueError("Invalid value for `token_id`, length must be greater than or equal to `1`")  # noqa: E501

        self._token_id = token_id

    @property
    def token_address(self) -> str:
        """Gets the token_address of this TransferResponse.


        :return: The token_address of this TransferResponse.
        :rtype: str
        """
        return self._token_address

    @token_address.setter
    def token_address(self, token_address: str):
        """Sets the token_address of this TransferResponse.


        :param token_address: The token_address of this TransferResponse.
        :type token_address: str
        """

        self._token_address = token_address

    @property
    def _from(self) -> str:
        """Gets the _from of this TransferResponse.


        :return: The _from of this TransferResponse.
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from: str):
        """Sets the _from of this TransferResponse.


        :param _from: The _from of this TransferResponse.
        :type _from: str
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from
