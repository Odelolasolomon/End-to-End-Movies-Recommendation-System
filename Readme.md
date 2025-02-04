# Movie Recommendation System

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Challenges & Insights](#challenges)
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

- Handled missing values by filling or dropping them where necessary.  
- Standardized formats for dates, genres, and other categorical fields.  
- Extracted relevant information from JSON-like columns (e.g., genres, cast, and crew)


- **Exploratory Data Analysis**: Provides insights into the dataset through statistical summaries and visualizations.

 Generated descriptive statistics for budget, revenue, ratings, and runtime.  
- Identified trends and correlations, such as **budget vs. revenue**.  
- Visualized genre distribution and most common movie languages.


- **Feature Engineering**: Combines text features, encodes categorical variables, and normalizes numeric features.
 
- **Recommendation Engine**: Implements a content-based recommendation system using TF-IDF and cosine similarity.

- Built a **content-based filtering model** using **TF-IDF and cosine similarity**.  
- Engineered features from **movie titles, genres, cast, and overview** for better recommendations.  
- Deployed an **interactive Streamlit dashboard** for users to explore movies and receive personalized suggestions.  

- **Interactive Dashboard**: Built with Streamlit, allowing users to explore movies, get recommendations, and analyze genres.

---

## Challenges 

### Challenges  
- **Messy Data & Missing Values**: Several key columns, such as `budget`, `revenue`, and `runtime`, had missing values. Some fields like `genres`, `cast`, and `crew` required careful extraction and cleaning.  
- **Data Expansion & Processing Time**: After cleaning, the dataset expanded from **24 to 29 columns**, increasing memory usage. Processing text-based features, especially for **TF-IDF vectorization**, demanded computational optimizations.  
- **Balancing Recommendation Relevance**: Popular movies tended to dominate recommendations, making it necessary to balance between **blockbuster hits and lesser-known gems**.  
- **Handling Subjectivity in Ratings**: Some highly-rated movies were niche films with limited audience reach, creating a challenge in ensuring that recommendations felt meaningful to a diverse user base.  

### Key Insights  
- **More Data ≠ Better Recommendations**: While adding more features (e.g., `cast`, `keywords`, `tagline`) improved recommendations slightly, the best results came from a combination of **movie overviews and genres**.  
- **Budget ≠ Success**: The analysis showed that **big budgets don’t always guarantee big box office returns**. While **higher budgets often correlated with revenue**, there were **exceptions where low-budget films achieved massive success**  
- **The Power of Similarity**: Using **cosine similarity** on **movie overviews** significantly improved recommendation accuracy. Many sequels and related films naturally clustered together, demonstrating the effectiveness of **content-based filtering**.  
- **Genre Popularity Matters**: **Action and Drama** dominated, meaning that users preferring niche genres (e.g., **Documentary or Foreign Films**) needed additional filtering for better recommendations.  

These findings shaped the **final recommendation system**, ensuring **balanced, accurate, and meaningful suggestions** for user.


## Installation

To set up the environment and run the project:

1. Clone the repository:
   ```bash
   git clone https://github.com/Odelolasolomon/movie-recommendation-system.git
   cd movie-recommendation-system

2. Create a virtual Environment 
   ```bash
   python -m venv movievenv
   source movievenv/bin/activate  # On Windows: venv\Scripts\activate

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


3. Install dependencies
   ```bash
   pip install -r requirements.txt



- Place your dataset (movies.csv) in the data directory.

## Usage
### Running the Script
4. Execute the main script to process the data, perform EDA, engineer features, and build the recommendation  
   ```bash
   python main.py

### Running the Dashboard
5. Start the Streamlit dashboard for interactive exploration:
   ```bash
   streamlit run streamlit_app.py

- Open the provided URL in your browser to access the dashboard.

## File Structure 
```Structure
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






