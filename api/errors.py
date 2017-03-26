class ApiError(StandardError):
    """ Base class for API errors. """


class UnauthorizedError(ApiError):
    """ Base class for unauthorized error. """


class NotFoundError(ApiError):
    """ Base class for not found error. """
