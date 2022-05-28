import pickle
import streamlit as st
import numpy as np
import pandas as pd

course_list=pickle.load(open("courses.pkl","rb"))
similarities=pickle.load(open("sim.pkl","rb"))

indices = pd.Series(course_list.index, index=course_list['Course Name']).drop_duplicates()

def get_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(similarities[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    courses = [i[0] for i in sim_scores]
    getcourse=[]
    for i in sim_scores[1:6]:
        getcourse.append(course_list[i[0]])
    return getcourse

#set the title of the app
st.title('Course Recommender')

course_list = course_list['Course Name'].values
coursechosen = st.text_input("Enter the course name")
if(st.button("Recommend")):
    getcourse=get_recommendations(coursechosen)
    st.text(getcourse[0])
    st.text(getcourse[1])
    st.text(getcourse[2])
    st.text(getcourse[3])
    st.text(getcourse[4])