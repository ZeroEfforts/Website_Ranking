from django.contrib import admin
from .models import SearchHistory, SearchResult
# Register your models here.

admin.site.register(SearchHistory)
admin.site.register(SearchResult)
