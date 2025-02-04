import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from data_loader import MovieDataLoader
from eda import MovieEDA
from recommender import MovieRecommender
from feature_engineering import FeatureEngineer

def load_data():
    data_loader = MovieDataLoader("C:/Users/512GB/OneDrive/Documents/Company tasks/data/movies.csv")
    df = data_loader.load_data()
    
    engineer = FeatureEngineer(df)
    df = engineer.create_combined_features()
    df = engineer.encode_categorical_features()
    df = engineer.normalize_numeric_features()
    
    return df

def main():
    st.title("Movie Analysis Dashboard")
    
    # Load data
    df = load_data()
    eda = MovieEDA(df)
    recommender = MovieRecommender(df)
    recommender.build_content_based_model()
    
    # Sidebar navigation
    page = st.sidebar.selectbox(
        "Choose a page", 
        ["Overview", "Movie Explorer", "Recommendations", "Genre Analysis"]
    )
    
    if page == "Overview":
        show_overview(df, eda)
    elif page == "Movie Explorer":
        show_movie_explorer(df)
    elif page == "Recommendations":
        show_recommendations(df, recommender)
    else:
        show_genre_analysis(df, eda)

def show_overview(df, eda):
    st.header("Dataset Overview")
    
    # Basic stats
    stats = eda.generate_basic_stats()
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Movies", f"{stats['total_movies']:,}")
    with col2:
        st.metric("Avg Budget", f"${stats['avg_budget']:,.0f}")
    with col3:
        st.metric("Avg Revenue", f"${stats['avg_revenue']:,.0f}")
    
    # Timeline
    st.subheader("Movies Over Time")
    yearly_movies = df.groupby('release_year').size()
    fig = px.line(x=yearly_movies.index, y=yearly_movies.values)
    fig.update_layout(title="Number of Movies by Year",
                     xaxis_title="Year",
                     yaxis_title="Number of Movies")
    st.plotly_chart(fig)
    
    # Top Movies
    st.subheader("Top Grossing Movies")
    top_movies = eda.get_top_movies('revenue', n=10)
    st.dataframe(pd.DataFrame(top_movies))

def show_movie_explorer(df):
    st.header("Movie Explorer")
    
    # Movie search
    movie_title = st.selectbox("Select a movie", df['title'].sort_values())
    
    if movie_title:
        movie = df[df['title'] == movie_title].iloc[0]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Details")
            st.write(f"**Release Date:** {movie['release_date'].strftime('%Y-%m-%d')}")
            st.write(f"**Runtime:** {movie['runtime']} minutes")
            st.write(f"**Genres:** {', '.join(movie['genre_names'])}")
            st.write(f"**Director:** {movie['director']}")
            
        with col2:
            st.subheader("Metrics")
            st.write(f"**Budget:** ${movie['budget']:,.2f}")
            st.write(f"**Revenue:** ${movie['revenue']:,.2f}")
            st.write(f"**ROI:** {movie['roi']*100:.1f}%")
            st.write(f"**Vote Average:** {movie['vote_average']:.1f}")
            
        st.subheader("Overview")
        st.write(movie['overview'])

def show_recommendations(df, recommender):
    st.header("Movie Recommendations")
    
    # Movie selection
    movie_title = st.selectbox("Select a movie for recommendations", 
                              df['title'].sort_values())
    
    if movie_title:
        recommendations = recommender.get_recommendations(movie_title)
        
        st.subheader("Similar Movies")
        for movie in recommendations:
            with st.expander(f"{movie['title']} ({movie['vote_average']:.1f}★)"):
                st.write(f"**Genres:** {', '.join(movie['genre_names'])}")
                st.write(movie['overview'])

def show_genre_analysis(df, eda):
    st.header("Genre Analysis")
    
    # Genre distribution
    genre_counts = eda.analyze_genres()
    fig = px.bar(x=genre_counts.index, y=genre_counts.values)
    fig.update_layout(title="Movies by Genre",
                     xaxis_title="Genre",
                     yaxis_title="Number of Movies")
    st.plotly_chart(fig)
    
    # Genre performance
    st.subheader("Genre Performance")
    genre_metrics = []
    
    for genre in genre_counts.index:
        genre_movies = df[df['genre_names'].apply(lambda x: genre in x)]
        genre_metrics.append({
            'genre': genre,
            'avg_revenue': genre_movies['revenue'].mean(),
            'avg_rating': genre_movies['vote_average'].mean(),
            'avg_roi': genre_movies['roi'].mean()
        })
    
    metrics_df = pd.DataFrame(genre_metrics)
    
    metric = st.selectbox("Select metric", 
                         ['avg_revenue', 'avg_rating', 'avg_roi'])
    
    fig = px.bar(metrics_df, x='genre', y=metric)
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()