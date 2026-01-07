from fastapi import FastAPI

app = FastAPI(title="Budget Tracker API")

@app.get("/")
async def root():
    return {"message": "Budget Tracker API - Welcome!"}