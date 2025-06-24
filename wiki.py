import streamlit as st
import wikipedia as wiki


st.title("Wikipedia scraping")



message = st.chat_input("message")
if message:
    search = wiki.page(message)
    cont = search.content
    st.write(cont)


