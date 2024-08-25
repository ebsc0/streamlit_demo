import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.write('Hello World!')

# st.write 
st.header('st.write')
st.write('Hello, *World!* :sunglasses:')
st.write(1234)

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})
st.write(df)
st.write('below is dataframe:', df, 'above is a dataframe.')

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns=['a','b','c']
)
c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', color='c', tooltip=['a','b','c']
)
st.write(c)

# st.button
st.header('st.button')
if st.button('say hello'):
    st.write('hello there')
else:
    st.write('goodbye')
