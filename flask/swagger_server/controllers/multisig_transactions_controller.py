import connexion
import six

from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.safe_multisig_confirmation import SafeMultisigConfirmation  # noqa: E501
from swagger_server.models.safe_multisig_transaction_response import SafeMultisigTransactionResponse  # noqa: E501
from swagger_server import util


def multisig_transactions_confirmations_create(safe_tx_hash, data):  # noqa: E501
    """multisig_transactions_confirmations_create

    Add a confirmation for a transaction. More than one signature can be used. This endpoint does not support the use of delegates to make a transaction trusted. # noqa: E501

    :param safe_tx_hash: 
    :type safe_tx_hash: str
    :param data: 
    :type data: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        data = SafeMultisigConfirmation.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def multisig_transactions_confirmations_list(safe_tx_hash, limit=None, offset=None):  # noqa: E501
    """multisig_transactions_confirmations_list

    Get the list of confirmations for a multisig transaction # noqa: E501

    :param safe_tx_hash: 
    :type safe_tx_hash: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    :rtype: InlineResponse2002
    """
    return 'do some magic!'


def multisig_transactions_read(safe_tx_hash):  # noqa: E501
    """multisig_transactions_read

     # noqa: E501

    :param safe_tx_hash: 
    :type safe_tx_hash: str

    :rtype: SafeMultisigTransactionResponse
    """
    return 'do some magic!'
