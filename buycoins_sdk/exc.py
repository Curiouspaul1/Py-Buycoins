class PycoinsException(Exception):
    """
    Buycoins python client error class
    """

    pass


class MissingKeyError(PycoinsException):
    pass


class SendLimitError(PycoinsException):
    pass


class InvalidClientObject(PycoinsException):
    pass
