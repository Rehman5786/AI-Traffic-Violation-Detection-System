class AppException(Exception):
    """
    Base exception for application-level errors.
    """

    def __init__(
        self,
        message: str,
        status_code: int = 400,
    ):
        self.message = message
        self.status_code = status_code

        super().__init__(message)


class UserNotFoundException(AppException):
    """
    Raised when a requested user does not exist.
    """

    def __init__(self):
        super().__init__(
            message="User not found.",
            status_code=404,
        )


class UsernameAlreadyExistsException(AppException):
    """
    Raised when a username is already registered.
    """

    def __init__(self):
        super().__init__(
            message="Username already exists.",
            status_code=409,
        )


class EmailAlreadyExistsException(AppException):
    """
    Raised when an email address is already registered.
    """

    def __init__(self):
        super().__init__(
            message="Email already exists.",
            status_code=409,
        )


class VehicleNotFoundException(AppException):
    """
    Raised when a requested vehicle does not exist.
    """

    def __init__(self):
        super().__init__(
            message="Vehicle not found.",
            status_code=404,
        )


class VehicleRegistrationAlreadyExistsException(AppException):
    """
    Raised when a vehicle registration number is already registered.
    """

    def __init__(self):
        super().__init__(
            message="Vehicle registration number already exists.",
            status_code=409,
        )


class CameraNotFoundException(AppException):
    """
    Raised when a requested camera does not exist.
    """

    def __init__(self):
        super().__init__(
            message="Camera not found.",
            status_code=404,
        )


class CameraNameAlreadyExistsException(AppException):
    """
    Raised when a camera name is already registered.
    """

    def __init__(self):
        super().__init__(
            message="Camera name already exists.",
            status_code=409,
        )