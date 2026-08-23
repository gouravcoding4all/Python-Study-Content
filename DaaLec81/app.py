#importing required libraries
import streamlit as st

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#setting page configuration
st.set_page_config(page_title="Sara Enterprises" , layout='wide')
st.header("SARA ENTERPRISES")
st.text("Dashboard for sales dataset of Medical Products from Sara Enterprises with slicers plots and dataframes")

#loading Dataset
df=pd.read_excel(r"C:\Users\dell\Downloads\1775106859-Financial_Sample.xlsx")
df.columns = df.columns.str.strip()

#Data cleaning(Removing null values)
for col in df.columns:
    if df[col].isnull().sum()>0:
        if df[col].dtype in [object , str]:
            df[col]=df[col].fillna(df[col].mode()[0])
        else:
            df[col]=df[col].fillna(round(df[col].mean(),2))

#Slicers
col1,col2,col3,col4,col5=st.columns(5)
with col1:
    country=st.selectbox("select Country",['All']+list(df.Country.unique()))
    if country!="All":
        df=df[df['Country']==country]
with col2:
    segment=st.selectbox("select Segtment",['All']+list(df.Segment.unique()))
    if segment!="All":
        df=df[df['Segment']==segment]
with col3:
    product=st.selectbox("select Product",['All']+list(df.Product.unique()))
    if product!="All":
        df=df[df['Product']==product]
with col4:
    db=st.selectbox("select Discount Band",['All']+list(df['Discount Band'].unique()))
    if db!="All":
        df=df[df['Discount Band']==db]
with col5:
    year=st.selectbox("select Year",['All']+list(df.Year.unique()))
    if year!="All":
        df=df[df['Year']==year]

#KPIs(Key Point Indicators)
col1 , col2 , col3 , col4 , col5 = st.columns(5)
li = ['Sales','Profit','Units Sold','COGS','Discounts']
cols = [col1,col2,col3,col4,col5]
i = 0
for col in cols:
    with col:
        if df[li[i]].sum()/1000000>1:
            st.metric("Total"+str(li[i]),str(round(df[li[i]].sum()/1000000,2))+"M")
        elif df[li[i]].sum()/1000>1:
            st.metric("Total"+str(li[i]),str(round(df[li[i]].sum()/1000,2))+"K")
        else:
            st.metric("Total"+str(li[i]),str(round(df[li[i]].sum(),2)))
    i=i+1

#Plotting/Graphs
col1 , col2 = st.columns(2)
x_axis = ['Country','Segment','Product','Discount Band']
y_axis = ['Profit','Sales','Units Sold','COGS']
with col1:
    colx,coly=st.columns(2)
    with colx:
        x=st.selectbox("Select X-Axis",x_axis)
    with coly:
            y=st.selectbox("Select Y-Axis Data Point",y_axis)
    pbs = df.groupby(x).agg({y:'sum'}).reset_index()
    fig , ax=plt.subplots(figsize=(12,4))
    ax.bar(pbs[x],pbs[y])
    st.pyplot(fig)
with col2:
    cola,colb = st.columns(2)
    x_axis = ['Month Number',"Year"]
    with cola:
        x = st.selectbox("Select Trend",x_axis)
    with colb:
        y = st.selectbox("Select Data",y_axis)
    pbm = df.groupby(x).agg({y:'sum'}).reset_index()
    fig2 ,ax2 = plt.subplots(figsize=(12,4))
    ax2.plot(pbm[x],pbm[y])
    st.pyplot(fig2)

#Sample Dataset
st.text("This is the filter dataset of shape"+str(df.shape))
st.dataframe(df,height=250)