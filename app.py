import streamlit as st
from agents.weather_agent import WeatherAgent
from agents.places_agent import PlacesAgent

# ---------- Page Styling ----------
st.set_page_config(page_title="Tourism AI", page_icon="🌍", layout="wide")

page_bg = """
<style>
    .stApp {
        background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
        color: white;
        font-family: 'Segoe UI', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 3rem;
        font-weight: 700;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        margin-bottom: 40px;
        color: #dce3e9;
    }
    .result-box {
        background: rgba(255, 255, 255, 0.10);
        padding: 20px;
        border-radius: 12px;
        margin-top: 25px;
        backdrop-filter: blur(8px);
        font-size: 1.1rem;
        line-height: 1.8;
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---------- Title ----------
st.markdown('<div class="title">🌍 Tourism AI – Travel Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Plan smarter, travel better — get live weather & must-visit places instantly</div>', unsafe_allow_html=True)

# ---------- Inputs ----------
city = st.text_input("🏙 Enter city name", placeholder="e.g., Mumbai, Paris, Tokyo")

left, right = st.columns(2)
with left:
    want_weather = st.checkbox("🌡 Show weather information")
with right:
    want_places = st.checkbox("📍 Show tourist places to visit")

weather_agent = WeatherAgent()
places_agent = PlacesAgent()

# ---------- Action Button ----------
if st.button("🚀 Get Travel Info"):
    if not city:
        st.warning("⚠ Please enter a city name first.")
    else:
        output = ""

        if want_weather:
            weather = weather_agent.get_weather_for_place(city)
            if not weather:
                st.error("❌ City not found. Try another.")
            else:
                output += f"🌡 **Temperature in {city}**: `{weather['temperature']}°C`\n"
                output += f"🌧 **Rain probability**: `{weather['rain_chance']}%`\n\n"

        if want_places:
            places = places_agent.get_places_for_place(city)
            if not places:
                st.error("❌ Unable to fetch tourist attractions.")
            else:
                output += f"🏞 **Top places to visit in {city}:**\n"
                for p in places["places"]:
                    output += f"🔹 {p}\n"

        st.markdown(f'<div class="result-box">{output}</div>', unsafe_allow_html=True)
