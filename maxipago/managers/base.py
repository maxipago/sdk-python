# coding: utf-8
import requests
from maxipago.exceptions import HttpErrorException
from maxipago.utils import etree, create_element_recursively


class Manager(object):
    api_type = None

    def __init__(self, maxid, api_key, api_version, sandbox):
        self.maxid = maxid
        self.api_key = api_key
        self.api_version = api_version
        self.sandbox = sandbox

        if sandbox:
            self.uri_transaction = 'https://testapi.maxipago.net/UniversalAPI/postXML'
            self.uri_api = 'https://testapi.maxipago.net/UniversalAPI/postAPI'
            self.uri_rapi = 'https://testapi.maxipago.net/ReportsAPI/servlet/ReportsAPI'
        else:
            self.uri_transaction = 'https://api.maxipago.net/UniversalAPI/postXML'
            self.uri_api = 'https://api.maxipago.net/UniversalAPI/postAPI'
            self.uri_rapi = 'https://api.maxipago.net/ReportsAPI/servlet/ReportsAPI'

    def request(self, xml_data, api_type=None):
        uri = self.get_uri(api_type)
        response = requests.post(url=uri, data=xml_data, headers={'content-type': 'text/xml'})

        if not str(response.status_code).startswith('2'):
            raise HttpErrorException(u'Error %s: %s' % (response.status_code, response.reason))
        return response

    def get_uri(self, api_type=None):
        api_type = api_type or self.uri_rapi

        uri_list = {
            'transaction': self.uri_transaction,
            'api': self.uri_api,
            'rapi': self.uri_rapi,
        }
        return uri_list.get(self.api_type)


class ManagerApi(Manager):
    api_type = 'api'

    def send(self, command, params=None, requester=None, api_type=None, resource=None):
        if not params:
            params = requester.translated_data

        root = etree.Element('api-request')

        verification = etree.SubElement(root, 'verification')
        etree.SubElement(verification, 'merchantId').text = self.maxid
        etree.SubElement(verification, 'merchantKey').text = self.api_key

        etree.SubElement(root, 'command').text = command

        request = etree.SubElement(root, 'request')

        for key, value in params:
            create_element_recursively(request, key).text = value

        xml_data = etree.tostring(root, pretty_print=True, encoding='UTF-8', xml_declaration=True)

        response = self.request(xml_data)
        if resource:
            return resource(data=response.content, requester=requester, manager=self)
        return response


class ManagerTransaction(Manager):
    api_type = 'transaction'

    def send(self, command, params=None, requester=None, api_type=None, resource=None):
        if not params:
            params = requester.translated_data

        root = etree.Element('transaction-request')

        etree.SubElement(root, 'version').text = self.api_version

        verification = etree.SubElement(root, 'verification')
        etree.SubElement(verification, 'merchantId').text = self.maxid
        etree.SubElement(verification, 'merchantKey').text = self.api_key

        order = etree.SubElement(root, 'order')

        command = etree.SubElement(order, command)

        for key, value in params:
            create_element_recursively(command, key).text = value

        xml_data = etree.tostring(root, pretty_print=True, encoding='UTF-8', xml_declaration=True)

        response = self.request(xml_data)
        if resource:
            return resource(data=response.content, requester=requester, manager=self)
        return response


class ManagerRapi(Manager):
    api_type = 'rapi'

    def send(self, command, params=None, requester=None, api_type=None, resource=None):
        if not params:
            params = requester.translated_data

        root = etree.Element('rapi-request')

        etree.SubElement(root, 'version').text = self.api_version

        verification = etree.SubElement(root, 'verification')
        etree.SubElement(verification, 'merchantId').text = self.maxid
        etree.SubElement(verification, 'merchantKey').text = self.api_key

        etree.SubElement(root, 'command').text = command

        request = etree.SubElement(root, 'request')
        options = etree.SubElement(request, 'filterOptions')

        for key, value in params:
            create_element_recursively(options, key).text = value

        xml_data = etree.tostring(root, pretty_print=True, encoding='UTF-8', xml_declaration=True)

        response = self.request(xml_data)
        if resource:
            return resource(data=response.content, requester=requester, manager=self)
        return response
