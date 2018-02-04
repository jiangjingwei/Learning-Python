class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return self.name

class Classes:
    def __init__(self, name, semester, course, course_date, teacher):
        self.name = name
        self.semester = semester
        self.course = course
        self.course_date = course_date
        self.teacher = teacher

class Course:
    def __init__(self):
