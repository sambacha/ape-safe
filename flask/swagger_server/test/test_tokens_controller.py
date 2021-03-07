# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2006 import InlineResponse2006  # noqa: E501
from swagger_server.models.token_info_response import TokenInfoResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTokensController(BaseTestCase):
    """TokensController integration test stubs"""

    def test_tokens_list(self):
        """Test case for tokens_list

        
        """
        query_string = [('name', 'name_example'),
                        ('address', 'address_example'),
                        ('symbol', 'symbol_example'),
                        ('decimals__lt', 8.14),
                        ('decimals__gt', 8.14),
                        ('decimals', 8.14),
                        ('search', 'search_example'),
                        ('ordering', 'ordering_example'),
                        ('limit', 56),
                        ('offset', 56)]
        response = self.client.open(
            '/api/v1/tokens/',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_tokens_read(self):
        """Test case for tokens_read

        
        """
        response = self.client.open(
            '/api/v1/tokens/{address}/'.format(address='address_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
