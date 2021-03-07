# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SafeModuleTransactionWithTransfersResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, created: datetime=None, execution_date: datetime=None, block_number: int=None, transaction_hash: str=None, safe: str=None, module: str=None, to: str=None, value: str=None, data: str=None, operation: int=None, data_decoded: str=None, transfers: List[TransferWithTokenInfoResponse]=None, tx_type: str=None):  # noqa: E501
        """SafeModuleTransactionWithTransfersResponse - a model defined in Swagger

        :param created: The created of this SafeModuleTransactionWithTransfersResponse.  # noqa: E501
        :type created: datetime
        :param execution_date: The execution_date of this SafeModuleTransactionWithTransfersResponse.  # noqa: E501
        :type execution_date: datetime
        :param block_number: The block_number of this SafeModuleTransactionWithTransfersResponse.  # noqa: E501
        :type block_number: int
        :param transaction_hash: The transaction_hash of this SafeModuleTransactionWithTransfersResponse.  # noqa: E501
        :type transaction_hash: str
        :param safe: The safe of this SafeModuleTransactionWithTransfersResponse.  # noqa: E501
        :type safe: str
        :param module: The module of this SafeModuleTransactionWithTransfersResponse.  # noqa: E501
        :type module: str
        :param to: The to of this SafeModuleTransactionWithTransfersResponse.  # noqa: E501
        :type to: str
        :param value: The value of this SafeModuleTransactionWithTransfersResponse.  # noqa: E501
        :type value: str
        :param data: The data of this SafeModuleTransactionWithTransfersResponse.  # noqa: E501
        :type data: str
        :param operation: The operation of this SafeModuleTransactionWithTransfersResponse.  # noqa: E501
        :type operation: int
        :param data_decoded: The data_decoded of this SafeModuleTransactionWithTransfersResponse.  # noqa: E501
        :type data_decoded: str
        :param transfers: The transfers of this SafeModuleTransactionWithTransfersResponse.  # noqa: E501
        :type transfers: List[TransferWithTokenInfoResponse]
        :param tx_type: The tx_type of this SafeModuleTransactionWithTransfersResponse.  # noqa: E501
        :type tx_type: str
        """
        self.swagger_types = {
            'created': datetime,
            'execution_date': datetime,
            'block_number': int,
            'transaction_hash': str,
            'safe': str,
            'module': str,
            'to': str,
            'value': str,
            'data': str,
            'operation': int,
            'data_decoded': str,
            'transfers': List[TransferWithTokenInfoResponse],
            'tx_type': str
        }

        self.attribute_map = {
            'created': 'created',
            'execution_date': 'executionDate',
            'block_number': 'blockNumber',
            'transaction_hash': 'transactionHash',
            'safe': 'safe',
            'module': 'module',
            'to': 'to',
            'value': 'value',
            'data': 'data',
            'operation': 'operation',
            'data_decoded': 'dataDecoded',
            'transfers': 'transfers',
            'tx_type': 'txType'
        }

        self._created = created
        self._execution_date = execution_date
        self._block_number = block_number
        self._transaction_hash = transaction_hash
        self._safe = safe
        self._module = module
        self._to = to
        self._value = value
        self._data = data
        self._operation = operation
        self._data_decoded = data_decoded
        self._transfers = transfers
        self._tx_type = tx_type

    @classmethod
    def from_dict(cls, dikt) -> 'SafeModuleTransactionWithTransfersResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SafeModuleTransactionWithTransfersResponse of this SafeModuleTransactionWithTransfersResponse.  # noqa: E501
        :rtype: SafeModuleTransactionWithTransfersResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created(self) -> datetime:
        """Gets the created of this SafeModuleTransactionWithTransfersResponse.


        :return: The created of this SafeModuleTransactionWithTransfersResponse.
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created: datetime):
        """Sets the created of this SafeModuleTransactionWithTransfersResponse.


        :param created: The created of this SafeModuleTransactionWithTransfersResponse.
        :type created: datetime
        """

        self._created = created

    @property
    def execution_date(self) -> datetime:
        """Gets the execution_date of this SafeModuleTransactionWithTransfersResponse.


        :return: The execution_date of this SafeModuleTransactionWithTransfersResponse.
        :rtype: datetime
        """
        return self._execution_date

    @execution_date.setter
    def execution_date(self, execution_date: datetime):
        """Sets the execution_date of this SafeModuleTransactionWithTransfersResponse.


        :param execution_date: The execution_date of this SafeModuleTransactionWithTransfersResponse.
        :type execution_date: datetime
        """
        if execution_date is None:
            raise ValueError("Invalid value for `execution_date`, must not be `None`")  # noqa: E501

        self._execution_date = execution_date

    @property
    def block_number(self) -> int:
        """Gets the block_number of this SafeModuleTransactionWithTransfersResponse.


        :return: The block_number of this SafeModuleTransactionWithTransfersResponse.
        :rtype: int
        """
        return self._block_number

    @block_number.setter
    def block_number(self, block_number: int):
        """Sets the block_number of this SafeModuleTransactionWithTransfersResponse.


        :param block_number: The block_number of this SafeModuleTransactionWithTransfersResponse.
        :type block_number: int
        """

        self._block_number = block_number

    @property
    def transaction_hash(self) -> str:
        """Gets the transaction_hash of this SafeModuleTransactionWithTransfersResponse.


        :return: The transaction_hash of this SafeModuleTransactionWithTransfersResponse.
        :rtype: str
        """
        return self._transaction_hash

    @transaction_hash.setter
    def transaction_hash(self, transaction_hash: str):
        """Sets the transaction_hash of this SafeModuleTransactionWithTransfersResponse.


        :param transaction_hash: The transaction_hash of this SafeModuleTransactionWithTransfersResponse.
        :type transaction_hash: str
        """

        self._transaction_hash = transaction_hash

    @property
    def safe(self) -> str:
        """Gets the safe of this SafeModuleTransactionWithTransfersResponse.


        :return: The safe of this SafeModuleTransactionWithTransfersResponse.
        :rtype: str
        """
        return self._safe

    @safe.setter
    def safe(self, safe: str):
        """Sets the safe of this SafeModuleTransactionWithTransfersResponse.


        :param safe: The safe of this SafeModuleTransactionWithTransfersResponse.
        :type safe: str
        """
        if safe is None:
            raise ValueError("Invalid value for `safe`, must not be `None`")  # noqa: E501
        if safe is not None and len(safe) > 42:
            raise ValueError("Invalid value for `safe`, length must be less than or equal to `42`")  # noqa: E501
        if safe is not None and len(safe) < 1:
            raise ValueError("Invalid value for `safe`, length must be greater than or equal to `1`")  # noqa: E501

        self._safe = safe

    @property
    def module(self) -> str:
        """Gets the module of this SafeModuleTransactionWithTransfersResponse.


        :return: The module of this SafeModuleTransactionWithTransfersResponse.
        :rtype: str
        """
        return self._module

    @module.setter
    def module(self, module: str):
        """Sets the module of this SafeModuleTransactionWithTransfersResponse.


        :param module: The module of this SafeModuleTransactionWithTransfersResponse.
        :type module: str
        """
        if module is None:
            raise ValueError("Invalid value for `module`, must not be `None`")  # noqa: E501
        if module is not None and len(module) > 42:
            raise ValueError("Invalid value for `module`, length must be less than or equal to `42`")  # noqa: E501
        if module is not None and len(module) < 1:
            raise ValueError("Invalid value for `module`, length must be greater than or equal to `1`")  # noqa: E501

        self._module = module

    @property
    def to(self) -> str:
        """Gets the to of this SafeModuleTransactionWithTransfersResponse.


        :return: The to of this SafeModuleTransactionWithTransfersResponse.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to: str):
        """Sets the to of this SafeModuleTransactionWithTransfersResponse.


        :param to: The to of this SafeModuleTransactionWithTransfersResponse.
        :type to: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501
        if to is not None and len(to) > 42:
            raise ValueError("Invalid value for `to`, length must be less than or equal to `42`")  # noqa: E501
        if to is not None and len(to) < 1:
            raise ValueError("Invalid value for `to`, length must be greater than or equal to `1`")  # noqa: E501

        self._to = to

    @property
    def value(self) -> str:
        """Gets the value of this SafeModuleTransactionWithTransfersResponse.


        :return: The value of this SafeModuleTransactionWithTransfersResponse.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this SafeModuleTransactionWithTransfersResponse.


        :param value: The value of this SafeModuleTransactionWithTransfersResponse.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501

        self._value = value

    @property
    def data(self) -> str:
        """Gets the data of this SafeModuleTransactionWithTransfersResponse.


        :return: The data of this SafeModuleTransactionWithTransfersResponse.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data: str):
        """Sets the data of this SafeModuleTransactionWithTransfersResponse.


        :param data: The data of this SafeModuleTransactionWithTransfersResponse.
        :type data: str
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")  # noqa: E501

        self._data = data

    @property
    def operation(self) -> int:
        """Gets the operation of this SafeModuleTransactionWithTransfersResponse.


        :return: The operation of this SafeModuleTransactionWithTransfersResponse.
        :rtype: int
        """
        return self._operation

    @operation.setter
    def operation(self, operation: int):
        """Sets the operation of this SafeModuleTransactionWithTransfersResponse.


        :param operation: The operation of this SafeModuleTransactionWithTransfersResponse.
        :type operation: int
        """
        if operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501

        self._operation = operation

    @property
    def data_decoded(self) -> str:
        """Gets the data_decoded of this SafeModuleTransactionWithTransfersResponse.


        :return: The data_decoded of this SafeModuleTransactionWithTransfersResponse.
        :rtype: str
        """
        return self._data_decoded

    @data_decoded.setter
    def data_decoded(self, data_decoded: str):
        """Sets the data_decoded of this SafeModuleTransactionWithTransfersResponse.


        :param data_decoded: The data_decoded of this SafeModuleTransactionWithTransfersResponse.
        :type data_decoded: str
        """

        self._data_decoded = data_decoded

    @property
    def transfers(self) -> List[TransferWithTokenInfoResponse]:
        """Gets the transfers of this SafeModuleTransactionWithTransfersResponse.


        :return: The transfers of this SafeModuleTransactionWithTransfersResponse.
        :rtype: List[TransferWithTokenInfoResponse]
        """
        return self._transfers

    @transfers.setter
    def transfers(self, transfers: List[TransferWithTokenInfoResponse]):
        """Sets the transfers of this SafeModuleTransactionWithTransfersResponse.


        :param transfers: The transfers of this SafeModuleTransactionWithTransfersResponse.
        :type transfers: List[TransferWithTokenInfoResponse]
        """
        if transfers is None:
            raise ValueError("Invalid value for `transfers`, must not be `None`")  # noqa: E501

        self._transfers = transfers

    @property
    def tx_type(self) -> str:
        """Gets the tx_type of this SafeModuleTransactionWithTransfersResponse.


        :return: The tx_type of this SafeModuleTransactionWithTransfersResponse.
        :rtype: str
        """
        return self._tx_type

    @tx_type.setter
    def tx_type(self, tx_type: str):
        """Sets the tx_type of this SafeModuleTransactionWithTransfersResponse.


        :param tx_type: The tx_type of this SafeModuleTransactionWithTransfersResponse.
        :type tx_type: str
        """

        self._tx_type = tx_type