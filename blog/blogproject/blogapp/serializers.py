from blogapp.models import  user_blogs
from  rest_framework import serializers


class blogserializer(serializers.ModelSerializer):
    class Meta:
        model= user_blogs
        fields="__all__"