# PR. 4 - Functional Treat
# Analyze student marks using Python built-in functions only.
# No NumPy or external libraries are required.

def analyze_marks(marks):
    """Analyze a list of student marks using built-in functions."""
    total_students = len(marks)
    highest_marks = max(marks)
    lowest_marks = min(marks)
    average_marks = sum(marks) / total_students

    passed = list(filter(lambda mark: mark >= 40, marks))
    failed = list(filter(lambda mark: mark < 40, marks))

    exact_100 = list(filter(lambda mark: mark == 100, marks))
    pass_percentage = (len(passed) / total_students) * 100

    sorted_marks = sorted(marks)
    grade_a = list(filter(lambda mark: 80 <= mark <= 100, marks))
    grade_b = list(filter(lambda mark: 70 <= mark <= 79, marks))

    return {
        "total_students": total_students,
        "highest": highest_marks,
        "lowest": lowest_marks,
        "average": average_marks,
        "passed": len(passed),
        "failed": len(failed),
        "exact_100": len(exact_100),
        "pass_percentage": pass_percentage,
        "sorted_marks": sorted_marks,
        "grade_a": len(grade_a),
        "grade_b": len(grade_b),
    }


def main():
    # 20 hardcoded student scores as required.
    marks = [
        100, 100, 80, 79, 78,
        75, 70, 69, 68, 67,
        66, 65, 64, 63, 62,
        58, 58, 35, 30, 21
    ]

    result = analyze_marks(marks)

    print(f"Total Students: {result['total_students']}")
    print(f"Highest Marks: {result['highest']}")
    print(f"Lowest Marks: {result['lowest']}")
    print(f"Average Marks: {result['average']:.1f}")
    print(f"Passed: {result['passed']}")
    print(f"Failed: {result['failed']}")
    print(f"Exact 100: {result['exact_100']}")
    print(f"Pass Percentage: {result['pass_percentage']:.1f}%")
    print(f"Sorted Marks: {result['sorted_marks']}")
    print(f"Grade A: {result['grade_a']} Students")
    print(f"Grade B: {result['grade_b']} Students")


if __name__ == "__main__":
    main()
