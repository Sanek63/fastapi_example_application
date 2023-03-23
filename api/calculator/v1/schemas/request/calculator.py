from pydantic import BaseModel


class CalculateByEvalRequestSchema(BaseModel):
    expression: str
    attributes: dict


class CalculateByNativeRequestSchema(BaseModel):
    expression: str
    attributes: dict
