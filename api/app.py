from fastapi import FastAPI

from .calculator.app import calculator_subapi


def init_sub_applications(app_: FastAPI):
    app_.mount('/api/calculator/', calculator_subapi)
