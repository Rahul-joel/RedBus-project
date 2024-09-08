# Redbus Data Scraping with Selenium & Dynamic Filtering using Streamlit

## Project Overview
This project involves scraping transportation data from the Redbus website using Selenium and storing the extracted data in a MySQL database. The data is then visualized and dynamically filtered using a Streamlit application.

## Table of Contents
- [Skills Takeaway](#skills-takeaway)
- [Problem Statement](#problem-statement)
- [Approach](#approach)
- [Technical Tags](#technical-tags)
- [Data Source](#data-source)
- [Required Fields](#required-fields)
- [Project Files Overview](#project-files-overview)

## Skills Takeaway
- Python Programming
- Web Scraping using Selenium
- MySQL DBMS for Data Storage and Retrieval
- Streamlit Development
- Data Visualization using Streamlit

## Problem Statement
The "Redbus Data Scraping and Filtering with Streamlit Application" project aims to simplify the collection, analysis, and visualization of bus travel data. By using Selenium for web scraping, this project automatically extracts detailed information from the Redbus website, such as bus routes, schedules, prices, and seat availability. The goal is to make data collection easier and provide tools for better decision-making, helping improve efficiency and planning in the transportation industry.

## Approach

### Data Scraping
Utilize Selenium to automate the extraction of Redbus data, including routes, schedules, prices, and seat availability.

### Data Storage
Store the scraped data in a SQL database for efficient querying and data management.

### Streamlit Application
Develop a Streamlit application to display and filter the scraped data. Implement various filters such as bus type, route, price range, star rating, and availability.

### Data Analysis and Filtering
Use SQL queries to retrieve and filter data based on user inputs. Utilize Streamlit to allow users to interact with and filter the data through the application.

## Data Source
Data is scraped from the [Redbus website](https://www.redbus.in/).

## Required Fields
- Bus Routes Link
- Bus Route Name
- Bus Name
- Bus Type (Sleeper/Seater)
- Departing Time
- Duration
- Reaching Time
- Star Rating
- Price
- Seat Availability

## Project Files Overview
- **`red_bus_scraping.ipynb`**: Jupyter Notebook with the Selenium script used to scrape bus data from the Redbus website.
- **`sql_script.ipynb`**: Jupyter Notebook containing the SQL script for storing the scraped data into a MySQL database.
- **`streamlit_app.py`**: Python script for a Streamlit application that visualizes and allows dynamic filtering of the scraped data.

