import math #Math library for calculations incl. Pi, sqrt etc
#import requests

# The URL for the API endpoint
#url = ""

# Make the API request
#response = requests.get(url)

# Check if the API request was successful
#if response.status_code == 200:
    # Process the API response data
    #data = response.json()
   
#else:
    # Handle the error
    #print("Request failed with status code:", response.status_code)

def distance(startlat, startlong, destlat, destlong):
    
    #Convert to radians
    startlat = math.radians(startlat)
    startlong = math.radians(startlong)
    destlat = math.radians(destlat)
    destlong = math.radians(destlong)
    
    #Calculate difference between the two latitudes and longitudes
    latitude_diff = startlong - startlat
    longitude_diff = destlong - destlat
    
    #Haversine formula Earths Circumference 
    a = math.sin(latitude_diff/2)**2 + math.cos(startlat) * math.cos(destlat) * math.sin(longitude_diff/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    distance = 6371 * c  # 6371 is the radius of the Earth in km
    
    return distance #return calculation

def calculate_emissions(distance, engine_size):
    Co2 = engine_size * distance * 0.001  #Co2 is .001 per kg
    return Co2 #return calculation

#User enters latitude longitude and engine capacity in litres
start_latitude = float(input("Enter start latitude --> Airport: "))
start_longitude = float(input("Enter start longitude --> Airport: "))
end_latitude = float(input("Enter latitude of destination : "))
end_longitude = float(input("Enter longitude destination: "))
engine_size = float(input("Enter Aircraft engine size: "))

distance_km = distance(start_latitude, start_longitude, end_latitude, end_longitude)
Co2_kg = calculate_emissions(distance_km, engine_size)

#Print the GPS distance in Km and Co2 emmsions
print("Distance: {:.2f} km".format(distance_km))
print("CO2 emissions: {:.2f} kg".format(Co2_kg))


