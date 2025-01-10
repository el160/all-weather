from django.shortcuts import render

import datetime

# Create your views here.


def home (request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Mombasa'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={'Mombasa'}&appid=2933b7b19ca8a87bdb67e21a091ffd5b' 
    PARAMS = {'units':'metric'}
    
    data = request.get(url,PARAMS).json() 
    
    description = data['weather'][0]['description'] 
    icon = data['weather'][0]['icon'] 
    temp = data['main']['temp']
    
    day = datetime.date.today()
    
    
    return render(request,'weatherapp/home.html',{'desription':description,'icon':temp,'day':day})
    