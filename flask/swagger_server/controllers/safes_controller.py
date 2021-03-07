import connexion
import six

from swagger_server.models.all_transactions_schema import AllTransactionsSchema  # noqa: E501
from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server.models.safe_balance_response import SafeBalanceResponse  # noqa: E501
from swagger_server.models.safe_balance_usd_response import SafeBalanceUsdResponse  # noqa: E501
from swagger_server.models.safe_collectible_response import SafeCollectibleResponse  # noqa: E501
from swagger_server.models.safe_creation_info_response import SafeCreationInfoResponse  # noqa: E501
from swagger_server.models.safe_delegate import SafeDelegate  # noqa: E501
from swagger_server.models.safe_info_response import SafeInfoResponse  # noqa: E501
from swagger_server.models.safe_multisig_transaction import SafeMultisigTransaction  # noqa: E501
from swagger_server.models.transfer_response import TransferResponse  # noqa: E501
from swagger_server import util


def safes_all_transactions_list(address, ordering=None, limit=None, offset=None, queued=None, trusted=None):  # noqa: E501
    """safes_all_transactions_list

    Returns a paginated list of transactions for a Safe. The list has different structures depending on the transaction type: - Multisig Transactions for a Safe. &#x60;tx_type&#x3D;MULTISIG_TRANSACTION&#x60;. If the query parameter &#x60;queued&#x3D;False&#x60; is set only the transactions with &#x60;safe nonce &lt; current Safe nonce&#x60; will be displayed. By default, only the &#x60;trusted&#x60; transactions will be displayed (transactions indexed, with at least one confirmation or proposed by a delegate). If you need that behaviour to be disabled set the query parameter &#x60;trusted&#x3D;False&#x60; - Module Transactions for a Safe. &#x60;tx_type&#x3D;MODULE_TRANSACTION&#x60; - Incoming Transfers of Ether/ERC20 Tokens/ERC721 Tokens. &#x60;tx_type&#x3D;ETHEREUM_TRANSACTION&#x60; # noqa: E501

    :param address: 
    :type address: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int
    :param queued: If &#x60;True&#x60; transactions with &#x60;nonce &gt;&#x3D; Safe current nonce&#x60; are also returned
    :type queued: bool
    :param trusted: If &#x60;True&#x60; just trusted transactions are shown (indexed, added by a delegate or with at least one confirmation)
    :type trusted: bool

    :rtype: AllTransactionsSchema
    """
    return 'do some magic!'


def safes_balances_list(address, trusted=None, exclude_spam=None):  # noqa: E501
    """safes_balances_list

    Get balance for Ether and ERC20 tokens # noqa: E501

    :param address: 
    :type address: str
    :param trusted: If &#x60;True&#x60; just trusted tokens will be returned
    :type trusted: bool
    :param exclude_spam: If &#x60;True&#x60; spam tokens will not be returned
    :type exclude_spam: bool

    :rtype: List[SafeBalanceResponse]
    """
    return 'do some magic!'


def safes_balances_usd_list(address, trusted=None, exclude_spam=None):  # noqa: E501
    """safes_balances_usd_list

    Get balance for Ether and ERC20 tokens with USD fiat conversion # noqa: E501

    :param address: 
    :type address: str
    :param trusted: If &#x60;True&#x60; just trusted tokens will be returned
    :type trusted: bool
    :param exclude_spam: If &#x60;True&#x60; spam tokens will not be returned
    :type exclude_spam: bool

    :rtype: List[SafeBalanceUsdResponse]
    """
    return 'do some magic!'


def safes_collectibles_list(address, trusted=None, exclude_spam=None):  # noqa: E501
    """safes_collectibles_list

    Get collectibles (ERC721 tokens) and information about them # noqa: E501

    :param address: 
    :type address: str
    :param trusted: If &#x60;True&#x60; just trusted tokens will be returned
    :type trusted: bool
    :param exclude_spam: If &#x60;True&#x60; spam tokens will not be returned
    :type exclude_spam: bool

    :rtype: List[SafeCollectibleResponse]
    """
    return 'do some magic!'


