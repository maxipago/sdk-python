# coding: utf-8
# from io import StringIO
from maxipago.utils import etree
from maxipago.resources.base import Resource
from maxipago.exceptions import TransactionException


class LinkResource(Resource):

    def process(self):
        tree = etree.fromstring(self.data)
        error_code = tree.find('errorCode')
        if error_code is not None and error_code.text != '0':
            error_message = tree.find('errorMessage').text
            raise TransactionException(message=error_message)

        result = tree.find('result')

        fields = [
            ('url', 'url'),
            ('pay_order_id', 'pay_order_id'),
            ('message', 'message')
        ]

        for f_name, f_translated in fields:
            field = result.find(f_name)
            if field is not None:
                setattr(self, f_translated, field.text)
