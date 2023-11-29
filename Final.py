import streamlit as st
from streamlit_extras.mandatory_date_range import date_range_picker 

def example():
    result = date_range_picker("Select a date range")
    st.write("Result:", result)
    st.text('Fixed width text')
    st.markdown('_Markdown_') # see #*
    st.caption('Balloons. Hundreds of them...')
    st.latex(r''' e^{i\pi} + 1 = 0 ''')
    st.write('Most objects') # df, err, func, keras!
    st.write(['st', 'is <', 3]) # see *
    st.title('My title')
    st.header('My header')
    st.subheader('My sub')
    st.code('for i in range(8): foo()')

example()



# * optional kwarg unsafe_allow_html = True