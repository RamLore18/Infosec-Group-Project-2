import pickle # This lets us use the saved model file
import numpy as np # For math operations, but it's not really used here
import streamlit as st  # This is for making the web app

model = pickle.load(open('model.pkl', 'rb')) # Loads the model that's already been trained from a file called model.pkl

col0, col1, col2, col3, col4, col5, col6 = st.columns([0.2, 0.2, 0.2, 6, 0.2, 0.2, 0.2]) # Makes 7 columns to put the title in the middle

with col0:
    st.write('')
with col1:
    st.write('')
with col2:
    st.write('')    
with col3:
    st.markdown("<h1 style='text-align: center;'>ⴍage</h1>", unsafe_allow_html=True) # Shows the title "ⴍage" in the center
with col4:
    st.write('')
with col5:
    st.write('')
with col6:
    st.write('')

col7, col8, col9 = st.columns(3) # Makes 3 columns for a small description
with col7:
    st.write('')    
with col8:
    st.markdown("<h6 style='text-align: center;'>A simple web app to predict annual salary</h6>", unsafe_allow_html=True) # Adds some text to say what the app does
with col9:
    st.write('')

# Lists for the options users can pick
gen_list = ["Female", "Male"]
edu_list = ["Bachelor's", "Master's", "PhD"]
job_list = ["Director of Marketing", "Director of Operations", "Senior Data Scientist", "Senior Financial Analyst", "Senior Software Engineer"]
job_idx = [0, 1, 10, 11, 20]

# To let users pick their info
gender = st.radio('Pick your gender', gen_list) # Buttons to choose gender
age = st.slider('Pick your age', 21, 55)   # Slider for age
education = st.selectbox('Pick your education level', edu_list)   # Dropdown for education level
job = st.selectbox('Pick your job title', job_list)   # Dropdown for job title
experience = st.slider('Pick your years of experience', 0.0, 25.0, 0.0, 0.5, "%1f") # Slider for years of experience

col10, col11, col12, col13, col14 = st.columns(5) # Makes 5 columns to put the predict button in the middle
with col10:
    st.write('')
with col11:
    st.write('')    
with col12:
    predict_btn = st.button('Predict Salary') # Button to get the salary
with col13:
    st.write('')
with col14:
    st.write('')

if(predict_btn): # If the button is clicked, do the prediction
    # To get the user’s inputs as numbers
    inp1 = int(age)
    inp2 = float(experience)
    inp3 = int(job_idx[job_list.index(job)])
    inp4 = int(edu_list.index(education))
    inp5 = int(gen_list.index(gender))
    X = [inp1, inp2, inp3, inp4, inp5] # Puts all inputs in a list
    salary = model.predict([X]) # Uses model to guess the salary
    
    # To show the result in the middle
    col15, col16, col17 = st.columns(3)
    with col15:
        st.write('')    
    with col16:
        st.text(f"Estimated salary: ${int(salary[0])}") # Shows the salary with a dollar sign
    with col17:
        st.write('')


