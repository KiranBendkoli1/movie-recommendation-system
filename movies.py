from click import open_file
import streamlit as st
import pickle
import pandas as pd

open_file= open("list.pkl","rb")
movies_file= open("movies.pkl","rb")
sm_file = open("similarity.pkl", "rb")
lst = pickle.load(open_file)
movies = pickle.load(movies_file)
similarity = pickle.load(sm_file)

def recommend(movie):
    movies_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movies_index]
    movies_list = sorted(list(enumerate(similarity[movies_index])),reverse=True, key=lambda x:x[1])[1:6]
    
    for i in movies_list:
        st.write(movies.iloc[i[0]].title)


st.title("Movie Recommendation System")
option = st.selectbox(
     'Select Movie',
     lst)

recommend(option)
# st.write('You selected:', option)