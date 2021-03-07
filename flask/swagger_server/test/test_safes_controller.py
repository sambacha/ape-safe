# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.all_transactions_schema import AllTransactionsSchema  # noqa: E501
from swagger_server.models.inline_response2003 import InlineResponse2003  # noqa: E501
from swagger_server.models.inline_response2004 import InlineResponse2004  # noqa: E501
from swagger_server.models.inline_response2005 import InlineResponse2005  # noqa: E501
from swagger_server.models.safe_balance_response import SafeBalanceResponse  # noqa: E501
from swagger_server.models.safe_balance_usd_response import SafeBalanceUsdResponse  # noqa: E501
from swagger_server.models.safe_collectible_response import SafeCollectibleResponse  # noqa: E501
from swagger_server.models.safe_creation_info_response import SafeCreationInfoResponse  # noqa: E501
from swagger_server.models.safe_delegate import SafeDelegate  # noqa: E501
from swagger_server.models.safe_info_response import SafeInfoResponse  # noqa: E501
from swagger_server.models.safe_multisig_transaction import SafeMultisigTransaction  # noqa: E501
from swagger_server.models.transfer_response import TransferResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSafesController(BaseTestCase):
    """SafesController integration test stubs"""

    def test_safes_all_transactions_list(self):
        """Test case for safes_all_transactions_list

        
        """
        query_string = [('ordering', 'ordering_example'),
                        ('limit', 56),
                        ('offset', 56),
                        ('queued', true),
                        ('trusted', true)]
        response = self.client.open(
            '/api/v1/safes/{address}/all-transactions/'.format(address='address_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_safes_balances_list(self):
        """Test case for safes_balances_list

        
        """
        query_string = [('trusted', false),
                        ('exclude_spam', false)]
        response = self.client.open(
            '/api/v1/safes/{address}/balances/'.format(address='address_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_safes_balances_usd_list(self):
        """Test case for safes_balances_usd_list

        
        """
        query_string = [('trusted', false),
                        ('exclude_spam', false)]
        response = self.client.open(
            '/api/v1/safes/{address}/balances/usd/'.format(address='address_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_safes_collectibles_list(self):
        """Test case for safes_collectibles_list

        
        """
        query_string = [('trusted', false),
                        ('exclude_spam', false)]
        response = self.client.open(
            '/api/v1/safes/{address}/collectibles/'.format(address='address_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_safes_creation_list(self):
        """Test case for safes_creation_list

        
        """
        response = self.client.open(
            '/api/v1/safes/{address}/creation/'.format(address='address_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_safes_delegates_create(self):
        """Test case for safes_delegates_create

        
        """
        data = SafeDelegate()
        response = self.client.open(
            '/api/v1/safes/{address}/delegates/'.format(address='address_example'),
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_safes_delegates_delete(self):
        """Test case for safes_delegates_delete

        
        """
        response = self.client.open(
            '/api/v1/safes/{address}/delegates/{delegate_address}/'.format(address='address_example', delegate_address='delegate_address_example'),
            method='DELETE',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_safes_delegates_list(self):
        """Test case for safes_delegates_list

        
        """
        query_string = [('limit', 56),
                        ('offset', 56)]
        response = self.client.open(
            '/api/v1/safes/{address}/delegates/'.format(address='address_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_safes_incoming_transactions_list(self):
        """Test case for safes_incoming_transactions_list

        
        """
        query_string = [('_from', '_from_example'),
                        ('block_number', 8.14),
                        ('block_number__gt', 8.14),
                        ('block_number__lt', 8.14),
                        ('execution_date__gte', 'execution_date__gte_example'),
                        ('execution_date__lte', 'execution_date__lte_example'),
                        ('execution_date__gt', 'execution_date__gt_example'),
                        ('execution_date__lt', 'execution_date__lt_example'),
                        ('to', 'to_example'),
                        ('token_address', 'token_address_example'),
                        ('transaction_hash', 'transaction_hash_example'),
                        ('value', 8.14),
                        ('value__gt', 8.14),
                        ('value__lt', 8.14),
                        ('limit', 56),
                        ('offset', 56)]
        response = self.client.open(
            '/api/v1/safes/{address}/incoming-transactions/'.format(address='address_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_safes_incoming_transfers_list(self):
        """Test case for safes_incoming_transfers_list

        
        """
        query_string = [('_from', '_from_example'),
                        ('block_number', 8.14),
                        ('block_number__gt', 8.14),
                        ('block_number__lt', 8.14),
                        ('execution_date__gte', 'execution_date__gte_example'),
                        ('execution_date__lte', 'execution_date__lte_example'),
                        ('execution_date__gt', 'execution_date__gt_example'),
                        ('execution_date__lt', 'execution_date__lt_example'),
                        ('to', 'to_example'),
                        ('token_address', 'token_address_example'),
                        ('transaction_hash', 'transaction_hash_example'),
                        ('value', 8.14),
                        ('value__gt', 8.14),
                        ('value__lt', 8.14),
                        ('limit', 56),
                        ('offset', 56)]
        response = self.client.open(
            '/api/v1/safes/{address}/incoming-transfers/'.format(address='address_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_safes_module_transactions_list(self):
        """Test case for safes_module_transactions_list

        
        """
        query_string = [('safe', 'safe_example'),
                        ('module', 'module_example'),
                        ('to', 'to_example'),
                        ('operation', 'operation_example'),
                        ('failed', 'failed_example'),
                        ('block_number', 8.14),
                        ('block_number__gt', 8.14),
                        ('block_number__lt', 8.14),
                        ('transaction_hash', 'transaction_hash_example'),
                        ('ordering', 'ordering_example'),
                        ('limit', 56),
                        ('offset', 56)]
        response = self.client.open(
            '/api/v1/safes/{address}/module-transactions/'.format(address='address_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_safes_multisig_transactions_create(self):
        """Test case for safes_multisig_transactions_create

        
        """
        data = SafeMultisigTransaction()
        response = self.client.open(
            '/api/v1/safes/{address}/multisig-transactions/'.format(address='address_example'),
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_safes_multisig_transactions_list(self):
        """Test case for safes_multisig_transactions_list

        
        """
        query_string = [('failed', 'failed_example'),
                        ('modified__lt', 'modified__lt_example'),
                        ('modified__gt', 'modified__gt_example'),
                        ('modified__lte', 'modified__lte_example'),
                        ('modified__gte', 'modified__gte_example'),
                        ('nonce__lt', 8.14),
                        ('nonce__gt', 8.14),
                        ('nonce__lte', 8.14),
                        ('nonce__gte', 8.14),
                        ('nonce', 8.14),
                        ('safe_tx_hash', 'safe_tx_hash_example'),
                        ('to', 'to_example'),
                        ('value__lt', 8.14),
                        ('value__gt', 8.14),
                        ('value', 8.14),
                        ('executed', 'executed_example'),
                        ('has_confirmations', 'has_confirmations_example'),
                        ('trusted', 'trusted_example'),
                        ('execution_date__gte', 'execution_date__gte_example'),
                        ('execution_date__lte', 'execution_date__lte_example'),
                        ('submission_date__gte', 'submission_date__gte_example'),
                        ('submission_date__lte', 'submission_date__lte_example'),
                        ('transaction_hash', 'transaction_hash_example'),
                        ('ordering', 'ordering_example'),
                        ('limit', 56),
                        ('offset', 56)]
        response = self.client.open(
            '/api/v1/safes/{address}/multisig-transactions/'.format(address='address_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_safes_read(self):
        """Test case for safes_read

        
        """
        response = self.client.open(
            '/api/v1/safes/{address}/'.format(address='address_example'),
            method='GET',
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_safes_transactions_create(self):
        """Test case for safes_transactions_create

        
        """
        data = SafeMultisigTransaction()
        response = self.client.open(
            '/api/v1/safes/{address}/transactions/'.format(address='address_example'),
            method='POST',
            data=json.dumps(data),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_safes_transactions_list(self):
        """Test case for safes_transactions_list

        
        """
        query_string = [('failed', 'failed_example'),
                        ('modified__lt', 'modified__lt_example'),
                        ('modified__gt', 'modified__gt_example'),
                        ('modified__lte', 'modified__lte_example'),
                        ('modified__gte', 'modified__gte_example'),
                        ('nonce__lt', 8.14),
                        ('nonce__gt', 8.14),
                        ('nonce__lte', 8.14),
                        ('nonce__gte', 8.14),
                        ('nonce', 8.14),
                        ('safe_tx_hash', 'safe_tx_hash_example'),
                        ('to', 'to_example'),
                        ('value__lt', 8.14),
                        ('value__gt', 8.14),
                        ('value', 8.14),
                        ('executed', 'executed_example'),
                        ('has_confirmations', 'has_confirmations_example'),
                        ('trusted', 'trusted_example'),
                        ('execution_date__gte', 'execution_date__gte_example'),
                        ('execution_date__lte', 'execution_date__lte_example'),
                        ('submission_date__gte', 'submission_date__gte_example'),
                        ('submission_date__lte', 'submission_date__lte_example'),
                        ('transaction_hash', 'transaction_hash_example'),
                        ('ordering', 'ordering_example'),
                        ('limit', 56),
                        ('offset', 56)]
        response = self.client.open(
            '/api/v1/safes/{address}/transactions/'.format(address='address_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_safes_transfers_list(self):
        """Test case for safes_transfers_list

        
        """
        query_string = [('_from', '_from_example'),
                        ('block_number', 8.14),
                        ('block_number__gt', 8.14),
                        ('block_number__lt', 8.14),
                        ('execution_date__gte', 'execution_date__gte_example'),
                        ('execution_date__lte', 'execution_date__lte_example'),
                        ('execution_date__gt', 'execution_date__gt_example'),
                        ('execution_date__lt', 'execution_date__lt_example'),
                        ('to', 'to_example'),
                        ('token_address', 'token_address_example'),
                        ('transaction_hash', 'transaction_hash_example'),
                        ('value', 8.14),
                        ('value__gt', 8.14),
                        ('value__lt', 8.14),
                        ('limit', 56),
                        ('offset', 56)]
        response = self.client.open(
            '/api/v1/safes/{address}/transfers/'.format(address='address_example'),
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
