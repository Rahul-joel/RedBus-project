import streamlit as st
import pandas as pd
import mysql.connector


# Custom CSS for styling
custom_css = """
    <style>
    /* Custom font and background color */
    body {
        font-family: 'Arial', sans-serif;
        background-color: #f4f4f9;
    }

    /* Title styling */
    .title {
        text-align: center;
        color: #4A4A4A;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #FF4C4C; /* Red background for the sidebar */
        border-right: 1px solid #dcdcdc;
    }
    
    [data-testid="stSidebar"] h1 {
        color: #FFF; /* White color for sidebar title */
    }
    
    /* Filter section styling */
    .filter-title {
        font-weight: bold;
        color: #FFF; /* White color for filter titles */
        margin-top: 10px;
    }

    /* Dataframe styling */
    .dataframe {
        border: 1px solid #dcdcdc;
        border-radius: 8px;
    }

    /* Slider styling */
    .stSlider > div > div > div {
        background-color: #FFF; /* White color for slider track */
        border-radius: 25px; /* Optional: Add rounded corners */
    }

    .stSlider > div > div > div > div > div {
        background-color: #FFF; /* Black color for slider handle */
        border-radius: 100%; /* Round slider handle */
        border: 2px solid #000; /* Black border for slider handle */
        width: 30px; /* Width of the slider handle */
        height: 30px; /* Height of the slider handle */
    }

    .stSlider > div > div > div > div > div::after {
        background-color: #FFF; /* Black color for slider indicator */
    }
    </style>
    """
st.markdown(custom_css, unsafe_allow_html=True)

# Initialize session state for sidebar visibility
if 'show_sidebar' not in st.session_state:
    st.session_state.show_sidebar = False

# Toggle sidebar visibility
def toggle_sidebar():
    st.session_state.show_sidebar = not st.session_state.show_sidebar

# Load data from MySQL
def load_data(state):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="redbuss"
    )
    query = f"SELECT * FROM {state}"
    df = pd.read_sql(query, mydb)
    mydb.close()
    return df

# Streamlit App
st.markdown('<h1 class="title">State Transport Data</h1>', unsafe_allow_html=True)

# Button to show/hide sidebar
if st.button("Select your bus"):
    toggle_sidebar()

# Conditionally show the sidebar based on the session state
if st.session_state.show_sidebar:
    # Sidebar title
    st.sidebar.markdown('<h1 class="title">Filter Details</h1>', unsafe_allow_html=True)

    # States 
    states = ['andhra', 'bihar', 'chandigar', 'himachel', 'jksrtc', 'kadamba', 'kerala', 'north_bengal', 'punjab', 'telungana']

    # Select state
    st.sidebar.markdown('<p class="filter-title">State Name</p>', unsafe_allow_html=True)
    selected_state = st.sidebar.selectbox('', states)

    # Load data for the selected state
    df = load_data(selected_state)

    # Specify the columns
    columns = ['route_name', 'route_link', 'busname', 'bustype', 'departing_time', 'duration', 'reaching_time', 'star_rating', 'price', 'seats_available']

    # Split 'route_name' into 'start_location' and 'end_location'
    df['start_location'] = df['route_name'].apply(lambda x: x.split(' to ')[0].strip())
    df['end_location'] = df['route_name'].apply(lambda x: x.split(' to ')[-1].strip())

    # Convert 'departing_time' to string format 'HH:MM:SS'
    df['formatted_departing_time'] = df['departing_time'].apply(lambda x: str(x).split()[2] if pd.notnull(x) else '')

    # Add 'All' option
    start_locations = ['All'] + list(df['start_location'].unique())
    end_locations = ['All'] + list(df['end_location'].unique())
    bus_types = ['All'] + list(df['bustype'].unique())
    time_options = ['All'] + list(df['formatted_departing_time'].unique())  # Add 'All' option for time

    # Start and End location filters
    st.sidebar.markdown('<p class="filter-title">Start Location</p>', unsafe_allow_html=True)
    start_location = st.sidebar.selectbox('', start_locations)

    st.sidebar.markdown('<p class="filter-title">End Location</p>', unsafe_allow_html=True)
    end_location = st.sidebar.selectbox('', end_locations)

    # Bus Type filter
    st.sidebar.markdown('<p class="filter-title">Select Bus Type</p>', unsafe_allow_html=True)
    bus_type = st.sidebar.selectbox('', bus_types)

    # Depart time filter
    st.sidebar.markdown('<p class="filter-title">Depart Time</p>', unsafe_allow_html=True)
    selected_time = st.sidebar.selectbox('', time_options)

    # Star Rating filter (slider)
    st.sidebar.markdown('<p class="filter-title">Select Star Rating Range</p>', unsafe_allow_html=True)
    rating_range = st.sidebar.slider('', 1.0, 5.0, (1.0, 5.0), step=0.1)
    st.sidebar.write(f'Selected Star Rating Range: {rating_range[0]:.1f} - {rating_range[1]:.1f}')

    # Price range slider
    st.sidebar.markdown('<p class="filter-title">Select Price Range</p>', unsafe_allow_html=True)
    price_range = st.sidebar.slider('', 
                                    min_value=int(df['price'].min()),  # Minimum price in your data
                                    max_value=int(df['price'].max()),  # Maximum price in your data
                                    value=(int(df['price'].min()), int(df['price'].max())),  # Default range (min, max)
                                    step=1)  # Adjust step as needed
    st.sidebar.write(f'Selected Price Range: {price_range[0]} - {price_range[1]}')

    # Sort options
    st.sidebar.markdown('<p class="filter-title">Sort By</p>', unsafe_allow_html=True)
    sort_by = st.sidebar.selectbox('', ['Price', 'Star Rating', 'Duration', 'Seats Available'])

    # Filter the DataFrame based on the selected filters
    filtered_df = df.loc[
        ((df['start_location'] == start_location) | (start_location == 'All')) &
        ((df['end_location'] == end_location) | (end_location == 'All')) &
        ((df['bustype'] == bus_type) | (bus_type == 'All')) &
        (df['star_rating'] >= rating_range[0]) &
        (df['star_rating'] <= rating_range[1]) &
        ((df['formatted_departing_time'] == selected_time) | (selected_time == 'All')) &
        (df['price'] >= price_range[0]) &  # Filter by minimum price
        (df['price'] <= price_range[1])  # Filter by maximum price
    ]

    # Apply sorting
    if sort_by == 'Price':
        filtered_df = filtered_df.sort_values(by='price',ascending=False)
    elif sort_by == 'Star Rating':
        filtered_df = filtered_df.sort_values(by='star_rating', ascending=False)
    elif sort_by == 'Duration':
        filtered_df = filtered_df.sort_values(by='duration',ascending=False)
    elif sort_by == 'Seats Available':
        filtered_df = filtered_df.sort_values(by='seats_available', ascending=False)

    # Display the results in the main area with adjustable width
    st.write(f"Showing results for: {start_location} to {end_location}")
    st.dataframe(filtered_df[columns], width=1500, height=500)  # Adjust the width and height as needed

    # Display the number of rows
    st.write(f"Total number of results: {len(filtered_df)}")
else:
    # Main page content when sidebar is hidden
    st.write("Click 'Select your bus' to show the sidebar and apply filters.")
# Display an image on the main page
st.image("d:\image.png",  width=300)



