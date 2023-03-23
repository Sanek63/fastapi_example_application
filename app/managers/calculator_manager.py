from core.exceptions import InvalidRequestData
from core.enum import APIResponseStatus


class CalculatorManager:

    @staticmethod
    async def calculate_by_eval():
        return 10
        raise InvalidRequestData(
            description='Name error',
            status_code=APIResponseStatus.ATTRIBUTE_NAME_ERROR
        )


    @staticmethod
    async def calculate_by_native():
        pass
