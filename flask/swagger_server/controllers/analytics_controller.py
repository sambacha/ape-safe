import connexion
import six

from swagger_server.models.analytics_multisig_txs_by_origin_response import AnalyticsMultisigTxsByOriginResponse  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server import util


def analytics_multisig_transactions_by_origin_list(safe=None, to=None, value__lt=None, value__gt=None, value__lte=None, value__gte=None, value=None, operation=None, failed=None, safe_tx_gas__lt=None, safe_tx_gas__gt=None, safe_tx_gas__lte=None, safe_tx_gas__gte=None, safe_tx_gas=None, base_gas__lt=None, base_gas__gt=None, base_gas__lte=None, base_gas__gte=None, base_gas=None, gas_price__lt=None, gas_price__gt=None, gas_price__lte=None, gas_price__gte=None, gas_price=None, gas_token=None, refund_receiver=None, trusted=None):  # noqa: E501
    """analytics_multisig_transactions_by_origin_list

     # noqa: E501

    :param safe: 
    :type safe: str
    :param to: 
    :type to: str
    :param value__lt: 
    :type value__lt: 
    :param value__gt: 
    :type value__gt: 
    :param value__lte: 
    :type value__lte: 
    :param value__gte: 
    :type value__gte: 
    :param value: 
    :type value: 
    :param operation: 
    :type operation: str
    :param failed: 
    :type failed: str
    :param safe_tx_gas__lt: 
    :type safe_tx_gas__lt: 
    :param safe_tx_gas__gt: 
    :type safe_tx_gas__gt: 
    :param safe_tx_gas__lte: 
    :type safe_tx_gas__lte: 
    :param safe_tx_gas__gte: 
    :type safe_tx_gas__gte: 
    :param safe_tx_gas: 
    :type safe_tx_gas: 
    :param base_gas__lt: 
    :type base_gas__lt: 
    :param base_gas__gt: 
    :type base_gas__gt: 
    :param base_gas__lte: 
    :type base_gas__lte: 
    :param base_gas__gte: 
    :type base_gas__gte: 
    :param base_gas: 
    :type base_gas: 
    :param gas_price__lt: 
    :type gas_price__lt: 
    :param gas_price__gt: 
    :type gas_price__gt: 
    :param gas_price__lte: 
    :type gas_price__lte: 
    :param gas_price__gte: 
    :type gas_price__gte: 
    :param gas_price: 
    :type gas_price: 
    :param gas_token: 
    :type gas_token: str
    :param refund_receiver: 
    :type refund_receiver: str
    :param trusted: 
    :type trusted: str

    :rtype: List[AnalyticsMultisigTxsByOriginResponse]
    """
    return 'do some magic!'


def analytics_multisig_transactions_by_safe_list(master_copy=None, limit=None, offset=None):  # noqa: E501
    """analytics_multisig_transactions_by_safe_list

     # noqa: E501

    :param master_copy: 
    :type master_copy: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    :rtype: InlineResponse200
    """
    return 'do some magic!'
