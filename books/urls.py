from django.urls import path
from django.urls.resolvers import URLPattern
from .views import BookListView

urlpatterns = [
    path('', BookListView.as_view(), name='home'),
]