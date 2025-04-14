from fastapi import FastAPI
from app.routers import table_api

app = FastAPI()
app.include_router(table_api.router)


@app.get("/")
async def root():
    return {"message": "Сервис запущен"}
