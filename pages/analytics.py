import streamlit as st
import pandas as pd

st.title("📊 Analytics")

if "incidents" not in st.session_state:
    st.warning("Please process a weekly brief first.")
    st.stop()

if st.session_state.incidents is None:
    st.warning("Please process a weekly brief first.")
    st.stop()

else:

    df = pd.DataFrame(st.session_state.incidents)

    st.subheader("Incidents by Category")

    st.bar_chart(df["category"].value_counts())

    st.subheader("Incidents by State")

    st.bar_chart(df["state"].value_counts())
