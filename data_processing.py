import numpy as np
import pandas as pd
import ast
import nltk
from nltk.stem.porter import PorterStemmer 
ps = PorterStemmer()



#importing raw datas
movies = pd.read_csv('tmdb_5000_movies.csv')
credit = pd.read_csv('tmdb_5000_credits.csv')

#Functions
def convert(obj):
    L =[]
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

def convert_cast(obj):
    L =[]
    count=0
    for i in ast.literal_eval(obj):
        if count!=3:
            L.append(i['name'])
            count+=1
        else:
            break
    return L

def get_director(obj):
    L =[]
    for i in ast.literal_eval(obj):
        if i['job']=='Director':
         L.append(i['name'])
    return L

def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)



#Preprocessing Data
merge_data = movies.merge(credit,on='title')
data = merge_data[['movie_id', 'title', 'overview','genres','keywords','cast', 'crew']]
data.dropna(inplace=True) #will drop null records
data['genres'] = data['genres'].apply(convert)
data['keywords'] = data['keywords'].apply(convert)
data['cast']=data['cast'].apply(convert_cast)
data['crew']=data['crew'].apply(get_director)
data['overview']=data['overview'].apply(lambda x:x.split())

data['genres']=data['genres'].apply(lambda X:[i.replace(" ","")for i in X])
data['keywords']=data['keywords'].apply(lambda X:[i.replace(" ","")for i in X])
data['cast']=data['cast'].apply(lambda X:[i.replace(" ","")for i in X])
data['crew']=data['crew'].apply(lambda X:[i.replace(" ","")for i in X])

data['tags']=data['overview']+data['crew']+data['cast']+data['keywords']+data['genres']

new_df = data[['movie_id','title','tags']]
new_df['tags'] = new_df['tags'].apply(lambda x:" ".join(x))
new_df['tags'] = new_df['tags'].apply(lambda x:x.lower())

new_df['tags'] = new_df['tags'].apply(stem)

new_df.to_csv('processed_data.csv')
# print(new_df['tags'][0])
# print(stem('loved you'))

