from app.analyzer import analyze_code


def test_detects_nested_loop():
    code = """
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
"""

    result = analyze_code(code)

    assert result["language"] == "Python"
    assert result["complexity"] == "Possible O(n^2) or higher"
    assert len(result["bottlenecks"]) > 0
    assert len(result["suggestions"]) > 0

def test_separate_loops_are_not_marked_as_nested():
    code = """
def print_two_lists(items, users):
    for item in items:
        print(item)

    for user in users:
        print(user)
"""

    result = analyze_code(code)

    assert result["language"] == "Python"
    assert result["complexity"] == "Possible O(n)"
    assert "Multiple separate loops detected." in result["bottlenecks"]

def test_analysis_includes_summary():
    code = """
def two_sum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
"""

    result = analyze_code(code)

    assert "summary" in result
    assert isinstance(result["summary"], str)
    assert len(result["summary"]) > 0
    assert "Nested loop detected." in result["summary"]