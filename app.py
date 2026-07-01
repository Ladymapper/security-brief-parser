import streamlit as st
from src.pipeline import run_pipeline

st.set_page_config(
    page_title="Nigeria Security Brief Intelligence Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# -------------------------
# Session State
# -------------------------

if "bronze" not in st.session_state:
    st.session_state.bronze = None

if "incidents" not in st.session_state:
    st.session_state.incidents = None

if "gold" not in st.session_state:
    st.session_state.gold = None

# -------------------------
# Header
# -------------------------

st.title("🛡️ Nigeria Security Brief Intelligence Dashboard")

st.write(
    """
Paste a weekly Nigeria security brief below.

The application will automatically convert it into structured intelligence.
"""
)

# -------------------------
# Input
# -------------------------

raw_text = st.text_area(
    "Weekly Security Brief",
    height=300
)

process = st.button(
    "🚀 Process Weekly Brief",
    use_container_width=True
)

# -------------------------
# Process
# -------------------------

if process:

    if raw_text.strip() == "":

        st.warning("Please paste a weekly brief.")

    else:

        with st.spinner("Running Bronze → Silver → Gold Pipeline..."):

            bronze, incidents, gold = run_pipeline(raw_text)

            st.session_state.bronze = bronze
            st.session_state.incidents = incidents
            st.session_state.gold = gold

        st.success("Pipeline completed successfully!")

# -------------------------
# Dashboard Summary
# -------------------------

if st.session_state.gold:

    gold = st.session_state.gold

    st.divider()

    st.subheader("Executive Summary")

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Incidents", gold["total_incidents"])
    c2.metric("Killed", gold["total_killed"])
    c3.metric("Abducted", gold["total_abducted"])
    c4.metric("States", len(gold["by_state"]))
