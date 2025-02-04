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



## Overview

This repository contains a movie recommendation system that processes movie data, performs exploratory data analysis (EDA), and builds a content-based recommendation model. The system is designed to provide personalized movie recommendations based on user preferences and movie attributes such as genres, cast, director, and overview.

Key capabilities include:
- Comprehensive data preprocessing and cleaning
- In-depth exploratory analysis with visual insights
- Feature engineering optimized for movie recommendations
- Content-based recommendation engine using TF-IDF and cosine similarity
- Interactive Streamlit dashboard for exploring recommendations



## Features

### Data Cleaning
- Systematic handling of missing values in critical fields (budget, revenue, runtime)
- Standardization of date formats and categorical fields
- Extraction and structuring of complex JSON-formatted data (genres, cast, crew)
- Quality assurance checks for data consistency

### Exploratory Data Analysis
- Statistical analysis of key metrics:
  - Budget and revenue distributions
  - Rating patterns and correlations
  - Runtime analysis
- Visual insights into:
  - Genre distribution across decades
  - Popular movie languages
  - Budget vs. revenue relationships

### Feature Engineering
- Text feature processing for improved recommendations
- Categorical variable encoding
- Numerical feature normalization
- Combined feature analysis for enhanced similarity matching

### Recommendation Engine
- Content-based filtering implementation using:
  - TF-IDF vectorization of movie descriptions
  - Cosine similarity calculations
  - Genre-weighted recommendations
  - Hybrid scoring system

### Interactive Dashboard
- User-friendly Streamlit interface
- Real-time movie recommendations
- Interactive data exploration tools
- Detailed movie information display

## Challenges & Insights

### Key Challenges
1. **Data Quality Management**
   - Handled missing values in critical fields
   - Processed complex nested JSON data
   - Standardized inconsistent data formats

2. **Performance Optimization**
   - Managed increased dataset size
   - Optimized TF-IDF vectorization processing
   - Balanced computation speed with recommendation quality

3. **Recommendation Balance**
   - Addressed popularity bias in recommendations
   - Balanced mainstream and niche movie suggestions
   - Handled subjective nature of user ratings

### Notable Insights
1. **Feature Impact**
   - Additional features showed diminishing returns
   - Optimal feature combination identified through testing

2. **Budget-Success Relationship**
   - Discovered non-linear relationship between budget and revenue
   - Identified successful low-budget films
   - Analyzed factors beyond budget affecting success

3. **Content Similarity**
   - Effective clustering of related movies using cosine similarity
   - Natural grouping of sequels and similar themes
   - Genre influence on recommendation accuracy


## Installation

1. Clone the repository:
```bash
git clone https://github.com/Odelolasolomon/movie-recommendation-system.git
cd movie-recommendation-system
```

2. Create virtual environment:
```bash
python -m venv movievenv
source movievenv/bin/activate  # On Windows: movievenv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Prepare data:
   - Place movies.csv in the data directory

## Usage

### Data Processing and Analysis
```bash
python main.py
```

### Launch Dashboard
```bash
streamlit run streamlit_app.py
```

## File Structure
```
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
```

## Dependencies
Required Python packages:
- numpy >= 1.21.0
- pandas >= 1.3.0
- scikit-learn >= 0.24.2
- streamlit >= 1.22.0
- plotly >= 5.13.0
- matplotlib >= 3.4.3
- seaborn >= 0.11.2
- python-dateutil >= 2.8.2






