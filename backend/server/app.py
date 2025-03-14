from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from server.routes.somefunction import router as some_function_router
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from server.database import client

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("App is starting...")
    yield
    print("App is shutting down...")
    client.close()

app = FastAPI(lifespan=lifespan)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(some_function_router, tags=["MongoData"], prefix="/some-function")

@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to FSM"}

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=500,
        content={"message": f"An unexpected error occurred: {exc}"}
    )

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail}
    )
