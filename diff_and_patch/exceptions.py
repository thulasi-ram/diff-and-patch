class InvalidDelta(ValueError):
    def __init__(self, message, errors=None):
        self.message = message
        self.errors = errors
        super(InvalidDelta, self).__init__(message=self.message)


class NoDelta(InvalidDelta):

    def __init__(self, message=''):
        self.message = "No difference detected {m}".format(m=message)
        super(NoDelta, self).__init__(message=self.message)


class PartialSuccess(Exception):

    def __init__(self, message, successes=None, errors=None):
        self.message = message
        self.successes = successes if successes else []
        self.errors = errors if errors else []

        super(PartialSuccess, self).__init__(message)
