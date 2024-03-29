from django.contrib.syndication.views import Feed

from .models import Post

class ALLPostsRssFeed(Feed):
    title = "django教程演示"

    link = "/"

    description='Django 博客测试文章'

    def items(self):
        return Post.objects.all()
    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)
    def item_description(self, item):
        return item.body