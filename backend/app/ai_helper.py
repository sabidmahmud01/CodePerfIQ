from typing import List

from click import prompt
from app.ai_provider import get_ai_provider


def build_ai_prompt(
    code: str,
    complexity: str,
    bottlenecks: List[str],
    suggestions: List[str],
) -> str:
    bottleneck_text = "\n".join(f"- {item}" for item in bottlenecks)
    suggestion_text = "\n".join(f"- {item}" for item in suggestions)

    return f"""
You are a helpful code performance assistant.

Analyze the following code and explain its performance issues in beginner-friendly language.

Code:
{code}

Rule-based analysis:
Complexity: {complexity}

Bottlenecks:
{bottleneck_text}

Suggestions:
{suggestion_text}

Your response should:
1. Explain why the code may be slow.
2. Explain the time complexity.
3. Suggest one practical improvement.
4. Keep the explanation clear and concise.
"""


def generate_ai_explanation(
    code: str,
    complexity: str,
    bottlenecks: List[str],
    suggestions: List[str],
) -> str:
    prompt = build_ai_prompt(code, complexity, bottlenecks, suggestions)

    provider = get_ai_provider()
    provider_response = provider.generate_response(prompt)

    return provider_response