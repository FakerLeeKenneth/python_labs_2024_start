import streamlit as st
import requests
import json
import pandas as pd

# Title of the Streamlit app
st.title("Hong Kong Weather Data")

# Make a GET request to the weather API
result = requests.get('https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en')

# Check if the request was successful
if result.status_code == 200:
    result_dict = result.json()  # Parse the JSON response directly into a dict object

    # Extract humidity and temperature data
    humidity_data = result_dict["humidity"]["data"]
    temperature_data = result_dict["temperature"]["data"]

    # Create a list of locations
    locations = [data["place"] for data in temperature_data]

    # Sidebar for location selection
    selected_location = st.sidebar.selectbox("Select a location", locations)

    # Display the humidity and temperature data for the selected location
    st.header(f"Location:  {selected_location}")

    # Find the humidity and temperature for the selected location
    humidity_value = next((data["value"] for data in humidity_data if data["place"] == selected_location), None)
    temperature_value = next((data["value"] for data in temperature_data if data["place"] == selected_location), None)
    temperature_unit = next((data["unit"] for data in temperature_data if data["place"] == selected_location), None)

    # Display the humidity and temperature data
    if humidity_value is not None:
        st.write(f"Humidity: {humidity_value}%")
    else:
        st.write("Humidity data not available")

    if temperature_value is not None and temperature_unit is not None:
        st.write(f"Temperature: {temperature_value} {temperature_unit}")
    else:
        st.write("Temperature data not available")

    # Display the temperature data as a chart
    st.header("Temperature Data for All Locations")
    temp_df = pd.DataFrame(temperature_data)
    temp_df.columns = ["Place", "Value", "Unit"]
    st.bar_chart(temp_df.set_index("Place")["Value"])
else:
    st.error(f"Failed to retrieve data: {result.status_code}")