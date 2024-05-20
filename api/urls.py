from django.urls import path
from .views import StudentDetailView, StudentView, ClassRoomView, ClassRoomUsingSerializerDetailView
app_name="api"

urlpatterns = [
    path("student/", StudentView.as_view(), name="student"),
    path("student/<int:id>/", StudentView.as_view(), name="student_patch"),
    path("student/<int:id>/", StudentDetailView.as_view(), name="student_detail"),
    path("classroom/", ClassRoomView.as_view(), name="classroom"),   
    path("classroom/<int:id>/", ClassRoomView.as_view(), name="classroom_patch"),   
       
]

using_serializer_path= [
    path("classroom-using-serializer/<int:id>/",ClassRoomUsingSerializerDetailView.as_view()),
]

urlpatterns += using_serializer_path
