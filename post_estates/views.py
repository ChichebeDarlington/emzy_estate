from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from . import forms
from post_estates.models import EstatePost 

# Create your views here.
def delete_estate(request, pk):
    estate = get_object_or_404(EstatePost, id=pk)

    if request.method == "POST":
        estate = estate.delete()
        messages.success(request, "Estate deleted successfully.")
        return redirect("post_estates:home")  # change to your listing page name
    return render(request, "confirm_delete.html", {"estate":estate})

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
      search = request.GET.get('search')
      min_price = request.GET.get('min_price')
      max_price = request.GET.get('max_price')
      types = request.GET.get('types')
      apartment = request.GET.get('apartment')

      if search:
        estates = estates.filter(
            Q(location__icontains=search) |
            Q(description__icontains=search)
        )

      if min_price:
        estates = estates.filter(fees__gte=min_price)

      if max_price:
        estates = estates.filter(fees__lte=max_price)

      if types:
        estates = estates.filter(types=apartment) #description

      if apartment:
        estates = estates.filter(apartment__icontains=apartment)
      context = {
        "estates": estates
    }
      return render(request, "home.html", context)   

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

