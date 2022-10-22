from school_schedule.middle_school_student import MiddleSchoolStudent

def test_new_valid_middle_school_student_needs_transportation():
    # Arrange
    name = "Bembi"
    grade = "7th-grader"
    classes = ["Painting"]

    # Act
    bembi = MiddleSchoolStudent(name, grade, classes, needs_transportation=True)

    # Assert
    assert bembi.needs_transportation

def test_new_valid_middle_school_student_with_defaults():
    # Arrange
    name = "Basia"
    grade = "6th-grader"
    classes = ["Matematyka", "Angielski"]

    # Act
    basia = MiddleSchoolStudent(name, grade, classes, needs_transportation=False)

    #Assert
    assert basia.name == name
    assert basia.grade == grade
    assert basia.classes == classes
    assert len(basia.classes) == 2
    assert not basia.needs_transportation

def test_middle_school_student_summary_with_transportation():
    # Arrange
    name = "Brock"
    grade = "8th-grader"
    classes = ["Social Studies", "P.E.", "Biology"]

    # Act
    brock = MiddleSchoolStudent(name, grade, classes, needs_transportation=False)
    brock_summary = brock.summary()

    #Assert
    assert not brock.needs_transportation
    assert brock_summary == "Brock is a 8th-grader enrolled in 3 classes: Social Studies, P.E., Biology.\nBrock doesn't need transportation to school."

def test_middle_school_student_summary_without_transportation():
    # Arrange
    name = "Joseph"
    grade = "7th-grader"
    classes = ["Painting", "History"]

    # Act
    joseph = MiddleSchoolStudent(name, grade, classes, needs_transportation=True)
    joseph_summary = joseph.summary()

    #Assert    
    assert joseph.needs_transportation
    assert joseph_summary == "Joseph is a 7th-grader enrolled in 2 classes: Painting, History.\nJoseph needs transportation to school."

