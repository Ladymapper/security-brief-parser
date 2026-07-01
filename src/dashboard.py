
import streamlit as st


def show_dashboard():

    st.sidebar.title("🛡️ Security Dashboard")

    page = st.sidebar.radio(
        "Navigation",
        [
            "🏠 Dashboard",
            "📋 Incidents",
            "📈 Analytics",
            "📥 Downloads",
            "ℹ️ About"
        ]
    )

    st.title("🛡️ Security Brief Intelligence Dashboard")

    st.caption(
        "Bronze → Silver → Gold Pipeline for Weekly Security Reports"
    )

    st.divider()

    if page == "🏠 Dashboard":
        show_home()

    elif page == "📋 Incidents":
        show_incidents()

    elif page == "📈 Analytics":
        show_analytics()

    elif page == "📥 Downloads":
        show_downloads()

    elif page == "ℹ️ About":
        show_about()


def show_home():

    st.header("Dashboard")

    st.info(
        "Paste a weekly security brief and process it to generate incident summaries."
    )


def show_incidents():

    st.header("Incident Explorer")

    st.info("Incident table will appear here.")


def show_analytics():

    st.header("Analytics")

    st.info("Charts will appear here.")


def show_downloads():

    st.header("Downloads")

    st.info("Download files here.")


def show_about():

    st.header("About")

    st.write(
        """
        This application converts unstructured weekly security briefs
        into structured intelligence using a Bronze–Silver–Gold
        data pipeline.
        """
    )
