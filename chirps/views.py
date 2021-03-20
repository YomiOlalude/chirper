from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views import generic

# Create your views here.

def chirps_list_view(request, *args, **kwargs):
    chirps = Chirp.objects.all()
    
    context = {
        "chirps": chirps
    }

    return render(request, "pages/home.html", context)

def chirp_create_view(request, *args, **kwargs):
    form = ChirpCreateForm(request.POST)
    content = request.POST.get("content")
    
    if form.is_valid():
        form.save()
        form = ChirpCreateForm()
        return redirect("/")
        
    context = {
        "form": form
    }
        
    return render(request, "components/form.html", context)
    
