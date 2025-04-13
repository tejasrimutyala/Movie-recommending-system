import pickle
import streamlit as st
import requests
import pandas as pd

def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=2ccf527752d66c7fb488fd73819056b5&language=en-US"
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raises HTTPError for bad responses (4XX or 5XX)
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']
    except requests.exceptions.RequestException as e:
        print(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750.png?text=Poster+Unavailable"

def recommend(movie, num_recommendations=5):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:num_recommendations+1]:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)
    return recommended_movie_names, recommended_movie_posters

# Set page config
st.set_page_config(layout="wide")

# Load data
st.header('🎬 Movie Recommender System')

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Convert to DataFrame if not already
if isinstance(movies_dict, dict):
    movies = pd.DataFrame(movies_dict)
else:
    movies = movies_dict

movie_titles = movies['title'].tolist()

selected_movie = st.selectbox(
    "🎥 Type or select a movie from the dropdown",
    movie_titles
)

num_recommendations = st.slider(
    "Number of recommendations",
    min_value=1,
    max_value=10,
    value=5,
    step=1
)

if st.button('🎯 Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie, num_recommendations)

    cols = st.columns(num_recommendations)
    for i in range(num_recommendations):
        with cols[i]:
            text_container = st.container()
            with text_container:
                st.markdown(f"<div style='height: 60px; text-align: center;'><p>{recommended_movie_names[i]}</p></div>",
                           unsafe_allow_html=True)
            # Display the image with consistent width
            st.image(recommended_movie_posters[i], width=200)