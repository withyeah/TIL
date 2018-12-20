# # 1. 평균을 구하세요.

# # scores = {
# #     "국어" : 87,
# #     "영어" : 92,
# #     "수학" : 40
# # }

# #1-1
# # total_score = 0
# # for score in scores.values():
# #     total_score += score
# #     #total+score = total_score + score 와 같음
# # average_score = total_score/len(score)
# # print(average_score)

# # #1-2
# # total_score = sum(scores.values)
# # average_score = sum/len(score)

# # 2반 평균을 구하시오
# scores = {
#     "철수" : {
#         "수학": 80,
#         "국어": 90,
#         "음악": 100,
#     },
#     "영희" : {
#         "수학": 70,
#         "국어": 60,
#         "음악": 50,
#     }
# }



# # for person in scores:
# #     for score in scores[person].values():
# #         total_score = total_score + score
# # total_len = len(scores["철수"]) + len(scores["영희"])
# # print(total_score/total_len)

# # print()# for person in scores:
# #     person = scores[person].values()

# total_score = 0
# count = 0

# for person_score in scores.values():
#     for indivisual_score in person_score.values():
#         total_score += indivisual_score
#         count += 1

# average_score = total_score / count

# 3 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

cities = {
    "서울": [-6, -10, 5],
    "대전": [-3, -5, 2],
    "광주": [0, -2, 10],
    "부산": [2, -2, 9],
}

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
