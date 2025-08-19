import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv


load_dotenv()
st.set_page_config(page_title="AI Travel Agent", page_icon=":rocket:")

st.title("AI Travel Planner")
st.write("Welcome to the AI Travel Itineary Planner! Let's plan your perfect trip.")

with st.form("planner_form"):
    city = st.text_input("Enter your destination city:")
    intrests = st.text_input("Enter your intrests (comma-separated):")
    submit_button = st.form_submit_button("Generate Itineary")
    
    if submit_button:
        if city and intrests:
            planner = TravelPlanner()
            planner.set_city(city)
            planner.set_intrests(intrests)
            itineary =planner.create_itineary()
            
            st.subheader("📃 Your Itineary")
            st.markdown(itineary)
            
        else:
            st.warning("Please enter both city and intrests.")

    