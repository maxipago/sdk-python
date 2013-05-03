# coding: utf-8
from StringIO import StringIO
from maxipago.utils import etree
from maxipago.resources.base import Resource
from maxipago.exceptions import PaymentException


class PaymentResource(Resource):

    def process(self):
        self.approved = False
        self.authorized = False
        self.captured = False

        tree = etree.parse(StringIO(self.data))
        error_code = tree.find('errorCode')
        if error_code is not None and error_code != '0':
            error_message = tree.find('errorMsg').text
            raise PaymentException(message=error_message)

        processor_code = tree.find('processorCode')
        if processor_code.text.lower() == 'a':
            self.approved = True

        if self.approved:
            response_message = tree.find('transactionID')

        fields = [
            ('transactionID', 'transaction_id'),
            ('authCode', 'auth_code'),
            ('orderID', 'order_id'),
            ('referenceNum', 'reference_num'),
            ('transactionTimestamp', 'transaction_timestamp'),
        ]

        for f_name, f_translated in fields:
            field = tree.find(f_name)
            if field is not None:
                setattr(self, f_translated, field.text)

        response_message = tree.find('responseMessage')
        if response_message is not None and response_message.text:
            response_message = response_message.text.lower()

            if response_message == 'authorized':
                self.authorized = True
            elif response_message == 'captured':
                self.authorized = True
                self.captured = True
