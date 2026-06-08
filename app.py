import streamlit as st
import pickle
import joblib

st.title("Movie Recommendation System")

with open('movie_list.pkl', 'rb') as m:
    movies = pickle.load(m)

similarities = joblib.load('similarity.joblib')

movies_name = movies['title'].values


def recommend(select_movie):
    index = movies[movies['title'] == select_movie].index[0]
    distances = similarities[index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

select_movie = st.selectbox("Select a Movie Name", options=movies_name)

st.write("You have selected: ", select_movie)

if st.button("Recommend"):
    recommend_movies = recommend(select_movie)

    st.write("Recommendations will be are")

    for i in recommend_movies:
        st.write(i)
