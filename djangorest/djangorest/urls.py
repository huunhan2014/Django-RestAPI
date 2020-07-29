from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest import views as rest_views
from . import views
from school import views as school_views

router = routers.DefaultRouter()
# router = routers.SimpleRouter()

router.register(r'posts', rest_views.PostListCreateAPIView)
router.register(r'posts', rest_views.PostDetailUpdateAPIView)

# Rest App
router.register(r'users', rest_views.UserViewSet)
router.register(r'groups', rest_views.GroupViewSet)
router.register(r'types', rest_views.TypeViewSet)
router.register(r'products', rest_views.ProductViewSet)
router.register(r'field-plannning-runs', rest_views.FieldPlanningRunViewSet)

# School App
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

    # path('classes/', school_views.index_class, name='index_class'),
    # path('classes/<int:classes_id>/', school_views.class_detail, name='classList'),
    # path('classes/add/', school_views.ClassViewSet.as_view(), name='classAdd'),
    # path('append/', school_views.put_class, name='index_class'),

]
