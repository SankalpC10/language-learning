from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    try:
        DATABASE_URL: str = os.environ['DATABASE_URL']
    except:
        DATABASE_URL: str = os.getenv('DATABASE_URL')

settings = Settings()