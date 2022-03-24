# coding: utf-8
# from io import StringIO
from maxipago.utils import etree
from maxipago.resources.base import Resource
from maxipago.exceptions import TransactionException


class TransactionResource(Resource):

    def process(self):
        tree = etree.fromstring(self.data)
        header = tree.find('header')
        error_code = header.find('errorCode')
        if error_code is not None and error_code.text != '0':
            error_message = header.find('errorMsg').text
            raise TransactionException(message=error_message)

        transaction = tree.find('result').find('records').find('record')

        fields = [
            ('transactionId', 'transaction_id'),
            ('approvalCode', 'auth_code'),
            ('orderId', 'order_id'),
            ('referenceNumber', 'reference_num'),
            ('transactionDate', 'transaction_date'),
            ('boletoUrl', 'boleto_url'),
            ('responseCode', 'response_code'),
            ('transactionAmount', 'amount'),
            ('transactionStatus', 'status')
        ]

        for f_name, f_translated in fields:
            field = transaction.find(f_name)
            if field is not None:
                setattr(self, f_translated, field.text)

        response_message = tree.find('responseMessage')
        if response_message is not None and response_message.text:
            response_message = response_message.text.lower()
