"""
    This is the main file of the program. It contains the main function and the author which is
    github.com/bloobsky
"""
import requests
import json
import pprint as pprint
import haversine as hs
import keys as keys
import numpy as np
import tkinter as tk
import customtkinter
import time
import pandas as pd

"""
Constants for faster calculations
"""
CW = 2.40 
EF = 3.15
M = 2
P = 0.54
AF = 0.00038
AFM = 11.68

"""
Main GUI Class
"""
class MainGUI(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x500")
        self.title("Flight Pollution Calculator")
        self.minsize(600, 500)
        
        photo = tk.PhotoImage(file = 'icon.png')
        self.wm_iconphoto(False, photo)
        
        # Grid
        self.grid_rowconfigure((0,1,2,3,4), weight=1)
        self.grid_rowconfigure(5, weight=3)
        self.grid_columnconfigure((0,1,2,3), weight=1)

        """
        Main Menu Callback
        """
        def main_menu_callback(choice):
            if choice == "Check estimated emissions of all of the scheduled flights":
                self.sub1_menu.configure(state="disabled")
                self.sub1_menu.configure(values=["disabled"])
                self.entry1.configure(state="disabled")
                self.textbox1.delete(1.0,tk.END)
                self.textbox1.insert("end", 'Please observe Console, as the calculation is too big for GUI to display!' + '\n\n')
                self.textbox1.insert("end", 'WARNING: Will take several minutes to finish!' + '\n\n')
                self.textbox1.insert("end", 'Click Start when ready!' + '\n')
                
            if choice == "List all Airports":
                self.entry1.configure(placeholder_text="Disabled")
                self.entry1.configure(state="disabled")
                self.sub1_menu.configure(state="disabled")
                self.sub1_menu.configure(values=["disabled"])
                self.textbox1.delete(1.0,tk.END)
                self.textbox1.insert("end", 'Click "Start" when ready!' + '\n')
                
            if choice == "List all Airlines":
                self.entry1.configure(placeholder_text="Disabled")
                self.entry1.configure(state="disabled")
                self.sub1_menu.configure(state="disabled")
                self.sub1_menu.configure(values=["disabled"])
                self.textbox1.delete(1.0,tk.END)
                self.textbox1.insert("end", 'Click "Start" when ready!' + '\n')
                
                
            if choice == "Check estimated CO2 emissions over the last five years":
                self.entry1.configure(state="disabled")
                self.textbox1.delete(1.0,tk.END)
                self.textbox1.insert("end", 'Please select the Context' + '\n')
                self.sub1_menu_var = customtkinter.StringVar(value="Please select an option")
                self.sub1_menu.configure(state="enabled")
                self.sub1_menu.configure(values=["Last five years by Region", "Last five years by Year & Region", "Last five years by Year, Month & Region"])
                
            if choice == "Top twenty most polluting routes globally, regionally or by country":
                self.entry1.configure(state = "normal")
                self.textbox1.delete(1.0,tk.END)
                self.textbox1.insert("end", 'Note: Due to API limitations, we require to filter by Airport Routes' + '\n\n')
                self.textbox1.insert("end", 'Note: Please observe the Console for result!' + '\n\n')
                self.textbox1.insert("end", 'WARNING: Will take several minutes to finish!' + '\n\n')
                self.textbox1.insert("end", 'Paramenters Required:' + '\n')
                self.textbox1.insert("end", '     Airport ICAO code (four letters, ex. EIDW for Dublin):' + '\n')
                self.sub1_menu.configure(state="disabled")
                self.entry1.configure(state = "normal")
                self.entry2.configure(state="disabled")
            
            if choice == "The total CO2 Emissions by each Airline?":
                textvariable = "Disabled"
                self.entry1.configure(placeholder_text="Disabled")
                self.entry1.configure(state = "disabled" )
                self.textbox1.delete(1.0,tk.END)
                self.textbox1.insert("end", 'Please observe Console, as the calculation is too big for GUI to display!' + '\n\n')
                self.textbox1.insert("end", 'WARNING: Will take several minutes to finish!' + '\n\n')
                self.textbox1.insert("end", 'Click Start when ready!' + '\n')
            
            if choice == "Estimated CO2 emissions by airport?":
                textvariable = "Disabled"
                self.entry1.configure(state="disabled")
                self.sub1_menu_var = customtkinter.StringVar(value="Please select an option")
                self.sub1_menu.configure(state="enabled")
                self.sub1_menu.configure(values=["Co2 emissions by Departure", "Co2 emissions by Arrival"])
                self.textbox1.insert("end", 'Please select the context' + '\n')
            
            if choice == "Top twenty countries responsible for aviation CO2 emissions":
                textvariable = "Disabled"
                self.entry1.configure(state="disabled")
                self.entry1.configure(textvariable=textvariable)
                self.sub1_menu_var = customtkinter.StringVar(value="Please select an option")
                self.sub1_menu.configure(state="enabled")
                self.sub1_menu.configure(values=["Top twenty by domestic flights", "Top twenty by international flights", "Domestic and international flights combined", "Top twenty by country of aircraft registration"])
            
            if choice == "Top twenty aircraft types responsible for the most CO2 emissions":
                self.sub1_menu.configure(state="disabled")
        
        """
        Sub-Menu Callback
        """
        def sub1_menu_callback(choice):

            if choice == "Last five years by Region":
                self.sub1_menu_var.set("Last five years by Region")
                self.entry1.configure(placeholder_text = "Region")
                self.entry1.configure(state = "normal")
                self.textbox1.delete(1.0,tk.END)
                self.textbox1.insert("end", 'Note: Please observe the Console for result!' + '\n\n')
                self.textbox1.insert("end", 'Paramenters Required:' + '\n')
                self.textbox1.insert("end", '     Region Code (three letters) into the first parameter box:' + '\n')
                
            if choice == "Last five years by Year & Region":
                self.sub1_menu_var.set("Last five years by Year & Region")
                self.entry1.configure(placeholder_text = "Year")
                self.entry2.configure(placeholder_text = "Region")
                self.entry1.configure(state = "normal")
                self.entry2.configure(state = "normal")
                self.textbox1.delete(1.0,tk.END)
                self.textbox1.insert("end", 'Note: Please observe the Console for result!' + '\n\n')
                self.textbox1.insert("end", 'Paramenters Required:' + '\n')
                self.textbox1.insert("end", '     Year into the first parameter box:' + '\n')
                self.textbox1.insert("end", '     Region Code (three letters) into the second parameter box:' + '\n')
            
            if choice == "Last five years by Year, Month & Region":
                self.sub1_menu_var.set("Last five years by Year, Month & Region")
                self.entry1.configure(placeholder_text = "Year")
                self.entry2.configure(placeholder_text = "Month")
                self.entry1.configure(state = "normal")
                self.entry2.configure(state = "normal")
                self.textbox1.delete(1.0,tk.END)
                self.textbox1.insert("end", 'Note: Please observe the Console for result!' + '\n\n')
                self.textbox1.insert("end", 'Paramenters Required:' + '\n')
                self.textbox1.insert("end", '     Month & Year (ex. Dec-20) into the second parameter box:' + '\n')
                self.textbox1.insert("end", '     Region Code (three letters) into the third parameter box:' + '\n')
                
            if choice == "Top most polluting routes by Region":
                self.sub1_menu_var.set("Top most polluting routes by Region")
                self.entry1.configure(state = "normal")
                self.textbox1.delete(1.0,tk.END)
                self.textbox1.insert("end", 'Note: Please observe the Console for result!' + '\n\n')
                self.textbox1.insert("end", 'Paramenters Required:' + '\n')
                self.textbox1.insert("end", '     Region Prefix Code (single letter, ex. E for Northern Europe):' + '\n')
            
            if choice == "Top most polluting routes by Country":
                self.sub1_menu_var.set("Top most polluting routes by Country")
                self.entry1.configure(state = "normal")
                self.textbox1.delete(1.0,tk.END)
                self.textbox1.insert("end", 'Note: Please observe the Console for result!' + '\n\n')
                self.textbox1.insert("end", 'Paramenters Required:' + '\n')
                self.textbox1.insert("end", '     Country Prefix Code (two letters, ex. LS for Switzerland):' + '\n')
            
            if choice == "Co2 emissions by Departure":
                self.sub1_menu_var.set("Co2 emissions by Departure")
                self.entry1.configure(state = "normal")
                self.textbox1.delete(1.0,tk.END)
                self.textbox1.insert("end", 'Note: Please observe the Console for result!' + '\n\n')
                self.textbox1.insert("end", 'Paramenters Required:' + '\n')
                self.textbox1.insert("end", '     Airport Code (ex EIDW for Dublin:' + '\n')
            
            if choice == "Co2 emissions by Arrival":
                self.sub1_menu_var.set("Co2 emissions by Arrival")
                self.entry1.configure(state = "normal")
                self.textbox1.delete(1.0,tk.END)
                self.textbox1.insert("end", 'Note: Please observe the Console for result!' + '\n\n')
                self.textbox1.insert("end", 'Paramenters Required:' + '\n')
                self.textbox1.insert("end", '     Airport Code (ex EIDW for Dublin):' + '\n')
                
            if choice == "Top twenty by domestic flights":
                self.sub1_menu_var.set("Top twenty by domestic flights")
                self.textbox1.delete(1.0,tk.END)
                self.textbox1.insert("end", 'Note: Please observe the Console for result!' + '\n\n')
            
            if choice == "Top twenty by international flights":
                self.sub1_menu_var.set("Top twenty by international flights")
                self.textbox1.delete(1.0,tk.END)
                self.textbox1.insert("end", 'Note: Please observe the Console for result!' + '\n\n')
            
            if choice == "Domestic and international flights combined":
                self.sub1_menu_var.set("Domestic and international flights combined")
                self.textbox1.delete(1.0,tk.END)
                self.textbox1.insert("end", 'Note: Please observe the Console for result!' + '\n\n')
            
            if choice == "Top twenty by country of aircraft registration":
                self.sub1_menu_var.set("Top twenty by country of aircraft registration")
                self.textbox1.delete(1.0,tk.END)
                self.textbox1.insert("end", 'Note: Please observe the Console for result!' + '\n\n')


        """
        GUI Setup
        """
        self.label1 = customtkinter.CTkLabel(self, text="Flight Pollution Calculator")
        self.label1.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

        self.label1 = customtkinter.CTkLabel(self, text="Function:", anchor=tk.E)
        self.label1.grid(row=1, column=0, padx=5, pady=5)
        
        self.main_menu_var = customtkinter.StringVar(value="")
        self.main_menu = customtkinter.CTkOptionMenu(self, command=main_menu_callback, width=400, variable=self.main_menu_var, values=["List all Airports", "List all Airlines", "List all Countries", "Check estimated emissions of all of the scheduled flights","Check estimated CO2 emissions over the last five years", "Top twenty most polluting routes globally, regionally or by country", "The total CO2 Emissions by each Airline?","Estimated CO2 emissions by airport?","Top twenty countries responsible for aviation CO2 emissions","Top twenty aircraft types responsible for the most CO2 emissions"],)
        self.main_menu.grid(row=1, column=1, padx=5, pady=10, columnspan=3)
        self.main_menu.set("Please select an Option                                                                            ")
        
        self.label1 = customtkinter.CTkLabel(self, text="Context:", anchor=tk.E)
        self.label1.grid(row=2, column=0, padx=5, pady=5)
        
        self.sub1_menu_var = customtkinter.StringVar(value = "")
        self.sub1_menu = customtkinter.CTkOptionMenu(self, state="disabled", width=400, command=sub1_menu_callback, variable=self.sub1_menu_var, values=[""])
        self.sub1_menu.grid(row=2, column=1, padx=5, pady=10, columnspan=3)
        self.sub1_menu.set("Please select an Option                                                                            ")     
        
        self.label1 = customtkinter.CTkLabel(self, text="Parameters:")
        self.label1.grid(row=3, column=0, padx=5, pady=5)
        
        #self.entry1var = customtkinter.StringVar()
        self.entry1 = customtkinter.CTkEntry(self, state="disabled")
        self.entry1.grid(row=3, column=1, padx=5, pady=10)
        
        #self.entry2var = customtkinter.StringVar()
        self.entry2 = customtkinter.CTkEntry(self, state="disabled")
        self.entry2.grid(row=3, column=2, padx=5, pady=10)

        self.entry3 = customtkinter.CTkEntry(self, state="disabled")
        self.entry3.grid(row=3, column=3, padx=5, pady=10)
        
        self.button1 = customtkinter.CTkButton(self, command=self.button_start_click, text="Start")
        self.button1.grid(row=4, column=0, columnspan=4, padx=5, pady=10)
        
        self.textbox1var = customtkinter.StringVar(value='')
        self.textbox1 = customtkinter.CTkTextbox(master=self)
        self.textbox1.grid(row=5, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")


    """
    Main Button Click
    """
    def button_start_click(self):
        main_menu_choice = self.main_menu_var.get() 
        sub_menu_choice = self.sub1_menu_var.get()
                
        if main_menu_choice == "Check estimated emissions of all of the scheduled flights":
            self.textbox1.insert("end", 'Starting!' + '\n')
            ApiResponse().list_all_flights(self)
        elif main_menu_choice == "Top twenty most polluting routes globally, regionally or by country":
            route = self.entry1.get()
            self.textbox1.insert("end", 'Starting!' + '\n')
            self.textbox1.insert("end", 'Getting data from Airlabs API...' + '\n')
            try:
                ApiConnector('airlabs', 'routes').save_routes(route)
                self.textbox1.insert("end", 'Calculating...' + '\n')
                ApiResponse().list_top_polluted_routes()
                self.textbox1.insert("end", 'Done!' + '\n')
            except:
                print('Unknown exception')
        elif main_menu_choice == "List all Airports":
            ApiResponse().list_all_airports(self)
        elif main_menu_choice == "List all Countries":
            ApiResponse().list_all_countries(self)
        elif main_menu_choice == "List all Airlines":
            ApiResponse().list_all_airlines(self)
        elif main_menu_choice == "The total CO2 Emissions by each Airline?":
            self.textbox1.insert("end", 'Calculating...' + '\n')
            ApiResponse().list_all_flights_by_airline(self)
            self.textbox1.insert("end", 'Done!' + '\n')
        elif main_menu_choice == "Top twenty aircraft types responsible for the most CO2 emissions":
            self.textbox1.insert("end", 'Calculating...' + '\n')
            ApiResponse().list_flights_by_aircraft_type()
            self.textbox1.insert("end", 'Done!' + '\n')
        
        if sub_menu_choice == "Last five years by Region":
            region = self.entry1.get()
            get_co2_by_region(region)
        if sub_menu_choice == "Last five years by Year & Region":
            year = self.entry1.get()
            region = self.entry2.get()
            get_time_and_region(region, year)
        if sub_menu_choice == "Last five years by Year, Month & Region":
            month_year = self.entry1.get()
            region = self.entry2.get()
            get_month_year_region(region, month_year)
            
        if sub_menu_choice == "Top most polluting routes Globally":
            pass
        if sub_menu_choice == "Top most polluting routes by Region":
            region = self.entry1.get()
        if sub_menu_choice == "Top most polluting routes by Country":
            country = self.entry1.get()
        
        if sub_menu_choice == "Co2 emissions by Departure":
            self.textbox1.insert("end", 'Calculating...' + '\n')
            dep_airport = self.entry1.get()
            try:
                ApiResponse().list_flights_with_departure_airport(dep_airport)
                self.textbox1.insert("end", 'Done!' + '\n')
            except:
                self.textbox1.insert("end", 'Invalid Parameter entered or API error!' + '\n')
        if sub_menu_choice == "Co2 emissions by Arrival":
            self.textbox1.insert("end", 'Calculating...' + '\n')
            arr_airport = self.entry1.get()
            ApiResponse().list_flights_with_arrival_airport(arr_airport)
            self.textbox1.insert("end", 'Done!' + '\n')
            
        if sub_menu_choice == "Top twenty by domestic flights":
            self.textbox1.insert("end", 'Calculating...' + '\n')
            ApiResponse().list_domestic_flights_by_countries()
            self.textbox1.insert("end", 'Done!' + '\n')
        if sub_menu_choice == "Top twenty by international flights":
            self.textbox1.insert("end", 'Calculating...' + '\n')
            ApiResponse().list_international_flights_by_countries()
            self.textbox1.insert("end", 'Done!' + '\n')
        if sub_menu_choice == "Domestic and international flights combined":
            self.textbox1.insert("end", 'Calculating...' + '\n')
            ApiResponse().list_flights_by_country()
            self.textbox1.insert("end", 'Done!' + '\n')
        if sub_menu_choice == "Top twenty by country of aircraft registration":
            self.textbox1.insert("end", 'Calculating...' + '\n')
            ApiResponse().list_all_flights_by_registration_country()
            self.textbox1.insert("end", 'Done!' + '\n')


root = MainGUI()


def is_long_haul(flight_distance):
    if (flight_distance < 1500):
        return False
    else:
        return True 


"""
Historical Data from Stats file
"""
df = pd.read_csv('Aviation_Co2.csv', low_memory=False)
df
#Data to retrieve
df_new = df[['LOCATION', 'Value', 'TIME', 'Time', 'Source of emissions']]
#Get Co2 by region
def get_co2_by_region(region_name):
    #self.root = root
    result = df_new.loc[df_new['LOCATION'] == region_name]
    print(result['Value'].sum())

    #Get filter region and year
def get_time_and_region(region_name, year):
    data = df_new.loc[df_new['LOCATION'] == region_name]
    data2 = data.loc[data['TIME'] == year]
    print(data2['Value'].sum())

    #Filter location month and year
def get_month_year_region(region_name, year):
    data = df_new.loc[df_new['LOCATION'] == region_name]

    data2 = data.loc[data['Time'] == year] 
    print(data2['Value'].sum())
    
    #Print region Austrailia in 2020
    #get_time_and_region('AUS','2020')
    #Print region USA in December 2022
    #get_month_year_region('USA','Dec-22')


class Emissions:
        
    def calculate_co2_emissions(self, flight_distance):

   # The following formula is used to calculate the total CO2-equivalent emissions:
   # Formula derives from myclimate.org and they have all copyrights over it. 
   # https://www.myclimate.org/fileadmin/user_upload/myclimate_-_home/01_Information/01_About_myclimate/09_Calculation_principles/Documents/myclimate-flight-calculator-documentation_EN.pdf
   # 𝑬 = ()𝒂𝒙 𝟐 +𝒃𝒙 +𝒄 / 𝑺 ∗ 𝑷𝑳𝑭) ∗ (𝟏 −𝑪𝑭) ∗ 𝑪𝑾 ∗ (𝑬𝑭 ∗ 𝑴 + 𝑷)+ 𝐀𝐅 ∗ 𝐱 + �
   #E: CO2-eq emissions per passenger [kg]
   #x: Flight Distance [km] which is defined as the sum of GCD, the great circle distance, and DC, a distance
   #correction for detours and holding patterns, and inefficiencies in the air traffic control systems [km]
   #S: Average number of seats (total across all cabin classes)
   #PLF: Passenger load factor
   #CF: Cargo factor
   #CW: Cabin class weighting factor
   #EF: CO2 emission factor for jet fuel combustion (kerosene)
   #M: Multiplier accounting for potential non-CO2 effects
   #P: CO2e emission factor for preproduction jet fuel, kerosene
   #AF: Aircraft factor
   #A: Airport infrastructure emissions
   #The part ax
   #2 + bx + c is a nonlinear approximation of f(x) + LTO
   #LTO: Fuel consumption during landing and takeoff cycle including taxi [kg]
   #s = number_of_seats # Shorthaul -> 153.51 , Longhaul -> 280.21
   #plf = passenger_load_factor # Shorthaul -> 0.82 ,  Longhaul -> 0.82 
   #cf = cargo_factor # Shorthaul -> 0.93 ,  Longhaul -> 0.74 

        if (is_long_haul(flight_distance)):
            s = 280.21
            plf = 0.82
            cf = 0.74
            a_func = 0.0001
            b_func = 7.104
            c_func = 5044.93
        else:
            s = 153.51
            plf = 0.82
            cf = 0.93
            a_func = 0
            b_func = 2.714
            c_func = 1166.52

        x = flight_distance


        function_result = (a_func**2) + (b_func) + c_func # quadratic equations result
        rest_equation = (s * plf)  * (1 - cf) * CW * (EF * M + P) + (AF * x) + AFM
        result = function_result / rest_equation
        return round(result, 2)


    def calculate_distance(self, departure_lat_lng, arrival_lat_lng):
        # Calculate distance
        distance = hs.haversine(departure_lat_lng, arrival_lat_lng)
        #  print(f'Total distance is {round(distance, 2)} kilometeres, but full distance is {distance}')
        return round(distance, 2)
    
    def is_distance_long_or_short(self, distance):
        # Check if distance is long or short
        if(distance > 1500):
            print(f'That was a long-haul flight.')
        else:
            print(f'That was a short-haul flight.')


class ApiResponse():
    
    def __init__(self):
        self.flights_list = ApiConnector('airlabs', 'flights', 'dep_icao,arr_icao,flag,aircraft_icao,flight_number,airline_icao')
        self.countries_list = ApiConnector('airlabs', 'countries')
        self.airports_list = ApiConnector('airlabs', 'airports', 'icao_code,lat,lng')
        self.cities_list = ApiConnector('airlabs', 'cities')
        self.fleets_list = ApiConnector('airlabs', 'fleets')
        self.airlines_list = ApiConnector('airlabs', 'airlines')
        self.timezones_list = ApiConnector('airlabs', 'airlines')
        self.taxes_list = ApiConnector('airlabs', 'taxes')
        self.routes_list = ApiConnector('airlabs', 'routes')


    def list_international_flights_by_countries(self):
    #List international flights by countries
        temp = {}
        total_result = 0 
        result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                if 'flag' in i:
                    if (i['dep_icao'][:1]) != (i['arr_icao'][:1]):
                        result += Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                        temp[i['flag']] = temp.get(i['flag'], round(result, 2)) + round(result, 2)
                        print(temp)
                        total_result += result
                        print(f'Total consumption so far is {round(total_result, 2)} KG  per passenger ')
                        sorted_temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)[:20]
        print(sorted_temp)
    def list_domestic_flights_by_countries(self):
        #List domestic flights by countries
        temp = {}
        total_result = 0 
        result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                if 'flag' in i and (i['dep_icao'][:1] == i['dep_icao'][:1]):
                    result += Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                    temp[i['flag']] = temp.get(i['flag'], round(result, 2)) + round(result, 2)
                    print(temp)
                    total_result += result
                    print(f'Total consumption so far is {round(total_result, 2)} KG  per passenger ') 
                    sorted_temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)[:20]
        print(sorted_temp)
    def list_flights_by_country(self):
        #List all flights by registration country
        temp = {}
        total_result = 0 
        result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                if 'flag' in i:
                    result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                    temp[i['flag']] = temp.get(i['flag'], round(result, 2)) + round(result, 2)
                    print(temp)
                    total_result += result
                    #print(f'Total consumption so far is {round(total_result, 2)} KG  per passenger ')
                    sorted_temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)[:20]
        print(sorted_temp)
        
    def list_all_flights_by_registration_country(self):
        #List all flights
        temp = {}
        result = 0
        for i in self.flights_list.get_data_from_api():
            if(i.get('dep_icao') and i.get('arr_icao')):
                if 'flag' in i:
                    result += Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                    temp["Country registration " +i['flag']] = temp.get(i['flag'], round(result, 2)) + round(result, 2)
                    print(temp)
            top_20 = sorted(temp.items(), key=lambda x: x[1], reverse=True)[:20]
        print(top_20)

    def list_all_flights_by_airline(self, root):
        self.root = root
        temp = {}
        total_result = 0 
        result = 0
        flights = self.flights_list.get_data_from_api()
        for i in flights:
            if(i.get('dep_icao') and i.get('arr_icao')):
                if 'airline_icao' in i:
                    result += Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                    temp[i['airline_icao']] = temp.get(i['airline_icao'], round(result, 2)) + round(result, 2)
                    print(temp)
                    total_result += result
        sorted_temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
        #print(sorted_temp)
        
        for airline, emissions in sorted_temp:
            print('\n\n')
            print(f"{airline}: {emissions} kg CO2 emissions")
            #root.textbox1.insert("end", 'Airline ' + airline + ' with emission of ' + emissions + 'kg CO2' + '\n')

    
    def list_all_countries(self, root):
        self.root = root
        root.textbox1.insert("end", 'Listing all Countries...' + '\n')
        for i in self.countries_list.read_data_file():
            if(i.get('code3') and i.get('name')):
                root.textbox1.insert("end", 'Country Code ' + i["code3"] + ' is ' + i["name"] + '\n')
                #print(f'Country name is {i["name"]} and the country code is {i["code3"]}')
    
    def get_iata_code(self):
        # Get all iata codes
        for i in self.airlines_list.read_data_file():
            yield[i['iata_code']]

    def get_all_flights_country(self):
        # Get all flights by country
        for i in self.flights_list:
            try:
                print(i['flag'])
            except:
                pass
            
    def get_airport_name(self, airport_code):
        # Get airport name based on icao_code
        for i in self.airports_list.read_data_file():
            if (i.get('icao_code') == airport_code):
                return i['name']

    def get_all_arrival_airport(self):
        # Get arrival airport based on icao_code
        print("Arrival Lang Lat")
        for i in self.flights_list:
            for j in self.airports_list:
                try:
                    if(i['arr_icao'] == j['icao_code']):
                        print(j['lat'], j['lng'])
                except:
                    pass   
    
    def get_all_departure_airport(self):
        # Get all airports latitute and longtitude
        print("Departure Lang Lat")
        for i in self.flights_list:
            if(i.get('dep_icao') and i.get('arr_icao')):
                for j in self.airports_list: 
                        try:
                            if(i['dep_icao'] == j['icao_code']):
                                print(j['lat'], j['lng'])
                                break;
                        except:
                            pass
                
    def get_airport_cordinates(self, airport_name):
        # Get airport cordinates based on icao_code
        for i in self.airports_list.read_data_file():
            if(i.get('icao_code') == airport_name):               
                return i['lat'], i['lng']

    def list_all_airlines(self, root):
        self.root = root
        # List all airlines
        for i in self.airlines_list.get_data_from_api():
            try:
                root.textbox1.insert("end", 'Airline ' + i['icao_code'] + ' is ' + i['name'] + '\n')
                #print(f"Airline name is {i['name']} and ICAO CODE is {i['icao_code']}")
            except:
                pass
            
    def list_all_airports(self, root):
        # List all airports
        self.root = root
        root.textbox1.insert("end", 'Listing all Airports...' + '\n')
        for i in self.airports_list.read_data_file():
            if(i.get('icao_code') and i.get('name')):
                root.textbox1.insert("end", 'Airport Code ' + i["icao_code"] + ' is ' + i["name"] + '\n')
                #print(f'Airport name is {i["name"]} and the airport code is {i["icao_code"]} ')
        print("Done!")
        root.textbox1.insert("end", 'Done!' + '\n')

    
    def list_all_flights(self, root):
        # List all flights
        self.root = root
        flights = self.flights_list.get_data_from_api()
        total_result = 0
        flights_data = [(i.get('flight_number'), i.get('flag'), i.get('aircraft_icao'), i.get('dep_icao'), i.get('arr_icao')) for i in flights if i.get('dep_icao') and i.get('arr_icao')]
        for flight_data in flights_data:
            try:
                dep_cord = ApiResponse().get_airport_cordinates(flight_data[3])
                arr_cord = ApiResponse().get_airport_cordinates(flight_data[4])
                flight_distance = Emissions().calculate_distance(dep_cord, arr_cord)
                flight_emissions = Emissions().calculate_co2_emissions(flight_distance)
                print(f"Flight Number is {flight_data[0]} and the airline is {flight_data[1]} and the aircraft is {flight_data[2]} going from {flight_data[3]} to {flight_data[4]}")
                print(f"Flight distance is {flight_distance} km")
                print(f"Flight CO2 emissions is {flight_emissions} kg")
                total_result += flight_emissions
                print(f"Total consumption so far is {round(total_result, 2)} KG per passenger")
            except:
                pass
    
    def list_all_flights_2(self):
        #List all flights
        temp = {}
        total_result = 0 
        result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                if 'flag' in i:
                    result += Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                    temp[i['flag']] = temp.get(i['flag'], round(result, 2)) + round(result, 2)
                    print(temp)
                    total_result += result
                    #print(f'Total consumption so far is {round(total_result, 2)} KG  per passenger ')

    def list_flights_with_departure_airport(self, airport_icao):
        # List flights by departure airport
        total_result = 0
        for i in self.flights_list.get_data_from_api():
            if(i.get('dep_icao') == airport_icao):
                filter_long_short_haul = Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao']))
                print(Emissions().is_distance_long_or_short(filter_long_short_haul))
                result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                total_result += result
                print(f'Total consumption from {ApiResponse().get_airport_name(airport_icao)} so far is {round(total_result, 2)} kg ')


    def list_flights_with_arrival_airport(self, airport_icao):
        # List flights by arrival airport
        total_result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('arr_icao') == airport_icao):
                filter_long_short_haul = Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao']))
                print(Emissions().is_distance_long_or_short(filter_long_short_haul))
                result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                total_result += result
                print(f'Total consumption to {ApiResponse().get_airport_name(airport_icao)} so far is {round(total_result, 2)} kg ')

    
    def list_domestic_flights_by_region(self, region_letter):
        #List domestic flights by region (passing one or two letters)
        total_result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                if(i['dep_icao'].startswith(region_letter) == i['arr_icao'].startswith(region_letter)):
                        result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                        print(f'Flight CO2 emissions is {Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i["dep_icao"]),  ApiResponse().get_airport_cordinates(i["arr_icao"])))} kg');
                        total_result += result
                        print(f'Total consumption from {ApiResponse().get_airport_name(region_letter)} so far is {round(total_result, 2)} kg ')

    def list_international_flights_by_region(self, region_letter):
        #List international flights by region (passing one or two letters)
        total_result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                if(i['dep_icao'].startswith(region_letter) != i['arr_icao'].startswith(region_letter)):
                        print(f"Flight Number is {i['flight_number']} and the airline is {i['flag']} and the aircraft is {i['aircraft_icao']} going from {i['dep_icao']} to {i['arr_icao']}");
                        print(f'Flight distance is {Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i["dep_icao"]),  ApiResponse().get_airport_cordinates(i["arr_icao"]))} km');
                        result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                        print(f'Flight CO2 emissions is {Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i["dep_icao"]),  ApiResponse().get_airport_cordinates(i["arr_icao"])))} kg');
                        total_result += result
                        print(f'Total consumption from {ApiResponse().get_airport_name(region_letter)} so far is {round(total_result, 2)} kg ')
        
                
                
    def list_flights_by_region(self, region_letter, is_domestic):
        #List flights by region (passing one or two letters)
        total_result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                if(i['dep_icao'].startswith(region_letter) and i['arr_icao'].startswith(region_letter)):
                    filter_long_short_haul = Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao']))
                    if(is_domestic == True and filter_long_short_haul < 1500):
                        
                        print(Emissions().is_distance_long_or_short(filter_long_short_haul))
                        result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                        total_result += result
                        print(f'Total consumption from {region_letter} so far is {round(total_result, 2)} kg ')
                    elif(is_domestic == False and filter_long_short_haul > 1500):
                        print(f"Flight Number is {i['flight_number']} and the airline is {i['flag']} and the aircraft is {i['aircraft_icao']} going from {i['dep_icao']} to {i['arr_icao']}");
                        print(f'Flight distance is {Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i["dep_icao"]),  ApiResponse().get_airport_cordinates(i["arr_icao"]))} km');
                        print(Emissions().is_distance_long_or_short(filter_long_short_haul))
                        result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                        total_result += result
                        print(f'Total consumption from {region_letter} so far is {round(total_result, 2)} kg ')

    def list_flights_by_airline(self, airline):
        #List flights by airline (passing airline name)
        total_result = 0
        for i in self.flights_list.read_data_file():
            try:
                if(i['airline_icao'] == airline):
                        result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                        print(f'Flight CO2 emissions is {Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i["dep_icao"]),  ApiResponse().get_airport_cordinates(i["arr_icao"])))} kg');
                        total_result += result
                        print(f'Total consumption from {airline} so far is {round(total_result, 2)} kg ')
            except:
                pass

    def list_all_flights_by_countries(self):
        #List all flights by countries
        temp = {}
        total_result = 0 
        result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                if 'flag' in i:
                    result += Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                    temp[i['flag']] = temp.get(i['flag'], round(result, 2)) + round(result, 2)
                    print(temp)
                    total_result += result
                    #print(f'Total consumption so far is {round(total_result, 2)} KG  per passenger ')

    def list_shorthaul_flights_by_countries(self):
    #List all flights by countries
        temp = {}
        total_result = 0 
        result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                filter_long_short_haul = Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao']))
                if 'flag' in i and filter_long_short_haul < 1500:
                    result += Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                    temp[i['flag']] = temp.get(i['flag'], round(result, 2)) + round(result, 2)
                    print(temp)
                    total_result += result
                    #print(f'Total consumption so far is {round(total_result, 2)} KG  per passenger ')
                    
    def list_longhaul_flights_by_countries(self):
    #List all flights by countries
        temp = {}
        total_result = 0 
        result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                filter_long_short_haul = Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao']))
                if 'flag' in i and filter_long_short_haul > 1500:
                    result += Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                    temp[i['flag']] = temp.get(i['flag'], round(result, 2)) + round(result, 2)
                    print(temp)
                    total_result += result
                    #print(f'Total consumption so far is {round(total_result, 2)} KG  per passenger ')
    
    def list_domestic_flights_by_countries(self):
        #List domestic flights by countries
        temp = {}
        total_result = 0 
        result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                if 'flag' in i and (i['dep_icao'][:1] == i['dep_icao'][:1]):
                    result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                    temp[i['flag']] = temp.get(i['flag'], round(result, 2)) + round(result, 2)
                    print(temp)
                    total_result += result
                    #print(f'Total consumption so far is {round(total_result, 2)} KG  per passenger ')                    
     
    def list_international_flights_by_countries(self):
    #List international flights by countries
        temp = {}
        total_result = 0 
        result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                if 'flag' in i:
                    if (i['dep_icao'][:1]) != (i['arr_icao'][:1]):
                        result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                        temp[i['flag']] = temp.get(i['flag'], round(result, 2)) + round(result, 2)
                        print(temp)
                        total_result += result
                        #print(f'Total consumption so far is {round(total_result, 2)} KG  per passenger ') 

    def list_flights_by_registration_country(self):
        #List all flights by registration country
        temp = {}
        total_result = 0 
        result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                if 'flag' in i:
                    result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                    temp[i['flag']] = temp.get(i['flag'], round(result, 2)) + round(result, 2)
                    print(temp)
                    total_result += result
                    #print(f'Total consumption so far is {round(total_result, 2)} KG  per passenger ')

    def list_flights_by_aircraft_type(self):
    #List all flights by aircraft type
        temp = {}
        result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                if 'aircraft_icao' in i:
                    result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                    temp[i['aircraft_icao']] = temp.get(i['aircraft_icao'], round(result, 2)) + round(result, 2)
                    print(temp)
                    #print(f'Total consumption so far is {round(total_result, 2)} KG  per passenger ')
            sorted_temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)[:20]
            print(sorted_temp)
        
    def list_top_polluted_routes(self):
    # List top polluted routes given by airport taking into account how many days flight is available
        temp = {}
        for i in self.routes_list.read_data_file():
            if i.get('dep_icao') and i.get('arr_icao'):
                result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao']))) * sum(len(d) for d in i['days'])
                route = i['dep_icao'] + '-' + i['arr_icao']
                temp[route] = temp.get(route, 0) + result
                # Print top 20 polluted routes so far
                top_20 = sorted(temp.items(), key=lambda x: x[1], reverse=True)[:20]
                print(top_20)
        # Print final top 20 polluted routes
        print(sorted(temp.items(), key=lambda x: x[1], reverse=True))


