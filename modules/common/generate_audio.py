# generate_audio.py
from gtts import gTTS
from models import Word
from db.database import Session, engine
import os

AUDIO_DIR = "../jumbled_words/audio_files"
os.makedirs(AUDIO_DIR, exist_ok=True)

def generate_audio_for_words():
    with Session(engine) as session:
        words = session.query(Word).all()
        for word in words:
            audio_path = f"{AUDIO_DIR}/{word.english_word}.mp3"
            if not os.path.exists(audio_path):
                tts = gTTS(text=word.english_word, lang="en")
                tts.save(audio_path)
                print(f"Generated audio for {word.english_word}")

generate_audio_for_words()
