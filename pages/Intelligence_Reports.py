
import streamlit as st

from src.session import ensure_pipeline_data
from src.downloads import generate_pdf

ensure_pipeline_data()

st.title("📄 Intelligence Report")

pdf = generate_pdf(
    st.session_state.gold,
    st.session_state.incidents
)

st.download_button(
    label="📥 Download Intelligence Report (PDF)",
    data=pdf,
    file_name="Nigeria_Security_Intelligence_Report.pdf",
    mime="application/pdf",
    use_container_width=True,
)
