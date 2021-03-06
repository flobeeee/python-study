print('1. 연산자')

print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3)
print(5 % 3)
print(10 % 3)
print(5//3)  # 몫구하기
print(10//3)

print(10 > 3)
print(4 >= 7)
print(10 < 3)
print(5 <= 5)

print(3 == 3)
print(4 == 2)
print(3 + 4 == 7)

print(1 != 3)
print(not (1 != 3))

print((3 > 0) and (3 < 5))
print((3 > 0) & (3 < 5))
print((3 > 0) or (3 < 5))
print((3 > 0) | (3 < 5))

print(5 > 4 > 3)
print(5 > 4 > 7)

print('2. 간단한 수식')

print(2 + 3 * 4)  # 14
print((2 + 3) * 4)  # 20
number = 2 + 3 * 4
print(number)  # 14

number = number + 2
print(number)  # 16

number += 2
print(number)  # 18

number *= 2
print(number)  # 36

number /= 2
print(number)  # 18.0

number -= 2
print(number)  # 16.0

number %= 2
print(number)  # 0

print('3. 숫자처리 함수')

print(abs(-5))  # 5 절대값
print(pow(4, 2))  # 4^2 = 16 제곱
print(max(5, 12))  # 12 최대값
print(min(5, 12))  # 5 최소값
print(round(3.14))  # 3 반올림
print(round(4.89))  # 5
print(round(4.89, 1))  # 4.9 소수점 첫째 자리까지 표시

from math import * # math 라이브러리에 있는 모든 걸 이용하겠다는 뜻

print(floor(4.99)) # 내림 4
print(ceil(3.14)) # 올림 4
print(sqrt(16)) # 제곱근 4.0

print('4. 랜덤 함수')

from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 0 ~ 10 미만의 임의의 값 생성
print(int(random() * 10) + 1) # 1 ~ 10 이하

print(int(random() * 45) + 1) # 1 ~ 45 이하 (로또)
print(randrange(1, 46)) # 1 ~ 45 이하
print(randint(1, 45)) # 1 ~ 45 이하

print('퀴즈 #2')

# 당신은 최근에 코딩 스터디 모임을 새로 만들었습니다.
# 월 4회 스터디를 하는데 3번은 온라인으로 하고, 1번은 오프라인으로 하기로 했습니다.
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램을 작성하시오.

# 조건 1: 랜덤으로 날짜 뽑기
# 조건 2: 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 함
# 조건 3: 매월 1~3일은 스터디 준비를 해야하므로 제외

# (출력문 예제)
# 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다.

# from random import * <- 위해 있어서 주석처리
day = randint(4, 28)
print('오프라인 스터디 모임 날짜는 매월 ' + str(day) +'일로 선정되었습니다.')
