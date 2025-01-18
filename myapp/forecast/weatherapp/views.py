from django.shortcuts import render
import requests #  library used to make HTTP requests
import datetime #  helps us work with dates
from django import messages

# Create your views here.


def home (request):
    # If the user has sent a city in the form, use that city. Otherwise, default to 'Mombasa'.
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Mombasa'
        # Replace 'Mombasa' with the dynamic city value in the URL
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2933b7b19ca8a87bdb67e21a091ffd5b' 
    
    #additional parameters we send to the API, e.g., units in Celsius
    PARAMS = {'units':'metric'}
    
    try:
        ## Use the 'requests' library to fetch data from the OpenWeather API
        data = requests.get(url,PARAMS).json() #method to make HTTP requests
    
    #Extract necessary information from the JSON response
        description = data['weather'][0]['description'] # Weather description (e.g., clear sky)
        icon = data['weather'][0]['icon']# Weather icon code
        temp = data['main']['temp'] # Current temperature in Celsius
    
    #get today's date 
        day = datetime.date.today()
    
    #render the template with data
        return render(request,'weatherapp/home.html',{
        'description':'clear sky','icon':'01d' ,'temp':25,'day':day,'city':'Mombasa','exception_occured':False})
    except:
        exception_occured=True
        messages.error(request,'Entered info is not available to API')
        day=datetime.date.today()
        
        return render(request,'weatherapp/home.html',{
        'description':'clear sky','icon':'01d' ,'temp':25,'day':day,'city':'Mombasa','exception_occured':False,})
    
    