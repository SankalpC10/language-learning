from fastapi import Depends, APIRouter,HTTPException
from fastapi.responses import FileResponse
from fastapi.responses import StreamingResponse
from sqlmodel import Session, select
from modules.jumbled_words.models import Word, WordCreate, Level
from db.database import get_session
import random
import os
from gtts import gTTS
from uuid import UUID
from io import BytesIO

AUDIO_DIR = "modules/jumbled_words/audio_files"

router = APIRouter()


@router.get("/random_word")
def get_random_word(level_name: str, session: Session = Depends(get_session)):
    level = session.exec(select(Level).where(Level.name == level_name)).first()
    if not level:
        raise HTTPException(status_code=404, detail="Level not found")

    words = session.exec(select(Word).where(Word.level_id == level.id)).all()
    if not words:
        raise HTTPException(status_code=404, detail=f"No words available for level: {level_name}")

    chosen_word = random.choice(words)
    jumbled_word = ''.join(random.sample(chosen_word.english_word, len(chosen_word.english_word)))

    return {
        "hindi_word": chosen_word.hindi_meaning,
        "jumbled_word": jumbled_word,
        "word_id": str(UUID(bytes=chosen_word.id)),  # Convert bytea to UUID string
        "level": level.name,
        "audio_url": f"/audio/{chosen_word.english_word}"
    }

@router.get("/audio/{word}", response_class=FileResponse)
def get_audio(word: str):
    audio_path = f"{AUDIO_DIR}/{word}.mp3"
    if not os.path.exists(audio_path):
        raise HTTPException(status_code=404, detail="Audio not found")
    return FileResponse(audio_path, media_type="audio/mpeg")


@router.post("/add_word")
def add_word(word: WordCreate, level_name: str, session: Session = Depends(get_session)):
    # Find the level by name
    level = session.exec(select(Level).where(Level.name == level_name)).first()
    if not level:
        raise HTTPException(status_code=404, detail="Level not found")

    # Check if the word already exists
    existing_word = session.exec(select(Word).where(Word.english_word == word.english_word)).first()
    if existing_word:
        raise HTTPException(status_code=400, detail="Word already exists")

    new_word = Word(
        english_word=word.english_word,
        pronunciation="",
        hindi_meaning=word.hindi_meaning,
        level_id=level.id
    )
    session.add(new_word)
    session.commit()
    session.refresh(new_word)

    audio_path = os.path.join(AUDIO_DIR, f"{new_word.english_word}.mp3")
    tts = gTTS(text=new_word.english_word, lang="en")
    tts.save(audio_path)

    new_word.pronunciation = audio_path
    session.add(new_word)
    session.commit()

    return {
        "message": "Word added successfully",
        "word_id": str(UUID(bytes=new_word.id)),
        "level": level.name
    }


@router.get("/generate_audio")
def generate_audio(word: str, language: str = "en", session: Session = Depends(get_session)):
    # Fetch the word from the database
    word_data = session.exec(select(Word).where(Word.english_word == word)).first()
    if not word_data:
        raise HTTPException(status_code=404, detail="Word not found in the database")

    # Determine the text to use based on the language parameter
    text_to_speak = word_data.hindi_meaning if language == "hi" else word_data.english_word

    # Generate audio with gTTS
    try:
        tts = gTTS(text=text_to_speak, lang=language)
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)  # Reset pointer to the start of the BytesIO buffer

        # Stream the audio file as an mp3 response
        return StreamingResponse(audio_bytes, media_type="audio/mpeg")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating audio: {str(e)}")
