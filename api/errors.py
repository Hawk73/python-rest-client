class ApiError(StandardError):
    """ Base class for API errors. """


class NotFoundError(ApiError):
    """ Base class for not found error. """


class UnauthorizedError(ApiError):
    """ Base class for unauthorized error. """


class UnknownError(ApiError):
    """ Base class for unknown error. """
