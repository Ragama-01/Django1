from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

app_name="teachers"
def Home(request):
    return HttpResponse("welcome to emobilis")

def about(request):
    return HttpResponse("about emobilis")