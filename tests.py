# coding: utf-8
import os
import unittest
from datetime import date
from maxipago import Maxipago, exceptions
from random import randint


MAXIPAGO_ID = os.getenv('MAXIPAGO_ID')
MAXIPAGO_API_KEY = os.getenv('MAXIPAGO_API_KEY')


class MaxipagoTestCase(unittest.TestCase):

    def setUp(self):
        self.maxipago = Maxipago(MAXIPAGO_ID, MAXIPAGO_API_KEY, sandbox=True)

    def test_add_customer(self):
        CUSTOMER_ID = randint(1, 100000)

        response = self.maxipago.customer.add(
            customer_id=CUSTOMER_ID,
            first_name='Vinicius',
            last_name='Cainelli',
        )

        self.assertTrue(getattr(response, 'id', False))

    def test_add_customer_already_existing(self):
        CUSTOMER_ID = randint(1, 100000)

        # creating customer with random id.
        response = self.maxipago.customer.add(
            customer_id=CUSTOMER_ID,
            first_name='Vinicius',
            last_name='Cainelli',
        )

        self.assertTrue(hasattr(response, 'id'))

        # creating customer with the same id.
        with self.assertRaises(exceptions.CustomerAlreadyExists):
            response = self.maxipago.customer.add(
                customer_id=CUSTOMER_ID,
                first_name='Vinicius',
                last_name='Cainelli',
            )

    def test_delete_customer(self):
        CUSTOMER_ID = randint(1, 100000)

        # creating customer with random id.
        response = self.maxipago.customer.add(
            customer_id=CUSTOMER_ID,
            first_name='Vinicius',
            last_name='Cainelli',
        )

        self.assertTrue(hasattr(response, 'id'))

        maxipago_customer_id = response.id

        response = self.maxipago.customer.delete(
            id=maxipago_customer_id,
        )

    def test_update_customer(self):
        CUSTOMER_ID = randint(1, 100000)

        # creating customer with random id.
        response = self.maxipago.customer.add(
            customer_id=CUSTOMER_ID,
            first_name=u'Vinicius',
            last_name=u'Cainelli',
        )

        self.assertTrue(hasattr(response, 'id'))

        maxipago_customer_id = response.id

        response = self.maxipago.customer.update(
            id=maxipago_customer_id,
            customer_id=CUSTOMER_ID,
            first_name=u'Antonio',
        )

    def test_add_card(self):
        CUSTOMER_ID = randint(1, 100000)

        response = self.maxipago.customer.add(
            customer_id=CUSTOMER_ID,
            first_name=u'Vinicius',
            last_name=u'Cainelli',
        )

        self.assertTrue(hasattr(response, 'id'))

        maxipago_customer_id = response.id

        response = self.maxipago.card.add(
            customer_id=maxipago_customer_id,
            number=u'4111111111111111',
            expiration_month=u'02',
            expiration_year=date.today().year + 3,
            billing_name=u'Vinicius Cainelli',
            billing_address1=u'Rua das Alamedas, 123',
            billing_city=u'Ribeirão Preto',
            billing_state=u'SP',
            billing_zip=u'14030360',
            billing_country=u'BR',
            billing_phone=u'1612341234',
            billing_email=u'me@vinicius.ca',
        )

        self.assertTrue(getattr(response, 'token', False))

    def test_delete_card(self):
        CUSTOMER_ID = randint(1, 100000)

        customer_response = self.maxipago.customer.add(
            customer_id=CUSTOMER_ID,
            first_name=u'Vinicius',
            last_name=u'Cainelli',
        )

        self.assertTrue(hasattr(customer_response, 'id'))

        maxipago_customer_id = customer_response.id

        card_response = self.maxipago.card.add(
            customer_id=maxipago_customer_id,
            number=u'4111111111111111',
            expiration_month=u'02',
            expiration_year=date.today().year + 3,
            billing_name=u'Vinicius Cainelli',
            billing_address1=u'Rua das Alamedas, 123',
            billing_city=u'Ribeirão Preto',
            billing_state=u'SP',
            billing_zip=u'14030360',
            billing_country=u'BR',
            billing_phone=u'1612341234',
            billing_email=u'me@vinicius.ca',
        )

        self.assertTrue(getattr(card_response, 'token', False))

        token = card_response.token

        response = self.maxipago.card.delete(
            customer_id=maxipago_customer_id,
            token=token,
        )

        self.assertTrue(getattr(response, 'success', False))

    def test_payment_authorize(self):
        REFERENCE = randint(1, 100000)

        response = self.maxipago.payment.authorize(
            processor_id=1,
            reference_num=REFERENCE,

            billing_name=u'Vinicius Cainelli',
            billing_address1=u'Rua das Alamedas, 123',
            billing_city=u'Ribeirão Preto',
            billing_state=u'SP',
            billing_zip=u'14030360',
            billing_country=u'BR',
            billing_phone=u'1612341234',
            billing_email=u'me@vinicius.ca',

            card_number='4111111111111111',
            card_expiration_month=u'02',
            card_expiration_year=date.today().year + 3,
            card_cvv='123',

            charge_total='100.00',
        )

        self.assertTrue(response.authorized)
        self.assertFalse(response.captured)

    def test_payment_direct(self):
        REFERENCE = randint(1, 100000)

        response = self.maxipago.payment.direct(
            processor_id=1,
            reference_num=REFERENCE,

            billing_name=u'Vinicius Cainelli',
            billing_address1=u'Rua das Alamedas, 123',
            billing_city=u'Ribeirão Preto',
            billing_state=u'SP',
            billing_zip=u'14030360',
            billing_country=u'BR',
            billing_phone=u'1612341234',
            billing_email=u'me@vinicius.ca',

            card_number='4111111111111111',
            card_expiration_month=u'02',
            card_expiration_year=date.today().year + 3,
            card_cvv='123',

            charge_total='100.00',
        )

        self.assertTrue(response.authorized)
        self.assertTrue(response.captured)

    def test_payment_direct_declined(self):
        REFERENCE = randint(1, 100000)

        response = self.maxipago.payment.direct(
            processor_id=1,
            reference_num=REFERENCE,

            billing_name=u'Vinicius Cainelli',
            billing_address1=u'Rua das Alamedas, 123',
            billing_city=u'Ribeirão Preto',
            billing_state=u'SP',
            billing_zip=u'14030360',
            billing_country=u'BR',
            billing_phone=u'1612341234',
            billing_email=u'me@vinicius.ca',

            card_number='4111111111111111',
            card_expiration_month=u'02',
            card_expiration_year=date.today().year + 3,
            card_cvv='123',

            charge_total='100.01',
        )

        self.assertFalse(response.authorized)
        self.assertFalse(response.captured)

if __name__ == '__main__':
    unittest.main()
