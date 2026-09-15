from django.shortcuts import render
from .models import Course
# Create your views here.
def home(request):
    Courses=Course.objects.all()
    return render(request,'home/index.html', {'courses':Courses})