import csv
import requests
import json
import os
from pprint import pprint

def writecsv(filename):
    TOKEN_ID = os.environ['TOKEN_ID']
    TOKEN_SECRET = os.environ['TOKEN_SECRET']
    movienamecode = dict()
    credential = {'X-Naver-Client-Id': TOKEN_ID, 'X-Naver-Client-Secret': TOKEN_SECRET}
    with open('movie.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            movienamecode.update({row['movie_name_ko']: row['movie_code']})
    with open(filename, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ('movie_code', 'thumb_url', 'link_url', 'user_rating')
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
    
            for movie_name_ko, movie_code in movienamecode.items():
                url = f'https://openapi.naver.com/v1/search/movie.json?query={movie_name_ko}'
                req = requests.get(url, headers=credential).json()
                thumb_url = req['items'][0]['image']
                link_url = req['items'][0]['link']
                user_rating = req['items'][0]['userRating']
                writer.writerow({'movie_code': f'{movie_code}', 'thumb_url': f'{thumb_url}',
                                    'link_url': f'{link_url}', 'user_rating': f'{user_rating}'})

writecsv('movie_naver.csv')




