from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.services.fetcher import get_cache_data
from app.routers import users, products


@asynccontextmanager
async def app_lifespan(app: FastAPI):
    # executes when the app starts
    await get_cache_data(refresh= True)

    yield
    # executes when app shuts down

app = FastAPI(lifespan=app_lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # endereço do Vue
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(products.router)

@app.get("/health")
async def root():
    return {"status": "ok"}