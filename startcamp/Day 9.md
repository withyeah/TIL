# Day 9



```python
"""
파이썬 dictionary 활용 기초!
"""

dict = {
    "대전" : 23,
    "서울" : 30,
    "구미" : 20
}
print((dict.values())
```

```
<class 'dict_values'>
#=>dict_values([23, 30, 20])
```



```python
# 1. 평균을 구하세요.

scores = {
    "국어" : 87,
    "영어" : 92,
    "수학" : 40
}

#1-1
total_score = 0
for score in scores.values():
    total_score += score
    #total+score = total_score + score 와 같음
average = total_score / len(score)
print(average)

#1-2
total_score = sum(scores.values)
average_score = sum/len(score)
```



```python
# 2반 평균을 구하시오
scores = {
    "철수" : {
        "수학": 80,
        "국어": 90,
        "음악": 100,
    },
    "영희" : {
        "수학": 70,
        "국어": 60,
        "음악": 50,
    }
}

	#내가 푼 거
total_score = 0

for person in scores:
    for score in scores[person].values():
        total_score = total_score + score
total_len = len(scores["철수"]) + len(scores["영희"])
print(total_score/total_len)

	#강사님 답
total_score = 0
count = 0

for person_score in scores.values():
    for indivisual_score in person_score.values():
        total_score += indivisual_score
        count += 1
        #여기가 포인트!!!!!!!!!!

average_score = total_score / count
print(average_score)
```



```python
# 3

#개념
scores = {
    "국어" : 87,
    "영어" : 92,
    "수학" : 40
}

for key, value in scores.items():
    print(key)
    print(value)

#=>
#국어
#87
#영어
#92
#수학
#40


```



```python
# 3 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

#강사님 답
hot = 0
cold = 0
hot_city = ""
cold_city = ""
count = 0

for name, temp in cities.items():
    # name = "서울"
    # temp = [-6, -10, 5]
    if count == 0:
       hot = max(temp)
       cold = min(temp)
       hot_city = name
       cold_city = name
    else:
        #최저 온도가 cold 보다 더 추우면, cold에 넣음
        if min(temp) < cold:
            cold = min(temp)
            cold_city = name
        #최고 온도가 hot 보다 더 더우면, hot에 넣음
        if max(temp) > hot:
            hot = max(temp)
            hot_city = name
    count += 1
print(f"{hot_city}, {cold_city}")


#상근천재님 답
ex_max = 0
ex_min = 0
hot_city = ""
cold_city = ""


for name, temp in cities.items():
  max_temp = max(temp)
  min_temp = min(temp)

  if max_temp > ex_max:
      ex_max = max_temp
      hot_city = name

  if min_temp < ex_min:
      ex_min = min_temp
      cold_city = name

print("더운도시", ex_max, "도", hot_city)
print("추운도시", ex_min, "도", cold_city)
```



---



c9

jinja - 눈에 보이지 않는 조건문 등은 {% %}

for문

{%  for i in item %}



{% endfor %}





1. 로또번호6개뽑기

```python
@app.route("/lotto")
def lotto():
    list = range(1, 46)
    num = random.sample(list, 6)
    return render_template("lotto.html", num = num)
```

```html
<h1> 행운의 번호는 </h1>
{% for i in num %}
	{{ i }}
{% endfor %}
<h1> 입니다! </h1>
```


2. fake naver

```python
@app.route("/naver")
def naver():
    return render_template("naver.html")
```

```html
<h1>네이버 검색</h1>
<form action="https://search.naver.com/search.naver">
    <!--여기가 포인트! name에 query를 넣음-->
    <input type="text" name="query"/>
    <input type="submit" value="Submit"/>
</form>
```



3. fake google

```python
@app.route("/google")
def google():
    return render_template("google.html")
```

```html
<h1>Google</h1>
<form action="https://www.google.com/search">
    <input type="text" name="q"/>
    <input type="submit" value="Submit"/>
</form>
```



4. pingpong

```python
@app.route("/ping")
def ping():
    return render_template("ping.html")
    
@app.route("/pong")
def pong():
    pingpong = request.args.get('ping')
    return render_template("pong.html", pingpong = pingpong)
```

```html
<!--ping.html-->
<h1>핑퐁핑퐁</h1>
<form action="/pong">
    <input type="text" name="ping"/>
    <input type="submit" value="Submit"/>
</form>

<!--pong.html-->
<h1>{{ pingpong }}</h1>
```

> 결과 : /ping으로 들어가면 텍스트 입력창 나옴. 입력한 텍스트(어쩌구저쩌구)를 pingpong에 담아서 submit하면 /pong에서 어쩌구저쩌구를 리턴해줌



5. opgg

> 1. 소환사가 있는지 없는지, 있다면 승리수 출력
> 2. 소환사가 있으나 랭크전적이 없을때



```python
@app.route("/sohwan")
def sohwan():
    return render_template("sohwan.html")
    
@app.route("/summoner")
def summoner():
    name = request.args.get('name')
    url = f"http://www.op.gg/summoner/userName={name}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    summoner = soup.select_one("body > div.l-wrap.l-wrap--summoner > div.l-container > div > div > div.Header > div.Profile > div.Information > span")
    wins = soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins")
    tier = soup.select_one("#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div > span")
    
    if summoner:
        if tier.text == "Unranked":
            return render_template("notier.html", name=name)
        else:
            return render_template("opgg.html", name=name, wins=wins.text)
    else:
        return render_template("nouser.html", name=name)
```

```html
<!--opgg.html-->
<h1>{{ name }} 의 이번시즌 랭크 승리: {{ wins }}</h1>
```

```html
<!--sohwan.html-->
<h1>소환사를 검색하세요.</h1>
<form action="/summoner">
    <input type="text" name="name"/>
    <input type="submit" value="Submit"/>
</form>
```

```html
<!--nouser.html-->
<h1>{{ name }} 소환사가 없습니다.</h1>
```

```html
<!--notier.html-->
<h1>{{ name }} 소환사는 랭크 전적이 없습니다.</h1>
```





중산도 -> 중리지구대 정류장