# coding: utf-8
from maxipago.managers.base import ManagerTransaction, ManagerApi
from maxipago.requesters.link import LinkRequester
from maxipago.resources.link import LinkResource


class LinkManager(ManagerApi):

    def create(self, **kwargs):
        fields = (
            ('consumer_authentication', {'translated_name': 'consumerAuthentication', 'default': 'N'}),
            ('reference_num', {'translated_name': 'referenceNum'}),
            ('fraud_check', {'translated_name': 'fraudCheck', 'default': 'N'}),

            ('billing_email', {'translated_name': 'billing/email'}),
            ('billing_language', {'translated_name': 'billing/language', 'default': 'pt'}),
            ('billing_name', {'translated_name': 'billing/firstName'}),
            ('customer_id', {'translated_name': 'billing/customerIdExt'}),

            ('payment_info', {'translated_name': 'transactionDetail/description'}),
            ('email_subject', {'translated_name': 'transactionDetail/emailSubject'}),
            ('expiration_date', {'translated_name': 'transactionDetail/expirationDate', 'required': False}),
            ('accept_pix', {'translated_name': 'transactionDetail/acceptPix', 'default': 'Y'}),
            ('amount', {'translated_name': 'transactionDetail/payType/creditCard/amount'}),
            ('soft_descriptor', {'translated_name': 'transactionDetail/payType/creditCard/softDescriptor'}),
        )

        requester = LinkRequester(fields, kwargs)
        return self.send(command='add-payment-order', requester=requester, resource=LinkResource)
