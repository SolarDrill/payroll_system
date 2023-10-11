from django.test import TestCase
from ..models import Position, Department, Schedule, Employee, Institution, OpenPosition
from django.contrib.auth.models import User

class ModelTestCase(TestCase):
    def setUp(self):
        # Create test objects, including related objects as needed
        self.position = Position.objects.create(name="Test Position")
        self.department = Department.objects.create(name="Test Department")
        self.schedule = Schedule.objects.create(
            name="Test Schedule",
            days="Lunes, Martes",
            start_time="08:00:00",
            end_time="17:00:00"
        )
        self.user = User.objects.create(username="testuser")
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

    def test_position_str(self):
        self.assertEqual(str(self.position), "Test Position")

    def test_department_str(self):
        self.assertEqual(str(self.department), "Test Department")

    def test_schedule_str(self):
        self.assertEqual(
            str(self.schedule),
            "Lunes, Martes de 08:00:00 a 17:00:00 - Test Schedule"
        )

    def test_employee_str(self):
        self.assertEqual(str(self.employee), "Test Employee")

    def test_institution_str(self):
        self.assertEqual(str(self.institution), "Test Institution")

    def test_open_position_str(self):
        self.assertEqual(str(self.open_position), "Test Open Position")

