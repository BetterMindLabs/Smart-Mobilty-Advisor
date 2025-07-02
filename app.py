import streamlit as st
import google.generativeai as genai

# ----------------------
# CONFIGURE GEMINI API
# ----------------------
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])  
model = genai.GenerativeModel("gemini-2.5-flash")

# ----------------------
# STREAMLIT APP
# ----------------------
st.title("🌱 Personal Mobility Advisor")

st.markdown("Get personalized transport recommendations to reduce environmental impact and improve your health!")

# --- Inputs
start_location = st.text_input("Start Location", "Home")
end_location = st.text_input("Destination", "Office")
distance_km = st.slider("Approximate distance (km)", 1, 50, 5)
priority = st.selectbox(
    "What do you prioritize most?",
    ("Environmental impact", "Cost", "Speed", "Health benefits")
)

if st.button("Get Mobility Advice"):
    with st.spinner("Analyzing..."):

        # Prompt to Gemini
        prompt = f"""
        I want you to act as a personal mobility advisor. I will provide trip details:
        - Start: {start_location}
        - End: {end_location}
        - Distance: {distance_km} km
        - User priority: {priority}

        Suggest the best transport option, considering:
        - CO2 emissions estimate (grams)
        - Cost estimate
        - Health benefits (calories burned if active)
        - Time estimate
        - Environmental impact score

        Present your recommendation in a friendly, clear bullet-point style, and suggest alternative options too.
        """

        response = model.generate_content(prompt)
        advice = response.text

        st.success("Here is your personalized recommendation:")
        st.markdown(advice)

# Footer
st.markdown("---")
st.caption("♻️ Built with Streamlit, Python & Gemini API")
