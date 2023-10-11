from django.conf import settings
from rest_framework.routers import DefaultRouter, SimpleRouter
from payroll_app.api.viewsets import PositionViewSet, DepartmentViewSet, EmployeeViewSet, InstitutionViewSet, OpenPositionViewSet, ScheduleViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register(r"positions", PositionViewSet)
router.register(r"departments", DepartmentViewSet)
router.register(r"employees", EmployeeViewSet)
router.register(r"institutions", InstitutionViewSet)
router.register(r"open_positions", OpenPositionViewSet)
router.register(r"schedules", ScheduleViewSet)


app_name = "api"
urlpatterns = router.urls


