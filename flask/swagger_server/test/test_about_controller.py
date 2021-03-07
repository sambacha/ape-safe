# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.master_copy_response import MasterCopyResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAboutController(BaseTestCase):
    """AboutController integration test stubs"""

    def test_about_list(self):
        """Test case for about_list

        
        """
        response = self.client.open(
            '/api/v1/about/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_about_master_copies_list(self):
        """Test case for about_master_copies_list

        
        """
        response = self.client.open(
            '/api/v1/about/master-copies/',
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
