# coding: utf-8


class MaxipagoException(Exception):
    def __init__(self, message, code=None):
        self.message = message
        self.code = code

    def __str__(self):
        if self.code:
            return u"({}) {}".format(self.code, self.message)
        else:
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
