# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.owner_response import OwnerResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestOwnersController(BaseTestCase):
    """OwnersController integration test stubs"""

    def test_owners_read(self):
        """Test case for owners_read

        
        """
        response = self.client.open(
            '/api/v1/owners/{address}/'.format(address='address_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
