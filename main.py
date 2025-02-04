import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from data_loader import MovieDataLoader
from eda import MovieEDA
from feature_engineering import FeatureEngineer
from recommender import MovieRecommender

def main():
    # Step 1: Load Data
    print("Step 1: Loading Data...")
    data_loader = MovieDataLoader("C:/Users/512GB/OneDrive/Documents/Company tasks/data/movies.csv")  
    df = data_loader.load_data()
    print(f"Loaded {len(df)} movies")
    #print(f"Duplicates? {df.duplicated().sum()} movies")

    # Step 2: Exploratory Data Analysis
    print("\nStep 2: Performing Exploratory Data Analysis...")
    eda = MovieEDA(df)
    
    # Generate and print basic stats
    basic_stats = eda.generate_basic_stats()
    print("Basic Statistics:")
    for key, value in basic_stats.items():
        print(f"{key}: {value}")
    
    # Generate visualizations
    print("\nGenerating Visualizations...")
    genre_plot = eda.plot_genre_distribution('Outputs/genre_distribution.png')
    budget_revenue_plot = eda.plot_budget_revenue_correlation('Outputs/budget_revenue_correlation.png')
    print("Visualizations saved in 'outputs/' directory")

    # Step 3: Feature Engineering
    print("\nStep 3: Feature Engineering...")
    engineer = FeatureEngineer(df)
    df_processed = engineer.create_combined_features()
    df_processed = engineer.encode_categorical_features()
    df_processed = engineer.normalize_numeric_features()
    print("Feature engineering completed")

    # Step 4: Build Recommendation System
    print("\nStep 4: Building Recommendation System...")
    recommender = MovieRecommender(df_processed)
    recommender.build_content_based_model()
    
    # Example: Get recommendations for a movie
    try:
        recommendations = recommender.get_recommendations("The Dark Knight")
        print("\nRecommendations for 'The Dark Knight':")
        for rec in recommendations:
            print(f"- {rec['title']} (Rating: {rec['vote_average']})")
    except Exception as e:
        print(f"Could not get recommendations: {e}")

    # Step 5: Save Processed Data 
    print("\nStep 5: Saving Processed Data...")
    df_processed.to_csv('Outputs/processes_movies.csv', index=False)
    print("Processed data saved to 'Outputs/processes_movies.csv'")

if __name__ == "__main__":
    main()