
import streamlit as st

st.title("📊 Analytics")

if st.session_state.gold is None:

    st.warning(
        "No analytics available yet."
    )

else:

    st.success(
        "Charts will be added in Milestone 3."
    )
