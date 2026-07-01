import streamlit as st
import pandas as pd

st.title("📊 Analytics")

if st.session_state.incidents is None:

    st.warning("No data available.")

else:

    df = pd.DataFrame(st.session_state.incidents)

    st.subheader("Incidents by Category")

    st.bar_chart(df["category"].value_counts())

    st.subheader("Incidents by State")

    st.bar_chart(df["state"].value_counts())
