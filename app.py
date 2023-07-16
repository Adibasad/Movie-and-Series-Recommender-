import streamlit as st
import pickle
import pandas as pd

#importing cs matrix
cs = pickle.load(open('similarity.pkl','rb'))

#importing movies df
movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)


#recommender function
def recom(title):
  m_index = pd.Index(movies['title']).get_loc(title)
  distances = cs[m_index]
  enum = list(enumerate(distances))
  sorted_list = sorted(enum,reverse=True,key=lambda x:x[1])

  #get top 10
  get_rec=[]
  top10 = sorted_list[1:11]
  for i in top10:
      idx=i[0]
      get_rec.append(movies.iloc[idx])
  # req_idx = [i[0] for i in top10]
  return get_rec

st.title('Movies Recommemder System')

selected = st.selectbox(
    'select a movie',(movies['title'].values)
)

if st.button('Recommend'):
    #recommed func
    recommendation = recom(selected)
    for i in recommendation:
        st.write(i)
