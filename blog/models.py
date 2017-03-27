from django.db import models


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', default=1)
    title = models.CharField(null=False, blank=False, max_length=256)
    content = models.TextField(null=False, blank=False, max_length=2048)
    uploaded_date = models.DateTimeField(auto_created=True, auto_now=True)

    class Meta:
        db_table = 'api_post'

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.ForeignKey('auth.User', default=1)
    content = models.CharField(null=False, blank=False, max_length=256)
    uploaded_date = models.DateTimeField(auto_created=True, auto_now=True)

    class Meta:
        db_table = 'api_comment'

    def __str__(self):
        return self.text