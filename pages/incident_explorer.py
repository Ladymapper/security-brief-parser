import streamlit as st

st.title("📋 Incident Explorer")

st.info(
    "The structured incident table will appear here after processing a weekly brief."
)

if st.session_state.incidents is None:

    st.warning(
        "No incident data available yet.\n\nReturn to the Home page and process a weekly security brief."
    )

else:

    st.dataframe(
        st.session_state.incidents,
        use_container_width=True,
    )
