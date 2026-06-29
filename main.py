import sys
from models.gradebook import GradeBook


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py data/students.csv")
        return

    input_file = sys.argv[1]
    gradebook = GradeBook()

    try:
        gradebook.load_csv(input_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return

    gradebook.save_summary("summary.csv")

    print(f"Class average: {gradebook.class_average():.2f}")

    print("\nTop Performers:")
    for student in gradebook.top_performers():
        print(f"{student.name} ({student.average():.2f})")

    grades = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

    for student in gradebook.students:
        grades[student.grade()] += 1

    print("\nGrade Distribution:")
    print(
        f"A={grades['A']} "
        f"B={grades['B']} "
        f"C={grades['C']} "
        f"D={grades['D']} "
        f"F={grades['F']}"
    )


if __name__ == "__main__":
    main()
