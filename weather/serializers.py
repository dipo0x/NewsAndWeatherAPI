from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Weather, News

class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Weather
        fields = ['location']

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['news']