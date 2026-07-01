import streamlit as st
import pandas as pd

st.title("📋 Incident Explorer")

if st.session_state.incidents is None:

    st.warning("No incidents available.")

else:

    df = pd.DataFrame(st.session_state.incidents)

    st.dataframe(
        df,
        use_container_width=True
    )
