from typing import Any
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from crud.models import ClassRoom
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
from .forms import ClassRoomForm, ClassRoomModelForm


class HomeView(TemplateView):
    template_name = "classbased/home.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "harry"
        return context
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    
class ClassRoomView(ListView):
    queryset= ClassRoom.objects.all()
    template_name ="classbased/classroom.html"

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        form = ClassRoomForm()
        context["form"] = form
        return context 
    
    def post(self, *args, **kwargs):
        form = ClassRoomForm(self.request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # name = form.cleaned_data["name"]
            # ClassRoom.objects.create(name=name)
            form.save()
            messages.success(self.request, "classroom added successfully")
            
        else:
            messages.error(self.request, "invalid form data")
        return redirect("classbased:classroom")
    
class ClassroomListCreateView(CreateView):
    queryset = ClassRoom.objects.all()
    context_object_name="classrooms"
    template_name = "classbased/classroom.html"
    form_class = ClassRoomModelForm
    success_url  = reverse_lazy("classbased:classroom")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['classrooms']= self.get_queryset
        return context
    
    
    def post(self, *args, **kwargs):
        self.object = None
        form = self.get_form()
        if form.is_valid():
            messages.success(request,"classroom is added successfully")
            return self.form_valid(form)
        else:
            messages.success(request,"Something went wrong")
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
    context_object_name = "classroom"
    
    def post(self, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            messages.success(self.request,"classroom deleted successfully")
            return self.form_valid(form)
        else:
            messages.success(self.request,"Something went wrong")
            return self.form_invalid(form)
        
    
    
    
    
    
    
        





