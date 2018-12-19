# Flask를 활용한 어플리케이션 구축

#### 2018-12-19



##### `warm up quiz`

​	1-1

```python
# 아래 코드의 출력 결과를 예상하라.

```

​	1-2

```python
#자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램

item = int(input("번호를 입력하세요: "))
for i in range(1, item+1):
    print(i)
```

```python
#자연수 N이 주어졌을 때, 1부터 N까지 한 줄에 하나씩 출력하는 프로그램

item = int(input("번호를 입력하세요: "))
for i in range(item):
    print(i+1)
```

​	1-3

```python
'''
투자 경고 종목 리스트가 있을 때 사용자로부터 종목명을 입력 받은 후 해당 종목이 투자 경고 종목이라면
'투자 경고 종목입니다'를  아니면 '투자 경고 종목이 아닙니다.'를 출력하는 프로그램
'''

warn_investment_list = ["microsoft", "google", "naver", "kakao", "sansung", "lg"]
print(f"경고 종목 리스트: {warn_investment_list}")
item = input('투자 종목이 무엇입니까? ')
#not in 하면 반대로
if item.lower() in warn_investment_list:
    print("투자 경고 종목입니다.")
else:
    print("투자 경고 종목이 아닙니다.")
```

​	1-4

```python
'''
colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']
다음 리스트에서 0, 4, 5번째 요소를 지운 새로운 리스트를 생성하시오.'''

colors = ['Apple', 'Banana', 'Coconut', 'Deli', 'Ele', 'Grape']

#방법1
colors2 = []
for i in range(len(colors)):
    if i in [0, 4, 5]:
        pass
    else:
        colors2.append(colors[i])
print(colors2)

#방법2
fruit = []
deleteindex = [0, 4, 5]
for i in range(0, len(colors)):
    if i not in deleteindex:
        fruit.append(colors[i])
print(fruit)
```

​	1-5 딕셔너리101

```python
# ssafy의 semester1의 기간을 출력
# ssafy dictionary 안에 들어 있는 '대전'을 출력
# daejon의 매니저의 이름을 출력

ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"]
        }
    },
    "duration": {
        "semester1": "6월까지"
    },
    "classes": {
        "seoul":  {
            "lecturer": "john",
            "manager": "pro",
        },
        "daejeon":  {
            "lecturer": "tak",
            "manager": "yoon",
        }
    }
}

print(ssafy["duration"]["semester1"])
print(ssafy["location"][1])
print(ssafy["classes"]["daejeon"]["manager"])
```

---

### HTML

​	2-1 기본 뼈대

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8" />
    <title>Page Title</title>
    <!--google font에서 긁어온 폰트 소스-->
    <link href="https://fonts.googleapis.com/css?family=Aleo|Major+Mono+Display" rel="stylesheet">
</head>
<body>
    
</body>
</html>
```

닫는 태그 없는 태그 : br, hr, img

```html
id="uniqe" class="ssafy daegeon h-h"
```

​	ㄴclass 3개임! 띄어쓰기로 구분

---

### CSS

- html에 css 넣는 방법 3가지

  - embedding 스타일 : <head>안에 <style>태그 넣기

    - ```html
      <style>
              h1 { color: darkolivegreen; } 
          </style>
      ```

  - inline 스타일 : <body>안에서 각 태그에 넣기

    - ```html
      <h1 class="ssafy" style="color: red;">Hello HTML</h1>
      ```

  - css시트 외부에서 <head>에 삽입

    - ```html
      <link rel="stylesheet" href="style.css">
      ```

- selector

  - ```css
    /* universal selector */
    * {
        background: salmon;
    }
    /* 다중 select */
    h1, p {
        color: green;
    /* id selector */
    #lunch {
        color: brown;
    }
    /* class selector */
    .container {
        color: violet;
    }
    ```

- div, nav, section : 섹터 나누기

- span : 중간에 특정 부분 스타일 지정할 때

  - ```css
    /* 후손 selector 공백문자 */
    div p {
        color: green;
    }
    /* 자식 selector > */
    div > p {
        color: hotpink;
    }
    ```

  - ```css
    /* 형제 selector : div 바로 뒤에 붙어있는 p들  select */
    div + p {
        color: purple;
    }
    /* 물결 형제 selector : 동위 선상의 p부터 span까지 사이태그도 적용 */
    p ~ span {
        color: cadetblue;
    }
    ```



---

### Flask



> c9.io/login



```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return "안녕하세요!!"
#http://flask-basic-withyeah.c9users.io:8080/

