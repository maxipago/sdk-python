# coding: utf-8
from .base import ManagerApi
from maxipago.requesters.customer import CustomerRequester
from maxipago.resources.customer import CustomerAddResource, CustomerDeleteResource, CustomerUpdateResource


class CustomerManager(ManagerApi):

    def add(self, **kwargs):
        fields = (
            ('customer_id', {'translated_name': 'customerIdExt'}),
            ('first_name', {'translated_name': 'firstName'}),
            ('last_name', {'translated_name': 'lastName'}),
            ('address1', {'required': False}),
            ('address2', {'required': False}),
            ('city', {'required': False}),
            ('state', {'required': False}),
            ('zip_code', {'required': False, 'translated_name': 'zip'}),
            ('phone', {'required': False}),
            ('email', {'required': False}),
            ('birth_date', {'required': False, 'translated_name': 'dob'}),
            ('ssn', {'required': False}),
            ('sex', {'required': False}),
        )
        requester = CustomerRequester(fields, kwargs)
        return self.send(command='add-consumer', requester=requester, resource=CustomerAddResource)

    def delete(self, **kwargs):
        fields = (
            ('id', {'translated_name': 'customerId'}),
        )
        requester = CustomerRequester(fields, kwargs)
        return self.send(command='delete-consumer', requester=requester, resource=CustomerDeleteResource)

    def update(self, **kwargs):
        fields = (
            ('id', {'translated_name': 'customerId'}),
            ('customer_id', {'translated_name': 'customerIdExt'}),
            ('first_name', {'required': False, 'blank': True, 'translated_name': 'firstName'}),
            ('last_name', {'required': False, 'blank': True, 'translated_name': 'lastName'}),
            ('address1', {'required': False, 'blank': True}),
            ('address2', {'required': False, 'blank': True}),
            ('city', {'required': False, 'blank': True}),
            ('state', {'required': False, 'blank': True}),
            ('zip_code', {'required': False, 'blank': True, 'translated_name': 'zip'}),
            ('phone', {'required': False, 'blank': True}),
            ('email', {'required': False, 'blank': True}),
            ('birth_date', {'required': False, 'blank': True, 'translated_name': 'dob'}),
            ('ssn', {'required': False, 'blank': True}),
            ('sex', {'required': False, 'blank': True}),
        )
        requester = CustomerRequester(fields, kwargs)
        return self.send(command='update-consumer', requester=requester, resource=CustomerUpdateResource)
