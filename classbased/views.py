from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from crud.models import ClassRoom, Student, StudentProfile
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib import messages
from .forms import ClassRoomForm, ClassRoomModelForm, StudentModelForm



# Create your views here.


class HomeView(TemplateView):
    template_name = "classbased/home.html"

    def get_context_data(self, **kwargs ):
        context = super().get_context_data(**kwargs)
        context["name"] = "Suraj"
        print(context)
        return context

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


# class ClassRoomView(ListView):
#     queryset = ClassRoom.objects.all()
#     template_name = "classbased/classroom.html"
#     context_object_name = "classrooms"


#     def get_context_data(self, *args, **kwargs):
#         context = super().get_context_data(*args, **kwargs)
#         # form = ClassRoomForm()
#         form = ClassRoomModelForm()
#         context["form"] = form
        # return context

    # def post(self, *args, **kwargs):
    #     form = ClassRoomModelForm(self.request.POST)    # we are validating user input data
    #     if form.is_valid():
    #         print(form.cleaned_data)  # form.cleaned is a dict type
    #         # name = form.cleaned_data["name"]
    #         # ClassRoom.objects.create(name=name)
    #         form.save()
    #         messages.success(self.request, "Classroom added successfully")
    #     else:
    #         messages.error(self.request, "invalid form data")
    #     return redirect("classbased:classroom")      

class ClassroomListCreateView(CreateView):
    queryset = ClassRoom.objects.all()      #querysets are lazy in django
    template_name = "classbased/classroom.html"
    context_object_name = "classrooms"
    form_class = ClassRoomModelForm
    success_url = reverse_lazy("classbased:classroom")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["classrooms"] = self.get_queryset()
        return context


    def post(self, request, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            messages.success(request, "Classroom added successfully")
            return self.form_valid(form)
        else:
            messages.error(request, "Something went wrong !")
            return self.form_invalid(form)

class ClassroomUpdateView(UpdateView):
    queryset = ClassRoom.objects.all()
    template_name = "classbased/classroom_update.html"
    form_class = ClassRoomModelForm
    context_object_name = "classroom"
    success_url = reverse_lazy("classbased:classroom")

class ClassroomDeleteView(DeleteView):
    queryset = ClassRoom.objects.all()
    template_name = "classbased/classroom_delete.html"
    success_url = reverse_lazy("classbased:classroom")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            messages.success(request, "Classroom deleted successfully")
            return self.form_valid(form)
        else:
            messages.error(request, "Something went wrong !")
            return self.form_invalid(form)

class StudentListView(ListView):
    model = Student
    # queryset = Student.objects.all()
    template_name = "classbased/student.html"
    context_object_name = "students"
    success_url = reverse_lazy("classbased:student")


class StudentCreateView(CreateView):
    model = Student
    template_name = "classbased/student_create.html"
    form_class = StudentModelForm
    success_url = reverse_lazy("classbased:student")
    
    def form_valid(self, form):
        # cleaned_data = form.cleaned_data
        self.object = form.save()
        student = self.object
        bio = form.cleaned_data["bio"]
        phone = form.cleaned_data["phone_number"] 
        StudentProfile.objects.create(student = student, bio = bio, phone = phone )
        messages.success(self.request, "Student added successfully")
        return redirect("classbased:student")


    def form_invalid(self, form):
        messages.error(self.request, "Could not create student!")
        return super().form_invalid(form)

class StudentDeleteView(DeleteView):
    pass

class StudentDetailView(DetailView):
    queryset = Student.objects.all()
    template_name = "classbased/student_detail.html"
    context_object_name="student"