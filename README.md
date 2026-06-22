# AI Resume Analyzer Automation

## Overview

This project automates the AI Resume Analyzer application using Selenium WebDriver, Python, and Pytest.

## Tech Stack

* Python
* Selenium WebDriver
* Pytest
* Pytest HTML

## Framework Design

* Page Object Model (POM)
* Explicit Waits
* Screenshot on Failure
* HTML Reporting

## Automated Scenarios

### Positive Scenarios

* User Signup
* User Login
* Resume Upload
* Resume Analysis
* New Analysis Navigation

### Negative Scenarios

* Invalid Login
* Duplicate Signup
* Analysis Without Job Description
* Invalid File Upload

## Project Structure

```text
resume-analyzer-automation/
│
├── config/
├── pages/
├── reports/
├── screenshots/
├── test_data/
├── tests/
├── utils/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Installation

```bash
pip install -r requirements.txt
```

## Execute All Tests

```bash
pytest
```

## Execute Specific Test File

```bash
pytest tests/test_signup.py
```

```bash
pytest tests/test_login.py
```

```bash
pytest tests/test_resume_analysis.py
```

## Execute Single Test

```bash
pytest tests/test_login.py::test_valid_login -v
```

## Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

## View HTML Report

After execution, open:

```text
reports/report.html
```

in any browser.

## Screenshots

Screenshots are automatically captured for failed test cases and stored in:

```text
screenshots/
```
