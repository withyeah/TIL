# pyformat
# '{} {}'.format('one', 'two')
name = '김예랑'
e_name = 'KIM'
print("안녕하세요 {0}입니다. My name is {1}.".format(name, e_name))

# f-string python 3.6
print(f'안녕하세요 {name}입니다. My name is {e_name}.')

#이렇게 할 수도 있다
name = "김예랑"
print("안녕하세요. " + name + "입니다.")


#lotto
#오늘의 행운의 번호는 뭐뭐 입니다.
import random
numbers = list(range(1, 46))
lotto = random.sample(numbers, 6)
print("오늘의 행운의 번호는 {0}입니다".format(lotto))
print(f"오늘의 행운의 번호는 {lotto}입니다.")
print('오늘의 행운의 번호는 ' + " ".join("{0}".format(i) for i in lotto) + " 입니다.")
print('오늘의 행운의 번호는 ' + "".join(f"{lotto}") + " 입니다.")


