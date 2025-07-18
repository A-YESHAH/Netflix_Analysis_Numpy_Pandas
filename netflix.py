import pandas as pd
import numpy as np

netflix=pd.read_excel("netflix/netflix_titles.xlsx")
print(netflix.shape)
print(netflix.columns)
print(netflix.isnull().sum())
netflix['director']=netflix['director'].fillna('Not Specified')
netflix['cast']=netflix['cast'].fillna('Not specified')
netflix['date_added']=pd.to_datetime(netflix['date_added'],errors='coerce')
netflix['country']=netflix['country'].fillna('Not specified')
netflix['rating']=netflix['rating'].fillna('Not Specified')
netflix[['duration_int', 'duration_unit']] = netflix['duration'].str.extract(r'(\d+)\s*(\w+)')
netflix['duration_int']=pd.to_numeric(netflix['duration_int'],errors='coerce')
netflix['year_added'] = netflix['date_added'].dt.year

all_genres = netflix['listed_in'].str.split(', ').tolist()
flat_genres = np.hstack(all_genres)

genre_counts = pd.Series(flat_genres).value_counts()
print("Top 10 Genres:")
print(genre_counts.head(10))

countries=pd.Series(netflix['country']).value_counts().head(10)
print("Top 10 Countries")
print(countries)

content_per_year=pd.Series(netflix['year_added']).value_counts().sort_index()
print("Content Added Per Year:")
print(content_per_year)

tv_movie_trend=netflix.groupby(['year_added','type']).size().unstack().fillna(0).astype(int)
print("Movies vs TV Shows Added Per Year:")
print(tv_movie_trend)

