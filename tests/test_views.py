import pytest
from rest_framework.test import APIClient


client = APIClient()


@pytest.mark.django_db
def test_student_create_endpoint():
    input = dict(
        first_name='matt',
        last_name='charles',
        admission_number=234,
    )
    response = client.post('/students/register/', input)
    assert response.status_code == 201


@pytest.mark.django_db
def test_student_list_endpoint():
    response = client.get('/students/')
    assert response.status_code == 200
