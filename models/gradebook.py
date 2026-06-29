from models.student import Student
from utils.file_handler import read_csv, write_csv
from utils.validators import validate_score


class GradeBook:

    def __init__(self):
        self.students = []

    def load_csv(self, path):
        rows = read_csv(path)
        for row in rows:
            try:
                student = Student(
                    row["Name"],
                    validate_score(row["Math"]),
                    validate_score(row["Science"]),
                    validate_score(row["English"]),
                )
                self.students.append(student)

            except (ValueError, KeyError, TypeError) as error:
                print(f"Warning: {error}. " f"Skipping invalid row: {row}")

    def class_average(self):
        if not self.students:
            return 0

        total = sum(student.average() for student in self.students)
        return total / len(self.students)

    def top_performers(self, n=3):
        return sorted(
            self.students, key=lambda student: student.average(), reverse=True
        )[:n]

    def save_summary(self, path):
        summary = []

        sorted_students = sorted(
            self.students, key=lambda student: student.average(), reverse=True
        )

        for student in sorted_students:
            summary.append(
                {
                    "Name": student.name,
                    "Math": student.math,
                    "Science": student.science,
                    "English": student.english,
                    "Average": round(student.average(), 2),
                    "Grade": student.grade(),
                }
            )

        if self.students:
            num_students = len(self.students)

            math_avg = round(
                sum(s.math for s in self.students) / num_students,
                2,
            )

            science_avg = round(
                sum(s.science for s in self.students) / num_students,
                2,
            )

            english_avg = round(
                sum(s.english for s in self.students) / num_students,
                2,
            )

            summary.append(
                {
                    "Name": "Subject Average",
                    "Math": math_avg,
                    "Science": science_avg,
                    "English": english_avg,
                    "Average": "",
                    "Grade": "",
                }
            )

        write_csv(path, summary)
