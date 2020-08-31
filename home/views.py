from django.shortcuts import render, redirect
from .forms import SearchForm
from .private.gsearch import gsearch
# Create your views here.

def index(request):
    form=SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data=form.save()
            searchresult(data)
            return redirect('home:result data.id')

    context={
        'form':form
    }
    return render(request, 'home/index.html', context)

def result(request, pk):
    pass

def searchresult(request,data):
    count, weblist=gsearch(query=data.keyword, pause=data.pause)
    context={
        'total':count,
        'websites':weblist
    }
    print(count, weblist)
    return render(request, 'home/result.html', context)