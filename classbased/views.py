from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = "classbased/home.html"
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["name"] = "harry"
        return context
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
        





