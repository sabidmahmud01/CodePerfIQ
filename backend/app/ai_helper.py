from typing import List


def generate_ai_explanation(
    code: str,
    complexity: str,
    bottlenecks: List[str],
    suggestions: List[str],
) -> str:
    if not bottlenecks:
        return (
            "The current rule-based analyzer did not find any obvious performance bottlenecks. "
            "However, a deeper AI review could still check algorithm choice, memory usage, and hidden expensive operations."
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
        "In a future version, this function can call an LLM API to provide deeper reasoning and optimized code suggestions."
    )

    return explanation