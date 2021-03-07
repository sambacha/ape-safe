import connexion
import six

from swagger_server.models.contract import Contract  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server import util


def contracts_list(ordering=None, limit=None, offset=None):  # noqa: E501
    """contracts_list

     # noqa: E501

    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param limit: Number of results to return per page.
    :type limit: int
    :param offset: The initial index from which to return the results.
    :type offset: int

    :rtype: InlineResponse2001
    """
    return 'do some magic!'


def contracts_read(address):  # noqa: E501
    """contracts_read

     # noqa: E501

    :param address: A unique value identifying this contract.
    :type address: str

    :rtype: Contract
    """
    return 'do some magic!'
