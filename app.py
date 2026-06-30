import streamlit as st
import pandas as pd
import json
from datetime import datetime

from src.bronze import save_bronze
from src.silver import extract_silver
from src.gold import build_gold

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Security Brief Intelligence Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🛡️ Security Brief Intelligence Dashboard")

st.markdown(
    """
Convert weekly security briefs into structured incident data using a
**Bronze → Silver → Gold** data pipeline.
"""
)

st.divider()

# --------------------------------------------------
# User Input
# --------------------------------------------------

raw_text = st.text_area(
    "📋 Paste Weekly Security Brief",
    height=350,
    placeholder="Paste the complete weekly security brief here..."
)

process = st.button(
    "🚀 Process Weekly Brief",
    use_container_width=True
)

# --------------------------------------------------
# Process Pipeline
# --------------------------------------------------

if process:

    if raw_text.strip() == "":
        st.warning("Please paste a security brief first.")
        st.stop()

    with st.spinner("Processing..."):

        # Bronze
        bronze_data = save_bronze(raw_text)

        # Silver
        incidents = extract_silver(raw_text)

        # Gold
        gold = build_gold(incidents)

    st.success("Processing completed successfully!")

    # --------------------------------------------------
    # Executive Summary
    # --------------------------------------------------

    st.subheader("📊 Executive Summary")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Incidents", gold["total_incidents"])
    col2.metric("Killed", gold["total_killed"])
    col3.metric("Abducted", gold["total_abducted"])
    col4.metric("States", len(gold["by_state"]))

    # --------------------------------------------------
    # Incident Table
    # --------------------------------------------------

    st.subheader("📋 Structured Incidents")

    df = pd.DataFrame(incidents)

    st.dataframe(
        df,
        use_container_width=True
    )

    # --------------------------------------------------
    # Charts
    # --------------------------------------------------

    st.subheader("📈 Incidents by Category")

    st.bar_chart(df["category"].value_counts())

    st.subheader("📍 Incidents by State")

    st.bar_chart(df["state"].value_counts())

    # --------------------------------------------------
    # Downloads
    # --------------------------------------------------

    st.subheader("📥 Downloads")

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            "Download Silver JSON",
            json.dumps(incidents, indent=4),
            file_name="security_incidents.json",
            mime="application/json"
        )

    with col2:
        st.download_button(
            "Download Gold Summary",
            json.dumps(gold, indent=4),
            file_name="gold_summary.json",
            mime="application/json"
        )

    st.download_button(
        "Download CSV",
        df.to_csv(index=False),
        file_name="security_incidents.csv",
        mime="text/csv"
    )

st.divider()

st.caption(
    f"Security Brief Intelligence Dashboard | Generated {datetime.now():%d %B %Y}"
)
