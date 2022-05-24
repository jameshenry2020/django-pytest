import random
import factory
from schoolapp.models import Student, ClassRoom


class StudentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Student

    first_name = "james"
    last_name = "harry"
    admission_number = random.randint(1, 100)
    grade = 70


class ClassroomFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ClassRoom

    name = "primary 1"
    student_capacity = 80

    @factory.post_generation
    def students(self, create, extracted, **kwargs):
        if not create or not extracted:
            return

        self.students.add(*extracted)
