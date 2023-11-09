from django.db import models





class user(models.Model):
    username=models.CharField(max_length=1000)
    email=models.EmailField()
    password=models.CharField(max_length=1000)

    
# Create your models here.
class user_blogs(models.Model):
    blog_title=models.CharField(max_length=1000)
    blog_content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)


