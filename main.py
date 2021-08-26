import numpy as np
import pandas as pd
import ast
import nltk
from nltk.stem.porter import PorterStemmer 
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

ps = PorterStemmer()
cv = CountVectorizer(max_features=5000,stop_words='english')

data = pd.read_csv('processed_data.csv')

#function

def recommend(movie):
    movie_index = data[data['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]
    for i in movie_list:
        print(data.iloc[i[0]].title)

vectors = cv.fit_transform(data['tags']).toarray()
similarity = cosine_similarity(vectors)

# pickle.dump(data.to_dict(),open('movie_dict.pkl','wb'))
pickle.dump(similarity,open('similarity.pkl','wb'))


# print(recommend('Superman Returns'))
