# ==============================
# 1. IMPORTING REQUIRED LIBRARIES
# ==============================

import streamlit as st
# Streamlit ko import kar rahe hain
# Streamlit se hum Python ka dashboard/web app bana sakte hain

import pandas as pd
# Pandas ko import kar rahe hain
# Pandas ka use table/data ko handle karne ke liye hota hai

import numpy as np
# NumPy ko import kar rahe hain
# NumPy numbers aur calculations ke liye useful hai

import matplotlib.pyplot as plt
# Matplotlib ka pyplot part import kar rahe hain
# Isse hum graphs/charts bana sakte hain

import seaborn as sns
# Seaborn ko import kar rahe hain
# Seaborn bhi beautiful graphs banane ke liye use hota hai


# ==============================
# 2. SETTING PAGE CONFIGURATION
# ==============================

st.set_page_config(
    page_title="Sara Enterprises",
    # Browser tab mein "Sara Enterprises" naam dikhega

    layout='wide'
    # Dashboard ko full screen/wide size mein dikhayega
)


st.header("SARA ENTERPRISES")
# Dashboard ke top par bada heading show karega


st.text(
    "Dashboard for sales dataset of Medical Products from Sara Enterprises with slicers plots and dataframes"
)
# Dashboard ke neeche simple information/text show karega


# ==============================
# 3. LOADING DATASET
# ==============================

df = pd.read_excel(
    r"C:\Users\dell\Downloads\1775106859-Financial_Sample.xlsx"
)
# Excel file ko read/load kar rahe hain
# pd.read_excel() Excel file ko Python ke andar laata hai
# df mein poora Excel data store ho jayega


df.columns = df.columns.str.strip()
# Column names ke aage/peeche ke extra spaces hata raha hai
# Example:
# " Sales "  --->  "Sales"
# Isse KeyError jaise problem se bach sakte hain


# ==============================
# 4. DATA CLEANING
# ==============================

for col in df.columns:
    # Excel ke har column ko ek-ek karke check karenge
    # col = current column ka naam

    if df[col].isnull().sum() > 0:
        # Check kar rahe hain ki column mein koi blank/null value hai ya nahi
        # Agar blank value 0 se zyada hai, to cleaning karenge

        if df[col].dtype in [object, str]:
            # Check kar rahe hain ki column text/string wala hai ya nahi
            # Example: Country, Product, Segment etc.

            df[col] = df[col].fillna(df[col].mode()[0])
            # Blank text value ko sabse zyada baar aane wali value se fill karenge
            # mode() = jo value sabse zyada baar aayi hai

        else:
            # Agar column text nahi hai
            # Matlab column numbers wala hai

            df[col] = df[col].fillna(round(df[col].mean(), 2))
            # Blank number ko column ke average/mean se fill karenge
            # round(...,2) = answer ko 2 decimal tak rakhega


# ==============================
# 5. SLICERS / FILTERS
# ==============================

col1, col2, col3, col4, col5 = st.columns(5)
# Screen ko 5 columns mein divide kar rahe hain
# Har column mein ek filter/slicer rakhenge


# ---------- COUNTRY FILTER ----------

with col1:
    # Pehle column ke andar kaam kar rahe hain

    country = st.selectbox(
        "select Country",
        ['All'] + list(df.Country.unique())
    )
    # Country ka dropdown/filter bana rahe hain
    # "All" ka matlab sabhi countries
    # unique() duplicate countries ko hata deta hai

    if country != "All":
        # Agar user "All" ke alawa koi country select kare

        df = df[df['Country'] == country]
        # Sirf selected country ka data dataframe mein rakhenge


# ---------- SEGMENT FILTER ----------

with col2:
    # Dusre column ke andar kaam kar rahe hain

    segment = st.selectbox(
        "select Segment",
        ['All'] + list(df.Segment.unique())
    )
    # Segment ka dropdown bana rahe hain

    if segment != "All":
        # Agar user koi specific segment select kare

        df = df[df['Segment'] == segment]
        # Sirf selected segment ka data rakhenge


# ---------- PRODUCT FILTER ----------

with col3:
    # Teesre column ke andar kaam kar rahe hain

    product = st.selectbox(
        "select Product",
        ['All'] + list(df.Product.unique())
    )
    # Product ka dropdown bana rahe hain

    if product != "All":
        # Agar user koi specific product choose kare

        df = df[df['Product'] == product]
        # Sirf selected product ka data rakhenge


# ---------- DISCOUNT BAND FILTER ----------

with col4:
    # Chauthe column ke andar kaam kar rahe hain

    db = st.selectbox(
        "select Discount Band",
        ['All'] + list(df['Discount Band'].unique())
    )
    # Discount Band ka dropdown bana rahe hain

    if db != "All":
        # Agar user koi specific discount band select kare

        df = df[df['Discount Band'] == db]
        # Sirf selected discount band ka data rakhenge


# ---------- YEAR FILTER ----------

with col5:
    # Paanchve column ke andar kaam kar rahe hain

    year = st.selectbox(
        "select Year",
        ['All'] + list(df.Year.unique())
    )
    # Year ka dropdown bana rahe hain

    if year != "All":
        # Agar user koi specific year select kare

        df = df[df['Year'] == year]
        # Sirf selected year ka data rakhenge


# ==============================
# 6. KPI SECTION
# ==============================

# KPI = Key Performance Indicator
# Matlab important numbers jo business ki performance batate hain


col1, col2, col3, col4, col5 = st.columns(5)
# KPI cards ke liye 5 columns bana rahe hain


li = ['Sales', 'Profit', 'Units Sold', 'COGS', 'Discounts']
# Ye 5 important columns hain jinka total dashboard par dikhayenge


