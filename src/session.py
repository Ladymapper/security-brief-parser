
import streamlit as st

def ensure_pipeline_data():
    """
    Ensure the pipeline has been run before accessing session data.
    """
    if "incidents" not in st.session_state:
        st.warning("Please process a weekly security brief from the Home page first.")
        st.stop()

    if st.session_state.incidents is None:
        st.warning("Please process a weekly security brief from the Home page first.")
        st.stop()
