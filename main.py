import random
from datetime import datetime

# Список русских фамилий и имен
last_names = ["Иванов", "Петров", "Сидоров", "Кузнецов", "Попов", "Смирнов", "Лебедев", "Козлов", "Новиков", "Морозов", "Волков"]
first_names = ["Иван", "Петр", "Сергей", "Андрей", "Николай", "Алексей", "Дмитрий", "Владимир", "Константин", "Михаил", "Олег"]

# Список предметов
subjects = ["Математика", "Физика", "Информатика", "История", "Литература"]

# Список ФИО преподавателей
teachers = ["Иванов Иван Иванович", "Петрова Мария Петровна", "Сидоров Сергей Сергеевич", "Кузнецова Наталья Николаевна"]

# Функция для генерации даты рождения
def generate_birthdate():
    year = random.randint(2000, 2005)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return datetime(year, month, day)

# Функция для генерации зачетки
def generate_zachetka():
    subjects_count = random.randint(3, 5)
    zachetka = []
    for _ in range(subjects_count):
        subject = random.choice(subjects)
        exam_date = datetime(2024, random.randint(1, 12), random.randint(1, 28))
        teacher = random.choice(teachers)
        zachetka.append({"subject": subject, "exam_date": exam_date, "teacher": teacher})
    return zachetka

# Генерация списка студентов
students = []
for _ in range(20):
    last_name = random.choice(last_names)
    first_name = random.choice(first_names)
    birthdate = generate_birthdate()
    zachetka = generate_zachetka()
    students.append({"last_name": last_name, "first_name": first_name, "birthdate": birthdate, "zachetka": zachetka})

# Функция для вывода результатов
def print_students(students):
    for student in students:
        print(f"Фамилия: {student['last_name']}, Имя: {student['first_name']}, Дата рождения: {student['birthdate'].strftime('%d.%m.%Y')}")
        print("Зачетка:")
        for subject in student['zachetka']:
            print(f"  {subject['subject']}: {subject['exam_date'].strftime('%d.%m.%Y')} - {subject['teacher']}")
        print()

# Вывод результатов
print_students(students)

# Поиск самого младшего и самого старшего студента
youngest_student = max(students, key=lambda x: x['birthdate'])
oldest_student = min(students, key=lambda x: x['birthdate'])

print(f"Самый младший студент: {youngest_student['last_name']} {youngest_student['first_name']}, Дата рождения: {youngest_student['birthdate'].strftime('%d.%m.%Y')}")
print(f"Самый старший студент: {oldest_student['last_name']} {oldest_student['first_name']}, Дата рождения: {oldest_student['birthdate'].strftime('%d.%m.%Y')}")
