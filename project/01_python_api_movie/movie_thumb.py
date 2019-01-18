import csv
import requests
import json
import os

def writecsv():
    TOKEN_ID = os.environ['TOKEN_ID']
    TOKEN_SECRET = os.environ['TOKEN_SECRET']
    codeimg = dict()
    os.mkdir('images')
    # credential = {'X-Naver-Client-Id': TOKEN_ID, 'X-Naver-Client-Secret': TOKEN_SECRET}
    with open('movie_naver.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            codeimg.update({row['movie_code']: row['thumb_url']})
    for movie_code, thumb_url in codeimg.items():
        img_data = requests.get(thumb_url).content
        
        with open(f'./images/{movie_code}.jpg', 'wb') as handler:
                handler.write(img_data)

writecsv()




