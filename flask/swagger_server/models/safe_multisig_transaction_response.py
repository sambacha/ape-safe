# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class SafeMultisigTransactionResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, safe: str=None, to: str=None, value: str=None, data: str=None, operation: int=None, gas_token: str=None, safe_tx_gas: int=None, base_gas: int=None, gas_price: str=None, refund_receiver: str=None, nonce: int=None, execution_date: datetime=None, submission_date: datetime=None, modified: datetime=None, block_number: int=None, transaction_hash: str=None, safe_tx_hash: str=None, executor: str=None, is_executed: bool=None, is_successful: bool=None, eth_gas_price: str=None, gas_used: int=None, fee: int=None, origin: str=None, data_decoded: str=None, confirmations_required: int=None, confirmations: str=None, signatures: str=None):  # noqa: E501
        """SafeMultisigTransactionResponse - a model defined in Swagger

        :param safe: The safe of this SafeMultisigTransactionResponse.  # noqa: E501
        :type safe: str
        :param to: The to of this SafeMultisigTransactionResponse.  # noqa: E501
        :type to: str
        :param value: The value of this SafeMultisigTransactionResponse.  # noqa: E501
        :type value: str
        :param data: The data of this SafeMultisigTransactionResponse.  # noqa: E501
        :type data: str
        :param operation: The operation of this SafeMultisigTransactionResponse.  # noqa: E501
        :type operation: int
        :param gas_token: The gas_token of this SafeMultisigTransactionResponse.  # noqa: E501
        :type gas_token: str
        :param safe_tx_gas: The safe_tx_gas of this SafeMultisigTransactionResponse.  # noqa: E501
        :type safe_tx_gas: int
        :param base_gas: The base_gas of this SafeMultisigTransactionResponse.  # noqa: E501
        :type base_gas: int
        :param gas_price: The gas_price of this SafeMultisigTransactionResponse.  # noqa: E501
        :type gas_price: str
        :param refund_receiver: The refund_receiver of this SafeMultisigTransactionResponse.  # noqa: E501
        :type refund_receiver: str
        :param nonce: The nonce of this SafeMultisigTransactionResponse.  # noqa: E501
        :type nonce: int
        :param execution_date: The execution_date of this SafeMultisigTransactionResponse.  # noqa: E501
        :type execution_date: datetime
        :param submission_date: The submission_date of this SafeMultisigTransactionResponse.  # noqa: E501
        :type submission_date: datetime
        :param modified: The modified of this SafeMultisigTransactionResponse.  # noqa: E501
        :type modified: datetime
        :param block_number: The block_number of this SafeMultisigTransactionResponse.  # noqa: E501
        :type block_number: int
        :param transaction_hash: The transaction_hash of this SafeMultisigTransactionResponse.  # noqa: E501
        :type transaction_hash: str
        :param safe_tx_hash: The safe_tx_hash of this SafeMultisigTransactionResponse.  # noqa: E501
        :type safe_tx_hash: str
        :param executor: The executor of this SafeMultisigTransactionResponse.  # noqa: E501
        :type executor: str
        :param is_executed: The is_executed of this SafeMultisigTransactionResponse.  # noqa: E501
        :type is_executed: bool
        :param is_successful: The is_successful of this SafeMultisigTransactionResponse.  # noqa: E501
        :type is_successful: bool
        :param eth_gas_price: The eth_gas_price of this SafeMultisigTransactionResponse.  # noqa: E501
        :type eth_gas_price: str
        :param gas_used: The gas_used of this SafeMultisigTransactionResponse.  # noqa: E501
        :type gas_used: int
        :param fee: The fee of this SafeMultisigTransactionResponse.  # noqa: E501
        :type fee: int
        :param origin: The origin of this SafeMultisigTransactionResponse.  # noqa: E501
        :type origin: str
        :param data_decoded: The data_decoded of this SafeMultisigTransactionResponse.  # noqa: E501
        :type data_decoded: str
        :param confirmations_required: The confirmations_required of this SafeMultisigTransactionResponse.  # noqa: E501
        :type confirmations_required: int
        :param confirmations: The confirmations of this SafeMultisigTransactionResponse.  # noqa: E501
        :type confirmations: str
        :param signatures: The signatures of this SafeMultisigTransactionResponse.  # noqa: E501
        :type signatures: str
        """
        self.swagger_types = {
            'safe': str,
            'to': str,
            'value': str,
            'data': str,
            'operation': int,
            'gas_token': str,
            'safe_tx_gas': int,
            'base_gas': int,
            'gas_price': str,
            'refund_receiver': str,
            'nonce': int,
            'execution_date': datetime,
            'submission_date': datetime,
            'modified': datetime,
            'block_number': int,
            'transaction_hash': str,
            'safe_tx_hash': str,
            'executor': str,
            'is_executed': bool,
            'is_successful': bool,
            'eth_gas_price': str,
            'gas_used': int,
            'fee': int,
            'origin': str,
            'data_decoded': str,
            'confirmations_required': int,
            'confirmations': str,
            'signatures': str
        }

        self.attribute_map = {
            'safe': 'safe',
            'to': 'to',
            'value': 'value',
            'data': 'data',
            'operation': 'operation',
            'gas_token': 'gasToken',
            'safe_tx_gas': 'safeTxGas',
            'base_gas': 'baseGas',
            'gas_price': 'gasPrice',
            'refund_receiver': 'refundReceiver',
            'nonce': 'nonce',
            'execution_date': 'executionDate',
            'submission_date': 'submissionDate',
            'modified': 'modified',
            'block_number': 'blockNumber',
            'transaction_hash': 'transactionHash',
            'safe_tx_hash': 'safeTxHash',
            'executor': 'executor',
            'is_executed': 'isExecuted',
            'is_successful': 'isSuccessful',
            'eth_gas_price': 'ethGasPrice',
            'gas_used': 'gasUsed',
            'fee': 'fee',
            'origin': 'origin',
            'data_decoded': 'dataDecoded',
            'confirmations_required': 'confirmationsRequired',
            'confirmations': 'confirmations',
            'signatures': 'signatures'
        }

        self._safe = safe
        self._to = to
        self._value = value
        self._data = data
        self._operation = operation
        self._gas_token = gas_token
        self._safe_tx_gas = safe_tx_gas
        self._base_gas = base_gas
        self._gas_price = gas_price
        self._refund_receiver = refund_receiver
        self._nonce = nonce
        self._execution_date = execution_date
        self._submission_date = submission_date
        self._modified = modified
        self._block_number = block_number
        self._transaction_hash = transaction_hash
        self._safe_tx_hash = safe_tx_hash
        self._executor = executor
        self._is_executed = is_executed
        self._is_successful = is_successful
        self._eth_gas_price = eth_gas_price
        self._gas_used = gas_used
        self._fee = fee
        self._origin = origin
        self._data_decoded = data_decoded
        self._confirmations_required = confirmations_required
        self._confirmations = confirmations
        self._signatures = signatures

    @classmethod
    def from_dict(cls, dikt) -> 'SafeMultisigTransactionResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SafeMultisigTransactionResponse of this SafeMultisigTransactionResponse.  # noqa: E501
        :rtype: SafeMultisigTransactionResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def safe(self) -> str:
        """Gets the safe of this SafeMultisigTransactionResponse.


        :return: The safe of this SafeMultisigTransactionResponse.
        :rtype: str
        """
        return self._safe

    @safe.setter
    def safe(self, safe: str):
        """Sets the safe of this SafeMultisigTransactionResponse.


        :param safe: The safe of this SafeMultisigTransactionResponse.
        :type safe: str
        """
        if safe is None:
            raise ValueError("Invalid value for `safe`, must not be `None`")  # noqa: E501

        self._safe = safe

    @property
    def to(self) -> str:
        """Gets the to of this SafeMultisigTransactionResponse.


        :return: The to of this SafeMultisigTransactionResponse.
        :rtype: str
        """
        return self._to

    @to.setter
    def to(self, to: str):
        """Sets the to of this SafeMultisigTransactionResponse.


        :param to: The to of this SafeMultisigTransactionResponse.
        :type to: str
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def value(self) -> str:
        """Gets the value of this SafeMultisigTransactionResponse.


        :return: The value of this SafeMultisigTransactionResponse.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value: str):
        """Sets the value of this SafeMultisigTransactionResponse.


        :param value: The value of this SafeMultisigTransactionResponse.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")  # noqa: E501
        if value is not None and len(value) < 1:
            raise ValueError("Invalid value for `value`, length must be greater than or equal to `1`")  # noqa: E501

        self._value = value

    @property
    def data(self) -> str:
        """Gets the data of this SafeMultisigTransactionResponse.


        :return: The data of this SafeMultisigTransactionResponse.
        :rtype: str
        """
        return self._data

    @data.setter
    def data(self, data: str):
        """Sets the data of this SafeMultisigTransactionResponse.


        :param data: The data of this SafeMultisigTransactionResponse.
        :type data: str
        """

        self._data = data

    @property
    def operation(self) -> int:
        """Gets the operation of this SafeMultisigTransactionResponse.


        :return: The operation of this SafeMultisigTransactionResponse.
        :rtype: int
        """
        return self._operation

    @operation.setter
    def operation(self, operation: int):
        """Sets the operation of this SafeMultisigTransactionResponse.


        :param operation: The operation of this SafeMultisigTransactionResponse.
        :type operation: int
        """
        if operation is None:
            raise ValueError("Invalid value for `operation`, must not be `None`")  # noqa: E501
        if operation is not None and operation < 0:  # noqa: E501
            raise ValueError("Invalid value for `operation`, must be a value greater than or equal to `0`")  # noqa: E501

        self._operation = operation

    @property
    def gas_token(self) -> str:
        """Gets the gas_token of this SafeMultisigTransactionResponse.


        :return: The gas_token of this SafeMultisigTransactionResponse.
        :rtype: str
        """
        return self._gas_token

    @gas_token.setter
    def gas_token(self, gas_token: str):
        """Sets the gas_token of this SafeMultisigTransactionResponse.


        :param gas_token: The gas_token of this SafeMultisigTransactionResponse.
        :type gas_token: str
        """

        self._gas_token = gas_token

    @property
    def safe_tx_gas(self) -> int:
        """Gets the safe_tx_gas of this SafeMultisigTransactionResponse.


        :return: The safe_tx_gas of this SafeMultisigTransactionResponse.
        :rtype: int
        """
        return self._safe_tx_gas

    @safe_tx_gas.setter
    def safe_tx_gas(self, safe_tx_gas: int):
        """Sets the safe_tx_gas of this SafeMultisigTransactionResponse.


        :param safe_tx_gas: The safe_tx_gas of this SafeMultisigTransactionResponse.
        :type safe_tx_gas: int
        """
        if safe_tx_gas is None:
            raise ValueError("Invalid value for `safe_tx_gas`, must not be `None`")  # noqa: E501
        if safe_tx_gas is not None and safe_tx_gas < 0:  # noqa: E501
            raise ValueError("Invalid value for `safe_tx_gas`, must be a value greater than or equal to `0`")  # noqa: E501

        self._safe_tx_gas = safe_tx_gas

    @property
    def base_gas(self) -> int:
        """Gets the base_gas of this SafeMultisigTransactionResponse.


        :return: The base_gas of this SafeMultisigTransactionResponse.
        :rtype: int
        """
        return self._base_gas

    @base_gas.setter
    def base_gas(self, base_gas: int):
        """Sets the base_gas of this SafeMultisigTransactionResponse.


        :param base_gas: The base_gas of this SafeMultisigTransactionResponse.
        :type base_gas: int
        """
        if base_gas is None:
            raise ValueError("Invalid value for `base_gas`, must not be `None`")  # noqa: E501
        if base_gas is not None and base_gas < 0:  # noqa: E501
            raise ValueError("Invalid value for `base_gas`, must be a value greater than or equal to `0`")  # noqa: E501

        self._base_gas = base_gas

    @property
    def gas_price(self) -> str:
        """Gets the gas_price of this SafeMultisigTransactionResponse.


        :return: The gas_price of this SafeMultisigTransactionResponse.
        :rtype: str
        """
        return self._gas_price

    @gas_price.setter
    def gas_price(self, gas_price: str):
        """Sets the gas_price of this SafeMultisigTransactionResponse.


        :param gas_price: The gas_price of this SafeMultisigTransactionResponse.
        :type gas_price: str
        """
        if gas_price is None:
            raise ValueError("Invalid value for `gas_price`, must not be `None`")  # noqa: E501
        if gas_price is not None and len(gas_price) < 1:
            raise ValueError("Invalid value for `gas_price`, length must be greater than or equal to `1`")  # noqa: E501

        self._gas_price = gas_price

    @property
    def refund_receiver(self) -> str:
        """Gets the refund_receiver of this SafeMultisigTransactionResponse.


        :return: The refund_receiver of this SafeMultisigTransactionResponse.
        :rtype: str
        """
        return self._refund_receiver

    @refund_receiver.setter
    def refund_receiver(self, refund_receiver: str):
        """Sets the refund_receiver of this SafeMultisigTransactionResponse.


        :param refund_receiver: The refund_receiver of this SafeMultisigTransactionResponse.
        :type refund_receiver: str
        """

        self._refund_receiver = refund_receiver

    @property
    def nonce(self) -> int:
        """Gets the nonce of this SafeMultisigTransactionResponse.


        :return: The nonce of this SafeMultisigTransactionResponse.
        :rtype: int
        """
        return self._nonce

    @nonce.setter
    def nonce(self, nonce: int):
        """Sets the nonce of this SafeMultisigTransactionResponse.


        :param nonce: The nonce of this SafeMultisigTransactionResponse.
        :type nonce: int
        """
        if nonce is None:
            raise ValueError("Invalid value for `nonce`, must not be `None`")  # noqa: E501
        if nonce is not None and nonce < 0:  # noqa: E501
            raise ValueError("Invalid value for `nonce`, must be a value greater than or equal to `0`")  # noqa: E501

        self._nonce = nonce

    @property
    def execution_date(self) -> datetime:
        """Gets the execution_date of this SafeMultisigTransactionResponse.


        :return: The execution_date of this SafeMultisigTransactionResponse.
        :rtype: datetime
        """
        return self._execution_date

    @execution_date.setter
    def execution_date(self, execution_date: datetime):
        """Sets the execution_date of this SafeMultisigTransactionResponse.


        :param execution_date: The execution_date of this SafeMultisigTransactionResponse.
        :type execution_date: datetime
        """
        if execution_date is None:
            raise ValueError("Invalid value for `execution_date`, must not be `None`")  # noqa: E501

        self._execution_date = execution_date

    @property
    def submission_date(self) -> datetime:
        """Gets the submission_date of this SafeMultisigTransactionResponse.


        :return: The submission_date of this SafeMultisigTransactionResponse.
        :rtype: datetime
        """
        return self._submission_date

    @submission_date.setter
    def submission_date(self, submission_date: datetime):
        """Sets the submission_date of this SafeMultisigTransactionResponse.


        :param submission_date: The submission_date of this SafeMultisigTransactionResponse.
        :type submission_date: datetime
        """
        if submission_date is None:
            raise ValueError("Invalid value for `submission_date`, must not be `None`")  # noqa: E501

        self._submission_date = submission_date

    @property
    def modified(self) -> datetime:
        """Gets the modified of this SafeMultisigTransactionResponse.


        :return: The modified of this SafeMultisigTransactionResponse.
        :rtype: datetime
        """
        return self._modified

    @modified.setter
    def modified(self, modified: datetime):
        """Sets the modified of this SafeMultisigTransactionResponse.


        :param modified: The modified of this SafeMultisigTransactionResponse.
        :type modified: datetime
        """
        if modified is None:
            raise ValueError("Invalid value for `modified`, must not be `None`")  # noqa: E501

        self._modified = modified

    @property
    def block_number(self) -> int:
        """Gets the block_number of this SafeMultisigTransactionResponse.


        :return: The block_number of this SafeMultisigTransactionResponse.
        :rtype: int
        """
        return self._block_number

    @block_number.setter
    def block_number(self, block_number: int):
        """Sets the block_number of this SafeMultisigTransactionResponse.


        :param block_number: The block_number of this SafeMultisigTransactionResponse.
        :type block_number: int
        """

        self._block_number = block_number

    @property
    def transaction_hash(self) -> str:
        """Gets the transaction_hash of this SafeMultisigTransactionResponse.


        :return: The transaction_hash of this SafeMultisigTransactionResponse.
        :rtype: str
        """
        return self._transaction_hash

    @transaction_hash.setter
    def transaction_hash(self, transaction_hash: str):
        """Sets the transaction_hash of this SafeMultisigTransactionResponse.


        :param transaction_hash: The transaction_hash of this SafeMultisigTransactionResponse.
        :type transaction_hash: str
        """
        if transaction_hash is None:
            raise ValueError("Invalid value for `transaction_hash`, must not be `None`")  # noqa: E501

        self._transaction_hash = transaction_hash

    @property
    def safe_tx_hash(self) -> str:
        """Gets the safe_tx_hash of this SafeMultisigTransactionResponse.


        :return: The safe_tx_hash of this SafeMultisigTransactionResponse.
        :rtype: str
        """
        return self._safe_tx_hash

    @safe_tx_hash.setter
    def safe_tx_hash(self, safe_tx_hash: str):
        """Sets the safe_tx_hash of this SafeMultisigTransactionResponse.


        :param safe_tx_hash: The safe_tx_hash of this SafeMultisigTransactionResponse.
        :type safe_tx_hash: str
        """
        if safe_tx_hash is None:
            raise ValueError("Invalid value for `safe_tx_hash`, must not be `None`")  # noqa: E501

        self._safe_tx_hash = safe_tx_hash

    @property
    def executor(self) -> str:
        """Gets the executor of this SafeMultisigTransactionResponse.


        :return: The executor of this SafeMultisigTransactionResponse.
        :rtype: str
        """
        return self._executor

    @executor.setter
    def executor(self, executor: str):
        """Sets the executor of this SafeMultisigTransactionResponse.


        :param executor: The executor of this SafeMultisigTransactionResponse.
        :type executor: str
        """

        self._executor = executor

    @property
    def is_executed(self) -> bool:
        """Gets the is_executed of this SafeMultisigTransactionResponse.


        :return: The is_executed of this SafeMultisigTransactionResponse.
        :rtype: bool
        """
        return self._is_executed

    @is_executed.setter
    def is_executed(self, is_executed: bool):
        """Sets the is_executed of this SafeMultisigTransactionResponse.


        :param is_executed: The is_executed of this SafeMultisigTransactionResponse.
        :type is_executed: bool
        """
        if is_executed is None:
            raise ValueError("Invalid value for `is_executed`, must not be `None`")  # noqa: E501

        self._is_executed = is_executed

    @property
    def is_successful(self) -> bool:
        """Gets the is_successful of this SafeMultisigTransactionResponse.


        :return: The is_successful of this SafeMultisigTransactionResponse.
        :rtype: bool
        """
        return self._is_successful

    @is_successful.setter
    def is_successful(self, is_successful: bool):
        """Sets the is_successful of this SafeMultisigTransactionResponse.


        :param is_successful: The is_successful of this SafeMultisigTransactionResponse.
        :type is_successful: bool
        """

        self._is_successful = is_successful

    @property
    def eth_gas_price(self) -> str:
        """Gets the eth_gas_price of this SafeMultisigTransactionResponse.


        :return: The eth_gas_price of this SafeMultisigTransactionResponse.
        :rtype: str
        """
        return self._eth_gas_price

    @eth_gas_price.setter
    def eth_gas_price(self, eth_gas_price: str):
        """Sets the eth_gas_price of this SafeMultisigTransactionResponse.


        :param eth_gas_price: The eth_gas_price of this SafeMultisigTransactionResponse.
        :type eth_gas_price: str
        """

        self._eth_gas_price = eth_gas_price

    @property
    def gas_used(self) -> int:
        """Gets the gas_used of this SafeMultisigTransactionResponse.


        :return: The gas_used of this SafeMultisigTransactionResponse.
        :rtype: int
        """
        return self._gas_used

    @gas_used.setter
    def gas_used(self, gas_used: int):
        """Sets the gas_used of this SafeMultisigTransactionResponse.


        :param gas_used: The gas_used of this SafeMultisigTransactionResponse.
        :type gas_used: int
        """

        self._gas_used = gas_used

    @property
    def fee(self) -> int:
        """Gets the fee of this SafeMultisigTransactionResponse.


        :return: The fee of this SafeMultisigTransactionResponse.
        :rtype: int
        """
        return self._fee

    @fee.setter
    def fee(self, fee: int):
        """Sets the fee of this SafeMultisigTransactionResponse.


        :param fee: The fee of this SafeMultisigTransactionResponse.
        :type fee: int
        """

        self._fee = fee

    @property
    def origin(self) -> str:
        """Gets the origin of this SafeMultisigTransactionResponse.


        :return: The origin of this SafeMultisigTransactionResponse.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin: str):
        """Sets the origin of this SafeMultisigTransactionResponse.


        :param origin: The origin of this SafeMultisigTransactionResponse.
        :type origin: str
        """
        if origin is None:
            raise ValueError("Invalid value for `origin`, must not be `None`")  # noqa: E501
        if origin is not None and len(origin) < 1:
            raise ValueError("Invalid value for `origin`, length must be greater than or equal to `1`")  # noqa: E501

        self._origin = origin

    @property
    def data_decoded(self) -> str:
        """Gets the data_decoded of this SafeMultisigTransactionResponse.


        :return: The data_decoded of this SafeMultisigTransactionResponse.
        :rtype: str
        """
        return self._data_decoded

    @data_decoded.setter
    def data_decoded(self, data_decoded: str):
        """Sets the data_decoded of this SafeMultisigTransactionResponse.


        :param data_decoded: The data_decoded of this SafeMultisigTransactionResponse.
        :type data_decoded: str
        """

        self._data_decoded = data_decoded

    @property
    def confirmations_required(self) -> int:
        """Gets the confirmations_required of this SafeMultisigTransactionResponse.


        :return: The confirmations_required of this SafeMultisigTransactionResponse.
        :rtype: int
        """
        return self._confirmations_required

    @confirmations_required.setter
    def confirmations_required(self, confirmations_required: int):
        """Sets the confirmations_required of this SafeMultisigTransactionResponse.


        :param confirmations_required: The confirmations_required of this SafeMultisigTransactionResponse.
        :type confirmations_required: int
        """
        if confirmations_required is None:
            raise ValueError("Invalid value for `confirmations_required`, must not be `None`")  # noqa: E501

        self._confirmations_required = confirmations_required

    @property
    def confirmations(self) -> str:
        """Gets the confirmations of this SafeMultisigTransactionResponse.


        :return: The confirmations of this SafeMultisigTransactionResponse.
        :rtype: str
        """
        return self._confirmations

    @confirmations.setter
    def confirmations(self, confirmations: str):
        """Sets the confirmations of this SafeMultisigTransactionResponse.


        :param confirmations: The confirmations of this SafeMultisigTransactionResponse.
        :type confirmations: str
        """

        self._confirmations = confirmations

    @property
    def signatures(self) -> str:
        """Gets the signatures of this SafeMultisigTransactionResponse.


        :return: The signatures of this SafeMultisigTransactionResponse.
        :rtype: str
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures: str):
        """Sets the signatures of this SafeMultisigTransactionResponse.


        :param signatures: The signatures of this SafeMultisigTransactionResponse.
        :type signatures: str
        """
        if signatures is None:
            raise ValueError("Invalid value for `signatures`, must not be `None`")  # noqa: E501

        self._signatures = signatures
