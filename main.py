from fastapi import FastAPI

from accounts import router as accounts_router
from api import router as api_router

app = FastAPI()


app.include_router(
    accounts_router.app,
    prefix="/accounts",
    tags=["accounts"],
)


app.include_router(
    api_router.app,
    prefix="/api",
    tags=["api"],
)