@app.route("/hello")
def hello():
    return "hello를 타고 들어오셨군요?"
#http://flask-basic-withyeah.c9users.io:8080/hello

@app.route("/html_tag")
def html_tag():
    return "<h1>안녕안녕</h1>"
#http://flask-basic-withyeah.c9users.io:8080/html_tag

@app.route("/html_line")
def html_line():
    return """
    <h1>여러 줄 보내기</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """
#http://flask-basic-withyeah.c9users.io:8080/html_line

@app.route("/html_render")
def html_render():
    return render_template("index.html")
#templates dir에 html, css파일넣기
#import render_template하기
#http://flask-basic-withyeah.c9users.io:8080/html_render
```





> Flask와 Django는 Jinja2 언어를 쓴다

```python
@app.route("/html_name/<string:name>")
def html_name(name):
    return render_template("hello.html", your_name = name)
#hello.html의 your_name 자리에 <string:name>에서 받은 값을 할당해줌 (name이라는 변수의 string값)
```

```html
<h1>안녕하세요!, {{ your_name }}</h1>
```



> > 응용1 - 변수 여러개
>
> ```python
> @app.route("/html_variables/<string:idname>/<int:number>")
> def html_variables(idname, number):
>     return render_template("hello.html", your_name = idname, your_number = number)
> ```
>
> ```html
> <h1>안녕하세요!, {{ your_name }}</h1>
> <h2>{{ your_number }}번째 방문자입니다.</h2>
> ```
>
> http://flask-basic-withyeah.c9users.io:8080/html_variables/yerang/12598241



> > 응용2 - 세제곱 값 리턴
>
> ```python
> @app.route("/math/<int:num>")
> def math(num):
>     result = num**3
>     return render_template("math.html", inputnum = num, outputnum = result)
> ```
> - inputnum, outputnum 안쓰고 그냥 num = num, result = result 
>
> ```html
> <h1>{{ inputnum }} 의 세제곱 값은</h1>
> <h2>{{ outputnum }}</h2>
> ```
>
> http://flask-basic-withyeah.c9users.io:8080/math/3



> > 응용3 - 저녁메뉴 pick & 사진
>
> ```python
> @app.route("/dinner")
> def dinner():
>     list = ["초밥", "탕수육", "삼겹살", "돼지국밥"]
>     dict = {
>         "초밥" : "https://st3.depositphotos.com/1005524/17670/i/1600/depositphotos_176702996-stock-photo-nigiri-sushi-with-salmon.jpg",
>         "탕수육" : "https://i.ytimg.com/vi/aqaSvDylLaY/maxresdefault.jpg",
>         "삼겹살" : "https://img.insight.co.kr/static/2018/03/02/700/c2jup0e2y76th9bg072c.jpg",
>         "돼지국밥" : "http://blogs.chosun.com/gourmet/wp-content/uploads/sites/24/2014/07/20120315_102205_01204cf2ee26bb491e50b2dada83f7a0.jpg"
>     }
>     pick = random.choice(list)
>     url = dict[pick]
>     return render_template("dinner.html", pick = pick, url = url)
> ```
>
> ```html
> <h1>오늘의 저녁은 {{ pick }}</h1>
> <img src="{{ url }}" alt="{{ pick }}사진" width=400px height=300px>
> ```
>
> http://flask-basic-withyeah.c9users.io:8080/dinner







fontawesome

class명으로 icon넣기

