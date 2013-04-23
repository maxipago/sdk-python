# coding: utf-8
from StringIO import StringIO
from maxipago.utils import etree
from maxipago.resources.base import Resource
from maxipago.exceptions import CustomerAlreadyExists, CustomerException


class CustomerAddResource(Resource):

    def process(self):
        tree = etree.parse(StringIO(self.data))

        error_code = tree.find('errorCode').text

        if error_code != '0':
            error_message = tree.find('errorMessage').text

            if 'already exists' in error_message.lower():
                raise CustomerAlreadyExists(message=error_message)

            raise CustomerException(message=error_message)

        self._meta = {
            'command': tree.find('command').text,
            'time': tree.find('time').text,
        }

        self.id = tree.find('result').find('customerId').text


class CustomerDeleteResource(Resource):

    def process(self):
        tree = etree.parse(StringIO(self.data))

        error_code = tree.find('errorCode').text

        if error_code != '0':
            error_message = tree.find('errorMessage').text

            raise CustomerException(message=error_message)

        self._meta = {
            'command': tree.find('command').text,
            'time': tree.find('time').text,
        }

        self.success = True


class CustomerUpdateResource(Resource):

    def process(self):
        tree = etree.parse(StringIO(self.data))

        error_code = tree.find('errorCode').text

        if error_code != '0':
            error_message = tree.find('errorMessage').text

            raise CustomerException(message=error_message)

        self._meta = {
            'command': tree.find('command').text,
            'time': tree.find('time').text,
        }

        self.success = True
