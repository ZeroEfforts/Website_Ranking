import json
from django.shortcuts import render, redirect
from .forms import SearchForm
from .models import SearchResult, SearchHistory
from .gsearch import gsearch
# Create your views here.


def index(request):
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.save()
            result, weblist = searchresult(request, data)
            return redirect('home:result', pk=result.id, websites=weblist)

    context = {
        'form': form
    }
    return render(request, 'home/index.html', context)


def result(request, pk, websites):
    result = SearchResult.objects.get(id=pk)
    context = {
        'total': result.totalwebsites,
        'websites': websites
    }
    print(websites)
    return render(request, 'home/result.html', context)


def searchresult(request, data):
    results = gsearch(query_=data.keyword, pause_=data.pause)
    try:
        return(
            SearchResult.objects.create(
                searchhistory=data,
                totalwebsites=len(results),
                websiterank=1
            ),
            results
        )
    except Exception as err:
        return err
