import connexion
import six

from swagger_server.models.owner_response import OwnerResponse  # noqa: E501
from swagger_server import util


def owners_read(address):  # noqa: E501
    """owners_read

    Return Safes where the address provided is an owner # noqa: E501

    :param address: 
    :type address: str

    :rtype: OwnerResponse
    """
    return 'do some magic!'
