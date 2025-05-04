# test_model.py

import main

def test_create_profile():
    user_id = "user1"
    genres = ["Drama", "Sci-Fi"]
    result = main.create_profile(user_id, genres)
    assert result["user_id"] == user_id

def test_recommend_movies():
    user_id = "user2"
    main.create_profile(user_id, ["Action"])
    recommendations = main.recommend_movies(user_id)
    assert isinstance(recommendations, list)
    assert all("title" in m for m in recommendations)

def test_feedback():
    feedback = main.process_feedback("user1", 1, True)
    assert feedback["liked"] is True
