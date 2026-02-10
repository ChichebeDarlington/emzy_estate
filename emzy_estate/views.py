from django.shortcuts import render
from django.http import HttpResponse
from post_estates.models import EstatePost 

def homepage(request):
    estates = EstatePost.objects.all() 
    return render(request, "home.html", {"estates":estates})
    
