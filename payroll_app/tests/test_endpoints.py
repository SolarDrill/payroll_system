from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from ..models import (
    Position, Department, Employee, Institution, OpenPosition, Schedule
)
from django.contrib.auth.models import User
from django.urls import reverse

base_url = "http://127.0.0.1:8000/api/v1/"

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            username="testuser",
            password="testpass"
        )
        self.client.login(username="testuser", password="testpass")

        # Create test objects, including related objects as needed
        self.position = Position.objects.create(name="Test Position")
        self.department = Department.objects.create(name="Test Department")
        self.schedule = Schedule.objects.create(
            name="Test Schedule",
            days="Lunes, Martes",
            start_time="08:00:00",
            end_time="17:00:00"
        )
        self.employee = Employee.objects.create(
            name="Test Employee",
            position=self.position,
            department=self.department,
            salary=50000.00,
            birth_date="1990-01-01",
            hiring_date="2022-01-01"
        )
        self.institution = Institution.objects.create(name="Test Institution")
        self.institution.employees.add(self.employee)
        self.institution.departments.add(self.department)
        self.institution.positions.add(self.position)
        self.open_position = OpenPosition.objects.create(
            name="Test Open Position",
            institution=self.institution,
            department=self.department
        )

    def test_position_endpoint(self):
        url = base_url + "positions/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], self.position.name)

    def test_department_endpoint(self):
        url = base_url + "departments/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], self.department.name)

    def test_employee_endpoint(self):
        url = base_url + "employees/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], self.employee.name)

    def test_institution_endpoint(self):
        url = base_url + "institutions/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], self.institution.name)

    def test_open_position_endpoint(self):
        url = base_url + "open_positions/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], self.open_position.name)

    def test_schedule_endpoint(self):
        url = base_url + "schedules/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], self.schedule.name)
        self.assertEqual(
            response.data[0]["days"], ["Lunes", "Martes"]
        )
        self.assertEqual(
            response.data[0]["start_time"], "08:00:00"
        )
        self.assertEqual(
            response.data[0]["end_time"], "17:00:00"
        )

    # Add more test methods for other endpoints as needed
