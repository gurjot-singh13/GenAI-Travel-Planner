# GenAI Travel Planner

## Overview

GenAI Travel Planner is an AI-powered travel recommendation and itinerary generation system that helps users discover destinations based on their preferences, budget, travel month, and interests.

The project combines a recommendation engine using TF-IDF vectorization and cosine similarity with Google's Gemini API to generate personalized travel itineraries.

---

## Features

- Personalized destination recommendations
- Budget-aware travel suggestions
- Category-based destination filtering
- Month-wise travel recommendations
- AI-generated travel itineraries
- Interactive Streamlit interface

---

## Tech Stack

### Programming Language
- Python

### Machine Learning
- TF-IDF Vectorization
- Cosine Similarity
- Scikit-learn

### Generative AI
- Google Gemini API

### Frontend
- Streamlit

---

## Project Structure

```text
GenAI-Travel-Planner/
│
├── app.py
├── generator.py
├── ml_model.py
├── travel_data.json
├── requirements.txt
└── README.md
```

---

## How It Works

### Recommendation Engine

The system converts destination descriptions into TF-IDF vectors and calculates similarity scores based on user preferences.

Additional ranking factors include:

- Budget compatibility
- Travel month
- Destination category

### Itinerary Generation

Once a destination is selected, Gemini generates a personalized itinerary including:

- Activities
- Places to visit
- Food suggestions
- Travel tips

---

## Future Improvements

- User authentication
- Hotel integration
- Flight recommendations
- Collaborative filtering
- Multi-city itinerary planning

---

## Learning Outcomes

Through this project, I explored:

- Recommendation Systems
- Natural Language Processing concepts
- Similarity-based ranking techniques
- Generative AI integration
- Streamlit application development

---

## Author

Gurjot Singh Khanuja   
