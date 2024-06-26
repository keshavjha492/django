from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StudentDetailView, StudentView, ClassRoomView, ClassRoomUsingSerializerDetailView, ClassRoomListUsingSerializerView, StudentUsingSerializerView, StudentUsingModelSerializerView, ClassRoomGenericListView, ClassRoomGenericCreateView, ClassRoomGenericView, ClassRoomGenericUpdateView, ClassRoomGenericDetailView, ClassRoomGenericDeleteView, StudentUpdateRetriveDistroyView, ClassRoomViewSet, StudentViewSet, LoginApiView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

app_name="api"

router.register("viewset/classroom", ClassRoomViewSet, basename="classroom")
router.register("viewset/student", StudentViewSet, basename="student")


urlpatterns = [
    path("student/", StudentView.as_view(), name="student"),
    path("student/<int:id>/", StudentView.as_view(), name="student_patch"),
    path("student/<int:id>/", StudentDetailView.as_view(), name="student_detail"),
    path("classroom/", ClassRoomView.as_view(), name="classroom"),   
    path("classroom/<int:id>/", ClassRoomView.as_view(), name="classroom_patch"), 
    path("login/", obtain_auth_token),
    path('login/', LoginApiView.as_view(), name = "login"),
      
       
] + router.urls

using_serializer_path= [
    path("classroom-using-serializer/<int:id>/",ClassRoomUsingSerializerDetailView.as_view()),
    path("using-serializer/classroom/",ClassRoomListUsingSerializerView.as_view()),
    path("using-serializer/student/",StudentUsingSerializerView.as_view()),
    
]

using_model_path = [
    path("using-model-serializer/student/",StudentUsingModelSerializerView.as_view()),
]

generic_urls = [
    path("generic-classroom/list",ClassRoomGenericListView.as_view()),
    path("generic-classroom/Create",ClassRoomGenericCreateView.as_view()),
    path("generic-classroom/",ClassRoomGenericView.as_view()),
    path("generic-classroom/update/<int:pk>/",ClassRoomGenericUpdateView.as_view()),
    path("generic-classroom/Details/<int:pk>/",ClassRoomGenericDetailView.as_view()),
    path("generic-classroom/delete/<int:pk>/",ClassRoomGenericDeleteView.as_view()),
    path("generic/student/<int:pk>/",StudentUpdateRetriveDistroyView.as_view()),
]



urlpatterns += using_serializer_path + using_model_path + generic_urls
