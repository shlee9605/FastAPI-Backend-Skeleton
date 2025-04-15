import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import connection
from app.routes import router


# app initialization
app = FastAPI()


# CORS config
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# startup and shutdown events
app.add_event_handler("startup", connection.on_app_start)
app.add_event_handler("shutdown", connection.on_app_shutdown)


# routing
app.include_router(router)

# app runs
if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8001,
        reload=True,
    )
