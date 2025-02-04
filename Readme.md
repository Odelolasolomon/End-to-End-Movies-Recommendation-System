# Movie Recommendation System

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [File Structure](#file-structure)
6. [Dependencies](#dependencies)
7. [Contributing](#contributing)
8. [License](#license)

---

## Overview

This repository contains a movie recommendation system that processes movie data, performs exploratory data analysis (EDA), and builds a content-based recommendation model. The system is designed to provide personalized movie recommendations based on user preferences and movie attributes such as genres, cast, director, and overview.

The project includes:
- Data cleaning and preprocessing.
- Exploratory data analysis with visualizations.
- Feature engineering for enhancing the dataset.
- A content-based recommendation engine using TF-IDF and cosine similarity.
- A Streamlit dashboard for interactive exploration and recommendations.

---

## Features

- **Data Cleaning**: Handles missing values, standardizes data formats, and enriches the dataset with derived features.
- **Exploratory Data Analysis**: Provides insights into the dataset through statistical summaries and visualizations.
- **Feature Engineering**: Combines text features, encodes categorical variables, and normalizes numeric features.
- **Recommendation Engine**: Implements a content-based recommendation system using TF-IDF and cosine similarity.
- **Interactive Dashboard**: Built with Streamlit, allowing users to explore movies, get recommendations, and analyze genres.

---

## Installation

To set up the environment and run the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system

## Create a virtual Environment 
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

## Install dependencies
```bash
pip install -r requirements.txt

- Place your dataset (movies.csv) in the data directory.

## Usage
### Running the Script
- Execute the main script to process the data, perform EDA, engineer features, and build the recommendation system: 
```bash
python main.py

### Running the Dashboard
### Start the Streamlit dashboard for interactive exploration:
```bash
streamlit run streamlit_app.py

- Open the provided URL in your browser to access the dashboard.

## File Structure 
movie-recommendation-system/
├── data/
│   └── movies.csv
├── Outputs/
│   ├── genre_distribution.png
│   ├── budget_revenue_correlation.png
│   └── processed_movies.csv
├── data_loader.py
├── eda.py
├── feature_engineering.py
├── recommender.py
├── dashboard.py
├── main.py
├── requirements.txt
└── README.md

- data/ : Contains the raw dataset (movies.csv).
- Outputs/ : Stores generated visualizations and processed data.
- data_loader.py : Handles loading and cleaning of the dataset.
- eda.py : Performs exploratory data analysis and generates visualizations.
- feature_engineering.py : Implements feature creation and encoding.
- recommender.py : Builds the content-based recommendation system.
- dashboard.py : Provides an interactive interface using Streamlit.
- main.py : Entry point for running the entire pipeline.
- requirements.txt : Lists all required Python packages.
- README.md : Documentation for the project.

## Dependencies
- The following libraries are required to run this project:

- numpy>=1.21.0
- pandas>=1.3.0
- scikit-learn>=0.24.2
- streamlit>=1.22.0
- plotly>=5.13.0
- matplotlib>=3.4.3
- seaborn>=0.11.2
- python-dateutil>=2.8.2
- Install them using: 

```bash
pip install -r requirements.txt

## Contributing
### Contributions are welcome! To contribute:

Fork the repository.
Create a new branch for your feature or bug fix.
Commit your changes and push to your fork.
Submit a pull request detailing your changes

