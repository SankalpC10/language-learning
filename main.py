# main.py
from fastapi import FastAPI
from db.database import create_db_and_tables
from mangum import Mangum
from modules.jumbled_words.routers import router as jumbled_words_router
AUDIO_DIR = "audio_files"

app = FastAPI()
handler = Mangum(app)



app.include_router(jumbled_words_router, prefix="/v1", tags=["Jumbled Words"])

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


@app.get("/")
async def root():
    return {"message": "Welcome to the API"}


