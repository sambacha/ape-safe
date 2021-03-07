# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.analytics_multisig_txs_by_origin_response import AnalyticsMultisigTxsByOriginResponse  # noqa: E501
from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.test import BaseTestCase


class TestAnalyticsController(BaseTestCase):
    """AnalyticsController integration test stubs"""

    def test_analytics_multisig_transactions_by_origin_list(self):
        """Test case for analytics_multisig_transactions_by_origin_list

        
        """
        query_string = [('safe', 'safe_example'),
                        ('to', 'to_example'),
                        ('value__lt', 8.14),
                        ('value__gt', 8.14),
                        ('value__lte', 8.14),
                        ('value__gte', 8.14),
                        ('value', 8.14),
                        ('operation', 'operation_example'),
                        ('failed', 'failed_example'),
                        ('safe_tx_gas__lt', 8.14),
                        ('safe_tx_gas__gt', 8.14),
                        ('safe_tx_gas__lte', 8.14),
                        ('safe_tx_gas__gte', 8.14),
                        ('safe_tx_gas', 8.14),
                        ('base_gas__lt', 8.14),
                        ('base_gas__gt', 8.14),
                        ('base_gas__lte', 8.14),
                        ('base_gas__gte', 8.14),
                        ('base_gas', 8.14),
                        ('gas_price__lt', 8.14),
                        ('gas_price__gt', 8.14),
                        ('gas_price__lte', 8.14),
                        ('gas_price__gte', 8.14),
                        ('gas_price', 8.14),
                        ('gas_token', 'gas_token_example'),
                        ('refund_receiver', 'refund_receiver_example'),
                        ('trusted', 'trusted_example')]
        response = self.client.open(
            '/api/v1/analytics/multisig-transactions/by-origin/',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_analytics_multisig_transactions_by_safe_list(self):
        """Test case for analytics_multisig_transactions_by_safe_list

        
        """
        query_string = [('master_copy', 'master_copy_example'),
                        ('limit', 56),
                        ('offset', 56)]
        response = self.client.open(
            '/api/v1/analytics/multisig-transactions/by-safe/',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
