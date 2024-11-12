from errors import MaxStudentsReachedError, ERROR_MAX_STUDENT_NUM


class Group:
    MAX_STUDENTS = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.MAX_STUDENTS:
            raise MaxStudentsReachedError(ERROR_MAX_STUDENT_NUM)
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n{all_students}'