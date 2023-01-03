from django.shortcuts import render
import requests
import datetime


def home(request):
    city = request.POST.get('city', 'moulvibazar')
    if city is "":
        url = f"http://api.openweathermap.org/data/2.5/weather?q=moulvibazar&appid=1f77aaadc276c1bcc350c60b812f1447"
    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=1f77aaadc276c1bcc350c60b812f1447"
    data = requests.get(url).json()

    minutes = 0
    hours = 6

    current_time = datetime.datetime.now()

    hours_added = datetime.timedelta(hours=hours, minutes=minutes)

    future_time = current_time + hours_added
    payload = {
        'name': data['name'],
        'weather': data['weather'][0]['main'],
        'description': data['weather'][0]['description'],
        'country': data['sys']['country'],
        'icon': data['weather'][0]['icon'],
        'kel_temperature': int(((data['main']['temp']) - 273) * 9/5 + 32),
        'cel_temperature': int(data['main']['temp']) - 273,
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
        'wind': data['wind']['speed'],
        't': future_time
    }

    context = {'data': payload}
    # print(context)
    return render(request, 'homewea.html', context)
