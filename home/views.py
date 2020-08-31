from django.shortcuts import render, redirect
from .forms import SearchForm
from .models import SearchResult, SearchHistory
from .private.gsearch import gsearch
# Create your views here.

lala=list()

def index(request):
    form=SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data=form.save()
            searchresult(request,data)
            return redirect('home:result data.id')

    context={
        'form':form
    }
    return render(request, 'home/index.html', context)

def result(request, pk):
    history=SearchHistory.objects.get(id=pk)
    result=SearchResult.objects.get(searchhistory=history)
    context = {
        'total': result.totalwebsites,
        'websites': lala
    }
    return render(request, 'home/result.html', context)

def searchresult(request,data):
    count, lala=gsearch(query=data.keyword, pause=data.pause)
    SearchResult.objects.create(
        searchhistory=data,
        totalwebsites=count, 
        websiterank=1
    )
