from fastapi import FastAPI
from crud_screenhive import router as screenhive_router

app = FastAPI(
    title="API ScreenHive",
    version="1.0"
)

app.include_router(screenhive_router,
                   prefix="/screenhive", 
                   tags=["ScreenHive"])

# python -m uvicorn main:app --reload