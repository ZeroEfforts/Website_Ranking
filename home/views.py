from django.shortcuts import render
from .forms import SearchForm
# Create your views here.

def index(request):
    form=SearchForm()
    if request=="POST":
        pass

    context={
        'form':form
    }
    return render(request, 'home/index.html', context)