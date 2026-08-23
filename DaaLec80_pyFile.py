# #%pip install streamlit
# import streamlit as st
# #Streamlit skills
# st.set_page_config(page_tittle="My Application",Layout="wide")
# st.header("My First web Application")
# st.subheader("This application is for data analysis tool etc")

# streamlit run DaaLec80_pyfile.py        -> for  run streamlit file             
# and install streamlit in terminal with command ->pip install streamlit
#python -m streamlit run C:\Users\dell\Downloads\DaaLec80_pyFile.py
#streamlit run C:\Users\dell\Downloads\DaaLec80_pyFile.py
import pandas as pd
import streamlit as st
st.set_page_config(page_title="My Application",layout="wide")
st.header("My First web Application")
st.subheader("This application is for data analysis tool etc")
n1=st.number_input("Enter A Number")
n2=st.number_input("Enter B Number")
if st.button("Addition"):
    st.subheader("Addition:"+str(n1+n2))

st.slider("Enter Age",0,120)
st.slider("Enter Distance in KM",0.0,100.0)
st.selectbox("Select Course",['Data Science','Data Analyst','Business Analyst'])
st.radio("Select Gender",["Male","Female"])

col1 , col2 , col3 , col4 , col5 = st.columns(5)
with col1:
    st.metric("Total Sales",9283468)
with col2:
    st.metric("Total Profit",725844)
with col3:
    st.metric("Total Profit",895643)
with col4:
    st.metric("Total Profit",684522)
with col5:
    st.metric("Total Profit",537862)

path=st.file_uploader("select your File",type=['csv','xlsx'])
df=pd.read_excel(path)
st.dataframe(df)