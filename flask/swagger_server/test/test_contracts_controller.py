# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.contract import Contract  # noqa: E501
from swagger_server.models.inline_response2001 import InlineResponse2001  # noqa: E501
from swagger_server.test import BaseTestCase


class TestContractsController(BaseTestCase):
    """ContractsController integration test stubs"""

    def test_contracts_list(self):
        """Test case for contracts_list

        
        """
        query_string = [('ordering', 'ordering_example'),
                        ('limit', 56),
                        ('offset', 56)]
        response = self.client.open(
            '/api/v1/contracts/',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_contracts_read(self):
        """Test case for contracts_read

        
        """
        response = self.client.open(
            '/api/v1/contracts/{address}/'.format(address='address_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
