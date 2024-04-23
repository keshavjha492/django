from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    query_string = request.GET
    name = query_string.get("name")
    
    return HttpResponse(f"hello world this is {name},")
    
    
def portfolio(request):
    return render(request,template_name="myapp/portfolio.html")

    