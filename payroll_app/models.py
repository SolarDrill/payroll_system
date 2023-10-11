from payroll.abstract_models import CommonInfo, CommonOrganization
from .utils import WEEKDAYS
from django.db import models
from multiselectfield import MultiSelectField

class Position(CommonInfo):

    def __str__(self):
        return self.name

class Department(CommonInfo):

    def __str__(self):
        return self.name

class Schedule(CommonInfo):
    days = MultiSelectField(verbose_name='Dia de la semana', choices=WEEKDAYS, max_choices=7, max_length=100)
    start_time = models.TimeField(verbose_name="Start Time")
    end_time = models.TimeField(verbose_name="End Time")
    
    def __str__(self):
        return  "%s de %s a %s - %s" %(self.days, self.start_time, self.end_time, self.name)

class Employee(CommonOrganization):
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    schedules = models.ManyToManyField(Schedule, blank=True)
    birth_date = models.DateField(blank=True, null=True)
    hiring_date = models.DateField(blank=True, null=True)
    
    def __str__(self):
        return '{0} {1}'.format(self.name, self.email)

class Institution(CommonOrganization):
    employees = models.ManyToManyField(Employee, blank=True)
    departments = models.ManyToManyField(Department, blank=True)
    positions = models.ManyToManyField(Position, blank=True)
    
    def __str__(self):
        return self.name
    
class OpenPosition(CommonOrganization):
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, blank=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name