import streamlit as st
import pickle


def recommend(movie):
  index=movies[movies['title']==movie].index[0].item()
  distances=similerty[index]
  movies_recommended=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
  recommended_movies=[]

  for i in movies_recommended:
    recommended_movies.append(movies.iloc[i[0]].title)
  return recommended_movies

movies = pickle.load(open('movies.pkl','rb'))
similerty = pickle.load(open('similerty.pkl','rb'))
movies_list = movies['title'].values

st.title('MOVIE RECOMMENDATION SYSTEM')

selected_movie_name = st.selectbox(
    "MOVIE NAME",
    (movies_list),
)
if st.button("RECOMMEND"):
    recommendation=recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)