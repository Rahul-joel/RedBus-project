Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit
Project Overview
This project automates the extraction of transportation data from the Redbus website using Selenium, stores the data in a MySQL database, and visualizes it through a Streamlit application. The aim is to simplify data collection, enhance analysis, and improve decision-making in the transportation industry.

Table of Contents
Skills Takeaway
Problem Statement
Approach
Technical Tags
Data Source
Required Fields
Project Files Overview
Skills Takeaway
Python Programming
Web Scraping using Selenium
MySQL Database Management for Data Storage and Retrieval
Streamlit Development
Data Visualization with Streamlit
Pandas for Data Handling
Problem Statement
The "Redbus Data Scraping and Filtering with Streamlit Application" project seeks to streamline the collection, analysis, and visualization of bus travel data from Redbus. Utilizing Selenium for automated web scraping, the project extracts comprehensive details such as bus routes, schedules, prices, and seat availability. This tool aims to enhance data management and strategic planning in the transportation sector.

Approach
Data Scraping
Use Selenium to extract bus travel data from the Redbus website, including routes, schedules, prices, and seat availability.
Data Storage
Store the scraped data in a MySQL database to enable efficient querying and management.
Streamlit Application
Develop a Streamlit app to visualize and filter the scraped data. Implement features to filter by bus type, route, price range, star rating, and availability.
Data Analysis and Filtering
Use SQL queries to retrieve and filter data based on user inputs, and provide interactive data exploration through the Streamlit application.
Data Source
Data is collected from the Redbus website. The scraping targets bus routes, schedules, pricing information, and seat availability.

Required Fields
Bus Routes Link: URL of the bus route
Bus Route Name: Name of the bus route
Bus Name: Name of the bus
Bus Type: Type of bus (e.g., Sleeper, Seater)
Departing Time: Time the bus departs
Duration: Duration of the journey
Reaching Time: Time the bus reaches its destination
Star Rating: Rating of the bus
Price: Ticket price
Seat Availability: Number of available seats
Project Files Overview
red_bus_scraping.ipynb: Jupyter Notebook containing the Selenium script for scraping bus data from Redbus.
sql_script.ipynb: Jupyter Notebook with SQL commands for storing scraped data in a MySQL database.
streamlit_app.py: Python script for a Streamlit application that visualizes and allows dynamic filtering of the data.
