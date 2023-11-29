import streamlit as st
from streamlit_extras.mandatory_date_range import date_range_picker 

def example():
    result = date_range_picker("Select a date range")
    st.title('Stream Test')
    st.write('Hello, Streamlit!')

example()

jupyterlite(1500, 1600)


