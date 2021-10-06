from django.test import TestCase
import datetime as dt

from news.models import Editor, Tag, Article

# Create your tests here.
class EditorTestClass(TestCase):

    def setUp(self):
        self.peter = Editor(first_name = "peter", last_name="muturi", email="petermuturi@moringaschool.om")

    def test_instance(self):
        self.assertTrue(isinstance(self.peter, Editor))

    def test_save_method(self):
        james = Editor(first_name = "james", last_name="muiruri", email="jamesmuiruri@moringaschool.om")
        self.peter.save_editor() 
        james.save_editor()
        self.assertEqual(2, Editor.objects.count())

class ArticleTestClass(TestCase):
    def setUp(self):
        self.james = Editor(first_name="james", last_name="muriuki", email="james@moringaschool.com")
        self.james.save_editor()

        self.new_tag = Tag(name="testing")
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        Tag.objects.all().delete()
        Article.objects.all().delete()

    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news) > 0)

    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)