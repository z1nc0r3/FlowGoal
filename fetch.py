import sys, os

parent_folder_path = os.path.abspath(os.path.dirname(__file__))
sys.path.append(parent_folder_path)
sys.path.append(os.path.join(parent_folder_path, "lib"))
sys.path.append(os.path.join(parent_folder_path, "plugin"))

import requests
import datetime
import json

class Fetch():
    
    countryCode = 'US'
    locale = 'en'
    timezone = '5.30'
    today = str(datetime.date.today()).replace('-', '')
    
    def fetch(self):
        url = f"https://prod-public-api.livescore.com/v1/api/app/date/soccer/{self.today}/{self.timezone}?locale={self.locale}"
        response = requests.request("GET", url)
        
        return response
        
    def parser(self, response):
        data = response.json()
        print(data)
        # print(data['data']['matchDetails']


runner = Fetch()
runner.parser(runner.fetch())