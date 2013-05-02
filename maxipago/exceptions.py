# coding: utf-8


class MaxipagoException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class ValidationError(MaxipagoException):
    def __repr__(self):
        return 'ValidationError(%s)' % self.message


# customer
class CustomerException(MaxipagoException):
    pass


class CustomerAlreadyExists(CustomerException):
    pass


class CardException(MaxipagoException):
    pass


class PaymentException(MaxipagoException):
    pass


#http
class HttpErrorException(MaxipagoException):
    pass
