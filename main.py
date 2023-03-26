from fastapi import FastAPI, Depends
import models
from database import engine
from routes import customers,scanner

app = FastAPI(title="MedBuddy APIs")

models.Base.metadata.create_all(engine)

app.include_router(customers.router)
app.include_router(scanner.router)


@app.get('/')
async def home():
    return "Welcome to MedBuddy APIs, use authorised API Key to access all the APIs. Thank you!"