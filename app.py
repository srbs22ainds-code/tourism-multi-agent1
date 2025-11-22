import streamlit as st
from agents.weather_agent import WeatherAgent
from agents.places_agent import PlacesAgent

st.title("🌍 Tourism AI — Travel Assistant")

city = st.text_input("Enter city name")

want_weather = st.checkbox("Show weather information")
want_places = st.checkbox("Show tourist places")

weather_agent = WeatherAgent()
places_agent = PlacesAgent()

if st.button("Get Info"):
    if not city:
        st.write("⚠ Please enter a city name")
    else:
        output = ""

        if want_weather:
            weather = weather_agent.get_weather_for_place(city)
            if not weather:
                st.error("❌ Unknown city")
            else:
                output += f"🌡 Temperature in **{city}**: **{weather['temperature']}°C**\n"
                output += f"🌧 Rain probability: **{weather['rain_chance']}%**\n\n"

        if want_places:
            places = places_agent.get_places_for_place(city)
            if not places:
                st.error("❌ Unknown city")
            else:
                output += f"🏞 Tourist places in **{city}**:\n"
                for p in places["places"]:
                    output += f"- {p}\n"

        if output:
            st.markdown(output)
