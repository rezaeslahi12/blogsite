from django.db import models

from django.utils.translation import gettext as _
import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class test(models.Model):
    name = models.CharField(max_length=30)
    
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='authors/', default='authors/default.png')
    biography = models.TextField()

    def __str__(self):
        return self.user.username
# CATEGORY_CHOICES = (
#     ('sport', _('ورزشی')),
#     ('politics', _('سیاسی')),
#     ('economy', _('اقتصادی')),
#     ('entertainment', _('سرگرمی')),
#     ('technology', _('تکنولوژی')),
#     ('health', _('سلامتی')),
#     ('education', _('آموزش')),
#     ('lifestyle', _('زندگی‌نامه')),
#     ('travel', _('مسافرت')),
#     ('food', _('غذا')),
#     ('other', _('غیره')),
# )


class Category(models.Model):
    title = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.title


class Post(models.Model):
    maincategory = models.ForeignKey(Category,on_delete=models.CASCADE,null=True,blank=True)    
    content = models.TextField()
    image=models.ImageField(upload_to='%Y/%m/%d',null=True,blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(default=timezone.now)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200)
    likes = models.ManyToManyField(User, related_name='blogpost_like' , blank=True)

    def number_of_likes(self):
        return self.likes.count()
    
    def __str__(self):
        return self.title
    
    
    
    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField()
    
    def __str__(self):
        return self.text


class Page(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title










