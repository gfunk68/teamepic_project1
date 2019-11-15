import pandas as pd
import requests
from pprint import pprint
import os
 
def worldbank():

    # variables
    url = "http://api.worldbank.org/v2/"
    query_url = f"{url}countries?format=json"
    get_pages = requests.get(query_url).json()[0]['pages']
    all_pages_list = []
    country_list = []
    poverty_list = []
    region = []
    capital_city = []
    lat_long = []
    iso2code = []

    for page in range(get_pages):
        all_pages_list.append(requests.get(f'{query_url}&page={page+1}').json()[1])
    # pprint(all_pages_list)
    for y in range(len(all_pages_list)):
        for x in range(len(all_pages_list[y])):
            country_list.append(all_pages_list[y][x]['name'])
            poverty_list.append(all_pages_list[y][x]['incomeLevel']['value'])
            region.append(all_pages_list[y][x]['region']['value'])
            capital_city.append(all_pages_list[y][x]['capitalCity'])
            lat_long.append(f"{all_pages_list[y][x]['latitude']} , {all_pages_list[y][x]['longitude']}")
            iso2code.append(all_pages_list[y][x]['iso2Code'])
    # country_list
    # poverty_list
    # region
    # capital_city
    # lat_long
    #create dataframe from all derived worldbank info
    worldbank_df = pd.DataFrame({"Country": country_list,"Country Code": iso2code,"Region": region, "Poverty Level":poverty_list,"Capital City":capital_city,"Lat/Long":lat_long})

    #drop rows that are not countries
    worldbank_df = worldbank_df[worldbank_df.Region != "Aggregates"]
    worldbank_df = worldbank_df.reset_index(drop=True)
    
    return worldbank_df