def safes_creation_list(address):  # noqa: E501
    """safes_creation_list

    Get status of the safe # noqa: E501

    :param address: 
    :type address: str

    :rtype: SafeCreationInfoResponse
    """
    return 'do some magic!'


def safes_delegates_create(address, data):  # noqa: E501
    """safes_delegates_create

    Create a delegate for a Safe address with a custom label. Calls with same delegate but different label or signer will update the label or delegator if different. For the signature we are using TOTP with &#x60;T0&#x3D;0&#x60; and &#x60;Tx&#x3D;3600&#x60;. TOTP is calculated by taking the Unix UTC epoch time (no milliseconds) and dividing by 3600 (natural division, no decimals) For signature this hash need to be signed: keccak(address + str(int(current_epoch // 3600))) For example:      - we want to add the owner &#x60;0x132512f995866CcE1b0092384A6118EDaF4508Ff&#x60; and &#x60;epoch&#x3D;1586779140&#x60;.      - TOTP &#x3D; epoch // 3600 &#x3D; 1586779140 // 3600 &#x3D; 440771      - The hash to sign by a Safe owner would be &#x60;keccak(\&quot;0x132512f995866CcE1b0092384A6118EDaF4508Ff440771\&quot;)&#x60; # noqa: E501

    :param address: 
    :type address: str
    :param data: 
    :type data: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        data = SafeDelegate.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def safes_delegates_delete(address, delegate_address):  # noqa: E501
    """safes_delegates_delete

    Delete a delegate for a Safe. Signature is built the same way that for adding a delegate. Check &#x60;POST /delegates/&#x60; # noqa: E501

    :param address: 
    :type address: str
    :param delegate_address: 
    :type delegate_address: str

    :rtype: None
    """
    return 'do some magic!'


def safes_delegates_list(address, limit=None, offset=None):  # noqa: E501
    """safes_delegates_list

    Get the list of delegates for a Safe address # noqa: E501

    :param address: 
    :type address: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    :rtype: InlineResponse2003
    """
    return 'do some magic!'


def safes_incoming_transactions_list(address, _from=None, block_number=None, block_number__gt=None, block_number__lt=None, execution_date__gte=None, execution_date__lte=None, execution_date__gt=None, execution_date__lt=None, to=None, token_address=None, transaction_hash=None, value=None, value__gt=None, value__lt=None, limit=None, offset=None):  # noqa: E501
    """safes_incoming_transactions_list

    Returns the history of a multisig tx (safe) # noqa: E501

    :param address: 
    :type address: str
    :param _from: 
    :type _from: str
    :param block_number: 
    :type block_number: 
    :param block_number__gt: 
    :type block_number__gt: 
    :param block_number__lt: 
    :type block_number__lt: 
    :param execution_date__gte: 
    :type execution_date__gte: str
    :param execution_date__lte: 
    :type execution_date__lte: str
    :param execution_date__gt: 
    :type execution_date__gt: str
    :param execution_date__lt: 
    :type execution_date__lt: str
    :param to: 
    :type to: str
    :param token_address: 
    :type token_address: str
    :param transaction_hash: 
    :type transaction_hash: str
    :param value: 
    :type value: 
    :param value__gt: 
    :type value__gt: 
    :param value__lt: 
    :type value__lt: 
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    :rtype: List[TransferResponse]
    """
    return 'do some magic!'


def safes_incoming_transfers_list(address, _from=None, block_number=None, block_number__gt=None, block_number__lt=None, execution_date__gte=None, execution_date__lte=None, execution_date__gt=None, execution_date__lt=None, to=None, token_address=None, transaction_hash=None, value=None, value__gt=None, value__lt=None, limit=None, offset=None):  # noqa: E501
    """safes_incoming_transfers_list

    Returns the history of a multisig tx (safe) # noqa: E501

    :param address: 
    :type address: str
    :param _from: 
    :type _from: str
    :param block_number: 
    :type block_number: 
    :param block_number__gt: 
    :type block_number__gt: 
    :param block_number__lt: 
    :type block_number__lt: 
    :param execution_date__gte: 
    :type execution_date__gte: str
    :param execution_date__lte: 
    :type execution_date__lte: str
    :param execution_date__gt: 
    :type execution_date__gt: str
    :param execution_date__lt: 
    :type execution_date__lt: str
    :param to: 
    :type to: str
    :param token_address: 
    :type token_address: str
    :param transaction_hash: 
    :type transaction_hash: str
    :param value: 
    :type value: 
    :param value__gt: 
    :type value__gt: 
    :param value__lt: 
    :type value__lt: 
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    :rtype: List[TransferResponse]
    """
    return 'do some magic!'


def safes_module_transactions_list(address, safe=None, module=None, to=None, operation=None, failed=None, block_number=None, block_number__gt=None, block_number__lt=None, transaction_hash=None, ordering=None, limit=None, offset=None):  # noqa: E501
    """safes_module_transactions_list

    Returns the module transaction of a Safe # noqa: E501

    :param address: 
    :type address: str
    :param safe: 
    :type safe: str
    :param module: 
    :type module: str
    :param to: 
    :type to: str
    :param operation: 
    :type operation: str
    :param failed: 
    :type failed: str
    :param block_number: 
    :type block_number: 
    :param block_number__gt: 
    :type block_number__gt: 
    :param block_number__lt: 
    :type block_number__lt: 
    :param transaction_hash: 
    :type transaction_hash: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    :rtype: InlineResponse2004
    """
    return 'do some magic!'


def safes_multisig_transactions_create(address, data):  # noqa: E501
    """safes_multisig_transactions_create

    Creates a Multisig Transaction with its confirmations and retrieves all the information related. # noqa: E501

    :param address: 
    :type address: str
    :param data: 
    :type data: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        data = SafeMultisigTransaction.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def safes_multisig_transactions_list(address, failed=None, modified__lt=None, modified__gt=None, modified__lte=None, modified__gte=None, nonce__lt=None, nonce__gt=None, nonce__lte=None, nonce__gte=None, nonce=None, safe_tx_hash=None, to=None, value__lt=None, value__gt=None, value=None, executed=None, has_confirmations=None, trusted=None, execution_date__gte=None, execution_date__lte=None, submission_date__gte=None, submission_date__lte=None, transaction_hash=None, ordering=None, limit=None, offset=None):  # noqa: E501
    """safes_multisig_transactions_list

    Returns the history of a multisig tx (safe) # noqa: E501

    :param address: 
    :type address: str
    :param failed: 
    :type failed: str
    :param modified__lt: 
    :type modified__lt: str
    :param modified__gt: 
    :type modified__gt: str
    :param modified__lte: 
    :type modified__lte: str
    :param modified__gte: 
    :type modified__gte: str
    :param nonce__lt: 
    :type nonce__lt: 
    :param nonce__gt: 
    :type nonce__gt: 
    :param nonce__lte: 
    :type nonce__lte: 
    :param nonce__gte: 
    :type nonce__gte: 
    :param nonce: 
    :type nonce: 
    :param safe_tx_hash: 
    :type safe_tx_hash: str
    :param to: 
    :type to: str
    :param value__lt: 
    :type value__lt: 
    :param value__gt: 
    :type value__gt: 
    :param value: 
    :type value: 
    :param executed: 
    :type executed: str
    :param has_confirmations: 
    :type has_confirmations: str
    :param trusted: 
    :type trusted: str
    :param execution_date__gte: 
    :type execution_date__gte: str
    :param execution_date__lte: 
    :type execution_date__lte: str
    :param submission_date__gte: 
    :type submission_date__gte: str
    :param submission_date__lte: 
    :type submission_date__lte: str
    :param transaction_hash: 
    :type transaction_hash: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    :rtype: InlineResponse2005
    """
    return 'do some magic!'


