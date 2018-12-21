import random
import requests
import json
from pprint import pprint

"""
0. random 으로 로또번호를 생성
1. api를 통해 우승 번호를 가져옴
2. 0번과 1번을 비교하여 나의 등수를 알려줌
--------------------------------------------
1. url 요청 보내서 정보를 가져옵니다.
    - json 으로 받는다. (딕셔너리로 접근 가능)
2. api의 당첨번호와 보너스 번호를 저장하고
3. 뽑은 게 몇 등인지 뽑으세요. 끝.
--------------------------------------------

"""

url = "https://dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=837"
res = requests.get(url)
lotto = res.json()

# luckyset = set()
# for num in range(1,7):
#     lucky = lotto[f"drwtNo{num}"]
#     luckyset.add(lucky)
# bonusset = set()    
# bonusset.add(lotto["bnusNo"])

# count = 0
# want = 0

# while want != 1:
#     randomnum = set(random.sample(range(1,46), 6))
#     remaining = randomnum - luckyset
#     remaininglen = len(remaining)
#     if remaininglen > 3:
#         print("탈락")
#     elif remaininglen == 2:
#         print("4등! 5만원 당첨!")
#         # want = 1
#     elif remaininglen == 1:
#         if len(remaining - bonusset) == 0:
#             print("2등!")
#         else:
#             print("3등!")
#             # want = 1
#     elif remaininglen == 0:
#         print("1등!")
#         want = 1
#     count += 1
# print(count)


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
        print(count, "번만에 당첨되셨습니다.")
        money = format(count*1000, ",")
        print("쓴 돈은", money)
        break
    elif matched == 5:
        if bonus in my_numbers:
            print("2등")
        else:
            print("3등")
    elif matched == 4:
        print("4등")
    elif matched == 3:
        print("5등")
    else:
        print("응 안돼")