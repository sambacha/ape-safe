# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.firebase_device import FirebaseDevice  # noqa: E501
from swagger_server.test import BaseTestCase


class TestNotificationsController(BaseTestCase):
    """NotificationsController integration test stubs"""

    def test_notifications_devices_create(self):
        """Test case for notifications_devices_create

        
        """
        data = FirebaseDevice()
        response = self.client.open(
            '/api/v1/notifications/devices/',
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_notifications_devices_delete(self):
        """Test case for notifications_devices_delete

        
        """
        response = self.client.open(
            '/api/v1/notifications/devices/{uuid}/'.format(uuid='uuid_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_notifications_devices_safes_delete(self):
        """Test case for notifications_devices_safes_delete

        
        """
        response = self.client.open(
            '/api/v1/notifications/devices/{uuid}/safes/{address}/'.format(address='address_example', uuid='uuid_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
