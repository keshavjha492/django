from django.urls import path
from .views import student, classroom, classroom_update, classroom_delete, add_student, details_students, delete_student, update_student

urlpatterns = [
    path("classroom/<int:id>/", classroom_update, name="crud_classroom_update"),
    path ("classroom-delete/<int:id>/", classroom_delete, name="crud_classroom_delete"),
    path('classroom/', classroom, name="crud_classroom"),
    path ('add_student/', add_student, name = "crud_add_student"),
    path("details_student/<int:id>/", details_students, name ="details_students"),
    path("delete-student/<int:id>/", delete_student, name="delete_student"),
    path("update_student/<int:id>", update_student, name="update_student"),
    path('', student, name="crud_student"),
]