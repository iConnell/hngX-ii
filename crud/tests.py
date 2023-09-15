from django.test import TestCase
from django.urls import reverse
from .models import Person
import json

# Create your tests here.


class TestPersonViews(TestCase):
    def setUp(self) -> None:
        Person.objects.create(name="McConnell Ikechukwu", organisation="HNG", role="intern")
        Person.objects.create(name="Mark Essien", role="chief_mentor")

    def test_create_person_view(self):
        url = reverse("person-create-list")
        data = {"name": "Test name", "role": "QA"}

        response = self.client.post(url, data)

        assert response.status_code == 201
        assert response.data["id"]
        assert response.data["name"] == data["name"]
        assert response.data["role"] == data["role"]
        assert response.data["organisation"] == "HNGX"

    def test_list_persons_view(self):
        url = reverse("person-create-list")

        response = self.client.get(url)

        assert len(response.data) == 2
        assert response.status_code == 200

    def test_retrieve_person_view(self):
        person = Person.objects.get(pk=1)
        url = reverse("person-retrieve-update-destroy", kwargs={"pk": person.id})

        response = self.client.get(url)

        assert response.status_code == 200
        assert response.data["id"] == person.id
        assert response.data["name"] == person.name
        assert response.data["role"] == person.role
        assert response.data["organisation"] == person.organisation

    def test_update_person_view(self):
        person = Person.objects.get(pk=1)
        url = reverse("person-retrieve-update-destroy", kwargs={"pk": person.id})
        update_data = {"name": "New Name", "role": "updated role"}
        response = self.client.patch(url, update_data, content_type="application/json")

        updated_person = Person.objects.get(pk=person.id)

        assert response.status_code == 200
        assert updated_person.name == update_data["name"]
        assert updated_person.role == update_data["role"]

    def test_destroy_person_view(self):
        url = reverse("person-retrieve-update-destroy", kwargs={"pk": 1})

        response = self.client.delete(url)
        assert response.status_code == 204

        res = self.client.get(reverse("person-create-list"))
        assert len(res.data) == 1
