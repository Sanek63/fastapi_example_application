from pydantic import BaseModel
from typing import Any


class CalculateByEvalResponseSchema(BaseModel):
    expression: str
    expression_result: int | float


class CalculateByNativeResponseSchema(BaseModel):
    expression: str
    expression_result: int | float
