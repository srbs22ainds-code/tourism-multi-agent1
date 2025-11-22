# tourism-multi-agent-ai
🌍 Tourism AI — Multi-Agent Travel Assistant

A smart AI-powered travel planning system built using a multi-agent architecture.
The app helps travelers make informed decisions by providing:

✔ Real-time weather information
✔ Top tourist attractions near the destination
✔ A beautiful & user-friendly Streamlit web interface

🚀 Live Demo

🔗 Deployed App: https://tourism-multi-agent1-ragv8yiegv5odq9iv5thfz.streamlit.app/
🔗 GitHub Repository: https://github.com/srbs22ainds-code/tourism-multi-agent1

🧠 Project Architecture

The system follows a parent–child agent architecture:

Agent / Component	Responsibility
WeatherAgent	Fetches latitude/longitude from Nominatim + weather from Open-Meteo
PlacesAgent	Fetches tourist places within a 10 km radius using Overpass API
Parent (Streamlit app)	Handles user requests & calls respective agent(s)

🛠 APIs Used
API	Purpose
Nominatim (OpenStreetMap)	Convert city → latitude & longitude
Open-Meteo	Weather (temperature & probability of rain)
Overpass API	Retrieve top tourist places around coordinates

🏗 Tech Stack
Category	Tools Used
Language	Python
Frontend	Streamlit
Architecture	Multi-agent system
Libraries	requests, streamlit
Deployment	Streamlit Cloud

💡 Features

🔹 AI agent-based architecture (scalable & clean)
🔹 Get weather instantly by city name
🔹 Explore top tourist attractions nearby
🔹 Elegant UI with background image, modern fonts & icons
🔹 Fully deployed and accessible online

📌 How to Run Locally
1️⃣ Clone repository
git clone https://github.com/srbs22ainds-code/tourism-multi-agent1.git
cd tourism-multi-agent1

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the application
streamlit run app.py


🔮 Future Enhancements (optional scope)

AI-generated travel itinerary

Voice assistant

Maps integration

Hotel & restaurant suggestions

Save itinerary as PDF

👤 Author

Name: SRISHTI.B.S
Contact: srbs22ainds@cmrit.ac.in

🌟 Feedback

If you found this project helpful, feel free to ⭐ the repository.
