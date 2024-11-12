ERROR_MAX_STUDENT_NUM = "Max number of students reached"
ERROR_404 = ""


class MaxStudentsReachedError(Exception):
    def __init__(self, message=ERROR_MAX_STUDENT_NUM):
        self.message = message
        super().__init__(self.message)
