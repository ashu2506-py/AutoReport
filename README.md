# AutoReport – Automated Report & Analytics Generator

## Overview

AutoReport is a Python-based Automated Report & Analytics Generator developed as part of the Code A Nova Python Development Internship.

The application ingests data from multiple sources, performs statistical analysis, generates visualizations, and produces professional PDF and HTML reports. It also supports YAML-based report templates, scheduled report generation, and a command-line interface for seamless automation.

---

## Features

### Data Sources

* CSV Files
* Excel Files (.xlsx)
* JSON Files
* SQLite Databases
* REST APIs

### Analytics Engine

* Mean
* Median
* Standard Deviation
* Minimum & Maximum Values
* Category-wise Aggregations
* Executive Insights Generation

### Visualization

* Bar Charts
* Category-wise Sales Analysis
* Automated Chart Export

### Report Generation

* PDF Reports (ReportLab)
* HTML Reports (Jinja2)
* Executive Summary
* Statistical Summary
* Embedded Visualizations

### Configuration System

* YAML-based Templates
* Dynamic Template Selection
* Configurable Data Sources

### Automation

* APScheduler Integration
* Scheduled Report Generation

### Testing

* Pytest Test Suite
* Automated Validation of Core Modules

### CLI Commands

* Generate Reports
* Validate Templates
* List Available Templates
* Schedule Automated Reports

---

## Project Architecture

```text
Data Source
    │
    ▼
Reader Factory
    │
    ▼
Data Reader
(CSV / Excel / JSON / SQLite / API)
    │
    ▼
Analysis Engine
    │
    ├── Statistics
    ├── Insights
    └── Aggregations
    │
    ▼
Chart Generator
    │
    ▼
Report Engine
    │
    ├── PDF Generator
    └── HTML Generator
    │
    ▼
CLI & Scheduler
```

---

## Project Structure

```text
AutoReport/
│
├── analysis/
│   └── statistics.py
│
├── charts/
│   └── chart_generator.py
│
├── config/
│   └── config_loader.py
│
├── data_sources/
│   ├── base_reader.py
│   ├── csv_reader.py
│   ├── excel_reader.py
│   ├── json_reader.py
│   ├── sqlite_reader.py
│   ├── api_reader.py
│   └── reader_factory.py
│
├── reports/
│   ├── pdf_generator.py
│   └── html_generator.py
│
├── scheduler/
│   └── report_scheduler.py
│
├── templates/
│   ├── sales.yaml
│   ├── hr.yaml
│   └── inventory.yaml
│
├── tests/
│
├── sample_data/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd AutoReport
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Generate Sales Report

```bash
python main.py generate sales
```

### Generate HR Report

```bash
python main.py generate hr
```

### Generate Inventory Report

```bash
python main.py generate inventory
```

### Validate Templates

```bash
python main.py validate
```

### List Available Templates

```bash
python main.py list-templates
```

### Schedule Reports

```bash
python main.py schedule
```

---

## YAML Template Example

```yaml
name: Sales Report

data_source: sample_data/sales.db

report_title: Sales Analytics Report

chart:
  type: bar
  column: Sales
  group_by: Category

output:
  pdf: true
  html: true
```

---

## Testing

Run all tests:

```bash
pytest
```

Run tests with coverage:

```bash
pytest --cov=.
```

Current Test Coverage:

* CSV Reader Tests
* Factory Pattern Tests
* Statistics Engine Tests

---

## Sample Outputs

### PDF Report

* Executive Summary
* Statistical Summary
* Charts & Visualizations

### HTML Report

* Interactive Report Layout
* Embedded Visualizations
* Browser-Friendly Presentation

---

## Technologies Used

* Python 3
* Pandas
* NumPy
* Matplotlib
* ReportLab
* Jinja2
* PyYAML
* APScheduler
* Requests
* Typer
* Pytest

---

## Future Enhancements

* Interactive Plotly Dashboards
* Advanced Trend Detection
* Anomaly Detection Models
* Email Delivery of Reports
* Authentication & User Profiles
* Web-Based Dashboard
* Cloud Deployment Support

---

## Internship Project

Developed as part of the **Code A Nova Python Development Internship Program**.

The project demonstrates:

* Python Development
* Data Processing
* Software Architecture
* Automation
* Reporting Systems
* Testing & Documentation
* Design Patterns

---

## Author

Ashutosh Kumar Singh

B.Tech CSE (AI Specialization)

Python Developer | AI Enthusiast | Full Stack Learner
