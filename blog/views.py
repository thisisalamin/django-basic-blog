from django.shortcuts import render
from django.http import HttpResponse
from.models import Blog

# Create your views here.
def homepage(request):
    return render(request=request,template_name='blog/home.html',context={'blog':Blog.objects.all})
