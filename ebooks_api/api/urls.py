from django.urls import path
from . import views

urlpatterns = [
    path('ebooks/', views.EbookListCreateAPiView.as_view(), name='ebooks-list'),
]
