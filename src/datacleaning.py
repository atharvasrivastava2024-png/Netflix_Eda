import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df= pd.read_csv("netflix_titles.csv")

'''print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())'''

'''print(df.duplicated().sum())'''
df.drop_duplicates(inplace=True)

#missing_percent = (df.isnull().sum() / len(df)) * 100

#print(missing_percent.sort_values(ascending=False))

df['director'] =df['director'].fillna('Unknown')
df['cast'] =df['cast'].fillna('Unknown')
df['country'] =df['country'].fillna('Unknown')

df.dropna(subset=['date_added', 'rating'], inplace=True)


df['date_added'] = df['date_added'].str.strip()
df['date_added'] = pd.to_datetime(df['date_added'])

'''feature engineering'''
df['year_added'] = df['date_added'].dt.year
df['month_added'] = df['date_added'].dt.month
df['day_added'] = df['date_added'].dt.day
df['dayofweek_added'] = df['date_added'].dt.dayofweek
df['is_weekend'] = df['dayofweek_added'].isin([5, 6]).astype(int)


df['content_age'] = df['year_added'] - df['release_year']

df['cast_count'] = df['cast'].apply(lambda x: len(x.split(',')))
df['has_known_cast'] = (df['cast'] != "Unknown").astype(int)

df['has_director'] = (df['director'] != "Unknown").astype(int)
df['director_count'] = df['director'].apply(lambda x: len(x.split(',')))

df['country_count'] = df['country'].apply(lambda x: len(x.split(',')))
df['is_multinational'] = (df['country_count'] > 1).astype(int)

df['genre_count'] = df['listed_in'].apply(lambda x: len(x.split(',')))

rating_map = {
    'TV-Y': 'Kids', 'TV-Y7': 'Kids',
    'TV-G': 'Family',
    'TV-PG': 'Teen',
    'TV-14': 'Teen',
    'TV-MA': 'Adult',
    'R': 'Adult', 'PG-13': 'Teen'
}

df['rating_group'] = df['rating'].map(rating_map).fillna('Other')

print(df.info())
df.to_csv("netflix_cleaned_featured.csv", index=False)