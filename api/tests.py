from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from todos.models import Todo
import json


class AdminAuthenticationTestCase(APITestCase):
    def setUp(self):
        url = reverse("token_obtain_pair")
        # Creating admin user
        user_model = get_user_model()
        user_pwd = "django1234"
        user = user_model.objects.create(username="oliverreyes")
        user.set_password(user_pwd)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        response = self.client.post(
            url, {"username": user.username, "password": user_pwd}, format="json"
        )
        self.token = response.json()["access"]
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token)

    def test_authenticated_admin_get_request(self):
        url = reverse("todo_list_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_todo_create_view(self):
        url = reverse("todo_list_create")
        response = self.client.post(url, {"name": "Todo POST", "text": "Test POST Text",
                                          "status": True})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_todo_list_view(self):
        todo_1 = Todo.objects.create(
            name="Todo 1", text="Test text", status=True, owner=get_user_model().objects.get(id=1))
        url = reverse("todo_list_create")
        response = self.client.get(url)
        self.assertEquals(json.loads(response.content), [
                          {'id': 1, 'name': 'Todo 1', 'text': 'Test text', 'status': True, 'owner': 1}])

    def test_todo_create_and_list(self):
        url = reverse("todo_list_create")
        response = self.client.post(
            url, {"name": "Todo POST", "text": "Test POST Text", "status": True})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), [
                         {'id': 1, 'name': 'Todo POST', 'text': 'Test POST Text', 'status': True, 'owner': 1}])

    def test_acces_todo_from_another_user(self):
        url = "/api/todos/1/"
        url_2 = "/api/todos/2/"
        post_url = reverse("todo_list_create")
        user_model = get_user_model()
        user_pwd = "django1234"
        b_user = user_model.objects.create(username="b")
        b_user.set_password(user_pwd)
        b_user.save()

        Todo.objects.create(name="B Todo", text="B text",
                            status=True, owner=b_user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = self.client.post(
            post_url, {"name": "Todo POST", "text": "Test POST Text", "status": True})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.get(url_2)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
