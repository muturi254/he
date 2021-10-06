from django.db import models
import datetime as dt

# Create your models here.
class Editor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)
    article_image = models.ImageField(upload_to='articles/')

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=60)
    post = models.TextField()
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date=today)
        return news
    
    @classmethod
    def days_news(cls, date):
        news = cls.objects.filter(pub_date__date=date)
        return news

    @classmethod
    def search_by_title(cls, term):
        news = cls.objects.filter(title__icontains=term)
        return news