from datetime import datetime
import faker
from random import randint, choice
from database.db import session
from database.models import Group, Student, Teacher, Subject, Grade

NUMBER_TEACHERS = 5
NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3


def generate_fake_data(number_teachers, number_students, number_groups) -> tuple:
    fake_teachers = []
    fake_students = []
    fake_groups = [str(100+i) for i in range(number_groups)]  # генератор груп
    fake_subjects = [
        'Mathematics',
        'History',
        'English',
        'Computer Science',
        'Art',
        'Economics',
        'Music',
        'Physical Education'
    ]
    # fake_grades = ['A', 'B', 'C', 'D', 'E', 'FX', 'F']

    fake_data = faker.Faker()

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    return fake_teachers, fake_students, fake_groups, fake_subjects


def prepare_data(teachers, students, groups, subjects) -> tuple:
    for_teachers = []

    for teacher in teachers:
        for_teachers.append((teacher, ))  # name

    for_students = []

    for student in students:
        for_students.append((student, randint(1, len(groups))))  # name id_group

    for_groups = []

    for group in groups:
        for_groups.append((group, ))  # group_code

    for_subjects = []

    for subject in subjects:
        for_subjects.append((subject, randint(1, len(teachers))))  # name id_teacher

    for_grades = []

    for student in range(len(students)):
        for grade in range(21):
            grade_date = datetime(2022, randint(1, 6), randint(10, 20)).date()
            for_grades.append((student + 1, randint(1, len(subjects)), randint(60, 100), grade_date))  # можливі помилки
        # id_student id_subject grade date_of

    return for_teachers, for_students, for_groups, for_subjects, for_grades


def insert_data_to_db(teachers, students, groups, subjects, grades) -> None:

    for param in groups:
        new_group = Group(group_code=param[0])
        session.add(new_group)

    for param in students:
        new_student = Student(name=param[0], id_group=param[1])
        session.add(new_student)

    for param in teachers:
        new_teacher = Teacher(name=param[0])
        session.add(new_teacher)

    for param in subjects:
        new_subject = Subject(name=param[0], id_teacher=param[1])
        session.add(new_subject)

    for param in grades:
        new_grade = Grade(grade=param[2], date_of=param[3], id_student=param[0], id_subject=param[1])
        session.add(new_grade)

    session.commit()


if __name__ == "__main__":
    teachers, students, groups, subjects, grades = prepare_data(*generate_fake_data(NUMBER_TEACHERS, NUMBER_STUDENTS, NUMBER_GROUPS))
    insert_data_to_db(teachers, students, groups, subjects, grades)

