from sqlmodel import Field, SQLModel
from typing import Optional, List
import uuid
from sqlmodel import SQLModel, Field, Relationship


class Level(SQLModel, table=True):
    id: bytes = Field(default_factory=lambda: uuid.uuid4().bytes, primary_key=True, nullable=False)
    name: str = Field(index=True, unique=True)  # e.g., Starter, Learner, Explorer, etc.
    description: str = Field(default="")  # Optional description for the level

    # Relationship with words
    words: List["Word"] = Relationship(back_populates="level")


class Word(SQLModel, table=True):
    id: bytes = Field(default_factory=lambda: uuid.uuid4().bytes, primary_key=True, nullable=False)
    english_word: str = Field(index=True)
    pronunciation: str  # URL to audio file
    hindi_meaning: str

    # Foreign key to the level table, using bytes
    level_id: Optional[bytes] = Field(default=None, foreign_key="level.id")
    level: Optional[Level] = Relationship(back_populates="words")


class WordCreate(SQLModel):
    english_word: str
    hindi_meaning: str