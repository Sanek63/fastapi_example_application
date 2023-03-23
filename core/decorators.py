from functools import wraps
from logging import getLogger
from traceback import print_exc

from fastapi import status
from fastapi.responses import ORJSONResponse

from api.base.response import BaseResponseModel
from core.exceptions import InvalidRequestData
from core.enum import APIResponseStatus


logger = getLogger(__name__)


def response_decorator(handler):
    @wraps(handler)
    async def wrapper(*args, **kwargs):
        try:
            response = await handler(*args, **kwargs)
            return BaseResponseModel(result=response)

        except InvalidRequestData as err:
            response_body = BaseResponseModel(
                result={},
                error_message=err.description,
                status=err.status_code
            )
            return ORJSONResponse(
                content=response_body.dict(),
                status_code=status.HTTP_400_BAD_REQUEST,
            )

        except Exception:
            print_exc()
            response_body = BaseResponseModel(
                result={},
                error_message="API unexpected error.",
                status=APIResponseStatus.UNEXPECTED_ERROR
            )
            return ORJSONResponse(
                content=response_body.dict(),
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    return wrapper
