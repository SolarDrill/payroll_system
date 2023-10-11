from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from ..models import Position, Department, Employee, Institution, OpenPosition, Schedule
from .serializers import PositionSerializer, DepartmentSerializer, EmployeeSerializer, InstitutionSerializer, OpenPositionSerializer, ScheduleSerializer

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class =  PositionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id','name','description','created','modified', 'active')

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class =  DepartmentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id','name','description','created','modified', 'active')

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class =  ScheduleSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id','name', 'days', 'start_time', 'end_time', 'created','modified', 'active')
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class =  EmployeeSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id','name','position','department','salary','schedules','birth_date','hiring_date','telephone', 'email', 'created','modified', 'active')

class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class =  InstitutionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id','name','telephone', 'email', 'created','modified', 'active')

#Allow non-authenticated users to view open positions since it's information that should be public to get people to apply
class OpenPositionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = OpenPosition.objects.all()
    serializer_class =  OpenPositionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id','name','description','department', 'telephone', 'email', 'created','modified', 'active')