class ApiConnector:
    
    def __init__(self, api_get, query_type='flight', detailed_query=None):
        self.api_get = api_get;
        self.query_type = query_type
        self.detailed_query = detailed_query
        
        if(api_get == 'airlabs'):
            self.api_key = {'api_key': keys.AIRLABS_KEY}
            self.api_url = 'http://airlabs.co/api/v9/' + query_type
            # flight(default, airlines, airports, cities, fleets, routes, countries, timezones, taxes )
            
        elif(api_get == 'aviationstack'):
            self.api_key = {'access_key': keys.AVIATION_KEY}
            self.api_url = 'http://api.aviationstack.com/v1/' + query_type+'s'
            # flights(default), routes, airports, airlines, airplanes, aircraft_types , taxes, cities, countries
            
        else:
            print('Invalid api')
    
    def save_routes(self, airport_icao):
        params= {'api_key':  keys.AIRLABS_KEY,
                'dep_icao': airport_icao}
        api_result = requests.get(self.api_url, params)
        api_response = api_result.json()

        with open(self.query_type + '.json', 'w') as write_file: 
            write_file.write(json.dumps(api_response['response']))
        print(f'Data saved to {airport_icao} .json') 


    def get_data_from_api(self):
        # Get Data From Api
        params = {'api_key':  keys.AIRLABS_KEY }
        params["_fields"]= self.detailed_query
        try:
            api_result = requests.get(self.api_url, params)
            api_response = api_result.json()
            return api_response['response']
        except:
            print('API Error! Please try again later (API may be throttling your IP)')

    def write_to_file(self):
        # Write data to file
        params = {'api_key':  keys.AIRLABS_KEY }
        params["_fields"]= self.detailed_query
        api_result = requests.get(self.api_url, params)
        api_response = api_result.json()
        
        with open(self.query_type + '.json', 'w') as write_file: 
            write_file.write(json.dumps(api_response['response']))
        print(f'Data saved to {self.query_type} .json')   

    def read_data_file(self):
        # Read file with data
        with open(self.query_type + '.json', 'r') as read_file:
            data = np.array(json.load(read_file))
            return data
    
    def print_data_from_api(self):
        # Prints Data From Api
        api_result = self.get_data_from_api()
        api_response = api_result.json()
        pprint(api_response)
        
    def print_api_key(self):
       # print api key
        print(self.api_key)

    def check_server_is_running(self):
        # Check server 
        api_result = self.get_data_from_api()
        print(api_result.status_code)
        if api_result.status_code == 200:
            print('Server is running')
        else:
            print('Server is not running')

        
            
