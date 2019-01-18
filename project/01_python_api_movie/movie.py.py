import csv
import requests
import json
import os
from pprint import pprint
import datetime

def writecsv(filename):
    token = os.getenv('KOBIS_TOKEN')
    moviecodelist = []
    with open('boxoffice.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            moviecodelist.append(row['movieCd'])
    with open(filename, 'w', newline='', encoding='utf-8') as f:
            fieldnames = ('movie_code', 'movie_name_ko', 'movie_name_en',
             'movie_name_og', 'prdt_year', 'genres', 'directors', 'watch_grade_nm',
             'actor1', 'actor2', 'actor3')
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for movie_code in moviecodelist:
                base_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?'
                info_url = f'key={token}&movieCd={movie_code}'
                url = base_url + info_url
                req = requests.get(url).json()
                movie_name_ko = req['movieInfoResult']['movieInfo']['movieNm']
                movie_name_en = req['movieInfoResult']['movieInfo']['movieNmEn']
                movie_name_og = req['movieInfoResult']['movieInfo']['movieNmOg']
                prdt_year = req['movieInfoResult']['movieInfo']['prdtYear']
                # if len(req['movieInfoResult']['movieInfo']['genres']) == 1:
                #     genres = req['movieInfoResult']['movieInfo']['genres'][0]['genreNm']
                # else:
                #     genres = f'{req['movieInfoResult']['movieInfo']['genres'][0]['genreNm']}/{req['movieInfoResult']['movieInfo']['genres'][1]['genreNm']}'
                # if len(req['movieInfoResult']['movieInfo']['directors']) == 1:
                #     directors = req['movieInfoResult']['movieInfo']['directors'][0]['peopleNm']
                # else:
                #     directors = f'{req['movieInfoResult']['movieInfo']['directors'][0]['peopleNm']}/{req['movieInfoResult']['movieInfo']['directors'][1]['peopleNm']}'
                genres = req['movieInfoResult']['movieInfo']['genres'][0]['genreNm']
                directors = req['movieInfoResult']['movieInfo']['directors'][0]['peopleNm']
                watch_grade_nm = req['movieInfoResult']['movieInfo']['audits'][0]['watchGradeNm']
                ACTOR = req['movieInfoResult']['movieInfo']['actors']
                if len(ACTOR) < 3:
                    if len(ACTOR) == 0:
                        actor1 = ''
                        actor2 = ''
                        actor3 = ''
                    elif len(ACTOR) == 1:
                        actor1 = ACTOR[0]['peopleNm']
                        actor2 = ''
                        actor3 = ''
                    elif len(ACTOR) == 2:
                        actor1 = ACTOR[0]['peopleNm']
                        actor2 = ACTOR[1]['peopleNm']
                        actor3 = ''
                else:
                    actor1 = ACTOR[0]['peopleNm']
                    actor2 = ACTOR[1]['peopleNm']
                    actor3 = ACTOR[2]['peopleNm']    
                writer.writerow({'movie_code': f'{movie_code}', 
                'movie_name_ko': f'{movie_name_ko}', 
                'movie_name_en': f'{movie_name_en}', 
                'movie_name_og': f'{movie_name_og}',
                'prdt_year': f'{prdt_year}',
                'genres': f'{genres}',
                'directors': f'{directors}',
                'watch_grade_nm': f'{watch_grade_nm}',
                'actor1': f'{actor1}',
                'actor2': f'{actor2}',
                'actor3': f'{actor3}'})  

writecsv('movie.csv')



