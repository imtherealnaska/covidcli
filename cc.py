import requests 
import json 

# V4 endpoints 
current_dayV4 ="https://api.covid19india.org/v4/min/data.min.json" 

daily_numbersV4 = "https://api.covid19india.org/v4/min/timeseries.min.json"

perday_numbersV4= "https://api.covid19india.org/v4/min/data-all.min.json"

response = requests.get(current_dayV4)
json_response = response.json() 

districts = json_response['KA']['districts']['Bagalkote']
print('Bagalkote' , districts)
# dictionary = json.dumps (response.json() , sort_keys = True , indent=4)


