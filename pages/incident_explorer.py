import streamlit as st
import pandas as pd

st.title("📋 Incident Explorer")

if "incidents" not in st.session_state:
    st.warning("Please process a weekly brief first.")
    st.stop()

if st.session_state.incidents is None:
    st.warning("Please process a weekly brief first.")
    st.stop()

else:

    df = pd.DataFrame(st.session_state.incidents)

    st.dataframe(
        df,
        use_container_width=True
    )
