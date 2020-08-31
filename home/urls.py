from django.urls import path
from .views import index, result

app_name = 'home'
urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/result', result, name="result"),
]
