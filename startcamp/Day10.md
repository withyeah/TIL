# Day 10



#### 1. 어제 OP.GG 예제에서 flash 추가

> from flask import url_for, redirect, flash



```python
   if summoner:
        if tier.text == "Unranked":
            # flash message
            flash(f"{ name } 소환사는 랭크 전적이 없습니다.")
            return redirect(url_for('sohwan'))
        else:
            return render_template("opgg.html", name=name, wins=wins.text)
    else:
        # flash message
        flash(f"{ name } 소환사가 없습니다.")
        return redirect(url_for('sohwan'))
    
    #시크릿키 추가
if __name__ == "__main__":
    app.secret_key = "Super_secret_key"
    app.run(host="0.0.0.0", port=8080, debug=True)
```



```html
<h1>소환사를 검색하세요.</h1>
<h3>
    <!--이 부분 추가 (flask 공식 doc에서 가져옴-->
{% with messages = get_flashed_messages() %}
  {% if messages %}
    {% for message in messages %}
      {{ message }}
    {% endfor %}
  {% endif %}
{% endwith %}
</h3>
<form action="/summoner">
    <input type="text" name="name"/>
    <input type="submit" value="Submit"/>
</form>
```



---



#### 2. 최근 2개월간 로또 당첨번호 뽑기

```python
from bs4 import BeautifulSoup
import requests
import random

numbers = random.sample(range(800, 838), 8)
for num in numbers:
    url  = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={num}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    select_num = soup.select('.nums .win .ball_645')
    bonus_num = soup.select_one('#article > div > div > div.win_result > div > div.num.bonus > p > span').text

    print(f"{num}회차 당첨번호는 ")
    for i in select_num:
        print(i.text, end=" ")
    print("+ " + bonus_num)
```

```python
#상근천재님 답 : join함수 써서 iterable 리스트 숫자만 뽑기
from bs4 import BeautifulSoup
import requests, random

lottos = random.sample(range(800, 838), 8)
for lotto in lottos:
   url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=" + str(lotto)
   info = requests.get(url).text
   info = BeautifulSoup(info, "html.parser")
   selector_main = ".nums .win .ball_645"
   selector_bonus = "#article > div > div > div.win_result > div > div.num.bonus > p > span"
   main = info.select(selector_main)
   bonus = info.select_one(selector_bonus)
   print(f"{lotto}회차 당첨번호")
   print(" ".join(f"{i.text}" for i in main), "+", bonus.text)
```

```python
#강사님 답 : count와 for문의 본질을 활용, 보너스 번호까지 한 번에 뽑기
numbers = random.sample(range(800, 838), 8)
for num in numbers:
    count = 0
    url = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={num}"
    req = requests.get(url).text
    soup = BeautifulSoup(req, 'html.parser')
    lucky = soup.select(".ball_645")
    print(f"{num} 회차 당첨번호")
    for i in lucky:
        print(i.text, end=" ")
        count += 1
        if count == 6:
            print("+", end=" ")
    print()
```



---



#### 3. json

lotto

```python
0. random 으로 로또번호를 생성
1. api를 통해 우승 번호를 가져옴
2. 0번과 1번을 비교하여 나의 등수를 알려줌
--------------------------------------------
1. url 요청 보내서 정보를 가져옵니다.
    - json 으로 받는다. (딕셔너리로 접근 가능)
2. api의 당첨번호와 보너스 번호를 저장하고
3. 뽑은 게 몇 등인지 뽑으세요. 끝.
```

```python
#상근천재님의 답 참고한 내 답
import random
import requests
import json
from pprint import pprint

url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json()

luckyset = set()
for num in range(1,7):
    lucky = lotto[f"drwtNo{num}"]
    luckyset.add(lucky)
bonusset = set()    
bonusset.add(lotto["bnusNo"])

count = 0
want = 0

while want != 1:
    randomnum = set(random.sample(range(1,46), 6))
    remaining = randomnum - luckyset
    remaininglen = len(remaining)
    if remaininglen > 3:
        print("탈락")
    elif remaininglen == 2:
        print("4등! 5만원 당첨!")
        # want = 1
    elif remaininglen == 1:
        if len(remaining - bonusset) == 0:
            print("2등!")
        else:
            print("3등!")
            # want = 1
    elif remaininglen == 0:
        print("1등!")
        want = 1
    count += 1
print(count)
```



---




```python
#강사님 답

url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json()

winner = []
for i in range(1,7):
    winner.append(lotto[f"drwtNo{i}"])

bonus = lotto["bnusNo"]

print("이번 주 당첨번호 : " + str(winner))
print("보너스 번호 : " + str(bonus))

count = 0
while True:
    count += 1
    my_numbers = sorted(random.sample(range(1, 46), 6))
    matched = len(set(winner) & set(my_numbers))

    if matched == 6:
        print("1등")
    elif matched == 5:
        if bonus in my_numbers:
            print("2등")
        else:
            print("3등")
    elif matched == 4:
        print("4등")
    elif matched == 3:
        print("5등")
        print(count, "번만에 당첨되셨습니다.")
        money = format(count*1000, ",")
        print("쓴 돈은", money)
        # n등 찾을 때 해당 부분에 break
        break
    else:
        print("응 안돼")
```

```
...
응 안돼
응 안돼
5등
19 번만에 당첨되셨습니다.
쓴 돈은 19,000
```



---



#### 4. 영화진흥위원회

http://www.kobis.or.kr/kobisopenapi/homepg/apiservice/searchServiceInfo.do

http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieList.json?key=430156241533f1d058c603178cc3ca0e



---



#### 5. 텔레그램 챗봇



##### 1) message 보내기

```python
import requests
import json
from pprint import pprint
import os

#보안설정
token = os.getenv("TELEGRAM_BOT_TOKEN")
method_name = "getUpdates"
url = f"https://api.telegram.org/bot{token}/{method_name}"

update = requests.get(url).json()
chat_id = update["result"][0]["message"]["chat"]["id"]

msg = "Hello"
method_name = "sendmessage"
msg_url = f"https://api.telegram.org/bot{token}/{method_name}?chat_id={chat_id}&text={msg}"
```

> 보안설정 .bash_profile에서 토큰 export 후 rehash



##### 2) kospi지수 보내기

```python
import requests
import json
from pprint import pprint
import os
from bs4 import BeautifulSoup

token = os.getenv("TELEGRAM_BOT_TOKEN")
method_name = "getUpdates"
url = f"https://api.telegram.org/bot{token}/{method_name}"
# chat_id = 656902495

update = requests.get(url).json()
chat_id = update["result"][0]["message"]["chat"]["id"]
method_name = "sendmessage"

financeurl = "https://finance.naver.com/sise/"
req = requests.get(financeurl).text
soup = BeautifulSoup(req, 'html.parser')
kospi = soup.select_one("#KOSPI_now").text

msg_url = f"https://api.telegram.org/bot{token}/{method_name}?chat_id={chat_id}&text={kospi}"


print(msg_url)
print(requests.get(msg_url))
```

