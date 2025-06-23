import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns



st.title("WEB SCRAPING APP")



with st.expander("show sample data"):    
    df = pd.read_csv("Scrap.csv")
    st.dataframe(df.head(5))


