from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time=models.DateTimeField()
    modified_time=models.DateTimeField()
    excerpt = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)
    ###返回string
    def __str__(self):
        return self.title
    ### url
    def get_absolute_url(self):
        return reverse('blog1:detail', kwargs={'pk': self.pk})
    ###访问量计算
    def increase_views(self):
        self.views +=1
        self.save(update_fields=['views'])
    ###自动生成摘要
    def save(self, *args, **kwargs):
        if not self.excerpt:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            self.excerpt= strip_tags(md.convert(self.body))[:54]
        super(Post,self).save(*args, **kwargs)
    class Meta:
        ordering = ['-created_time']




