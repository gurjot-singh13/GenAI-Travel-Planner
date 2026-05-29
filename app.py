import streamlit as st
from ml_model import build_recommender
from generator import generate_itinerary
import os

st.set_page_config(page_title="AI Travel Planner", layout="wide")

# ==============================
# LOAD MODEL (CACHED)
# ==============================
@st.cache_resource
def load_model():
    return build_recommender()

model = load_model()

# ==============================
# SIDEBAR
# ==============================
with st.sidebar:
    st.title("⚙️ Preferences")

    # 🔐 API KEY INPUT
    api_key = st.text_input("🔐 Enter Gemini API Key", type="password")

    if not api_key:
        st.info("👈 Please enter your API key to continue")
        st.stop()
    else:
        os.environ["GOOGLE_API_KEY"] = api_key

    category = st.selectbox(
        "Category",
        ["adventure", "beach", "heritage", "spiritual", "romantic", "nature"]
    )

    month = st.selectbox(
        "Month",
        ["January","February","March","April","May","June",
         "July","August","September","October","November","December"]
         
    )

    budget = st.slider("💰 Budget (₹)", 1000, 100000, 10000)
    days = st.slider("📅 Days", 1, 15, 5)

    preference = st.text_input("✨ Extra preference (optional)")
    destination_input = st.text_input("📍 Preferred destination (optional)")

    run = st.button("🔍 Get Recommendations")

# ==============================
# SESSION STATE
# ==============================
if "recs" not in st.session_state:
    st.session_state.recs = []

if "selected" not in st.session_state:
    st.session_state.selected = None

if "plan" not in st.session_state:
    st.session_state.plan = None

# ==============================
# TITLE
# ==============================
st.title("🌍 AI Travel Planner")
st.caption("Plan your perfect trip with AI ✨")

# ==============================
# MAIN LOGIC
# ==============================
if run:

    st.session_state.selected = None
    st.session_state.plan = None

    query = f"{destination_input} {preference} {category}"

    with st.spinner("🔍 Finding best destinations..."):
        recs = model.recommend(
            user_query=query,
            budget=budget,
            month=month,
            category=category,
            top_n=8
        )

    # Add preferred destination at top
    if destination_input:
        preferred = {
            "name": destination_input.title(),
            "avg_cost": budget,
            "category": category
        }

        recs = [preferred] + [
            r for r in recs
            if r["name"].lower() != destination_input.lower()
        ]

    st.session_state.recs = recs

# ==============================
# SHOW RECOMMENDATIONS
# ==============================
if st.session_state.recs:

    st.subheader("🎯 Recommended Destinations")

    cols = st.columns(4)

    for i, place in enumerate(st.session_state.recs):
        with cols[i % 4]:

            if st.button(f"Select {place['name']}", key=f"select_{i}"):
                st.session_state.selected = place

            st.markdown(f"""
            <div style="
                background:#1e293b;
                padding:15px;
                border-radius:12px;
                margin-bottom:10px;
            ">
            <b style="color:white">{place['name']}</b><br>
            <span style="color:#94a3b8">💰 ₹{place['avg_cost']}</span><br>
            <span style="color:#94a3b8">📌 {place['category']}</span>
            </div>
            """, unsafe_allow_html=True)

# ==============================
# SELECTED DESTINATION
# ==============================
if st.session_state.selected:

    st.success(f"📍 Selected: {st.session_state.selected['name']}")

    if st.button("🚀 Generate Plan"):

        with st.spinner("🧠 Generating AI travel plan..."):
            st.session_state.plan = generate_itinerary(
                destination=st.session_state.selected["name"],
                days=days,
                budget=budget,
                preference=preference,
                month=month,
                category=category
            )

# ==============================
# SHOW PLAN
# ==============================
if st.session_state.plan:
    st.subheader("🧭 Your Travel Plan")
    st.markdown(st.session_state.plan)