from django.urls import path
from .views import StudentDetailView, StudentView, ClassRoomView, ClassRoomUsingSerializerDetailView, ClassRoomListUsingSerializerView, StudentUsingSerializerView, StudentUsingModelSerializerView, ClassRoomGenericListView, ClassRoomGenericCreateView, ClassRoomGenericView, ClassRoomGenericUpdateView, ClassRoomGenericDetailView, ClassRoomGenericDeleteView
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
]

urlpatterns += using_serializer_path + using_model_path + generic_urls
