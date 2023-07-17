from database.db import session
from database.models import Group, Student, Teacher, Subject, Grade
from sqlalchemy import func, select, desc


def select_1():
    """Знайти 5 студентів із найбільшим середнім балом з усіх предметів."""

    q = select(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade.student)\
        .group_by(Student.id)\
        .order_by(desc('avg_grade'))\
        .limit(5)

    result = session.execute(q)
    print(list(result))


def select_2():
    """Знайти студента із найвищим середнім балом з певного предмета."""

    q = select(Student.name, func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Grade.student)\
        .join(Grade.subject)\
        .where(Subject.name == 'History')\
        .group_by(Student.id)\
        .order_by(desc('avg_grade'))\
        .limit(1)

    result = session.execute(q)
    print(list(result))


def select_3():
    """Знайти середній бал у групах з певного предмета."""

    q = select(Group.group_code, func.round(func.avg(Grade.grade), 2))\
        .join(Grade.student)\
        .join(Student.group)\
        .join(Grade.subject)\
        .where(Subject.name == 'History')\
        .group_by(Group.id)

    result = session.execute(q)
    print(list(result))


def select_4():
    """Знайти середній бал на потоці (по всій таблиці оцінок)."""

    q = select(func.round(func.avg(Grade.grade)))

    result = session.execute(q)
    print(list(result))


def select_5():
    """Знайти, які курси читає певний викладач."""

    q = select(Subject.name)\
        .join(Subject.teacher)\
        .where(Teacher.name == 'Jeremy Hunter')

    result = session.execute(q)
    print(list(result))


def select_6():
    """Знайти список студентів у певній групі."""

    q = select(Student.name)\
        .join(Student.group)\
        .where(Group.group_code == '101')

    result = session.execute(q)
    print(list(result))


def select_7():
    """Знайти оцінки студентів в окремій групі з певного предмета."""

    q = select(Student.name, Grade.grade)\
        .join(Grade.student)\
        .join(Student.group)\
        .join(Grade.subject)\
        .where(Group.group_code == '102', Subject.name == 'History')

    result = session.execute(q)
    print(list(result))


def select_8():
    """Знайти середній бал, який ставить певний викладач зі своїх предметів."""

    q = select(Teacher.name, func.round(func.avg(Grade.grade), 2))\
        .join(Grade.subject)\
        .join(Subject.teacher)\
        .group_by(Teacher.id)

    result = session.execute(q)
    print(list(result))


def select_9():
    """Знайти список курсів, які відвідує студент."""

    q = select(Subject.name)\
        .join(Grade.subject)\
        .join(Grade.student)\
        .where(Student.name == 'Christopher Webb')\
        .distinct()

    result = session.execute(q)
    print(list(result))


def select_10():
    """Список курсів, які певному студенту читає певний викладач."""

    q = select(Subject.name)\
        .join(Grade.subject)\
        .join(Grade.student)\
        .join(Subject.teacher)\
        .where(Student.name == 'Christopher Webb', Teacher.name == 'Jeremy Hunter')\
        .distinct()

    result = session.execute(q)
    print(list(result))


def select_11():
    """Середній бал, який певний викладач ставить певному студентові."""

    q = select(func.round(func.avg(Grade.grade), 2))\
        .join(Grade.student)\
        .join(Grade.subject)\
        .join(Subject.teacher)\
        .where(Student.name == 'Christopher Webb', Teacher.name == 'Jeremy Hunter')

    result = session.execute(q)
    print(list(result))


def select_12():
    """Оцінки студентів у певній групі з певного предмета на останньому занятті."""

    inner_q = select(func.max(Grade.date_of))\
        .join(Grade.student)\
        .join(Grade.subject)\
        .join(Student.group)\
        .where(Group.group_code == '100', Subject.name == 'History')

    q = select(Student.name, Grade.grade, Grade.date_of)\
        .join(Grade.student)\
        .join(Grade.subject)\
        .join(Student.group)\
        .where(Group.group_code == '100', Subject.name == 'History', Grade.date_of == inner_q.scalar_subquery())

    result = session.execute(q)
    print(list(result))