# Program starts here
#if __name__ == "__main__":
 
   #ApiConnector('airlabs', 'flights').write_to_file()
   #Flights = ApiConnector('airlabs', 'flights',).get_data_from_api()
   # print(Flights)

   #Print Flight Flag
   # ApiResponse().get_all_flights_country()
    
   #Print Airport Coordinates
   # print(ApiResponse().get_airport_cordinates('EDDL'));
   # print(ApiResponse().get_airport_cordinates('EDDF'));
   
   
   #ApiConnector('airlabs', 'flights', 'dep_icao,arr_icao,flight_number,flag,aircraft_icao').write_to_file()
   # ApiConnector('airlabs', 'flights').get_data_from_api()
    
   # print(ApiConnector('airlabs', 'routes', 'dep_icao=EDDL').get_data_from_api())
    
   # a = ApiResponse().flights_list.read_data_file()
   # country = a.get('flag')
    #for country, value in enumerate(a):
     #   print(country, value)
             

    
     
    
   #All Flights - q1 
   #ApiResponse().list_all_flights()
    #print(ApiResponse().list_all_flights_2()) -- countries magic
  # print(ApiResponse().get_all_departure_airport());

   # Get Emissions by Airport

   #print(ApiResponse().list_flights_with_departure_airport('EDDL'))
   # print(ApiResponse().list_flights_with_departure_airport('EDDF'))
    
   # List all airports
   #print(ApiResponse().list_all_airports())
    
   #List by country - domestic
   #ApiResponse().list_flights_by_region('ED', False)
   # ApiResponse().list_domestic_flights_by_region('ED')

   #List by country - international
   # ApiResponse().list_international_flights_by_region('response = requests.get(url, headers=headers, auth=(nso_server['username'], nso_server['password']), verify=False).json()
   #ApiResponse().list_shorthaul_flights_by_countries()
    #ApiResponse().list_domestic_flights_by_countries()
    #ApiResponse().list_international_flights_by_countries()

   # ApiResponse().list_flights_by_aircraft_type()

   ### routes
    #ApiConnector('airlabs', 'routes').save_routes('KJFK')
    #ApiResponse().list_top_polluted_routes()

