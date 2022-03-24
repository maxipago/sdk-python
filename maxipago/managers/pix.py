# coding: utf-8
from maxipago.managers.base import ManagerTransaction, ManagerApi
from maxipago.requesters.pix import PixRequester


class PixManager(ManagerTransaction):

    def create(self, **kwargs):
        fields = (
            ('processor_id', {'translated_name': 'processorID'}),
            ('reference_num', {'translated_name': 'referenceNum'}),
            ('fraud_check', {'translated_name': 'fraudCheck', 'default': 'N'}),
            ('customer_id', {'translated_name': 'customerIdExt'}),
            ('billing_name', {'translated_name': 'billing/name'}),
            ('billing_address1', {'translated_name': 'billing/address'}),
            ('billing_complement', {'translated_name': 'billing/address2'}),
            ('billing_neighborhood', {'translated_name': 'billing/district'}),
            ('billing_city', {'translated_name': 'billing/city'}),
            ('billing_state', {'translated_name': 'billing/state'}),
            ('billing_zip', {'translated_name': 'billing/postalcode'}),
            ('billing_country', {'translated_name': 'billing/country', 'default': 'BR'}),
            ('billing_phone', {'translated_name': 'billing/phone'}),
            ('billing_email', {'translated_name': 'billing/email'}),
            ('document_type', {'translated_name': 'billing/documents/document/documentType', 'default': 'CPF'}),
            ('document', {'translated_name': 'billing/documents/document/documentValue'}),
            ('expiration_time', {'translated_name': 'transactionDetail/payType/pix/expirationTime'}),
            ('payment_info', {'translated_name': 'transactionDetail/payType/pix/paymentInfo'}),
            ('charge_total', {'translated_name': 'payment/chargeTotal'}),
        )

        requester = PixRequester(fields, kwargs)
        return self.send(command='sale', requester=requester)
