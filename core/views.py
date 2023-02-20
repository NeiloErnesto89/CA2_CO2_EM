from django.shortcuts import render
import json
from core.api_services.services import ApiConnector, ApiResponse, Emissions
## from django.core.Services.services import ApiResponse, ApiConnector, Emissions

def home(request):
    return render(request, 'core/index.html')


def q1(request):
    
    
    #flight_number = i['flight_number']
    #result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
    #print(type(result))
    #emissions = Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i["dep_icao"]), ApiResponse().get_airport_cordinates(i["arr_icao"]))



    temp_file = {'flight_number': flight_number, 'distance': result, 'co2_emissions': emissions}

    with open('sample.json', 'a') as f:
        json.dump(temp_file, f)
    

    #f = open('core/api_services/test.json')
    
    with open('core/api_services/test.json') as json_file:
        data = json.load(json_file)
    
    
    #data = json.load(f)
    flights = {}
    
    
    
    return render(request, 'core/q1.html', context = data)




def q2(request):
    return render(request, 'core/q2.html')

def q3(request):
    return render(request, 'core/q3.html')

def q4(request):
    return render(request, 'core/q4.html')

def q5(request):
    return render(request, 'core/q5.html')

def q6(request):
    return render(request, 'core/q6.html')

def q7(request):
    return render(request, 'core/q7.html')