import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Researcher Profile Page with STEM Data")

# Collect basic information
name = "Dr. Godfrey"
field = "Microbiology"
institution = "NWU"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "data:image/jpeg;base64,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",
    caption="Godfrey"
)

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")
        

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add STEM Data Section
st.header("Explore STEM Data")

# Generate dummy data
physics_data = pd.DataFrame({
    "Experiment": ["Alpha Decay", "Beta Decay", "Gamma Ray Analysis", "Quark Study", "Higgs Boson"],
    "Energy (MeV)": [4.2, 1.5, 2.9, 3.4, 7.1],
    "Date": pd.date_range(start="2024-01-01", periods=5),
})

astronomy_data = pd.DataFrame({
    "Celestial Object": ["Mars", "Venus", "Jupiter", "Saturn", "Moon"],
    "Brightness (Magnitude)": [-2.0, -4.6, -1.8, 0.2, -12.7],
    "Observation Date": pd.date_range(start="2024-01-01", periods=5),
})

weather_data = pd.DataFrame({
    "City": ["Cape Town", "London", "New York", "Tokyo", "Sydney"],
    "Temperature (°C)": [25, 10, -3, 15, 30],
    "Humidity (%)": [65, 70, 55, 80, 50],
    "Recorded Date": pd.date_range(start="2024-01-01", periods=5),
})

# Tabbed view for STEM data
st.subheader("STEM Data Viewer")
data_option = st.selectbox(
    "Choose a dataset to explore", 
    ["Physics Experiments", "Astronomy Observations", "Weather Data"]
)

if data_option == "Physics Experiments":
    st.write("### Physics Experiment Data")
    st.dataframe(physics_data)
    # Add widget to filter by Energy levels
    energy_filter = st.slider("Filter by Energy (MeV)", 0.0, 10.0, (0.0, 10.0))
    filtered_physics = physics_data[
        physics_data["Energy (MeV)"].between(energy_filter[0], energy_filter[1])
    ]
    st.write(f"Filtered Results for Energy Range {energy_filter}:")
    st.dataframe(filtered_physics)

elif data_option == "Astronomy Observations":
    st.write("### Astronomy Observation Data")
    st.dataframe(astronomy_data)
    # Add widget to filter by Brightness
    brightness_filter = st.slider("Filter by Brightness (Magnitude)", -15.0, 5.0, (-15.0, 5.0))
    filtered_astronomy = astronomy_data[
        astronomy_data["Brightness (Magnitude)"].between(brightness_filter[0], brightness_filter[1])
    ]
    st.write(f"Filtered Results for Brightness Range {brightness_filter}:")
    st.dataframe(filtered_astronomy)

elif data_option == "Weather Data":
    st.write("### Weather Data")
    st.dataframe(weather_data)
    # Add widgets to filter by temperature and humidity
    temp_filter = st.slider("Filter by Temperature (°C)", -10.0, 40.0, (-10.0, 40.0))
    humidity_filter = st.slider("Filter by Humidity (%)", 0, 100, (0, 100))
    filtered_weather = weather_data[
        weather_data["Temperature (°C)"].between(temp_filter[0], temp_filter[1]) &
        weather_data["Humidity (%)"].between(humidity_filter[0], humidity_filter[1])
    ]
    st.write(f"Filtered Results for Temperature {temp_filter} and Humidity {humidity_filter}:")
    st.dataframe(filtered_weather)

# Add a contact section
st.header("Contact Information")
email = "jane.doe@example.com"
st.write(f"You can reach {name} at {email}.")