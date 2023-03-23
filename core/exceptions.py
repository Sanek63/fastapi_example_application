from .enum import APIResponseStatus


class InvalidRequestData(Exception):
    def __init__(
            self,
            status_code: str = APIResponseStatus.UNEXPECTED_ERROR,
            description: str = ''
    ):
        self.status_code = status_code
        self.description = description
