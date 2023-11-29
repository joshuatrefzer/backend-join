from rest_framework.exceptions import ValidationError
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.http import HttpResponseBadRequest
from rest_framework.test import APIClient, APITestCase
from django.urls import reverse
from .models import Task
from .serializers import TaskSerializer
from .views import TaskViewSet


class SignupViewTest(TestCase):
    def setUp(self):
        # Set up a test client
        self.client = APIClient()

        # Set up some test data for signup
        self.signup_data = {"username": "newuser", "password": "newpassword"}

    def test_signup_successful(self):
        response = self.client.post("/signup/", self.signup_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)
        self.assertIn("user", response.data)

        # Check if a user was created in the database
        self.assertEqual(User.objects.count(), 1)
        created_user = User.objects.get(username="newuser")
        self.assertEqual(created_user.username, "newuser")

        # Check if a token was created for the user
        self.assertTrue(Token.objects.filter(user=created_user).exists())

    def test_signup_invalid_data(self):
        # Provide invalid data to trigger validation error
        invalid_signup_data = {"username": "", "password": "weak"}
        response = self.client.post("/signup/", invalid_signup_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check if the appropriate validation error is present in the response
        self.assertIn("blank", response.data["username"][0].code)

        # Check that no user was created in the database
        self.assertEqual(User.objects.count(), 0)


class LoginViewTest(TestCase):
    def setUp(self):
        # Set up a test user
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        self.client = APIClient()
        self.login_data = {"username": "testuser", "password": "testpassword"}

    def test_login_successful(self):
        response = self.client.post("/login/", self.login_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)
        self.assertIn("user", response.data)

    def test_login_user_not_found(self):
        # Provide a non-existent username for user not found scenario
        self.login_data["username"] = "nonexistentuser"
        response = self.client.post("/login/", self.login_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertIn("detail", response.data)


class TaskViewSetTest(APITestCase):
    def setUp(self):
        self.task_data = {"title": "Test Task", "description": "Test Description"}
        self.client = APIClient()

        # Erstellen Sie einen Benutzer und Token für den Test
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)

    def test_create_task(self):
        # Fügen Sie den Token zum Testclient hinzu
        # Fügen Sie den Token zum Testclient hinzu
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        # Aktualisieren Sie task_data mit allen erforderlichen Feldern
        self.task_data = {
            "title": "Test Task",
            "description": "Test Description",
            "assigned_to": [],  # Beispiel für ein leeres Feld assigned_to
            "subtasks": [],  # Beispiel für ein leeres Feld subtasks
            "date": "2023-12-01",  # Beispiel für ein Datum
            "category": "example_category",  # Beispiel für eine Kategorie
        }

        response = self.client.post("/api/tasks/", self.task_data, format="json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class SubtaskViewSetTest(APITestCase):
    def setUp(self):
        self.subtask_data = {
            "title": "Test Subtask",
            "description": "Test Subtask Description",
        }
        self.client = APIClient()

        # Erstellen Sie einen Benutzer und Token für den Test
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)

    def test_create_subtask(self):
        # Fügen Sie den Token zum Testclient hinzu
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")

        # Aktualisieren Sie subtask_data mit allen erforderlichen Feldern
        self.subtask_data = {
            "title": "Test Subtask",
            "description": "Test Subtask Description",
            # Fügen Sie hier erforderliche Felder für Subtask hinzu
        }

        response = self.client.post("/api/subtasks/", self.subtask_data, format="json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class ContactViewSetTest(APITestCase):
    def setUp(self):
        self.contact_data = {
            "first_name": "John",
            "last_name": "Doe",
            "mail": "john.doe@example.com",
            "phone": "123456789",
        }
        self.client = APIClient()

        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)


    def test_create_contact(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.token.key}")
        
        self.contact_data = {
            "first_name": "John",
            "last_name": "Doe",
            "mail": "john.doe@example.com",
            "phone": "123456789",
        }

        response = self.client.post("/api/contacts/", self.contact_data, format="json")
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
