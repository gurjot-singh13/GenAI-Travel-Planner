from google import genai
from google.genai import types
import os

# ✅ Your supported model
MODEL_ID = "gemini-2.5-flash"


# =========================
# PROMPT
# =========================
def _build_prompt(destination, days, budget, preference, month, category):

    return f"""
Create a detailed travel itinerary.

Destination: {destination}
Days: {days}
Budget: ₹{budget}
Preference: {preference}
Month: {month}
Category: {category}

Include:
- Overview
- Day-wise itinerary
- Food recommendations
- Nearby attractions
- Budget tips
- Travel tips

Format properly using markdown.
"""


# =========================
# FALLBACK
# =========================
def fallback_itinerary(destination, days, budget):

    plan = f"# 🌍 {destination} Travel Plan (Fallback Mode)\n\n"

    plan += f"## 💰 Budget: ₹{budget}\n\n"

    for d in range(1, days + 1):

        plan += f"""
## Day {d}

- Morning: Explore attractions
- Afternoon: Visit local cafes and markets
- Evening: Sightseeing and sunset points
- Night: Dinner and rest

"""

    return plan


# =========================
# GEMINI CALL
# =========================
def call_gemini(prompt):

    try:

        api_key = os.getenv("GOOGLE_API_KEY")

        print("API KEY FOUND:", bool(api_key))

        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.8,
                max_output_tokens=4096
            )
        )

        print("RAW RESPONSE:", response)

        if response and response.text:
            return response.text

        return None

    except Exception as e:

        print("REAL GEMINI ERROR:", e)

        return None


# =========================
# MAIN
# =========================
def generate_itinerary(destination, days, budget, preference, month, category):

    try:

        prompt = _build_prompt(
            destination,
            days,
            budget,
            preference,
            month,
            category
        )

        text = call_gemini(prompt)

        if not text:

            print("Using fallback itinerary")

            return fallback_itinerary(destination, days, budget)

        return text

    except Exception as e:

        print("FINAL ERROR:", e)

        return fallback_itinerary(destination, days, budget)