from django.db import models

class Weather(models.Model):
    location = models.TextField(blank=True, default='')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location

class News(models.Model):
    news = models.TextField(blank=True, default='')
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.news