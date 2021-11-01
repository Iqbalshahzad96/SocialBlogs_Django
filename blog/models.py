from django.db import models
from django.db.models.fields import TextField
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title=  models.CharField(max_length=200)
    text= TextField()
    create_date = models.DateTimeField(default=timezone.now)
    publish_date = models.DateTimeField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
    def publish(self):
        self.publish_date = timezone.now()
        self.save()

    def approve_comments(self):
        #'approved' should be same to 'approved' field in comments
        return self.comments.filter(approved = True)

    def get_absolute_url(self):
        return reverse ('post_detail', kwargs={'pk':self.pk})

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author=  models.CharField(max_length=200)
    text= TextField()
    create_date = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.text

    def approve(self):
        self.approved = True
        self.save()

    def get_absolute_url(self):
        return reverse ('post_list')
