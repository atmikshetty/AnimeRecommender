import streamlit as st
import pickle

def recommend(movie):
    index = anime[anime['name'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(anime.iloc[i[0]]['name'])
        print(recommended_movie_names)
    return recommended_movie_names


st.header('Anime Recommender System')
anime = pickle.load(open('animes.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

anime_list = anime['name'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    anime_list
)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    for i in recommended_movie_names:
        st.write(i)