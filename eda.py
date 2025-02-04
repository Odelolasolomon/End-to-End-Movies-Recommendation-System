import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class MovieEDA:
    def __init__(self, df):
        self.df = df

        
    def generate_basic_stats(self):
        """Generate basic statistical analysis"""
        return {
            'total_movies': len(self.df),
            'avg_budget': self.df['budget'].mean(),
            'avg_revenue': self.df['revenue'].mean(),
            'avg_rating': self.df['vote_average'].mean(),
            'avg_runtime': self.df['runtime'].mean()
        }
    
    def get_top_movies(self, column, n=10):
        """Get top N movies by specified column"""
        return self.df.nlargest(n, column)[
            ['title', column, 'release_date', 'vote_average']
        ].to_dict('records')
    
    def analyze_genres(self):
        """Analyze genre distribution"""
        genres = []
        for genre_list in self.df['genre_names']:
            genres.extend(genre_list)
        return pd.Series(genres).value_counts()
    
    def analyze_languages(self):
        """Analyze language distribution"""
        return self.df['original_language'].value_counts()
    
    def plot_genre_distribution(self, save_path=None):
        """Plot top genres distribution"""
        plt.figure(figsize=(12, 6))
        self.analyze_genres().head(10).plot(kind='bar')
        plt.title('Top 10 Movie Genres')
        plt.xlabel('Genre')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
        return plt
    
    def plot_budget_revenue_correlation(self, save_path=None):
        """Plot budget vs revenue correlation"""
        plt.figure(figsize=(10, 6))
        plt.scatter(self.df['budget'], self.df['revenue'], alpha=0.5)
        plt.xlabel('Budget ($)')
        plt.ylabel('Revenue ($)')
        plt.title('Movie Budget vs Revenue')
        plt.tight_layout()
        if save_path:
            plt.savefig(save_path)
        return plt