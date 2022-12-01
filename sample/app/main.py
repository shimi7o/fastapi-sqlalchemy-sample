from fastapi import FastAPI
from routers import pair1, pair2, pair3

app = FastAPI()
api_base_path = "/api/v1"
app.include_router(pair1.router, prefix=api_base_path)
app.include_router(pair2.router, prefix=api_base_path)
app.include_router(pair3.router, prefix=api_base_path)
