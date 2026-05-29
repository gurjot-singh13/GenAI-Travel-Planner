# GenAI Travel Planner

## Overview

GenAI Travel Planner is an AI-powered travel recommendation and itinerary generation system that helps users discover destinations based on their preferences, budget, travel month, and interests.

The project combines a recommendation engine using TF-IDF vectorization and cosine similarity with Google's Gemini API to generate personalized travel itineraries.

---
## Application Preview

### Home Screen

<img width="1784" height="967" alt="homepage" src="https://github.com/user-attachments/assets/97f09095-f600-4743-b83a-33093418891c" />


Users can enter their travel preferences including category, month, budget, duration, and optional destination preferences.

---

### Destination Recommendations

<img width="1839" height="957" alt="recommendations" src="https://github.com/user-attachments/assets/2ac051c6-a23d-42e7-833d-49b28b03fd1b" />


The recommendation engine uses TF-IDF vectorization and cosine similarity to identify destinations that best match user preferences.

---

### Destination Selection

<img width="1818" height="964" alt="destination-selection" src="https://github.com/user-attachments/assets/98bfe060-19b0-4e96-b44f-7f6caef4a5f5" />


Users can select a recommended destination and generate a personalized travel itinerary.

---

### AI-Generated Travel Plan

<img width="1893" height="969" alt="itinerary-overview" src="https://github.com/user-attachments/assets/284f669d-9498-4f2b-9a00-606a758980ff" />


Google Gemini generates a customized itinerary including budget estimates, attractions, travel suggestions, and planning insights.

---

### Day-wise Itinerary

<img width="1632" height="957" alt="itinerary-details" src="https://github.com/user-attachments/assets/f0751711-0c4b-468e-83e6-0263e7af7017" />


The system produces a structured day-by-day itinerary tailored to the user's travel duration and interests.

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
