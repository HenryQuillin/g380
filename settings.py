
from keywords import render_keywords
from watchlist import render_watchlist
import streamlit as st

st.set_page_config(page_title="Settings", page_icon="", layout="centered")


st.title('SETTINGS')

render_watchlist()

st.markdown("""<hr style="background-color:#333;" /> """, unsafe_allow_html=True)

render_keywords()

st.markdown("""<hr style="background-color:#333;" /> """, unsafe_allow_html=True)

