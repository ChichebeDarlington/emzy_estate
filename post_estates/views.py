from django.shortcuts import render, redirect
from . import forms
from post_estates.models import EstatePost 

# Create your views here.
def create_post_view(request):
    if request.method == "POST":
        form = forms.EstatePost(request.POST, request.FILES)
        if form.is_valid:
            new_estate = form.save(commit=False)
            new_estate.author = request.user
            new_estate.save()
            return redirect('post_estates:home')
    else:
        form = forms.EstatePost()
    return render(request, "new_estate.html", {"form":form})
    

def fetch_post_view(request):
      estates = EstatePost.objects.all() 
      return render(request, "home.html", {"estates":estates})   

def estate_detail(request, id):
     estate = EstatePost.objects.get(id=id) 
     return render(request, "details.html", {"estate":estate})

def estate_tab(request, pk, tab):
    estate = Estate.objects.get(pk=pk)

    if tab == "details":
        return render(request, "tabs/tabsdetails.html", {"estate": estate})
    if tab == "map":
        return render(request, "tabs/tabsmap.html", {"estate": estate})
    return render(request, "tabs/tabsareaguide.html", {"estate": estate})