def safes_read(address):  # noqa: E501
    """safes_read

    Get status of the safe # noqa: E501

    :param address: 
    :type address: str

    :rtype: SafeInfoResponse
    """
    return 'do some magic!'


def safes_transactions_create(address, data):  # noqa: E501
    """safes_transactions_create

    Creates a Multisig Transaction with its confirmations and retrieves all the information related. # noqa: E501

    :param address: 
    :type address: str
    :param data: 
    :type data: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        data = SafeMultisigTransaction.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def safes_transactions_list(address, failed=None, modified__lt=None, modified__gt=None, modified__lte=None, modified__gte=None, nonce__lt=None, nonce__gt=None, nonce__lte=None, nonce__gte=None, nonce=None, safe_tx_hash=None, to=None, value__lt=None, value__gt=None, value=None, executed=None, has_confirmations=None, trusted=None, execution_date__gte=None, execution_date__lte=None, submission_date__gte=None, submission_date__lte=None, transaction_hash=None, ordering=None, limit=None, offset=None):  # noqa: E501
    """safes_transactions_list

    Returns the history of a multisig tx (safe) # noqa: E501

    :param address: 
    :type address: str
    :param failed: 
    :type failed: str
    :param modified__lt: 
    :type modified__lt: str
    :param modified__gt: 
    :type modified__gt: str
    :param modified__lte: 
    :type modified__lte: str
    :param modified__gte: 
    :type modified__gte: str
    :param nonce__lt: 
    :type nonce__lt: 
    :param nonce__gt: 
    :type nonce__gt: 
    :param nonce__lte: 
    :type nonce__lte: 
    :param nonce__gte: 
    :type nonce__gte: 
    :param nonce: 
    :type nonce: 
    :param safe_tx_hash: 
    :type safe_tx_hash: str
    :param to: 
    :type to: str
    :param value__lt: 
    :type value__lt: 
    :param value__gt: 
    :type value__gt: 
    :param value: 
    :type value: 
    :param executed: 
    :type executed: str
    :param has_confirmations: 
    :type has_confirmations: str
    :param trusted: 
    :type trusted: str
    :param execution_date__gte: 
    :type execution_date__gte: str
    :param execution_date__lte: 
    :type execution_date__lte: str
    :param submission_date__gte: 
    :type submission_date__gte: str
    :param submission_date__lte: 
    :type submission_date__lte: str
    :param transaction_hash: 
    :type transaction_hash: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    :rtype: InlineResponse2005
    """
    return 'do some magic!'


def safes_transfers_list(address, _from=None, block_number=None, block_number__gt=None, block_number__lt=None, execution_date__gte=None, execution_date__lte=None, execution_date__gt=None, execution_date__lt=None, to=None, token_address=None, transaction_hash=None, value=None, value__gt=None, value__lt=None, limit=None, offset=None):  # noqa: E501
    """safes_transfers_list

    Returns the history of a multisig tx (safe) # noqa: E501

    :param address: 
    :type address: str
    :param _from: 
    :type _from: str
    :param block_number: 
    :type block_number: 
    :param block_number__gt: 
    :type block_number__gt: 
    :param block_number__lt: 
    :type block_number__lt: 
    :param execution_date__gte: 
    :type execution_date__gte: str
    :param execution_date__lte: 
    :type execution_date__lte: str
    :param execution_date__gt: 
    :type execution_date__gt: str
    :param execution_date__lt: 
    :type execution_date__lt: str
    :param to: 
    :type to: str
    :param token_address: 
    :type token_address: str
    :param transaction_hash: 
    :type transaction_hash: str
    :param value: 
    :type value: 
    :param value__gt: 
    :type value__gt: 
    :param value__lt: 
    :type value__lt: 
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    :rtype: List[TransferResponse]
    """
    return 'do some magic!'
