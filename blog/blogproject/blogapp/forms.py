from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms 
from blogapp.models import user_blogs
class CreateblogForm(forms.ModelForm):
    class Meta:
        model= user_blogs
        fields=['blog_title', 'blog_content']