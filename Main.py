---

### `main.py`

```python
# main.py

from typing import List
from fastapi import HTTPException
import random

MOVIES_DB = [
    {"id": 1, "title": "Inception", "genres": ["Action", "Sci-Fi"]},
    {"id": 2, "title": "The Shawshank Redemption", "genres": ["Drama"]},
    {"id": 3, "title": "The Dark Knight", "genres": ["Action", "Drama"]},
    {"id": 4, "title": "Interstellar", "genres": ["Sci-Fi", "Adventure"]},
    {"id": 5, "title": "Forrest Gump", "genres": ["Drama", "Romance"]},
]

USER_PROFILES = {}

def create_profile(user_id: str, genres: List[str]):
    USER_PROFILES[user_id] = genres
    return {"message": "Profile saved", "user_id": user_id}

def recommend_movies(user_id: str):
    if user_id not in USER_PROFILES:
        raise HTTPException(status_code=404, detail="User not found")

    prefs = USER_PROFILES[user_id]
    matches = [m for m in MOVIES_DB if any(g in m["genres"] for g in prefs)]
    return matches or random.sample(MOVIES_DB, 2)

def process_feedback(user_id: str, movie_id: int, liked: bool):
    return {"user_id": user_id, "movie_id": movie_id, "liked": liked}
