# seed_data.py
from modules.jumbled_words.models import Word, Level
from database import Session, engine

# Copy paste below code to seed level data in routers.py
@router.get("/populate-levels")
def populate_levels(session: Session = Depends(get_session)):
    level_names = [
        "Starter", "Learner", "Explorer", "Achiever", "Champion", "Word Guru"
    ]

    for name in level_names:
        level = Level(name=name)
        session.add(level)
    session.commit()