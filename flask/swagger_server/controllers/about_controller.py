import connexion
import six

from swagger_server.models.master_copy_response import MasterCopyResponse  # noqa: E501
from swagger_server import util


def about_list():  # noqa: E501
    """about_list

    Returns information and configuration of the service # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def about_master_copies_list():  # noqa: E501
    """about_master_copies_list

     # noqa: E501


    :rtype: List[MasterCopyResponse]
    """
    return 'do some magic!'
