# coding: utf-8
import os
import unittest
from datetime import date
from maxipago import Maxipago, exceptions
from maxipago.utils import payment_processors
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
            first_name='Fulano',
            last_name='de Tal',
        )

        self.assertTrue(getattr(response, 'id', False))

    def test_add_customer_already_existing(self):
        CUSTOMER_ID = randint(1, 100000)

        # creating customer with random id.
        response = self.maxipago.customer.add(
            customer_id=CUSTOMER_ID,
            first_name='Fulano',
            last_name='de Tal',
        )

        self.assertTrue(hasattr(response, 'id'))

        # creating customer with the same id.
        with self.assertRaises(exceptions.CustomerAlreadyExists):
            response = self.maxipago.customer.add(
                customer_id=CUSTOMER_ID,
                first_name='Fulano',
                last_name='de Tal',
            )

    def test_delete_customer(self):
        CUSTOMER_ID = randint(1, 100000)

        # creating customer with random id.
        response = self.maxipago.customer.add(
            customer_id=CUSTOMER_ID,
            first_name='Fulano',
            last_name='de Tal',
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
            first_name=u'Fulano',
            last_name=u'de Tal',
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
            first_name=u'Fulano',
            last_name=u'de Tal',
        )

        self.assertTrue(hasattr(response, 'id'))

        maxipago_customer_id = response.id

        response = self.maxipago.card.add(
            customer_id=maxipago_customer_id,
            number=u'4111111111111111',
            expiration_month=u'02',
            expiration_year=date.today().year + 3,
            billing_name=u'Fulano de Tal',
            billing_address1=u'Rua das Alamedas, 123',
            billing_city=u'Rio de Janeiro',
            billing_state=u'RJ',
            billing_zip=u'20123456',
            billing_country=u'BR',
            billing_phone=u'552140634666',
            billing_email=u'fulano@detal.com',
        )

        self.assertTrue(getattr(response, 'token', False))

    def test_add_card_minimal_fields(self):
        CUSTOMER_ID = randint(1, 100000)

        response = self.maxipago.customer.add(
            customer_id=CUSTOMER_ID,
            first_name=u'Fulano',
            last_name=u'de Tal',
        )

        self.assertTrue(hasattr(response, 'id'))

        maxipago_customer_id = response.id

        response = self.maxipago.card.add(
            customer_id=maxipago_customer_id,
            number=u'4111111111111111',
            expiration_month=u'02',
            expiration_year=date.today().year + 3,
            billing_name=u'Fulano de Tal',
        )

        self.assertTrue(getattr(response, 'token', False))

    def test_delete_card(self):
        CUSTOMER_ID = randint(1, 100000)

        customer_response = self.maxipago.customer.add(
            customer_id=CUSTOMER_ID,
            first_name=u'Fulano',
            last_name=u'de Tal',
        )

        self.assertTrue(hasattr(customer_response, 'id'))

        maxipago_customer_id = customer_response.id

        card_response = self.maxipago.card.add(
            customer_id=maxipago_customer_id,
            number=u'4111111111111111',
            expiration_month=u'02',
            expiration_year=date.today().year + 3,
            billing_name=u'Fulano de Tal',
            billing_address1=u'Rua das Alamedas, 123',
            billing_city=u'Rio de Janeiro',
            billing_state=u'RJ',
            billing_zip=u'20345678',
            billing_country=u'RJ',
            billing_phone=u'552140634666',
            billing_email=u'fulano@detal.com',
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
            processor_id=payment_processors.TEST,
            reference_num=REFERENCE,

            billing_name=u'Fulano de Tal',
            billing_address1=u'Rua das Alamedas, 123',
            billing_city=u'Rio de Janeiro',
            billing_state=u'RJ',
            billing_zip=u'20345678',
            billing_country=u'RJ',
            billing_phone=u'552140634666',
            billing_email=u'fulano@detal.com',

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
            processor_id=payment_processors.TEST,
            reference_num=REFERENCE,

            billing_name=u'Fulano de Tal',
            billing_address1=u'Rua das Alamedas, 123',
            billing_city=u'Rio de Janeiro',
            billing_state=u'RJ',
            billing_zip=u'20345678',
            billing_country=u'RJ',
            billing_phone=u'552140634666',
            billing_email=u'fulano@detal.com',

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
            processor_id=payment_processors.TEST,
            reference_num=REFERENCE,

            billing_name=u'Fulano de Tal',
            billing_address1=u'Rua das Alamedas, 123',
            billing_city=u'Rio de Janeiro',
            billing_state=u'RJ',
            billing_zip=u'20345678',
            billing_country=u'RJ',
            billing_phone=u'552140634666',
            billing_email=u'fulano@detal.com',

            card_number='4111111111111111',
            card_expiration_month=u'02',
            card_expiration_year=date.today().year + 3,
            card_cvv='123',

            charge_total='100.01',
        )

        self.assertFalse(response.authorized)
        self.assertFalse(response.captured)

    def test_payment_direct_with_token(self):
        CUSTOMER_ID = randint(1, 100000)

        response = self.maxipago.customer.add(
            customer_id=CUSTOMER_ID,
            first_name=u'Fulano',
            last_name=u'de Tal',
        )

        self.assertTrue(hasattr(response, 'id'))

        maxipago_customer_id = response.id

        response = self.maxipago.card.add(
            customer_id=maxipago_customer_id,
            number=u'4111111111111111',
            expiration_month=u'02',
            expiration_year=date.today().year + 3,
            billing_name=u'Fulano de Tal',
            billing_address1=u'Rua das Alamedas, 123',
            billing_city=u'Rio de Janeiro',
            billing_state=u'RJ',
            billing_zip=u'20123456',
            billing_country=u'BR',
            billing_phone=u'552140634666',
            billing_email=u'fulano@detal.com',
        )

        self.assertTrue(getattr(response, 'token', False))
        REFERENCE = randint(1, 100000)

        response = self.maxipago.payment.direct(
            processor_id=payment_processors.TEST,
            reference_num=REFERENCE,

            customer_id=maxipago_customer_id,
            token=response.token,

            charge_total='100.00',
        )

        self.assertTrue(response.authorized)
        self.assertTrue(response.captured)

    def test_payment_direct_with_token_decline(self):
        CUSTOMER_ID = randint(1, 100000)

        response = self.maxipago.customer.add(
            customer_id=CUSTOMER_ID,
            first_name=u'Fulano',
            last_name=u'de Tal',
        )

        self.assertTrue(hasattr(response, 'id'))

        maxipago_customer_id = response.id

        response = self.maxipago.card.add(
            customer_id=maxipago_customer_id,
            number=u'4111111111111111',
            expiration_month=u'02',
            expiration_year=date.today().year + 3,
            billing_name=u'Fulano de Tal',
            billing_address1=u'Rua das Alamedas, 123',
            billing_city=u'Rio de Janeiro',
            billing_state=u'RJ',
            billing_zip=u'20123456',
            billing_country=u'BR',
            billing_phone=u'552140634666',
            billing_email=u'fulano@detal.com',
        )

        self.assertTrue(getattr(response, 'token', False))
        REFERENCE = randint(1, 100000)

        response = self.maxipago.payment.direct(
            processor_id=payment_processors.TEST,
            reference_num=REFERENCE,

            customer_id=maxipago_customer_id,
            token=response.token,

            charge_total='100.01',
        )

        self.assertFalse(response.authorized)
        self.assertFalse(response.captured)

    def test_http_exception(self):
        CUSTOMER_ID = randint(1, 100000)
        customer_manager = self.maxipago.customer
        customer_manager.uri_api = 'https://testapi.maxipago.net/UniversalAPI/WrongUri'
        with self.assertRaises(exceptions.HttpErrorException):
            customer_manager.add(
                customer_id=CUSTOMER_ID,
                first_name='Fulano',
                last_name='de Tal',
            )


if __name__ == '__main__':
    unittest.main()
