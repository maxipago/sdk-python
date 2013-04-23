# coding: utf-8
from maxipago.managers.base import ManagerRapi
from maxipago.requesters.transaction import TransactionRequester


class TransactionManager(ManagerRapi):

    def get(self, **kwargs):
        fields = (
            ('transaction_id', {'translated_name': 'transactionId'}),
        )
        requester = TransactionRequester(fields, kwargs)
        return self.send(command='transactionDetailReport', requester=requester)

    def list(self, **kwargs):
        fields = (
            ('period', {'translated_name': 'filterOptions/period'}),
            ('page_size', {'translated_name': 'filterOptions/pageSize', 'required': False}),
            ('start_date', {'translated_name': 'filterOptions/startDate', 'required': False}),
            ('end_date', {'translated_name': 'filterOptions/endDate', 'required': False}),
            ('start_time', {'translated_name': 'filterOptions/startTime', 'required': False}),
            ('end_time', {'translated_name': 'filterOptions/endTime', 'required': False}),
            ('order_by', {'translated_name': 'filterOptions/orderByName', 'required': False}),
            ('order_direction', {'translated_name': 'filterOptions/orderByDirection', 'required': False}),
            ('offset', {'translated_name': 'filterOptions/startRecordNumber', 'required': False}),
            ('end_record_number', {'translated_name': 'filterOptions/endRecordNumber', 'required': False}),
            ('page_token', {'translated_name': 'filterOptions/pageToken', 'required': False}),
            ('page_number', {'translated_name': 'filterOptions/pageNumber', 'required': False}),
        )
        requester = TransactionRequester(fields, kwargs)
        return self.send(command='transactionDetailReport', requester=requester)

    def request_status(self, **kwargs):
        fields = (
            ('request_token', {'translated_name': 'requestToken'}),
        )
        requester = TransactionRequester(fields, kwargs)
        return self.send(command='checkRequestStatus', requester=requester)
