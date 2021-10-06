import datetime as dt
from django.http.response import Http404
from django.shortcuts import redirect, render, get_object_or_404

from news.models import Article, Editor

# Create your views here.

def convert_dates(dates):
    days_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    day = days[days_number]
    return day

def article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "news/article.html", {"article": article})

def news_of_day(request):
    date = dt.datetime.now()
    news = Article.days_news(date)
    editors = Editor.objects.get(pk=3)
    return render(request, 'news/today-news.html', {"date": date, "news": news, "editor":editors})

def past_days_news(request, past_date):
    try:
        date = dt.datetime.strptime (past_date, '%Y-%m-%d').date()
    except ValueError:
        raise Http404()
    
    if date == dt.date.today():
        return redirect('news')
    
    news = Article.days_news(date)
    return render(request, 'news/past-news.html', {"date": date, "news": news})

def search_results(request):
    if 'article' in request.GET and request.GET['article']:
        search_term = request.GET.get('article')
        searched_article = Article.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'news/search.html', {"message": message, "articles": searched_article})
    
    else:
        message = "You havent searched for any term"
        return render(request, 'news/search.html', {"message": message})