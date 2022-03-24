# coding: utf-8
from urllib.parse import urlencode
from hashlib import md5
from maxipago.managers.base import ManagerTransaction
from maxipago.requesters.payment import PaymentRequester
from maxipago.resources.payment import PaymentResource


class PaymentManager(ManagerTransaction):

    def authorize(self, **kwargs):
        fields = (
            ('processor_id', {'translated_name': 'processorID'}),
            ('reference_num', {'translated_name': 'referenceNum'}),
            ('fraud_check', {'translated_name': 'fraudCheck', 'required': False}),
            ('ip_address', {'translated_name': 'ipAddress', 'required': False}),

            ('billing_name', {'translated_name': 'billing/name', 'required': False}),
            ('billing_address', {'translated_name': 'billing/address', 'required': False}),
            ('billing_address2', {'translated_name': 'billing/address2', 'required': False}),
            ('billing_city', {'translated_name': 'billing/city', 'required': False}),
            ('billing_state', {'translated_name': 'billing/state', 'required': False}),
            ('billing_postalcode', {'translated_name': 'billing/postalcode', 'required': False}),
            ('billing_country', {'translated_name': 'billing/country', 'required': False}),
            ('billing_phone', {'translated_name': 'billing/phone', 'required': False}),
            ('billing_email', {'translated_name': 'billing/email', 'required': False}),

            ('shipping_name', {'translated_name': 'shipping/name', 'required': False}),
            ('shipping_address', {'translated_name': 'shipping/address', 'required': False}),
            ('shipping_address2', {'translated_name': 'shipping/address2', 'required': False}),
            ('shipping_city', {'translated_name': 'shipping/city', 'required': False}),
            ('shipping_state', {'translated_name': 'shipping/state', 'required': False}),
            ('shipping_postalcode', {'translated_name': 'shipping/postalcode', 'required': False}),
            ('shipping_country', {'translated_name': 'shipping/country', 'required': False}),
            ('shipping_phone', {'translated_name': 'shipping/phone', 'required': False}),
            ('shipping_email', {'translated_name': 'shipping/email', 'required': False}),

            ('card_number', {'translated_name': 'transactionDetail/payType/creditCard/number', 'required': False}),
            ('card_expiration_month', {'translated_name': 'transactionDetail/payType/creditCard/expMonth', 'required': False}),
            ('card_expiration_year', {'translated_name': 'transactionDetail/payType/creditCard/expYear', 'required': False}),
            ('card_cvv', {'translated_name': 'transactionDetail/payType/creditCard/cvvNumber', 'required': False}),

            ('customer_id', {'translated_name': 'transactionDetail/payType/onFile/customerId', 'required': False}),
            ('token', {'translated_name': 'transactionDetail/payType/onFile/token', 'required': False}),

            ('charge_total', {'translated_name': 'payment/chargeTotal'}),
            ('installments', {'translated_name': 'payment/creditInstallment/numberOfInstallments', 'required': False}),
            ('installments_interest', {'translated_name': 'payment/creditInstallment/chargeInterest', 'required': False}),
        )

        requester = PaymentRequester(fields, kwargs)
        return self.send(command='auth', requester=requester, resource=PaymentResource)

    def capture(self, **kwargs):
        fields = (
            ('order_id', {'translated_name': 'orderID'}),
            ('reference_num', {'translated_name': 'referenceNum'}),

            ('ip_address', {'translated_name': 'ipAddress', 'required': False}),
            ('charge_total', {'translated_name': 'payment/chargeTotal'}),
        )

        requester = PaymentRequester(fields, kwargs)
        return self.send(command='capture', requester=requester, resource=PaymentResource)

    def direct(self, **kwargs):
        fields = (
            ('processor_id', {'translated_name': 'processorID'}),
            ('reference_num', {'translated_name': 'referenceNum'}),
            ('fraud_check', {'translated_name': 'fraudCheck', 'required': False}),

            ('ip_address', {'translated_name': 'ipAddress', 'required': False}),

            ('billing_name', {'translated_name': 'billing/name', 'required': False}),
            ('billing_address', {'translated_name': 'billing/address', 'required': False}),
            ('billing_address2', {'translated_name': 'billing/address2', 'required': False}),
            ('billing_city', {'translated_name': 'billing/city', 'required': False}),
            ('billing_state', {'translated_name': 'billing/state', 'required': False}),
            ('billing_postalcode', {'translated_name': 'billing/postalcode', 'required': False}),
            ('billing_country', {'translated_name': 'billing/country', 'required': False}),
            ('billing_phone', {'translated_name': 'billing/phone', 'required': False}),
            ('billing_email', {'translated_name': 'billing/email', 'required': False}),

            ('shipping_name', {'translated_name': 'shipping/name', 'required': False}),
            ('shipping_address', {'translated_name': 'shipping/address', 'required': False}),
            ('shipping_address2', {'translated_name': 'shipping/address2', 'required': False}),
            ('shipping_city', {'translated_name': 'shipping/city', 'required': False}),
            ('shipping_state', {'translated_name': 'shipping/state', 'required': False}),
            ('shipping_postalcode', {'translated_name': 'shipping/postalcode', 'required': False}),
            ('shipping_country', {'translated_name': 'shipping/country', 'required': False}),
            ('shipping_phone', {'translated_name': 'shipping/phone', 'required': False}),
            ('shipping_email', {'translated_name': 'shipping/email', 'required': False}),

            ('card_number', {'translated_name': 'transactionDetail/payType/creditCard/number', 'required': False}),
            ('card_expiration_month', {'translated_name': 'transactionDetail/payType/creditCard/expMonth', 'required': False}),
            ('card_expiration_year', {'translated_name': 'transactionDetail/payType/creditCard/expYear', 'required': False}),
            ('card_cvv', {'translated_name': 'transactionDetail/payType/creditCard/cvvNumber', 'required': False}),

            ('customer_id', {'translated_name': 'transactionDetail/payType/onFile/customerId', 'required': False}),
            ('token', {'translated_name': 'transactionDetail/payType/onFile/token', 'required': False}),

            ('charge_total', {'translated_name': 'payment/chargeTotal'}),
            ('installments', {'translated_name': 'payment/creditInstallment/numberOfInstallments', 'required': False}),
            ('installments_interest', {'translated_name': 'payment/creditInstallment/chargeInterest', 'required': False}),
        )

        requester = PaymentRequester(fields, kwargs)
        return self.send(command='sale', requester=requester, resource=PaymentResource)

    def cancel(self, **kwargs):
        fields = (
            ('transaction_id', {'translated_name': 'transactionID'}),
        )

        requester = PaymentRequester(fields, kwargs)
        return self.send(command='void', requester=requester, resource=PaymentResource)

    def chargeback(self, **kwargs):
        fields = (
            ('order_id', {'translated_name': 'orderID'}),
            ('reference_num', {'translated_name': 'referenceNum'}),
            ('charge_total', {'translated_name': 'payment/chargeTotal'}),
        )

        requester = PaymentRequester(fields, kwargs)
        return self.send(command='return', requester=requester, resource=PaymentResource)

    def bank_slip(self, **kwargs):
        fields = (
            ('processor_id', {'translated_name': 'processorID'}),
            ('reference_num', {'translated_name': 'referenceNum'}),
            ('ip_address', {'translated_name': 'ipAddress', 'required': False}),

            ('billing_name', {'translated_name': 'billing/name'}),
            ('billing_address', {'translated_name': 'billing/address', 'required': False}),
            ('billing_address2', {'translated_name': 'billing/address2', 'required': False}),
            ('billing_city', {'translated_name': 'billing/city', 'required': False}),
            ('billing_state', {'translated_name': 'billing/state', 'required': False}),
            ('billing_postalcode', {'translated_name': 'billing/postalcode', 'required': False}),
            ('billing_country', {'translated_name': 'billing/country', 'required': False}),
            ('billing_phone', {'translated_name': 'billing/phone', 'required': False}),
            ('billing_email', {'translated_name': 'billing/email', 'required': False}),

            ('shipping_name', {'translated_name': 'shipping/name', 'required': False}),
            ('shipping_address', {'translated_name': 'shipping/address', 'required': False}),
            ('shipping_address2', {'translated_name': 'shipping/address2', 'required': False}),
            ('shipping_city', {'translated_name': 'shipping/city', 'required': False}),
            ('shipping_state', {'translated_name': 'shipping/state', 'required': False}),
            ('shipping_postalcode', {'translated_name': 'shipping/postalcode', 'required': False}),
            ('shipping_country', {'translated_name': 'shipping/country', 'required': False}),
            ('shipping_phone', {'translated_name': 'shipping/phone', 'required': False}),
            ('shipping_email', {'translated_name': 'shipping/email', 'required': False}),

            ('expiration_date', {'translated_name': 'transactionDetail/payType/boleto/expirationDate'}),
            ('number', {'translated_name': 'transactionDetail/payType/boleto/number'}),
            ('instructions', {'translated_name': 'transactionDetail/payType/boleto/instructions', 'required': False}),

            ('charge_total', {'translated_name': 'payment/chargeTotal'}),
        )

        requester = PaymentRequester(fields, kwargs)
        return self.send(command='sale', requester=requester, resource=PaymentResource)

    def get_fraud_check_iframe(self, **kwargs):
        fields = (
            ('order_id', {}),
        )
        requester = PaymentRequester(fields, kwargs)

        params = {
            'm': self.maxid,
            's': requester.cleaned_data.get('order_id'),
            'h': md5('{0}*{1}'.format(self.maxid, requester.cleaned_data.get('order_id'))).hexdigest()
        }

        url = 'https://testauthentication.maxipago.net/redirection_service/logo?{0}'.format(urlencode(params))
        return '<iframe width="1" height="1" frameborder="0" src="{0}"></iframe>'.format(url)
