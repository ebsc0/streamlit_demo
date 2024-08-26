import numpy as np
import altair as alt
import pandas as pd
from datetime import time, datetime
import streamlit as st

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

# st.slider
st.header('st.slider')

st.subheader('Slider')
age = st.slider('how old are you?', 0, 130, 25) # args: string, max, min, default
st.write('im ', age, ' years old')

st.subheader('Range slider')
values = st.slider(
    'select range of values',
    0.0, 100.0, (25.0, 75.0) # tuple denotes default value pair
)
st.write('values: ', values)

st.subheader('Range time slider')
appointment = st.slider(
    'schedule your appointment:',
    value=(time(11,30), time(12,45)) # tuple denotes default datetime value pair
)
st.write('youre scheduled for: ', appointment)

st.subheader('Datetime slider')
start_time = st.slider(
    'when do you start?',
    value=datetime(2020,1,1,9,30), # default datetime value
    format='MM/DD/YY - hh:mm'
)
st.write('start time: ', start_time)

st.header('st.line_chart') # based on altair charts
chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)
st.line_chart(chart_data)

st.header('st.selectbox')
option = st.selectbox(
    'what is your favorite color?',
    ('blue', 'green', 'red')
)
st.write('your favorite color is ', option)

st.header('st.multiselect')
options = st.multiselect(
    'what are your favorite colors?',
    ['green','yellow','red','blue'],
    ['yellow','red'] # default selection
)
st.write('you selected: ', options)

st.header('st.checkbox')
st.write('what would you like to order?')

ice_cream = st.checkbox('ice cream')
coffee = st.checkbox('coffee')
cola = st.checkbox('cola')

if ice_cream:
    st.write('🍦')
if coffee:
    st.write('☕')
if cola:
    st.write('🥤')

st.header('st.latex')
st.latex(r'''
         a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
         \sum_{k=0}^{n-1} ar^k =
         a \left(\frac{1-r^n}{1-r}\right)
''')

st.header('st.secrets')
st.write(st.secrets['message'])

st.header('st.file_uploader')
st.subheader('CSV')
file = st.file_uploader('choose a file')
if file is not None:
    df = pd.read_csv(file)
    st.subheader('dataframe')
    st.write(df)
    st.subheader('describe')
    st.write(df.describe())
else:
    st.info('☝️ Upload a CSV file')