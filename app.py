import streamlit as st
from agents.weather_agent import WeatherAgent
from agents.places_agent import PlacesAgent

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Tourism AI", page_icon="🌍", layout="wide")

# ---- BACKGROUND & FONT ----
background_image_url = "https://images.unsplash.com/photo-1507525428034-b723cf961d3e"  # Ocean/Travel aesthetic
page_bg = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {{
    font-family: 'Poppins', sans-serif;
}}

.stApp {{
    background: url("{background_image_url}") no-repeat center center fixed;
    background-size: cover;
    color: white;
}}

.title {{
    text-align: center;
    font-size: 3.4rem;
    font-weight: 700;
    margin-bottom: -10px;
}}

.subtitle {{
    text-align: center;
    font-size: 1.2rem;
    margin-bottom: 40px;
    font-weight: 300;
}}

.input-box {{
    background: rgba(0, 0, 0, 0.45);
    padding: 25px;
    border-radius: 14px;
    backdrop-filter: blur(8px);
    margin-bottom: 25px;
}}

.result-box {{
    background: rgba(0, 0, 0, 0.55);
    padding: 25px;
    border-radius: 14px;
    margin-top: 25px;
    backdrop-filter: blur(10px);
    font-size: 1.1rem;
    line-height: 1.9;
}}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# ---- TITLE ----
st.markdown('<div class="title">🌍 Tourism AI — Travel Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Plan smarter, travel better — get weather & must-visit attractions instantly</div>', unsafe_allow_html=True)

weather_agent = WeatherAgent()
places_agent = PlacesAgent()

# ---- INPUT CARD ----
with st.container():
    st.markdown('<div class="input-box">', unsafe_allow_html=True)

    city = st.text_input("🏙 Enter city name", placeholder="e.g., Dubai, Rome, Singapore")
    
    col1, col2 = st.columns(2)
    with col1:
        want_weather = st.checkbox("🌡 Show weather information")
    with col2:
        want_places = st.checkbox("📍 Show tourist places")
    
    submit = st.button("🚀 Get Travel Insights")

    st.markdown('</div>', unsafe_allow_html=True)

# ---- BUTTON TRIGGER ----
if submit:
    if not city:
        st.warning("⚠ Please enter a city name.")
    else:
        output = ""

        if want_weather:
            weather = weather_agent.get_weather_for_place(city)
            if not weather:
                st.error("❌ City not found. Try another name.")
            else:
                output += f"🌡 **Temperature in {city}**: `{weather['temperature']}°C`\n"
                output += f"🌧 **Rain probability**: `{weather['rain_chance']}%`\n\n"

        if want_places:
            places = places_agent.get_places_for_place(city)
            if not places:
                st.error("❌ Unable to fetch tourist places for this location.")
            else:
                output += f"🏞 **Top places to visit in {city}:**\n"
                for p in places["places"]:
                    output += f"🔹 {p}\n"

        if output:
            st.markdown(f'<div class="result-box">{output}</div>', unsafe_allow_html=True)
