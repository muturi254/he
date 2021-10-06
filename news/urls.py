from django.urls import path

from news import views
# urlpatterns 
urlpatterns = [
    path('', views.news_of_day, name='index'),
    path('archives/<past_date>/', views.past_days_news, name='past'),
    path('search/', views.search_results, name='search_results'),
    path('article/<int:pk>/', views.article, name='article'),
]