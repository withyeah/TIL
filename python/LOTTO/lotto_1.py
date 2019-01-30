from bs4 import BeautifulSoup
import requests
import random

# numbers = random.sample(range(800, 838), 8)
# for num in numbers:
#     url  = f"https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={num}"
#     req = requests.get(url).text
#     soup = BeautifulSoup(req, 'html.parser')
#     select_num = soup.select('.nums .win .ball_645')
#     bonus_num = soup.select_one('#article > div > div > div.win_result > div > div.num.bonus > p > span').text

#     print(f"{num}회차 당첨번호는 ")
#     for i in select_num:
#         print(i.text, end=" ")
#     print("+ " + bonus_num)

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