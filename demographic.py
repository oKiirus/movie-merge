import pandas as pd
import numpy as pd

data = pd.read_csv('movies.csv')
C = data['vote_average'].mean()
m = data['vote_count'].quantile(0.9)
new_data = data.copy().loc[data['vote_count'] >= m]

def ratings(x):
  v = x['vote_count'] 
  R = x['vote_average']
  return (v/(v + m)*R) + (m/(m + v)*C)

new_data['score'] = new_data.apply(ratings, axis = 1)
new_data = new_data.sort_values('score', ascending=False)

output = new_data[['title', 'release_data', 'runtime', 'vote_average', 'overview']].head(20).values.tolist()
