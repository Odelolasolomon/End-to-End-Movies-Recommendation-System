from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd

class FeatureEngineer:
    def __init__(self, df):
        self.df = df.copy()
        self.label_encoders = {}
        
    def create_combined_features(self):
        """Create combined features for content-based filtering"""
        self.df['combined_features'] = self.df.apply(self._combine_text_features, axis=1)
        return self.df
    
    def _combine_text_features(self, row):
        """Combine text features for a single movie"""
        features = []
        if isinstance(row['overview'], str):
            features.append(row['overview'])
        if isinstance(row['tagline'], str) and row['tagline']:
            features.append(row['tagline'])
        features.extend([' '.join(row['genre_names'])])
        features.extend([' '.join(row['main_cast'])])
        if row['director']:
            features.append(row['director'])
        return ' '.join(features)
    
    def encode_categorical_features(self):
        """Encode categorical features"""
        categorical_cols = ['original_language', 'status']
        
        for col in categorical_cols:
            le = LabelEncoder()
            self.df[f'{col}_encoded'] = le.fit_transform(self.df[col].astype(str))
            self.label_encoders[col] = le
            
        # One-hot encode genres (multiple genres per movie)
        genres = set()
        for genre_list in self.df['genre_names']:
            genres.update(genre_list)
            
        for genre in genres:
            self.df[f'genre_{genre}'] = self.df['genre_names'].apply(
                lambda x: 1 if genre in x else 0)
        
        return self.df
    
    def normalize_numeric_features(self):
        """Normalize numeric features"""
        numeric_cols = ['budget', 'revenue', 'runtime', 'popularity', 
                       'vote_average', 'vote_count', 'roi']
        
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(self.df[numeric_cols])
        
        for i, col in enumerate(numeric_cols):
            self.df[f'{col}_normalized'] = scaled_features[:, i]
            
        return self.df