## day7 2018/12/18

- CLI

  - 파일 생성 touch 파일명
  - 파일 접근 open 파일명
    - vscode - code
    - atom - atom

- string format

```python
# pyformat
# '{} {}'.format('one', 'two')
name = '김예랑'
e_name = 'KIM'
print("안녕하세요 {0}입니다. My name is {1}.".format(name, e_name))

# f-string python 3.6 이상
print(f"안녕하세요 {name}입니다. My name is {e_name}.")

#이렇게 할 수도 있다
name = "김예랑"
print("안녕하세요. " + name + "입니다.")
```

```
$ python string_test.py
안녕하세요 김예랑입니다. My name is KIM.
안녕하세요 김예랑입니다. My name is KIM.
안녕하세요. 김예랑입니다.
```



- lotto 예제  string  format 연습

```python
#lotto
#오늘의 행운의 번호는 뭐뭐 입니다.
import random
numbers = list(range(1, 46))
lotto = random.sample(numbers, 6)
print("오늘의 행운의 번호는 {0}입니다".format(lotto))
print(f"오늘의 행운의 번호는 {lotto}입니다.")
print('오늘의 행운의 번호는 ' + " ".join("{0}".format(i) for i in lotto) + " 입니다.")
print('오늘의 행운의 번호는 ' + "".join(f"{lotto}") + " 입니다.")
```

```
$ python string_test.py
오늘의 행운의 번호는 [40, 23, 35, 34, 5, 12]입니다
오늘의 행운의 번호는 [40, 23, 35, 34, 5, 12]입니다.
오늘의 행운의 번호는 40 23 35 34 5 12 입니다.
오늘의 행운의 번호는 [7, 17, 11, 29, 19, 34] 입니다.
```

> 위에서 3번 4번 줄 출력 다른 이유 : for문으로 



---



#### 파일명 바꾸기

- dummy  파일 만들기 (dir에 더미 파일 500개 만들기)

```python
import os
import random
family = ['김','이','박','최','황','오','강','한','제갈','하','정','송','현','손','조']
given = ['길동','준','민준','소미','수진','지은','동해','민태','준호','세정','지훈','성우','성원']

for i in range(500):
    cmd = f"touch {str(i)}_{random.choice(family)}{random.choice(given)}.txt"
    print(cmd)
    os.system(cmd)
```

- **import os**

  1)  os.**chdir**(r'폴더주소')

  	> r은 윈도우에서만 붙이면 됨! 맥에서는 빼기

  ​	- 작업하고 있는 위치 변경

  2)  os.**listdir**('폴더주소')

  ​	- 지정된 디렉토리 전체 파일 목록 열기

  3)  os.**rename**('현재파일명','바꿀 파일명')

```python
#파일명 앞에 SAMSUNG 다 붙이기
import os
os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
for filename in os.listdir("."):
    os.rename(filename, "SAMSUNG " + filename)
```

##### 다시 바꾸기! 

```python
#파일명 앞에 붙어있던 SAMSUNG -> SSAFY 바꾸기
import os
os.chdir(r"C:\Users\student\Desktop\TIL\dummy")
for filename in os.listdir("."):
    os.rename(filename, filename.replace("SAMSUNG","SSAFY"))
```



#### 파일내용 쓰기

- 파일 열고 닫기 write & close

```python
#직관적이지만 불편한 방법
f = open("new.txt", "w")
f.write("Hello World")
f.close()

#빠른 방법
with open("new.txt", "w") as f:
    f.write("Goodbye World")
```

	> 두가지 다 한꺼번에 실행하면 goodbye로 덮어짐
	>
	> f는 임의의 변수지만 일반적으로는 f를 쓴다

- 파일 읽기 read

```python
#방법1
f = open("new.txt", "r")
data = f.read()
print(data)
f.close()

#방법2
with open("new.txt", "r") as f:
    data = f.read()
print(data)
```

```
$ python make_txt.py
Hello World
```

- 여러 줄 쓰기

