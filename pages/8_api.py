import streamlit as st
import numpy as np
import requests

st.title('🏀 Movies API app')

st.sidebar.header('Input')
selected_type = st.sidebar.selectbox('Select a movie type', ["animation", "classic", "comedy", "drama", "horror", "family", "mystery", "western"])

movies_url = f'https://api.sampleapis.com/movies/{selected_type}'
json_data = requests.get(movies_url)
movies = json_data.json()

c1, c2 = st.columns(2)
with c1:
  with st.expander('About this app'):
    st.write('Need a movie suggestion? This API sends a list of movie lists depending on what category you select.')
with c2:
  with st.expander('JSON data'):
    st.write(movies)

movie = movies[np.random.randint(100)]
st.header('Suggested movie')

st.info(movie)

col1, col2, col3 = st.columns(3)
with col1:
  st.metric(label='title', value=movie['title'].capitalize(), delta='')
with col2:
  st.metric(label='poster URL', value=movie['posterURL'], delta='')
with col3:
  st.metric(label='imdbId', value=movie['imdbId'], delta='')