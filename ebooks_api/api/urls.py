from django.urls import path
from . import views

urlpatterns = [
    path('ebooks/', views.EbookListCreateAPiView.as_view(), name='ebooks-list'),
    path('ebooks/<int:pk>/', views.EbookDetailAPiView.as_view(), name='ebooks-detail'),
    path('ebooks/<int:ebook_pk>/reviews',
         views.ReviewCreateAPiVeiw.as_view(), name='review-list'),
    path('review/<int:pk>/', views.ReviewDetailAPiView.as_view(),
         name='review-detail'),
]
