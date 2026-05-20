# CodePerfIQ

CodePerfIQ is a Python FastAPI backend that analyzes code performance and identifies possible bottlenecks, time complexity patterns, and optimization suggestions.

## Current Features

- Detects possible programming language
- Estimates basic time complexity from loop patterns
- Detects possible nested loops
- Detects repeated list lookup patterns
- Detects list building inside loops
- Detects file operations inside loops
- Suggests optimization strategies
- Includes pytest unit tests
- Detects actual nested loops using indentation-based analysis
- Differentiates nested loops from separate loops
- Returns a human-readable analysis summary
- Includes a CLI tester for local code analysis

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- pytest
- Git and GitHub

## Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

## CLI Tester

You can also test the analyzer directly from the terminal:

```bash
cd backend
source venv/bin/activate
python -m app.cli