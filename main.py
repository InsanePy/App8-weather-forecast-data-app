import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input("Place")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    # Get temparature and sky data
    filtered_data = get_data(place, days)
    if option == "Temperature":
        temperatures = [item["main"]["temp"] for item in filtered_data]
        dates = [item["dt_txt"] for item in filtered_data]
        figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        sky_conditions = [item["weather"][0]["main"] for item in filtered_data]
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow":"images/snow.png"}
        image_paths = [images[item] for item in sky_conditions]
        st.image(image_paths, width=115)