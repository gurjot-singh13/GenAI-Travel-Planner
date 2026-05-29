import json
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_data(filepath=None):
    if filepath is None:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(base_dir, "travel_data.json")

    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


class TravelRecommender:

    def __init__(self, data):
        self.data = data

        self.vectorizer = TfidfVectorizer(
            stop_words="english",
            ngram_range=(1, 2),
            max_features=1000
        )

        descriptions = [
            place["category"] + " " + place["description"]
            for place in data
        ]

        self.tfidf_matrix = self.vectorizer.fit_transform(descriptions)

    def recommend(self, user_query, budget, month=None, category=None, top_n=8):

        # 🔥 Always valid query
        if not user_query or user_query.strip() == "":
            user_query = category if category else "travel"

        user_vector = self.vectorizer.transform([user_query])
        similarity_scores = cosine_similarity(user_vector, self.tfidf_matrix).flatten()

        results = []

        for idx, score in enumerate(similarity_scores):
            place = self.data[idx]

            # Budget score (soft)
            cost = place["avg_cost"]
            budget_score = 1 if cost <= budget else 0.7

            # Month score (soft)
            if month in place.get("best_months", []):
                month_score = 1
            else:
                month_score = 0.8

            # Category score
            category_score = 1 if place["category"] == category else 0.8

            final_score = (
                score * 0.5 +
                category_score * 0.2 +
                month_score * 0.15 +
                budget_score * 0.15
            )

            results.append({
                **place,
                "similarity_score": round(float(score), 4),
                "final_score": round(float(final_score), 4)
            })

        # 🔥 ALWAYS sort
        results.sort(key=lambda x: x["final_score"], reverse=True)

        # 🔥 ALWAYS return something
        return results[:top_n]


def build_recommender(filepath=None):
    data = load_data(filepath)
    return TravelRecommender(data)