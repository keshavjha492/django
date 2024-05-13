from django.shortcuts import render, redirect
from crud.models import ClassRoom
from django.views.generic import TemplateView, ListView
from django.contrib import messages
from .forms import ClassRoomForm


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
            name = form.cleaned_data["name"]
            ClassRoom.objects.create(name=name)
            messages.success(self.request, "classroom added successfully")
            
        else:
            messages.error(self.request, "invalid form data")
        return redirect("classbased:classroom")
    
        





