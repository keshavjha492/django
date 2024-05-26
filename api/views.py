from rest_framework.views import APIView
from .permission import IsSuperAdminUser
from crud.models import Student, ClassRoom
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ClassRoomSerializer, StudentSerializer, StudentModelSerializer, ClassRoomModelSerializer


class StudentDetailView(APIView):
    def get(self, *args, **kwargs):
        id = self.kwargs["id"]
        try:
            student = Student.objects.get(id=id)
        except Student.DoesNotExist:
            return Response({"detail" : "Not Found"}, status = status.HTTP_404_NOT_FOUND)
        return Response({
            "id" : student.id,
            "name" : student.name,
            "age" : student.age,
            "address" : student.address
        })
        # return Response({
        #     "id" : 1, 
        #     "name" : "jon",
        #     "age" : 22, 
        #     "address" : "KTM"
        # })
    def patch(self, *args, **kwargs):
        data = self.request.data
        if not data:
            return Response({
                "message" : "please mention name, age, address, and email."
            })
        student_id = kwargs["id"]
        try:
            student = Student.objects.get(id = student_id)
        except Student.DoesNotExist:
            return Response({
                "message" : "Not found"
                },status = status.HTTP_404_NOT_FOUND )
        Student.objects.filter(id = student.id).update(**data)
        student = Student.objects.get(id = student_id)
        return Response({
            "message": "Student updated successfully",
            "id" : student.id,
            "name" : student.name,
            "age" : student.age,
            "address" : student.address,
            "email" : student.email
        })
        # response = {" message" : "updated successfully"}
        # response.update()


class StudentView(APIView):
    def get(self, *args, **kwargs):
        student = Student.objects.all()
        result = [] 
        for s in student:
            result.append({
                "id" : s.id,
                "name" : s.name,
                "age" : s.age,
                "address" : s.address,
                })
        return Response(result)

    def post(self, *args, **kwargs):
        data = self.request.data
        if not data:
            return Response({"message" : "name, age, address and email are required."})
        if "name" not in data or "age" not in data or "email" not in data or "address" not in data:
            return Response({"message" : "name, age, email and address are required"})
        name = self.request.data["name"]
        age = self.request.data["age"]
        address = self.request.data["address"]
        email = self.request.data["email"]

        Student.objects.create(name = name, age = age, address = address, email = email)
        return Response({
            "message" : "Student created successfully",
            "name" : name, 
            "age" : age,
            "address" : address,
            "email" : email
        },status = status.HTTP_20_CREATED)

    
class ClassRoomView(APIView):
    def get(self, *args, **kwargs):
        classroom = ClassRoom.objects.all()
        result = []
        for c in classroom:
            result.append({
                "id" : c.id,
                "name" : c.name,
            })
        return Response(result)
        
    def post(self, *args, **kwargs):
        name = self.request.data.get("name")
        if not name:
            return Response({
                "name" : "This field is required."
            })
        ClassRoom.objects.create(name=name)
        return Response({
            "message" : "Classroom created successfully.",
            "name" : name
        })

    def patch(self, *args, **kwargs):
        data = self.request.data
        classroom_id = kwargs["id"]
        if not data or "name" not in data:
            return Response({
                "message": "name field is required for classroom update"
            })
        try:
            classroom = ClassRoom.objects.get(id=classroom_id)
        except ClassRoom.DoesNotExist:
            return Response({
                "detail" : "Not Found"
            })
        ClassRoom.objects.filter(id = classroom.id).update(**data)
        Classroom = ClassRoom.objects.get(id=classroom_id)

        return Response({
            "message": "Classroom updated successfully!",
             "id" : classroom.id,
             "name" : classroom.name
        })


        
        
class ClassRoomUsingSerializerDetailView(APIView):
    def get(self, *args, **kwargs):
        id = kwargs["id"]
        try:
            classroom = ClassRoom.objects.get(id=id)
        except ClassRoom.DoesNotExist:
            return Response({"detail" : "Not Found"}, status = status.HTTP_404_NOT_FOUND)
        serializer = ClassRoomSerializer(classroom)
        return Response(serializer.data)
    
class ClassRoomListUsingSerializerView(APIView):
    def get(self, *args, **kwargs):
        classrooms = ClassRoom.objects.all()
        serializer = ClassRoomSerializer(classrooms, many = True)
        return Response(serializer.data)
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = ClassRoomSerializer(data = data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            c = ClassRoom.objects.create(**validated_data)
            return Response({
                "message" : "Classroom created successfully",
                "name" : c.name
            }, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class StudentUsingSerializerView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many = True)
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = StudentSerializer(data = data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            s = Student.objects.create(**validated_data)
            return Response({
                "message" : "Student created successfully",
                "name" : s.name
            }, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class StudentUsingModelSerializerView(APIView):
    def get(self, *args, **kwargs):
        students = Student.objects.all()
        serializer = StudentModelSerializer(students, many = True, context = {"request" : self.request})
        return Response(serializer.data)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = StudentModelSerializer(data = data, context = {"request" : self.request})
        if serializer.is_valid():
            s = serializer.save()
            return Response({
                "message" : "Student created successfully",
                "name" : s.name
            }, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
class ClassRoomGenericListView(ListAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer
    
class ClassRoomGenericCreateView(CreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer
    
class ClassRoomGenericView(ListCreateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer
        
class ClassRoomGenericUpdateView(UpdateAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer
    
class ClassRoomGenericDetailView(RetrieveAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer
    
class ClassRoomGenericDeleteView(DestroyAPIView):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomModelSerializer
    
class StudentUpdateRetriveDistroyView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
class ClassRoomViewSet(ModelViewSet):
    serializer_class = ClassRoomSerializer
    queryset = ClassRoom.objects.all()
    
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsSuperAdminUser()]
        if self.request.method == "POST":
            return [(IsAdminUser | IsSuperAdminUser)()]
        return[IsAuthenticated()]
    
class StudentViewSet(ModelViewSet):
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter,DjangoFilterBackend]
    filterset_fields =["classroom__name"]
    search_fields = ["name", "email", "address",]
    serializer_class = StudentSerializer
    queryset = Student.objects.all().order_by('-id')
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsSuperAdminUser()]
        if self.request.method == "POST":
            return [(IsAdminUser | IsSuperAdminUser)()]
        return[IsAuthenticated()]

class LoginApiView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get.serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.validated_data["user"]
        Token.objects.get_or_create(user = user).delete()
        token, created = Token.objects.get_or_create(user = user)
        return Response({"token" : token.key, "is_staff" : user.is_staff,"is_superuser" : user.is_superuser, "is_active" : user.is_active})
        
