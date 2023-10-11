from rest_framework import serializers
from ..models import Position, Department, Employee, Institution, OpenPosition, Schedule

class PositionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Position
        fields = ('id','name','description','created','modified', 'active')
        
class DepartmentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Department
        fields = ('id','name','description','created','modified', 'active')

class ScheduleSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Schedule
        fields = ('id','name', 'days', 'start_time', 'end_time', 'created','modified', 'active')
        
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    position = serializers.PrimaryKeyRelatedField(queryset=Position.objects.all())
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    schedules = serializers.PrimaryKeyRelatedField(queryset=Schedule.objects.all(), many=True)
    
    class Meta:
        model = Employee
        fields = ('id','name','position','department','salary','schedules','birth_date','hiring_date','telephone', 'email', 'created','modified', 'active')
        
class InstitutionSerializer(serializers.HyperlinkedModelSerializer):
    departments = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), many=True)
    positions = serializers.PrimaryKeyRelatedField(queryset=Position.objects.all(), many=True)
    employees = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), many=True)

    class Meta:
        model = Institution
        fields = ('id','name','telephone','departments','positions','employees','email', 'created','modified', 'active')
        
class OpenPositionSerializer(serializers.HyperlinkedModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())
    institution = serializers.PrimaryKeyRelatedField(queryset=Institution.objects.all())

    class Meta:
        model = OpenPosition
        fields = ('id','name','description','institution','department', 'telephone', 'email', 'created','modified', 'active')

