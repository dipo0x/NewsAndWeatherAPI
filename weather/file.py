from rest_framework.decorators import api_view
from rest_framework.response import Response
import pyowm
from .serializers import WeatherSerializer, NewsSerializer
from .models import Weather, News
from django.http import HttpResponse
from newsapi import NewsApiClient
#EVERYTHING WEATHER API
api_key = "4401b62bcf88000c711e2c769205c9bf"
owm_obj=pyowm.OWM(api_key)

#EVERYTHING NEWS API
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key='82f24d96198e42cc80de0c7a53d1e9ae')

# Create your views here.
@api_view(['GET', "POST"])
def home(request):
    if request.method == "POST":
        serializer = WeatherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            for x in Weather.objects.all().order_by('-date_added')[:1]:
                place = str(x)        
            mgr = owm_obj.weather_manager()
            x=mgr.weather_at_place(str(place))
            Data=x.weather
            temp = Data.temperature(unit='celsius')
            city = (place)
            obs = mgr.weather_at_place(city)
            w = obs.weather
            k = w.status
            x = w.temperature(unit='celsius')
            av = temp['temp']
            mi = temp['temp_min']

            responseData = {
                "weather": k,
                "temperature": x,
                "max_temp": x,
                "min_temp": mi
            }
            return Response(responseData)
        else:
            return HttpResponse("error")
    else:
        location = Weather.objects.all().order_by('-date_added')[:1]
        serializer = WeatherSerializer(location, many=True)
        return Response(serializer.data)

@api_view(['GET', "POST"])
def news(request):
    if request.method == "POST":
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            for x in News.objects.all().order_by('-date_added')[:1]:
                query = str(x)        

            all_articles = newsapi.get_everything(
            q=query,
            language='en',   
            ) 
            for article in all_articles['articles']:
                s = 'Source : ',article['source']['name']
                t= 'Title : ',article['title']
                d = 'Description : ',article['description']

            responseData = {
                "Source": s,
                "Title": t,
                "Description": d
            }
            return Response(responseData)
        else:
            return HttpResponse("error")
    else:
        query = News.objects.all().order_by('-date_added')[:1]
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)