import streamlit as st
import json
import pandas as pd

st.title("📥 Downloads")

if "incidents" not in st.session_state:
    st.warning("Please process a weekly security brief first.")
    st.stop()

if st.session_state.incidents is None:
    st.warning("Please process a weekly security brief first.")
    st.stop()
else:

    incidents = st.session_state.incidents
    gold = st.session_state.gold

    df = pd.DataFrame(incidents)

    st.download_button(
        "Download Silver JSON",
        json.dumps(incidents, indent=4),
        "silver.json",
        "application/json"
    )

    st.download_button(
        "Download Gold JSON",
        json.dumps(gold, indent=4),
        "gold.json",
        "application/json"
    )

    st.download_button(
        "Download CSV",
        df.to_csv(index=False),
        "incidents.csv",
        "text/csv"
    )
