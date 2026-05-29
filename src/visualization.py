import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('darkgrid')
df=pd.read_csv('netflix_cleaned_featured.csv')
#movies vs tv shows
sns.countplot(data=df,x='type',hue='rating_group', order=df['type'].value_counts().index)
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.title("Distribution of Movies vs TV Shows")
plt.savefig('DistributionOfMoviesAndTvShows.png',dpi=300,bbox_inches='tight')



df_country = df.copy()

df_country['country'] = df_country['country'].str.split(', ')
df_country = df_country.explode('country')
df_country = df_country[df_country['country'] != 'Unknown']
top_countries = df_country['country'].value_counts().head(10)
country_type = df_country.groupby(['country', 'type']).size().reset_index(name='count')
top_countries = df_country['country'].value_counts().head(15)
top_list = top_countries.index
country_type = country_type[country_type['country'].isin(top_list)]



plt.figure(figsize=(10,5))
sns.countplot(data=df,x='year_added',hue='type',order=df['year_added'].value_counts().index)
plt.xlabel("Year added")
plt.ylabel("Count")
plt.title('Year added vs Type')
plt.savefig('YearvsType.png',dpi=300,bbox_inches='tight')



sns.barplot(
    x=top_countries.values,
    y=top_countries.index,
    palette='viridis'
)

plt.title("Top 10 Countries on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Country")

plt.savefig('TopCountries.png',dpi=300,bbox_inches='tight')


plt.figure(figsize=(12,6))

sns.barplot(
    data=country_type,
    x='country',
    y='count',
    hue='type'
)

plt.title("Movies vs TV Shows by Top Countries")
plt.xlabel("Country")
plt.ylabel("Count")

plt.xticks(rotation=45)
plt.legend(title="Type")

plt.savefig('movievsshowsintop.png',dpi=300,bbox_inches='tight')


df_genre = df.copy()

df_genre['listed_in'] = df_genre['listed_in'].str.split(', ')
df_genre = df_genre.explode('listed_in')

'''top 10 genre'''
top_genres = df_genre['listed_in'].value_counts().head(10)

plt.figure(figsize=(10,5))

sns.barplot(
    x=top_genres.values,
    y=top_genres.index,
    palette='magma'
)

plt.title("Top 10 Netflix Genres")
plt.xlabel("Number of Titles")
plt.ylabel("Genre")

plt.savefig('top10genre.png',dpi=300,bbox_inches='tight')

genre_type = df_genre.groupby(['listed_in', 'type']).size().reset_index(name='count')
top_list = top_genres.index
genre_type = genre_type[genre_type['listed_in'].isin(top_list)]


plt.figure(figsize=(12,6))

sns.barplot(
    data=genre_type,
    x='listed_in',
    y='count',
    hue='type',
    palette='Set2'
)

plt.title("Top Genres by Movies vs TV Shows")
plt.xlabel("Genre")
plt.ylabel("Count")

plt.xticks(rotation=45)
plt.legend(title="Type")

plt.savefig('groupedgenre.png',dpi=300,bbox_inches='tight')


sns.histplot(df['content_age'], bins=30)
plt.savefig('contentage.png',dpi=300,bbox_inches='tight')


sns.histplot(df['release_year'], bins=30)
plt.savefig('releaseyear.png',dpi=300,bbox_inches='tight')


top_directors = (
    df[df['director'] != 'Unknown']['director']
    .value_counts()
    .head(15)
)
sns.barplot(
    x=top_directors.values,
    y=top_directors.index
)

plt.title("Top 15 Directors")
plt.xlabel("Number of Titles")
plt.ylabel("Director")

plt.savefig('topdirectors.png',dpi=300,bbox_inches='tight')


movies = df[df['type'] == 'Movie'].copy()

movies['duration_num'] = (
    movies['duration']
    .str.extract(r'(\d+)')
    .astype(int)
)

plt.figure(figsize=(10,6))

sns.scatterplot(
    data=movies,
    x='duration_num',
    y='cast_count',
    alpha=0.6
)

plt.xlabel("Movie Duration (minutes)")
plt.ylabel("Cast Count")
plt.title("Movie Duration vs Cast Count")

plt.savefig('moviedurationvscastcount.png',dpi=300,bbox_inches='tight')


num_cols = [
    'release_year',
    'year_added',
    'content_age',
    'cast_count',
    'director_count',
    'country_count',
    'genre_count'
]

plt.figure(figsize=(10,6))

sns.heatmap(
    df[num_cols].corr(),
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title("Correlation Heatmap of Numerical Features")
plt.savefig('CorrelationHeatmap.png', dpi=300, bbox_inches='tight')
plt.show()  


plt.figure(figsize=(10,6))

sns.boxplot(
    data=df,
    x='genre_count',
    y='cast_count'
)

plt.title("Cast Count Distribution by Genre Count")

sns.violinplot(
    data=df,
    x='genre_count',
    y='cast_count'
)

plt.savefig('genrevscast.png', dpi=300, bbox_inches='tight')

