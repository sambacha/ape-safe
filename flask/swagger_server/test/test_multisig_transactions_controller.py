# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response2002 import InlineResponse2002  # noqa: E501
from swagger_server.models.safe_multisig_confirmation import SafeMultisigConfirmation  # noqa: E501
from swagger_server.models.safe_multisig_transaction_response import SafeMultisigTransactionResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMultisigTransactionsController(BaseTestCase):
    """MultisigTransactionsController integration test stubs"""

    def test_multisig_transactions_confirmations_create(self):
        """Test case for multisig_transactions_confirmations_create

        
        """
        data = SafeMultisigConfirmation()
        response = self.client.open(
            '/api/v1/multisig-transactions/{safe_tx_hash}/confirmations/'.format(safe_tx_hash='safe_tx_hash_example'),
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_multisig_transactions_confirmations_list(self):
        """Test case for multisig_transactions_confirmations_list

        
        """
        query_string = [('limit', 56),
                        ('offset', 56)]
        response = self.client.open(
            '/api/v1/multisig-transactions/{safe_tx_hash}/confirmations/'.format(safe_tx_hash='safe_tx_hash_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_multisig_transactions_read(self):
        """Test case for multisig_transactions_read

        
        """
        response = self.client.open(
            '/api/v1/multisig-transactions/{safe_tx_hash}/'.format(safe_tx_hash='safe_tx_hash_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
