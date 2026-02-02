import streamlit as st
import pickle
import pandas as pd
import requests

api_key = ""

def fetch_imdbID(movie_title):
    response = requests.get(f"https://www.omdbapi.com/?t={movie_title}&apikey={api_key}&")
    data_received = response.json()
    return data_received['imdbID']


def fetch_poster(imdbID):
    response = f"https://img.omdbapi.com/?i={imdbID}&apikey={api_key}&"
    # data = response.json()
    return response

def recommend(movie):
    movie_index = movies[movies['title']==movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key= lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        movie_name = movies.iloc[i[0]].title
        movie_imdbid = fetch_imdbID(movie_name)
        recommended_movies_posters.append(fetch_poster(movie_imdbid))
    return recommended_movies, recommended_movies_posters

movie_dict = pickle.load(open('model/movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('model/similarity.pkl', 'rb'))

st.title("Movie Recommender System")

selected_movie = st.selectbox(
    "Find me a movie similar to:",
    movies['title'].values
)


if st.button('Recommend'):
    names, poster = recommend(selected_movie)
    
    col1, col2, col3, col4, col5 = st.columns(5, width = 5000, gap="small")

    with col1:
        st.text(names[0])
        st.image(poster[0])
    with col2:
        st.text(names[1])
        st.image(poster[1])
    with col3:
        st.text(names[2])
        st.image(poster[2])
    with col4:
        st.text(names[3])
        st.image(poster[3])
    with col5:
        st.text(names[4])
        st.image(poster[4])