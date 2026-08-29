import logging

logging.basicConfig(level=logging.WARNING, format="%(levelname)s: %(message)s")

def calculate_average(scores):
    if not scores:
        logging.warning("Empty scores list received — skipping average calculation")
        return None
    total = 0
    for score in scores:
        total += score
    return total / len(scores)

def process_student_grades(students):
    results = {}
    for name, scores in students.items():
        avg = calculate_average(scores)
        if avg is None:
            logging.warning(f"No scores on record for '{name}'")
        results[name] = avg
    return results

data = {
    "Alice": [85, 90, 78],
    "Bob": [],
    "Charlie": [70, 88, 92]
}

print(process_student_grades(data))
