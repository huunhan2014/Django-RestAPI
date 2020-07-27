from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest.views import PostListCreateAPIView, PostDetailUpdateAPIView, UserViewSet, GroupViewSet, TypeViewSet, ProductViewSet, FieldPlanningRunViewSet
from . import views
from school import views as school_views

router = routers.DefaultRouter()
# router = routers.SimpleRouter()

router.register(r'posts', PostListCreateAPIView)
router.register(r'posts', PostDetailUpdateAPIView)

router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'types', TypeViewSet)
router.register(r'products', ProductViewSet)
router.register(r'field-plannning-runs', FieldPlanningRunViewSet)
router.register(r'school-api', school_views.SchoolViewSet)
router.register(r'class-api', school_views.ClassViewSet)
router.register(r'student-api', school_views.StudentViewSet)

urlpatterns = [
    # API 
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    # School App
    path('school/', school_views.index, name='index'),
    path('school/<int:school_id>/', school_views.class_list, name='classList'),
    path('school/<int:school_id>/<int:class_id>/', school_views.student_list, name='studentList'),
    # Polls App
    path('polls/', include('polls.urls')),

]
