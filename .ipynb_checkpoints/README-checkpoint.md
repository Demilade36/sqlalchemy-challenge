# Climate Analysis API

This project implements a Flask API to provide climate data for Honolulu, Hawaii. It connects to an SQLite database and exposes various routes to access precipitation, temperature observations, and station data. The goal is to perform climate data analysis using SQLAlchemy and build a Flask API for querying the results.

### Technologies Used
- Python
- Flask (web framework)
- SQLAlchemy (ORM)
- SQLite (database)
- Pandas (data manipulation)
- Matplotlib (data visualization)

---

## Project Structure

| File Name             | Description                             |
|-----------------------|----------------------------------------- |
| `hawaii.sqlite`        | SQLite database in the Resources folder |
| `climate_analysis.py`  | Jupyter notebook with data analysis     |
| `app.py`               | Flask app to serve the API              |
| `README.md`            | Project documentation                  |


---

## Steps to Run the Project

1. **Install Dependencies**
    ```bash
    python -m venv venv
    source venv/bin/activate    # For Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

2. **Run the Flask API**
    ```bash
    python app.py
    ```
    The API will run locally at `http://127.0.0.1:5000/`.

3. **Access the Routes**
    - **Home (`/`)**: Displays a welcome message and lists routes.
    - **Precipitation (`/api/v1.0/precipitation`)**: Returns precipitation data for the last 12 months.
    - **Stations (`/api/v1.0/stations`)**: Lists all stations.
    - **Temperature Observations (`/api/v1.0/tobs`)**: Returns TOBS data for the most active station in the last year.
    - **Temperature by Date (`/api/v1.0/<start>`)**: Returns min, max, and avg temperatures for dates from `start` to the latest.
    - **Temperature by Date Range (`/api/v1.0/<start>/<end>`)**: Returns min, max, and avg temperatures for a specific range.

---

## Climate Data Analysis

### Precipitation Analysis
- Query the last 12 months of precipitation data, load into a Pandas DataFrame, sort it, and plot the results.
- Print summary statistics for precipitation.

### Station Analysis
- Query the number of stations, find the most active station, and retrieve TOBS data.
- Plot a histogram for temperature data over the past year.

---

## Flask API Design

### Routes
- **`/`**: Welcome message and list of available routes.
- **`/api/v1.0/precipitation`**: JSON of precipitation data for the past year.
- **`/api/v1.0/stations`**: JSON of station data.
- **`/api/v1.0/tobs`**: JSON of temperature observations for the most active station in the past year.
- **`/api/v1.0/<start>`**: JSON of min, max, and average temperatures from `start` date onward.
- **`/api/v1.0/<start>/<end>`**: JSON of min, max, and average temperatures for a date range.

---

## Conclusion

This project provides a simple API to query and analyze climate data for Honolulu. It uses Python, Flask, SQLAlchemy, and Pandas for querying the SQLite database and visualizing the results.

