from fastapi import FastAPI
from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router
from app.db.models import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Budget Tracker API")

app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Budget Tracker API — Welcome!"}

app.include_router(users_router)
