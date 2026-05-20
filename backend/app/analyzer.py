from typing import Dict, List

def detect_language(code: str) -> str:
    if "def " in code or "import " in code:
        return "Python"
    if "function " in code or "const " in code or "let " in code:
        return "JavaScript"
    if "#include " in code or "std::" in code:
        return "C++"
    
    return "Unknown"

def analyze_code(code: str) -> Dict[str, object]:
    lower_code = code.lower()

    bottlenecks: List[str] = []
    suggestions: List[str] = []

    loop_count = lower_code.count("for ") + lower_code.count("while ")

    if loop_count >= 2:
        complexity = "Possible O(n^2) or higher"
        bottlenecks.append("Multiple loops detected. This may indicate nested or repeated iterations.")
        suggestions.append("Use a dictionary, set, or better algorithm to reduce repeated scanning.")

    elif loop_count == 1:
        complexity = "Possible O(n)"
        bottlenecks.append("Single loop detected. Check if it can be optimized.")
        suggestions.append("Check whether operations inside the loop are expensive.")

    else:
        complexity = "Possible O(1) or non-loop based logic"

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

    return {
        "language": detect_language(code),
        "complexity": complexity,
        "bottlenecks": bottlenecks,
        "suggestions": suggestions,
    }
    