from io import BytesIO
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)

styles = getSampleStyleSheet()


def generate_pdf(gold, incidents):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4
    )

    story = []

    # -------------------------------------------------
    # Title
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b><font size=20>"
            "Nigeria Security Brief Intelligence Report"
            "</font></b>",
            styles["Title"],
        )
    )

    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            f"Generated: {datetime.now():%d %B %Y %H:%M}",
            styles["Normal"],
        )
    )

    story.append(Spacer(1, 25))

    # -------------------------------------------------
    # Executive Summary
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b>Executive Summary</b>",
            styles["Heading2"],
        )
    )

    summary = [
        ["Indicator", "Value"],
        ["Total Incidents", gold["total_incidents"]],
        ["States Affected", len(gold["by_state"])],
        ["Fatalities", gold["total_killed"]],
        ["Abductions", gold["total_abducted"]],
    ]

    table = Table(summary, colWidths=[220, 120])

    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#005EB8")),
            ("TEXTCOLOR", (0,0), (-1,0), colors.white),

            ("GRID", (0,0), (-1,-1), 0.5, colors.grey),

            ("BACKGROUND", (0,1), (-1,-1), colors.whitesmoke),

            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

            ("BOTTOMPADDING", (0,0), (-1,0), 10),

            ("TOPPADDING", (0,1), (-1,-1), 8),

            ("BOTTOMPADDING", (0,1), (-1,-1), 8),
        ])
    )

    story.append(table)

    story.append(Spacer(1, 25))

    # -------------------------------------------------
    # State Summary
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b>Incidents by State</b>",
            styles["Heading2"],
        )
    )

    state_table = [["State", "Incidents"]]

    for state, count in gold["by_state"].items():
        state_table.append([state, count])

    table = Table(state_table)

    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.darkblue),
            ("TEXTCOLOR", (0,0), (-1,0), colors.white),

            ("GRID", (0,0), (-1,-1), 0.3, colors.black),

            ("BACKGROUND", (0,1), (-1,-1), colors.beige),
        ])
    )

    story.append(table)

    story.append(Spacer(1, 25))

    # -------------------------------------------------
    # High Priority Incidents
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b>High Priority Incidents</b>",
            styles["Heading2"],
        )
    )

    if gold["high_priority"]:

        for incident in gold["high_priority"]:

            text = (
                f"<b>{incident['date']}</b> | "
                f"{incident['state']} | "
                f"{incident['category']}<br/>"
                f"{incident['summary']}"
            )

            story.append(
                Paragraph(
                    text,
                    styles["BodyText"],
                )
            )

            story.append(Spacer(1, 10))

    else:

        story.append(
            Paragraph(
                "No high-priority incidents.",
                styles["Normal"],
            )
        )

    story.append(Spacer(1, 20))

    # -------------------------------------------------
    # Incident Explorer
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<b>Incident Explorer</b>",
            styles["Heading2"],
        )
    )

    incident_table = [[
        "Date",
        "State",
        "Category",
        "Killed",
        "Abducted",
    ]]

    for item in incidents:

        incident_table.append([
            item["date"],
            item["state"],
            item["category"],
            item["casualties_killed"],
            item["casualties_abducted"],
        ])

    table = Table(
        incident_table,
        repeatRows=1
    )

    table.setStyle(
        TableStyle([
            ("BACKGROUND", (0,0), (-1,0), colors.HexColor("#005EB8")),
            ("TEXTCOLOR", (0,0), (-1,0), colors.white),

            ("GRID", (0,0), (-1,-1), 0.25, colors.grey),

            ("BACKGROUND", (0,1), (-1,-1), colors.white),

            ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),

            ("FONTSIZE", (0,0), (-1,-1), 8),
        ])
    )

    story.append(table)

    story.append(Spacer(1, 25))

    # -------------------------------------------------
    # Footer
    # -------------------------------------------------

    story.append(
        Paragraph(
            "<font size=9 color='grey'>"
            "Generated by Nigeria Security Brief Intelligence Dashboard"
            "</font>",
            styles["Normal"],
        )
    )

    doc.build(story)

    pdf = buffer.getvalue()

    buffer.close()

    return pdf