```python
#방법1
f = open("new.txt", "w", encoding = 'utf-8')
for i in range(5):
    data = f"{i}번째 줄입니다.\n"
    f.write(data)
f.close()

#방법2
with open("new.txt", "w", encoding = 'utf-8') as f:
    for i in range(5):
        data = f"{i}번째 줄입니다.\n"
        f.write(data)
```

```python
#복기 test
f = open("test.txt", "w", encoding = "utf-8")
for i in range(1, 6):
    f.write(f"{i}"+"번째 줄입니다.\t")
f.close()

with open("test.txt", "w", encoding = "utf-8") as f:
    for i in range(1, 6):
        f.writelines(f"{i}" + "번째 줄입니다.\t")
```

> 메모장 매번 들어가서 확인하지 말고 $ cat 파일명 하면 파일 내용 출력됨
>
> 한글 쓸 때 encoding = 'utf-8'

```python
menu = ["카레\n", "레카\n", "카카\n", "레레\n"]
#방법1
f = open("menu.txt", "w", encoding = 'utf-8')
f.writelines(menu)
f.close()

#방법2
with open("menu.txt", "w", encoding = 'utf-8') as f:
    f.writelines(menu)
```

---



#### 파일읽기

- `readline()` : 한 줄로 읽어서 리턴
- `readlines()` : 파일 전체를 읽어 list 형태로 리턴 

```python
#readline()
with open("new.txt", "r", encoding='utf-8') as f:
    line = f.readline()
    print(line)
```
> 개행이 두 번 됨! (readline과 print)

```python
#readline()
with open("new.txt", "r", encoding='utf-8') as f:
    line = f.readline()
    print(line.strip())
```
> `strip()` : 왼/오른쪽 공백 삭제
>
> `lstrip()` : 왼쪽 공백 삭제
>
> `rstrip()` : 오른쪽 공백 삭제

- 여러 줄 읽기

```python
with open("new.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
```

> > `갑분크롬익스텐션추천` 
> >
> > ---
> >
> > - ublock origin : adblock 대체재
> >
> > - momentum / earth view from google earth : 탭화면 이쁘게
> > - wappalyzer : 각 웹사이트 어떤 언어, 서버, 프레임웤, 라이브러리 쓰는지 알려줌
> > - octotree : code tree for GitHub
> > - turn off the lights : youtube 다크모드랑 비슷

---



#### scraping

import requests

- import requests
  - requests.get(주소)
  - requests.get(주소).text
  - requests.get(주소).status_code

- 정보 스크랩 1단계

  - 원하는 정보가 있는 주소로 요청을 보내, 응답을 저장한다.

    - ```
      import requests
      req = requests.get('주소').text
      ```

  - 정보를 출력하여 확인한다.

    - ```
      print(req)
      ```

- 정보 스크랩 2단계

  - beautifulsoup으로 kospi지수 스크래핑

    - ```python
      #BeautifulSoup import하기
      import requests
      from bs4 import BeautifulSoup
      
      #text로 긁어오기
      req = requests.get("https://finance.naver.com/sise/").text
      #html을 soup변수에 담기
      soup = BeautifulSoup(req, 'html.parser')
      #select vs select_one
      kospi = soup.select_one("#KOSPI_now")
      #.text붙이면 앞뒤에 html코드 빼고 텍스트만 출력
      print(kospi.text)
      ```

    - ```python
      #야후재팬 원달러 환율 긁어오기 예시
      req = requests.get("https://finance.yahoo.co.jp/").text
      soup = BeautifulSoup(req, 'html.parser')
      currency = soup.select_one("#fx > div > div.chartInner > div.rateListArea.clearfix > div.rateListBox.rateup > div")
      print(currency.text)
      ```

  - 네이버 실시간 검색어 스크래핑  ***여기 코딩 다시 해보기***

    - ```python
      import requests
      from bs4 import BeautifulSoup
      
      req = requests.get("https://www.naver.com/").text
      soup = BeautifulSoup(req, 'html.parser')
      
      for tag in soup.select('.PM_CL_realtimeKeyword_rolling .ah_item'):
          rank = tag.select_one('.ah_r').text
          name = tag.select_one('.ah_k').text
          print(f'{rank}는 {name}입니다.')
      ```