cols = [col1, col2, col3, col4, col5]
# Banaye gaye 5 Streamlit columns ko ek list mein store kar rahe hain


i = 0
# i ka use list ke items ko ek-ek karke access karne ke liye hoga


for col in cols:
    # Har column ko ek-ek karke use karenge

    with col:
        # Current KPI column ke andar kaam kar rahe hain

        if df[li[i]].sum() / 1000000 > 1:
            # Current column ka total nikal rahe hain
            # Agar total 10 lakh se bada hai
            # To value ko Million (M) mein show karenge

            st.metric(
                "Total" + str(li[i]),
                str(round(df[li[i]].sum() / 1000000, 2)) + "M"
            )
            # Dashboard par KPI card show karega
            # Example: TotalSales = 2.50M

        elif df[li[i]].sum() / 1000 > 1:
            # Agar million nahi hai
            # To check karenge ki value 1000 se badi hai ya nahi
            # Agar hai to Thousand (K) mein show karenge

            st.metric(
                "Total" + str(li[i]),
                str(round(df[li[i]].sum() / 1000, 2)) + "K"
            )
            # Example: 25000 ko 25K show karega

        else:
            # Agar value 1000 se bhi chhoti hai

            st.metric(
                "Total" + str(li[i]),
                str(round(df[li[i]].sum(), 2))
            )
            # Normal number show karega

    i = i + 1
    # Next item par move karne ke liye i ko 1 se increase kar rahe hain


# ==============================
# 7. GRAPH SECTION
# ==============================

col1, col2 = st.columns(2)
# Screen ko 2 parts mein divide kar rahe hain
# Left side = Bar Chart
# Right side = Line Chart


x_axis = ['Country', 'Segment', 'Product', 'Discount Band']
# Bar chart ke X-axis ke liye options


y_axis = ['Profit', 'Sales', 'Units Sold', 'COGS']
# Graph ke Y-axis ke liye options


# ==============================
# 8. BAR CHART
# ==============================

with col1:
    # Left side wale column mein bar chart banayenge

    colx, coly = st.columns(2)
    # Left chart ke andar 2 chhote columns banaye
    # Ek X-axis select karne ke liye
    # Ek Y-axis select karne ke liye

    with colx:
        # Pehle chhote column mein

        x = st.selectbox(
            "Select X-Axis",
            x_axis
        )
        # User ko X-axis choose karne ka dropdown milega

    with coly:
        # Dusre chhote column mein

        y = st.selectbox(
            "Select Y-Axis Data Point",
            y_axis
        )
        # User ko Y-axis ka data choose karne ka dropdown milega


    pbs = df.groupby(x).agg({y: 'sum'}).reset_index()
    # Selected X-axis ke according data ko group kar rahe hain
    # Aur selected Y-axis ka total/sum nikal rahe hain
    #
    # Example:
    # X = Country
    # Y = Sales
    #
    # To har country ki total Sales milegi


    fig, ax = plt.subplots(figsize=(12, 4))
    # Graph ka empty box bana rahe hain
    # figsize = graph ki width aur height


    ax.bar(pbs[x], pbs[y])
    # Bar chart bana rahe hain
    # pbs[x] = X-axis
    # pbs[y] = Y-axis


    st.pyplot(fig)
    # Graph ko Streamlit dashboard par show kar rahe hain


# ==============================
# 9. LINE CHART
# ==============================

with col2:
    # Right side wale column mein line chart banayenge

    cola, colb = st.columns(2)
    # Line chart ke andar 2 chhote columns


    x_axis = ['Month Number', 'Year']
    # Line chart ke X-axis ke options


    with cola:
        # Pehle chhote column mein

        x = st.selectbox(
            "Select Trend",
            x_axis
        )
        # User Month Number ya Year select kar sakta hai


    with colb:
        # Dusre chhote column mein

        y = st.selectbox(
            "Select Data",
            y_axis
        )
        # User Sales, Profit, Units Sold ya COGS select kar sakta hai


    pbm = df.groupby(x).agg({y: 'sum'}).reset_index()
    # Selected X-axis ke according data ko group kar rahe hain
    # Aur selected Y-axis ka total nikal rahe hain


    fig2, ax2 = plt.subplots(figsize=(12, 4))
    # Line chart ke liye graph ka box bana rahe hain


    ax2.plot(pbm[x], pbm[y])
    # Line graph bana rahe hain
    # X-axis = selected trend
    # Y-axis = selected data


    st.pyplot(fig2)
    # Line graph ko Streamlit dashboard par show kar rahe hain


# ==============================
# 10. FILTERED DATASET
# ==============================

st.text(
    "This is the filter dataset of shape" + str(df.shape)
)
# Screen par filtered data ka size show karega
#
# Example:
# (50, 14)
#
# 50 = rows
# 14 = columns


st.dataframe(df, height=250)
# Filter hone ke baad poora dataframe dashboard par show karega
# height=250 means table ki height 250 pixels hogi

# Is dashboard ko school ki marksheet jaisa samjho:

# Excel file → Data ki notebook 📒
# Pandas → Notebook ko read karne wala helper 👨‍🏫
# Data Cleaning → Galti/blank values ko fix karna 🧹
# Slicers → Filter/search buttons 🔍
# KPI → Important total numbers ⭐
# Bar Chart → Countries/products ko compare karna 📊
# Line Chart → Time ke saath sales/profit kaise change hua dekhna 📈
# DataFrame → Filter ki hui table dikhana 📋
# Streamlit → In sabko ek beautiful dashboard mein dikhana 🖥️

# Ek line mein:
# Excel → Pandas → Clean Data → Filters → KPI → Charts → Streamlit Dashboard