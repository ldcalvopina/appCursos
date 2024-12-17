from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, CourseViewSet
from django.urls import path

router = DefaultRouter()
router.register('courses',CourseViewSet)
router.register('students',StudentViewSet)

urlpatterns = router.urls