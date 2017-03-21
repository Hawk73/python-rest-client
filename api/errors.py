class ApiError(StandardError):
    """ Base class for API errors. """


class UnauthorizedError(ApiError):
    """ Base class for unauthorized error. """
