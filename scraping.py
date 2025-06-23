import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config("web scraping","🕸️",layout="wide")

st.title("WEB SCRAPING APP")




with st.expander("show sample data"):    
    df = pd.read_csv("Scrap.csv")
    st.dataframe(df.head(5))


tab1, tab2 = st.tabs(["Descriptive Analysis","Visualisation"])

@st.fragment
def descriptive():
    with tab1:
        descriptive_col1, descriptive_col2, descriptive_col3 = st.columns(3, border=True)

        with descriptive_col1:
            st.markdown(" Count of Rating")
            rating = df["Rating"].value_counts()
            st.write(rating)

        with descriptive_col2:
            tab_min_price, tab_max_price, tab_ave_price, tab_sum_price = st.tabs(["Mininum Price", "Maximun price","Average Price", "Sum Price"]) 
            with tab_min_price:
                min_price = df["Price"].min()
                st.subheader(f"£{min_price}")
                st.write("Table with the minimum price")
                st.dataframe(df[df["Price"] == min_price])

            with tab_max_price:
                max_price = df["Price"].max()
                st.subheader(f"£{max_price}")
                st.write("Table with the maximum price")
                st.dataframe(df[df["Price"] == max_price])


            with tab_ave_price:
                ave_price = df["Price"].mean()
                st.subheader(f"£{ave_price.__round__(2)}")
                st.write("Price above the averange price")
                st.dataframe(df[df["Price"] > ave_price].head(2))

            
            with tab_sum_price:
                sum_price = df["Price"].sum()
                st.subheader(f"£{sum_price.__round__(2)}")                
                title_number, = st.tabs(["Total Number of Book"])
                with title_number:
                    total_number_book = len(df["Title"])
                    st.write("Total Number of Book Title")
                    st.subheader(total_number_book)
        
        with descriptive_col3:
            title_top_price = df.groupby("Title")["Price"].max().sort_values(ascending=False)
            st.write("Top 5 Books with the highest Price")
            st.dataframe(title_top_price.head(5))


@st.fragment               
def visualisation():
    with tab2:
        visualisation_col1, visualisation_col2, visualisation_col3 = st.columns(3, border=True)

        with visualisation_col1:
            pass
        
descriptive()
visualisation()