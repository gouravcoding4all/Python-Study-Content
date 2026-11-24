# Importing Required Libraries
import streamlit as st
import pandas as pd
import joblib

#load the dataset
df = pd.read_csv('datasets/clean_data.csv')
df =df.dropna()
input_cols = ['Age','Gender','Family_Income','Internet_Access','Study_Hours_Per_Day','Attendance_Rate', 'Assignment_Delay_Days',
       'Travel_Time_Minutes', 'Part_Time_Job', 'Scholarship', 'Stress_Index',
       'GPA', 'Semester_GPA', 'CGPA', 'Semester', 'Department',
       'Parental_Education']

# st.sidebar.header("Dashboard")
# st.subheader("Total Students : "+str(df.shape[0]))
# st.sidebar.button("check student By SID")
# st.sidebar.button("By Enter Detail")
# st.sidebar.button("Multiple Students")

# Load Model Function
def load_model():
    # Load the model from a file
    model = joblib.load('models/dropout_model.pkl')
    return model

# Set Page Configuration
st.set_page_config(page_title="Dropout Prediction App",page_icon=":bar_chart",layout="wide")

st.header("Dropout Prediction App")
st.text("This app predicts the likelihood of a student dropping out based on various features.")

#Student Input Features
st.divider()
st.text_input("Enter Student Name")
age = st.slider("Age", min_value=10, max_value=30, value=18)
col1 , col2 = st.columns(2)
with col1:
    gender = st.selectbox("Select Gender",df.Gender.unique())
    internet = st.selectbox("Internet Access?",df.Internet_Access.unique())
    assignment_delay = st.selectbox("Assignment Delay Days",sorted(df.Assignment_Delay_Days.unique())   )
    part_time =st.selectbox("Part Time Job?",df.Part_Time_Job_unique())
    scholarship = st.selectbox("Scholarship?",df.Scholarship.unique())
    semester = st.selectbox("Select Semester",df.Semester.unique())
    department = st.selectbox("Select Department",df.Department.unique())
    parental_education = st.selectbox("Select Parental Education",df.Parental_Education.unique())

with col2:
    income = st.number_input("Enter Family Income")
    study_hours = st.slider("Enter Study Hours Per Day",1.0,12.0,3.5)
    attendance =st.slider("Enter Attendance Rate",1.0,100.0,60.0)
    travel_time = st.slider("Select Travel Time",df.Travel_Time_Minutes.min(),df.Travel_Time_Minutes.max(),df.Travel_Time_Minutes.mean())
    stress_index = st.slider("Select Stress Index",0.0,10.0,df.stress_Index.mean())
    semester_gpa = st.slider("Select Semester GPA",df.Semester_GPA.min(),df.Semester_GPA.max(),df.Semester_GPA.mean())
    gpa = st.slider("Select GPA",df.GPA.min(),df.GPA.max(),df.GPA.mean())
    cgpa = st.slider("Select CGPA",df.CGPA.min(),df.CGPA.max(),df.CGPA.mean())

data = [[age,gender,income,internet,study_hours,attendance,assignment_delay,travel_time,part_time,scholarship,stress_index,gpa,semester,department,parental_education]]
if st.button("Predict Dropout"):
    model = load_model()
    input_df = pd.DataFrame(data,columns=input_cols)
    y_pred = model.predict(input_df)
    if y_pred[0]==0:
        st.success("Not About To Dropout")
    else:
        st.error("He/She is about to Dropout")
    st.dataframe(input_df)

