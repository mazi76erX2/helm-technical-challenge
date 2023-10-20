import pandas as pd

# Pandas
# Load the movies dataset
movies = pd.read_csv("movies.csv")

# Load the ratings dataset
ratings = pd.read_csv("ratings.csv")

# Load the links dataset
links = pd.read_csv("links.csv")

# Merge the datasets based on movieId
merged_data = pd.merge(movies, ratings, on="movieId")
merged_data = pd.merge(merged_data, links, on="movieId")

# Display the first few rows of the merged dataset
print(merged_data.head())

# Get the average rating for each movie
average_ratings = merged_data.groupby("title")["rating"].mean()
print("\nAverage ratings:")
print(average_ratings)

# Get the maximum rating for each genre
max_ratings_by_genre = merged_data.groupby("genres")["rating"].max()
print("\nMax ratings by genre:")
print(max_ratings_by_genre)

# Filter the dataset to only include movies with a rating above 4.5
highly_rated_movies = merged_data[merged_data["rating"] > 4.5]
print("\nHighly rated movies:")
print(highly_rated_movies)
