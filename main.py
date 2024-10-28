# main.py
from fastapi import FastAPI
from db.database import create_db_and_tables
from mangum import Mangum
from modules.jumbled_words.routers import router as jumbled_words_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
handler = Mangum(app)

# Set up CORS middleware
origins = [
    "http://localhost:8000",
    "https://production-api.fernglasz.in",
    "https://staging-api.fernglasz.in",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(jumbled_words_router, prefix="/v1", tags=["Jumbled Words"])

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def root():
    return {"message": "Welcome to the API"}


