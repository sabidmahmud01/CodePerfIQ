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