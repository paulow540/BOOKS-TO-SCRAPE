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

 


def visulisation():
    with tab2:
        visualisation_col1, visualisation_col2, visualisation_col3 = st.columns(3, border=True)

        with visualisation_col1:
            st.subheader("Rating vs. Average Price")
            avg_price_rating = df.groupby('Rating')['Price'].mean().reset_index()
            fig4 = px.bar(avg_price_rating, x='Rating', y='Price', color='Rating', title="Average Price by Rating")
            st.plotly_chart(fig4)

        with visualisation_col2:
            st.subheader("Number of Books per Rating")
            rating_counts = df['Rating'].value_counts().reset_index()
            rating_counts.columns = ['Rating', 'Count']
            fig1 = px.bar(rating_counts, x='Rating', y='Count', color='Rating', title="Books per Rating")
            st.plotly_chart(fig1)

        with visualisation_col3:
            st.subheader("Price Distribution (Histogram)")
            fig3 = px.histogram(df, x='Price', nbins=20, title="Price Distribution")
            st.plotly_chart(fig3)



     
descriptive()
visulisation()






