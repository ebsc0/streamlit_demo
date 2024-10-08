import pandas as pd
import ydata_profiling
from streamlit_pandas_profiling import st_profile_report
import streamlit as st

st.write('streamlit_pandas_profiling')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
pr = df.profile_report()
st_profile_report(pr)