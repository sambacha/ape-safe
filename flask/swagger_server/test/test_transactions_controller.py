# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.safe_multisig_transaction_response import SafeMultisigTransactionResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTransactionsController(BaseTestCase):
    """TransactionsController integration test stubs"""

    def test_transactions_read(self):
        """Test case for transactions_read

        
        """
        response = self.client.open(
            '/api/v1/transactions/{safe_tx_hash}/'.format(safe_tx_hash='safe_tx_hash_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