"""

1	At any given moment, what are the estimated total global CO2 emissions of all of the scheduled live flights currently in the air? 
1	Consider only those flights with specified departure and destination airports.   --> DONE
2	What are the estimated global CO2 emissions over the last five years (2017-2022)? --  Pandas
3	What are the emissions for each year/month within that timeframe? -- Pandas
4	What are the top twenty most polluting routes globally, regionally (USA, Europe) and by country. --> ROUTES
5	Within each region and country, differentiate by domestic and international flights.  --> DONE
6	What are the total CO2 emissions by each Airline? --> "flag": "US", no problem with --> DONE
6	Within this, filter by routes and short-haul and long-haul. --> DONE
7	What are the estimated CO2 emissions by airport? --> dep_icao(out of flights) == icao_code DONE
7	Show a breakdown of both arrivals and departures and then short-haul and long-haul. () DONE 
7	What are the top twenty countries responsible for aviation CO2 emissions. --> "country_code": "US", no problem with
•	Top twenty countries responsible for aviation CO2 emissions. Filter by: #Done
o	By domestic flights only. #Done
o	By international flights only. DONE
o	Combined CO2 emissions from domestic and international flights. DONE
o	By country of aircraft registration. DONE
•	Top twenty aircraft types responsible for the most CO2 emissions. DONE
""" 


