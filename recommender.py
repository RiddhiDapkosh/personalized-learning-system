import pandas as pd

def load_data():
    return pd.read_csv("data/courses.csv")


def recommend_courses(user_interest, user_level):
    df = load_data()

    filtered = df[
        (df["category"].str.lower() == user_interest.lower()) &
        (df["level"].str.lower() == user_level.lower())
    ]

    if filtered.empty:
        return []

    return filtered.to_dict(orient="records")


def generate_learning_path(interest, level):
    return f"""
Learning Path for {interest} ({level}):

1. Start with basics
2. Practice consistently
3. Build small projects
4. Learn advanced topics
5. Build real-world applications
"""