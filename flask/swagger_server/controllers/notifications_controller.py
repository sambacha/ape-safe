import connexion
import six

from swagger_server.models.firebase_device import FirebaseDevice  # noqa: E501
from swagger_server import util


def notifications_devices_create(data):  # noqa: E501
    """notifications_devices_create

    Creates a new FirebaseDevice. If uuid is not provided a new device will be created. If a uuid for an existing Safe is provided the FirebaseDevice will be updated with all the new data provided. Safes provided on the request are always added and never removed/replaced # noqa: E501

    :param data: 
    :type data: dict | bytes

    :rtype: FirebaseDevice
    """
    if connexion.request.is_json:
        data = FirebaseDevice.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def notifications_devices_delete(uuid):  # noqa: E501
    """notifications_devices_delete

    Remove a FirebaseDevice # noqa: E501

    :param uuid: A UUID string identifying this Firebase Device.
    :type uuid: 

    :rtype: None
    """
    return 'do some magic!'


def notifications_devices_safes_delete(address, uuid):  # noqa: E501
    """notifications_devices_safes_delete

    Remove a Safe for a FirebaseDevice # noqa: E501

    :param address: 
    :type address: str
    :param uuid: A UUID string identifying this Firebase Device.
    :type uuid: 

    :rtype: None
    """
    return 'do some magic!'
