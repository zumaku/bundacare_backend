from fastapi import FastAPI
from app.routers import home, user, nutrition, predict
from pathlib import Path

app = FastAPI()

# Registrasi Router
app.include_router(home.router)
app.include_router(user.router)
app.include_router(nutrition.router)
app.include_router(predict.router)
