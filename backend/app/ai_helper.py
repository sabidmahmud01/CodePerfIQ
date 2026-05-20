from typing import List

from click import prompt
from app.ai_provider import MockAIProvider


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
    provider = MockAIProvider()
    provider_response = provider.generate_response(prompt)
    

    if not bottlenecks:
        return (
            "The current rule-based analyzer did not find any obvious performance bottlenecks. "
            "However, a deeper AI review could still check algorithm choice, memory usage, and hidden expensive operations. "
            f"Prompt prepared for future LLM use with {len(prompt)} characters."
        )

    explanation = (
        "AI-style explanation: "
        f"The analyzer estimated the code as {complexity}. "
        f"The main bottleneck is: {bottlenecks[0]} "
    )

    if suggestions:
        explanation += f"A recommended improvement is: {suggestions[0]} "

    explanation += (
        "This explanation is generated from rule-based results for now. "
        "In a future version, this function can call an LLM API to provide deeper reasoning and optimized code suggestions. "
        f"{provider_response}"
        f"Prompt prepared for future LLM use with {len(prompt)} characters."
    )

    return explanation