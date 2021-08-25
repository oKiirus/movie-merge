import pandas as pd
import numpy as pd
from sklearn.metrics.pairwise import cosine_similarity as cos
from sklearn.feature_extraction.text import CountVectorizer as cv

data = pd.read_csv('movies.csv')

count = cv(stop_words = 'english')
countMetrics = count.fit_transform(data['words'])

cm = cos(countMetrics, countMetrics)

data = data.reset_index()
idx = pd.Series(data.index, index = data['title'])

def findRec(title):
  id = idx[title]
  score = list(enumerate(cm[id]))
  score = sorted(score, key = lambda x : x[1], reverse = True)
  score = score[1 : 11]
  movies = [i[0] for i in score] 
  return data[['title', 'release_data', 'runtime', 'vote_average', 'overview']].iloc[movies].tolist()