"""
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


root = customtkinter.CTk()
root.geometry("600x500")
root.title("Flight Pollution Calculator")
root.minsize(300, 200)

# Grid
root.grid_rowconfigure((0,1,3), weight=1)
root.grid_rowconfigure(2, weight=3)
root.grid_columnconfigure((0,1,2), weight=1)



def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)
    
def print_to_console(print_value):
    print_value = print_value
    textbox1.insert("end", print_value + '\n')

def button_start():
    print(textbox1)
    #ApiResponse().list_all_flights(textbox1)

label1 = customtkinter.CTkLabel(master=root, text="Flight Pollution Calculator", anchor=tkinter.CENTER)
label1.grid(row=0, column=0, padx=10, pady=10, columnspan=4)

label1 = customtkinter.CTkLabel(master=root, text="Chose your Option:")
label1.grid(row=1, column=0, padx=5, pady=10)

combobox = customtkinter.CTkOptionMenu(master=root, command=optionmenu_callback, values=["List all Airports", "List all Airlines", "List all Flights", ], )
combobox.grid(row=1, column=1, padx=5, pady=10)
combobox.set("option 2")  # set initial value

entry = customtkinter.CTkEntry(master=root)
entry.grid(row=1, column=2, padx=5, pady=10)

button1 = customtkinter.CTkButton(master=root, command=button_start, text="Start")
button1.grid(row=1, column=3, padx=5, pady=10)

textbox1 = customtkinter.CTkTextbox(master=root)
textbox1.grid(row=2, column=0, columnspan=4, padx=20, pady=10, sticky="nsew")

ApiConnector('airlabs', 'countries').write_to_file()
"""


## ApiResponse().list_all_flights()


#if __name__ == "__main__":

root.textbox1.insert("end", 'App initialized' + '\n')


root.mainloop()
