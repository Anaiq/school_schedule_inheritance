from .student import Student

# add MiddleSchoolStudent here
class MiddleSchoolStudent(Student):
    def __init__(self, name, grade, classes, needs_transportation=True):
        super().__init__(name, grade, classes)
        self.needs_transportation = needs_transportation

    def summary(self):
        student_summary = super().summary()
        transportation_message = self.display_transportation_message()

        return "\n".join((student_summary, transportation_message))

    def display_transportation_message(self):
        needs_message = "needs" if self.needs_transportation else "doesn't need"
        return f"{self.name} {needs_message} transportation to school."
