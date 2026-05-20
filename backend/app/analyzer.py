from typing import Dict, List

def detect_language(code: str) -> str:
    if "def " in code or "import " in code:
        return "Python"
    if "function " in code or "const " in code or "let " in code:
        return "JavaScript"
    if "#include " in code or "std::" in code:
        return "C++"
    
    return "Unknown"

def has_nested_loop(code: str) -> bool:
    lines = code.splitlines()
    loop_indent_stack: List[int] = []

    for line in lines:
        stripped_line = line.lstrip()

        if not stripped_line:
            continue

        current_indent = len(line) - len(stripped_line)

        while loop_indent_stack and current_indent <= loop_indent_stack[-1]:
            loop_indent_stack.pop()

        if stripped_line.startswith("for ") or stripped_line.startswith("while "):
            if loop_indent_stack:
                return True

            loop_indent_stack.append(current_indent)

    return False

def generate_summary(complexity: str, bottlenecks: List[str], suggestions: List[str]) -> str:
    if not bottlenecks:
        return "No obvious performance bottlenecks were detected using the current rule-based checks."

    main_bottleneck = bottlenecks[0]
    main_suggestion = suggestions[0] if suggestions else "Review the code structure for possible optimization opportunities."

    return (
        f"This code has {complexity}. "
        f"The main issue found is: {main_bottleneck} "
        f"A possible improvement is: {main_suggestion}"
    )

def analyze_code(code: str) -> Dict[str, object]:
    lower_code = code.lower()

    bottlenecks: List[str] = []
    suggestions: List[str] = []

    loop_count = lower_code.count("for ") + lower_code.count("while ")

    loop_count = lower_code.count("for ") + lower_code.count("while ")
    nested_loop_found = has_nested_loop(code)

    if nested_loop_found:
        complexity = "Possible O(n^2) or higher"
        bottlenecks.append("Nested loop detected.")
        suggestions.append("Consider using a dictionary, set, or optimized algorithm to reduce repeated scanning.")

    elif loop_count >= 2:
        complexity = "Possible O(n)"
        bottlenecks.append("Multiple separate loops detected.")
        suggestions.append("Separate loops may still be linear if they are not nested, but review repeated passes over the same data.")

    elif loop_count == 1:
        complexity = "Possible O(n)"
        bottlenecks.append("Single loop detected.")
        suggestions.append("Check whether operations inside the loop are expensive.")

    else:
        complexity = "Possible O(1) or non-loop-based logic"

    if " in " in lower_code and "list" in lower_code:
        bottlenecks.append("Possible repeated list lookup detected.")   
        suggestions.append("Consider using a set for faster lookups if order is not important.")   

    if "append" in lower_code and loop_count > 0:
        bottlenecks.append("List building inside a loop detected.")
        suggestions.append("Consider using a list comprehension or vectorized operations when appropriate.")

    if "open(" in lower_code and loop_count > 0:
        bottlenecks.append("File operation inside a loop detected.")
        suggestions.append("Avoid opening or reading files repeatedly inside loops.")

    if "numpy" in lower_code or "pandas" in lower_code:
        suggestions.append("Look for vectorized operations instead of regular Python loops.")

    summary = generate_summary(complexity, bottlenecks, suggestions)

    return {
        "language": detect_language(code),
        "complexity": complexity,
        "bottlenecks": bottlenecks,
        "suggestions": suggestions,
        "summary": summary
    }
    