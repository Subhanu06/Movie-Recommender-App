import streamlit as st
import pickle
import requests
from dotenv import load_dotenv
import os

load_dotenv()

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

print(f"movies.pkl size: {os.path.getsize('movies.pkl')/(1024*1024):.2f} MB")
print(f"similarity.pkl size: {os.path.getsize('similarity.pkl')/(1024*1024):.2f} MB")

st.title('Movie Recommendation System')

selected_movie = st.selectbox(
    'Select a movie:',
    movies['title'].values
)
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {os.getenv('TMDB_API_KEY')}"
    }
    

    response = requests.get(url, headers=headers)
    data = response.json()
    

    return "https://image.tmdb.org/t/p/w500"+data['poster_path']



def recommend(movie_name):

    movie_index = movies[movies['title'] == movie_name].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movie_list:
        movie_id=movies.iloc[i[0]].movie_id

        recommended_movies.append(
            movies.iloc[i[0]].title
        )
        recommended_movies_posters.append(
            fetch_poster(movie_id)
        )

    return recommended_movies, recommended_movies_posters




if st.button('Get Recommendations'):
    names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for i, col in enumerate(cols):
        with col:
            st.image(posters[i], width='stretch')
            st.caption(names[i])