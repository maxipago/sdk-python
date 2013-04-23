# coding: utf-8
from .base import ManagerApi
from maxipago.requesters.card import CardRequester
from maxipago.resources.card import CardAddResource, CardDeleteResource


class CardManager(ManagerApi):

    def add(self, **kwargs):
        fields = (
            ('customer_id', {'translated_name': 'customerId'}),
            ('number', {'translated_name': 'creditCardNumber'}),
            ('expiration_month', {'translated_name': 'expirationMonth'}),
            ('expiration_year', {'translated_name': 'expirationYear'}),
            ('billing_name', {'translated_name': 'billingName'}),
            ('billing_address1', {'translated_name': 'billingAddress1'}),
            ('billing_address2', {'translated_name': 'billingAddress2', 'required': False}),
            ('billing_city', {'translated_name': 'billingCity'}),
            ('billing_state', {'translated_name': 'billingState'}),
            ('billing_zip', {'translated_name': 'billingZip'}),
            ('billing_country', {'translated_name': 'billingCountry'}),
            ('billing_phone', {'translated_name': 'billingPhone'}),
            ('billing_email', {'translated_name': 'billingEmail'}),
            ('onfile_end_date', {'translated_name': 'onFileEndDate', 'required': False}),
            ('onfile_permissions', {'translated_name': 'onFilePermissions', 'required': False}),
            ('onfile_comment', {'translated_name': 'onFileComment', 'required': False}),
            ('onfile_max_charge_amount', {'translated_name': 'onFileMaxChargeAmount', 'required': False}),
        )
        requester = CardRequester(fields, kwargs)
        return self.send(command='add-card-onfile', requester=requester, resource=CardAddResource)

    def delete(self, **kwargs):
        fields = (
            ('customer_id', {'translated_name': 'customerId'}),
            ('token', {}),
        )
        requester = CardRequester(fields, kwargs)
        return self.send(command='delete-card-onfile', requester=requester, resource=CardDeleteResource)
