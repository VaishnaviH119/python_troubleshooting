def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def process_student_grades(students):
    results = {}
    for name, scores in students.items():
        results[name] = calculate_average(scores)
    return results

data = {
    "Alice": [85, 90, 78],
    "Bob": [],
    "Charlie": [70, 88, 92]
}

print(process_student_grades(data))
