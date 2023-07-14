from django.urls import path
from .views import create_issue

urlpatterns = [
    path('', create_issue, name='create_issue'),
]
