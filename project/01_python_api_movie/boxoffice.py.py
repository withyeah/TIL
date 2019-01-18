import csv
import requests
from bs4 import BeautifulSoup
import json
import os
from pprint import pprint
import datetime

def writecsv(filename):
    token = os.getenv('KOBIS_TOKEN')
    with open(filename, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ('movieCd', 'movieNm', 'audiAcc', 'recorded_at')
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            comparelist = []
            for i in range(10):
                d7 = datetime.timedelta(7*i)
                date = datetime.datetime(2019, 1, 13)
                targetDt = (date - d7).strftime("%Y%m%d")
                base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?'
                info_url = f'key={token}&targetDt={targetDt}&weekGb=0'
                url = base_url + info_url
                req = requests.get(url).json()
                for i in range(len(req['boxOfficeResult']['weeklyBoxOfficeList'])):
                    movieCode = req['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieCd']
                    movieName = req['boxOfficeResult']['weeklyBoxOfficeList'][i]['movieNm']
                    audiACCnum = req['boxOfficeResult']['weeklyBoxOfficeList'][i]['audiAcc']
                    if movieCode not in comparelist:
                        writer.writerow({'movieCd': f'{movieCode}', 'movieNm': f'{movieName}', 'audiAcc': f'{audiACCnum}', 'recorded_at': f'{targetDt}'})
                        comparelist.append(movieCode)    

writecsv('boxoffice.csv')
