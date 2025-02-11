import pandas as pd
from sklearn.neighbors import NearestNeighbors
import numpy as np
#Declare the File Path
file_path = 'C://Users//AjayM//Downloads//Modified_Book_for_retail_with_harry_potter(2).xlsx'

df = pd.read_excel(file_path)
average_ratings = df.groupby(['Book_ID', 'Genre'])['Rating'].mean().reset_index()
average_ratings = average_ratings.rename(columns={'Rating': 'Average_Rating'})
genre_dummies = pd.get_dummies(average_ratings['Genre'], prefix='Genre')
X = pd.concat([average_ratings[['Book_ID', 'Average_Rating']], genre_dummies], axis=1)
def recommend_books_by_genre_ml(genre, num_recommendations=5):
    genre_books = average_ratings[average_ratings['Genre'] == genre]
    
    if genre_books.empty:
        print(f"No books found for genre '{genre}'.")
        return pd.DataFrame(columns=['Book_ID', 'Average_Rating'])
# KNN Algorithm Declaration
    genre_books_features = X[X['Book_ID'].isin(genre_books['Book_ID'])]
    knn = NearestNeighbors(n_neighbors=num_recommendations, algorithm='auto')
    knn.fit(X.drop(columns=['Book_ID']))

    distances, indices = knn.kneighbors(genre_books_features.drop(columns=['Book_ID']))

    recommended_books = []
    for idx_list in indices:
        for idx in idx_list:
            recommended_books.append(X.iloc[idx][['Book_ID', 'Average_Rating']])

    recommended_books_df = pd.DataFrame(recommended_books, columns=['Book_ID', 'Average_Rating'])
    recommended_books_df = recommended_books_df.drop_duplicates().sort_values(by='Average_Rating', ascending=False)
    
    return recommended_books_df.head(num_recommendations)
genre = input("Enter the genre you're interested in: ")
recommendations = recommend_books_by_genre_ml(genre=genre, num_recommendations=5)
print(f"Recommended Books in '{genre}' genre:")
print(recommendations)
