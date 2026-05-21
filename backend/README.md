# CodePerfIQ

CodePerfIQ is an AI-powered code performance analysis tool built with Python and FastAPI.

The project analyzes source code, detects possible performance bottlenecks, estimates basic time complexity, and generates beginner-friendly AI explanations using a provider-based AI architecture.

The goal of this project is to combine traditional rule-based program analysis with modern LLM-powered explanations.

---

## Project Goal

CodePerfIQ helps developers understand why their code may be slow.

Instead of only saying that code has a nested loop or possible `O(n^2)` complexity, the system explains the issue clearly and suggests practical improvements.

This project is designed as a portfolio-level computer science project focused on:

- Code performance analysis
- Time complexity reasoning
- Rule-based static analysis
- AI-assisted explanation generation
- Backend API design
- Clean provider-based architecture

---

## Current Features

- Detects likely programming language
- Detects single loops
- Detects multiple separate loops
- Detects nested loops
- Estimates possible time complexity
- Identifies repeated scanning patterns
- Detects possible expensive operations inside loops
- Detects list building inside loops
- Detects file operations inside loops
- Builds structured AI prompts from analyzer results
- Supports mock AI responses for safe development
- Supports real Gemini AI explanations
- Provides a FastAPI backend
- Provides interactive API documentation through Swagger UI
- Includes a CLI tester
- Includes automated tests with pytest

---

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- pytest
- Google GenAI SDK
- python-dotenv
- Git and GitHub

---

## Project Structure

```text
CodePerfIQ/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── analyzer.py
│   │   ├── ai_helper.py
│   │   ├── ai_provider.py
│   │   └── cli.py
│   ├── tests/
│   │   └── test_analyzer.py
│   ├── requirements.txt
│   └── .env.example
├── README.md
└── .gitignore