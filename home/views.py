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
            result = searchresult(request, data)
            return redirect('home:result', pk=result.id)

    context = {
        'form': form
    }
    return render(request, 'home/index.html', context)


def result(request, pk):
    result = SearchResult.objects.get(id=pk)
    with open(".temp", "r") as fp:
        websites = json.load(fp)

    indices = [i for i, s in enumerate(websites) if result.searchhistory.website in s]

    context = {
        'total': result.totalwebsites,
        'websites': websites,
        'rank':indices[0]
    }
    print(websites)
    return render(request, 'home/result.html', context)


def searchresult(request, data):
    results = gsearch(query_=data.keyword, pause_=data.pause)
    with open(".temp", "w") as fp:
        json.dump(results, fp)
    try:
        return SearchResult.objects.create(
            searchhistory=data,
            totalwebsites=len(results),
            websiterank=1
        )

    except Exception as err:
        return err
