import connexion
import six

from swagger_server.models.safe_multisig_transaction_response import SafeMultisigTransactionResponse  # noqa: E501
from swagger_server import util


def transactions_read(safe_tx_hash):  # noqa: E501
    """transactions_read

     # noqa: E501

    :param safe_tx_hash: 
    :type safe_tx_hash: str

    :rtype: SafeMultisigTransactionResponse
    """
    return 'do some magic!'
