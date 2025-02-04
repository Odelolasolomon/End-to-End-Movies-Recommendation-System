import pandas as pd
import numpy as np
from ast import literal_eval
import json
import logging

class MovieDataLoader:
    def __init__(self, file_path, log_level=logging.INFO):
        """
        Initialize MovieDataLoader with logging
        
        Args:
            file_path (str): Path to the movies CSV file
            log_level (int): Logging level
        """
        self.file_path = file_path
        
        # Configure logging
        logging.basicConfig(
            level=log_level, 
            format='%(asctime)s - %(levelname)s: %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def load_data(self):
        """
        Load and clean movie dataset
        
        Returns:
            pd.DataFrame: Cleaned and processed movie dataset
        """
        try:
            # Read CSV file
            self.logger.info(f"Loading data from {self.file_path}")
            df = pd.read_csv(self.file_path)
            
            # Log initial dataset info
            self.logger.info(f"Initial dataset shape: {df.shape}")
            
            # Clean and process data
            cleaned_df = self._clean_data(df)
            
            # Log cleaned dataset info
            self.logger.info(f"Cleaned dataset shape: {cleaned_df.shape}")
            
            return cleaned_df
        
        except Exception as e:
            self.logger.error(f"Error loading dataset: {e}")
            raise
    
    def _clean_data(self, df):
        """
        Comprehensive data cleaning method
        
        Args:
            df (pd.DataFrame): Input DataFrame
        
        Returns:
            pd.DataFrame: Cleaned DataFrame
        """
        # Deep copy to avoid warnings
        df = df.copy()
        
        # Cleaning methods for specific columns
        cleaning_methods = {
            'genres': self._clean_genres,
            'homepage': self._clean_homepage,
            'keywords': self._clean_keywords,
            'overview': self._clean_overview,
            'release_date': self._clean_release_date,
            'runtime': self._clean_runtime,
            'tagline': self._clean_tagline,
            'cast': self._clean_cast,
            'crew': self._clean_crew
        }
        
        # Apply cleaning methods
        for column, method in cleaning_methods.items():
            if column in df.columns:
                try:
                    df[column] = df[column].apply(method)
                    self.logger.info(f"Cleaned column: {column}")
                except Exception as e:
                    self.logger.warning(f"Error cleaning {column}: {e}")
        
        # Additional data enrichment
        df = self._enrich_data(df)
        
        return df
    
    def _clean_genres(self, genres):
        """Clean and standardize genres"""
        try:
            # Handle NaN or empty values
            if pd.isna(genres) or genres == '':
                return [{'name': 'Unknown'}]
            
            # Parse string representation or use existing
            parsed_genres = literal_eval(genres) if isinstance(genres, str) else genres
            
            # Ensure list of dicts with 'name' key
            if not parsed_genres:
                return [{'name': 'Unknown'}]
            
            # Validate genre structure
            return [
                {'name': genre['name'] if isinstance(genre, dict) and 'name' in genre else str(genre)} 
                for genre in parsed_genres
            ]
        except Exception:
            return [{'name': 'Unknown'}]
    
    def _clean_homepage(self, homepage):
        """Clean homepage column"""
        return homepage if pd.notna(homepage) and homepage != '' else ''
    
    def _clean_keywords(self, keywords):
        """Clean keywords column"""
        try:
            if pd.isna(keywords) or keywords == '':
                return []
            
            parsed_keywords = literal_eval(keywords) if isinstance(keywords, str) else keywords
            return parsed_keywords if parsed_keywords else []
        except Exception:
            return []
    
    def _clean_overview(self, overview):
        """Clean overview column"""
        return overview if pd.notna(overview) and overview != '' else 'No description available.'
    
    def _clean_release_date(self, date):
        """Clean and convert release date"""
        try:
            return pd.to_datetime(date, errors='coerce')
        except Exception:
            return pd.NaT
    
    def _clean_runtime(self, runtime):
        """Clean runtime column"""
        return runtime if pd.notna(runtime) else np.nan
    
    def _clean_tagline(self, tagline):
        """Clean tagline column"""
        return tagline if pd.notna(tagline) and tagline != '' else ''
    
    def _clean_cast(self, cast):
        """Clean cast column"""
        try:
            if pd.isna(cast) or cast == '':
                return []
            
            parsed_cast = literal_eval(cast) if isinstance(cast, str) else cast
            return parsed_cast if parsed_cast else []
        except Exception:
            return []
    
    def _clean_crew(self, crew):
        """Clean crew column"""
        try:
            if pd.isna(crew) or crew == '':
                return []
            
            parsed_crew = literal_eval(crew) if isinstance(crew, str) else crew
            return parsed_crew if parsed_crew else []
        except Exception:
            return []
    
    def _enrich_data(self, df):
        """
        Enrich dataset with additional derived features
        
        Args:
            df (pd.DataFrame): Input DataFrame
        
        Returns:
            pd.DataFrame: DataFrame with additional features
        """
        # Extract director
        df['director'] = df['crew'].apply(self._extract_director)
        
        # Extract main cast (top 3)
        df['main_cast'] = df['cast'].apply(
            lambda x: [actor['name'] for actor in x[:3]] if x else []
        )
        
        # Extract genre names
        df['genre_names'] = df['genres'].apply(
            lambda x: [genre['name'] for genre in x]
        )
        
        # Add release year and month
        df['release_year'] = df['release_date'].dt.year
        df['release_month'] = df['release_date'].dt.month
        
        # Compute additional metrics
        df['roi'] = np.where(
            df['budget'] > 0, 
            (df['revenue'] - df['budget']) / df['budget'], 
            0
        )
        
        return df
    
    def _extract_director(self, crew):
        """Extract primary director from crew"""
        if not crew:
            return 'Unknown'
        
        directors = [
            member.get('name', 'Unknown') 
            for member in crew 
            if member.get('job', '').lower() == 'director'
        ]
        
        return directors[0] if directors else 'Unknown'
    
    def validate_cleaning(self, df):
        """
        Validate data cleaning process
        
        Args:
            df (pd.DataFrame): Cleaned DataFrame
        
        Returns:
            dict: Validation metrics
        """
        validation_results = {
            'total_rows': len(df),
            'columns': list(df.columns),
            'missing_values': df.isnull().sum().to_dict(),
            'data_types': df.dtypes.to_dict(),
            'genre_distribution': df['genre_names'].explode().value_counts().head(10).to_dict(),
            'year_range': {
                'min_year': df['release_year'].min(),
                'max_year': df['release_year'].max()
            }
        }
        
        return validation_results

def main():
    # Example usage
    loader = MovieDataLoader('movies.csv')
    df = loader.load_data()
    
    # Validate cleaning
    validation = loader.validate_cleaning(df)
    
    # Print validation results
    for key, value in validation.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()