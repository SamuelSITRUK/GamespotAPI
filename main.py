# Function to retrieve the name and dates articles published between 2 dates ont the website GamespotAPI

# Function to retrieve the name games released between 2 dates either on all platforms or on specific(s) platforms

import requests
import re
import os
import json
from datetime import datetime, timedelta



# gather the API key via the environment variables
API_KEY=os.environ.get('GAMESTOP_API_KEY')

#####Definition of starting and ending datesfor the construction of the file name
end_date='2025-01-29' 
start_date='2024-12-01' 
date_name_file= str(start_date + '_' + end_date)


BASE_URL = "https://www.gamespot.com/api/articles/?api_key= "+ API_KEY + "&format=json&filter=publish_date:" + start_date + "|" + end_date + "&field_list=publish_date,title&lim=1000000"
#BASE_URL_ARTICLES = "https://www.gamespot.com/api/articles/"

BASE_URL_releases = "https://www.gamespot.com/api/releases/?api_key="+ API_KEY + "&format=json&filter=publish_date:" + start_date + "|" + end_date + "&field_list=publish_date,title&lim=1000000"

params2_articles = {
        "api_key": API_KEY,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0"
}

response= requests.get(BASE_URL, headers=params2_articles).json() #response object decoded into json(via requests method decoded of json)









