import streamlit as st
import pickle
import requests
from dotenv import load_dotenv
import os
from concurrent.futures import ThreadPoolExecutor

load_dotenv()



@st.cache_resource
def load_data():
    movies = pickle.load(open("movies.pkl", "rb"))
    similarity = pickle.load(open("similarity.pkl", "rb"))
    return movies, similarity

movies, similarity = load_data()



session = requests.Session()



@st.cache_data
def fetch_poster(movie_id):

    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {os.getenv('TMDB_API_KEY')}"
    }

    try:
        response = session.get(
            url,
            headers=headers,
            timeout=5
        )

        response.raise_for_status()

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return f"https://image.tmdb.org/t/p/w500{poster_path}"

        return None

    except Exception:
        return None



def recommend(movie_name):

    movie_index = movies[movies['title'] == movie_name].index[0]

    distances = similarity[movie_index]

    movie_list = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    recommended_movies = []
    movie_ids = []

    for i in movie_list:
        recommended_movies.append(
            movies.iloc[i[0]].title
        )

        movie_ids.append(
            movies.iloc[i[0]].movie_id
        )

    # Fetch all posters in parallel
    with ThreadPoolExecutor(max_workers=5) as executor:
        recommended_movies_posters = list(
            executor.map(fetch_poster, movie_ids)
        )

    return recommended_movies, recommended_movies_posters



st.title("Movie Recommendation System")

selected_movie = st.selectbox(
    "Select a movie:",
    movies["title"].values
)

if st.button("Get Recommendations"):

    with st.spinner("Finding recommendations..."):
        names, posters = recommend(selected_movie)

    cols = st.columns(5)

    for i, col in enumerate(cols):
        with col:

            if posters[i]:
                st.image(posters[i], width="stretch")
            else:
                st.write("No Poster")

            st.caption(names[i])