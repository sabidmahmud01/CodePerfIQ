from app.analyzer import analyze_code


def main():
    print("CodePerfIQ CLI Tester")
    print("Paste your code below. Type END on a new line when finished.")

    lines = []

    while True:
        line = input()

        if line.strip() == "END":
            break

        lines.append(line)

    code = "\n".join(lines)
    result = analyze_code(code)

    print("\nAnalysis Result")
    print("----------------")
    print(f"Language: {result['language']}")
    print(f"Complexity: {result['complexity']}")

    print("\nBottlenecks:")
    for bottleneck in result["bottlenecks"]:
        print(f"- {bottleneck}")

    print("\nSuggestions:")
    for suggestion in result["suggestions"]:
        print(f"- {suggestion}")


if __name__ == "__main__":
    main()