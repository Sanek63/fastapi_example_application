from fastapi import FastAPI

from .v1.router import router as router_v1


calculator_subapi = FastAPI()
calculator_subapi.include_router(router_v1)

# add some exceptions handler
