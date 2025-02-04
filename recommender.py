from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class MovieRecommender:
    def __init__(self, df):
        self.df = df
        self.similarity_matrix = None
        
    def build_content_based_model(self):
        """Build content-based recommendation system"""
        tfidf = TfidfVectorizer(stop_words='english')
        tfidf_matrix = tfidf.fit_transform(self.df['combined_features'].fillna(''))
        self.similarity_matrix = cosine_similarity(tfidf_matrix)
        
    def get_recommendations(self, movie_title, n=5):
        """Get movie recommendations based on title"""
        try:
            idx = self.df[self.df['title'] == movie_title].index[0]
            sim_scores = list(enumerate(self.similarity_matrix[idx]))
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
            sim_scores = sim_scores[1:n+1]
            movie_indices = [i[0] for i in sim_scores]
            
            return self.df.iloc[movie_indices][
                ['title', 'genre_names', 'vote_average', 'overview']
            ].to_dict('records')
        except IndexError:
            return f"Movie '{movie_title}' not found in database."
    
    def get_popular_in_genre(self, genre, n=5):
        """Get top rated movies in a specific genre"""
        genre_movies = self.df[self.df['genre_names'].apply(lambda x: genre in x)]
        return genre_movies.nlargest(n, 'vote_average')[
            ['title', 'vote_average', 'genre_names']
        ].to_dict('records')