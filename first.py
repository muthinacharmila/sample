import streamlit as st
st.title('MY FIRST APP')
data=pd.read_csv('hdp.csv')
st.dataframe(data)
