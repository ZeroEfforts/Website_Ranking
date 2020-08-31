from django.shortcuts import render, redirect
from .forms import SearchForm
from .models import SearchResult, SearchHistory
from .gsearch import gsearch
# Create your views here.

globalres=list()


def index(request):
    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            data = form.save()
            result = searchresult(request, data)
            print(result)
            return redirect('home:result result.id')

    context = {
        'form': form
    }
    return render(request, 'home/index.html', context)


def result(request, pk):
    result = SearchResult.objects.get(id=pk)
    context = {
        'total': result.totalwebsites,
        'websites': globalres
    }
    return render(request, 'home/result.html', context)


def searchresult(request, data):
    results = gsearch(query=data.keyword, pause=data.pause)
    globalres=results
    try:
        return SearchResult.objects.create(
            searchhistory=data,
            totalwebsites=len(results),
            websiterank=1
        )
    except Exception as err:
        return err
