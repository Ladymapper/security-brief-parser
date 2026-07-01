pdf = generate_pdf(gold, incidents)

st.download_button(
    "📄 Download Executive Intelligence Report",
    pdf,
    "Nigeria_Security_Report.pdf",
    "application/pdf",
)
