import connexion
import six

from swagger_server.models.inline_response2006 import InlineResponse2006  # noqa: E501
from swagger_server.models.token_info_response import TokenInfoResponse  # noqa: E501
from swagger_server import util


def tokens_list(name=None, address=None, symbol=None, decimals__lt=None, decimals__gt=None, decimals=None, search=None, ordering=None, limit=None, offset=None):  # noqa: E501
    """tokens_list

     # noqa: E501

    :param name: 
    :type name: str
    :param address: 
    :type address: str
    :param symbol: 
    :type symbol: str
    :param decimals__lt: 
    :type decimals__lt: 
    :param decimals__gt: 
    :type decimals__gt: 
    :param decimals: 
    :type decimals: 
    :param search: A search term.
    :type search: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    :rtype: InlineResponse2006
    """
    return 'do some magic!'


def tokens_read(address):  # noqa: E501
    """tokens_read

     # noqa: E501

    :param address: A unique value identifying this token.
    :type address: str

    :rtype: TokenInfoResponse
    """
    return 'do some magic!'
