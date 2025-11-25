# F1-stats
Formula 1 statistics storage and viewing using SQL database.

Project Overview

F1 Stats is a robust and scalable data management and analysis system designed to capture, store, and interpret historical and real-time Formula 1 racing statistics. Leveraging the power of Python for data processing and MySQL for structured persistence, this application transforms raw race data into meaningful, actionable insights for enthusiasts, analysts, and fantasy league players.

Technology Stack

Component

Technology

Role

Data Processing

Python (Pandas, Requests)

Handles data ingestion from external APIs (e.g., Ergast), cleaning, transformation, and calculation of derived metrics.

Database

MySQL

Provides a stable, relational environment for storing structured F1 data, including race results, driver profiles, team history, and circuit information.

Interface (Optional)

Python (Flask/Streamlit)

Can be extended with a lightweight web interface for visualization and interactive querying.

Core Features

1. Robust Data Ingestion & Storage

API Integration: Automated Python scripts to fetch and serialize data from public F1 statistics APIs or targeted web scraping.

Structured Storage: Implementation of a normalized MySQL database schema to manage complex F1 entities (Drivers, Constructors, Seasons, Races, Lap Times, Pit Stops).

Data Integrity: Validation checks during ingestion to ensure data consistency before committing to the database.

2. Advanced Statistical Analysis

Metric Calculation: Dynamic Python processing to calculate advanced metrics not readily available in raw data, such as:

Driver Consistency Index (DCI) across different circuits.

Average Pit Stop Time per Constructor over a season.

Head-to-Head performance analysis between two drivers.

Query Engine: Optimized SQL queries to retrieve specific datasets rapidly (e.g., all DNF results for a specific engine manufacturer in a given decade).

3. Data Visualization & Reporting

Reporting: Generation of textual summaries or dataframes summarizing key race weekend events.

Visualization Hooks: Data output structured perfectly for integration with visualization tools (Matplotlib, Seaborn, Tableau) to plot trends, performance degradation, and competitive gaps.
