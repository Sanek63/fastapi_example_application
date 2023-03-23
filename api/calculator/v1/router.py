from fastapi import APIRouter

from app.managers.calculator_manager import CalculatorManager
from core.decorators import response_decorator

from .schemas.response.calculator import (
    CalculateByNativeResponseSchema,
    CalculateByEvalResponseSchema)
from .schemas.request.calculator import (
    CalculateByEvalRequestSchema,
    CalculateByNativeRequestSchema)


router = APIRouter(prefix='/v1')


@router.post(
    "/calculate_eval"
)
@response_decorator
async def calculate_by_eval(
    body: CalculateByEvalRequestSchema
):
    result = await CalculatorManager.calculate_by_eval()
    return CalculateByEvalResponseSchema(
        expression=body.expression,
        expression_result=result
    )


@router.post(
    "/calculate_native"
)
@response_decorator
async def calculate_by_native(
    body: CalculateByNativeRequestSchema
):
    result = await CalculatorManager.calculate_by_native()
    return CalculateByEvalResponseSchema(
        expression=body.expression,
        expression_result=result
    )
