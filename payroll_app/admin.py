from django.contrib import admin
from .models import Position, Department, Employee, Institution, OpenPosition, Schedule
# Register your models here.

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']
    list_filter = ['name']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']
    list_filter = ['name']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'department', 'position', 'active']
    list_filter = ['name', 'department', 'position']

@admin.register(Institution)
class InstitutionAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']
    list_filter = ['name', 'departments', 'positions', 'employees']
    
@admin.register(OpenPosition)
class OpenPositionAdmin(admin.ModelAdmin):
    list_display = ['name', 'institution', 'department', 'active']
    list_filter = ['name', 'institution', 'department']

@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['name', 'active']
    list_filter = ['name',]