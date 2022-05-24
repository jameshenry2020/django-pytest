import pytest
from schoolapp.models import Student, ClassRoom


@pytest.mark.django_db
def test_student_instance(student_factory):
    student = student_factory.create()
    assert isinstance(student, Student)
    assert str(student) == "james"


@pytest.mark.django_db
def test_classroom_instance(classroom_factory):
    classroom = classroom_factory.create()
    assert isinstance(classroom, ClassRoom)
    assert str(classroom) == "primary 1"


@pytest.mark.parametrize(
    "first_name, last_name, admission_number, grade, validity",
    [
        ('harry', 'john', 29, 35, "Fail"),
        ('harry', 'john', 43, 60, "Passed"),
        ('harry', 'john', 26, 75, "Excellent"),
        ('harry', 'john', 46, 40, "Error"),

    ],
)
def test_model_obj_instance(db, student_factory, first_name, last_name, admission_number, grade, validity):
    student = student_factory(
        first_name=first_name,
        last_name=last_name,
        admission_number=admission_number,
        grade=grade
    )
    assert student.get_grade() == validity
