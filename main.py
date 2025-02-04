import streamlit as st
import time

st.title("Streamlit超入門")
st.write("DataFrame")

bar = st.progress(0)
latest_iteration = st.empty()
for i in range(1, 101):
    latest_iteration.text(f"Iteration {i}")
    bar.progress(i)
    time.sleep(0.1)

"done!"