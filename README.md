
Security Brief Parser
Overview

Security Brief Parser is a Python application that converts unstructured weekly security briefings into structured, machine-readable data using a Bronze–Silver–Gold data pipeline.

The project demonstrates data engineering principles by transforming raw operational reports into standardized JSON outputs and summary statistics for analysis and reporting.

Features
Stores the original security brief (Bronze layer)
Extracts structured security incidents (Silver layer)
Generates summary statistics (Gold layer)
Saves outputs as JSON files
Designed to be extended into a web application
Project Structure
security-brief-parser/

├── app.py
├── main.py
├── README.md
├── requirements.txt

├── bronze/
├── silver/
├── gold/

└── src/
    ├── bronze.py
    ├── silver.py
    └── gold.py
Data Pipeline
Bronze Layer

Stores the original security brief exactly as received.

Silver Layer

Extracts structured incident records containing:

Date
Time
LGA
State
Incident category
Summary
Fatalities
Abductions
Gold Layer

Produces analytical summaries including:

Total incidents
Incidents by state
Incidents by category
Total fatalities
Total abductions
High-priority incidents
Arrests and security operations
Technologies
Python
Pandas
JSON
Regular Expressions (Regex)
