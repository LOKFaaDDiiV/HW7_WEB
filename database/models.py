from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .db import Base


class Group(Base):

    __tablename__ = 'groups'

    id = Column(Integer, primary_key=True, autoincrement=True)
    group_code = Column(String(10), nullable=False)


class Student(Base):

    __tablename__ = 'students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)
    id_group = Column(Integer, ForeignKey('groups.id', ondelete='CASCADE', onupdate='CASCADE'))
    group = relationship(Group)


class Teacher(Base):

    __tablename__ = 'teachers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False)


class Subject(Base):

    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40), nullable=False)
    id_teacher = Column(Integer, ForeignKey('teachers.id', ondelete='CASCADE', onupdate='CASCADE'))
    teacher = relationship(Teacher)


class Grade(Base):

    __tablename__ = 'grades'

    id = Column(Integer, primary_key=True, autoincrement=True)
    grade = Column(Integer, nullable=False)
    date_of = Column(Date, nullable=False)
    id_student = Column(Integer, ForeignKey('students.id', ondelete='CASCADE', onupdate='CASCADE'))
    student = relationship(Student)
    id_subject = Column(Integer, ForeignKey('subjects.id', ondelete='CASCADE', onupdate='CASCADE'))
    subject = relationship(Subject)
