print('hello')

print('1. 숫자자료형')

print(5)
print(-10)
print(3.14)
print(1000)
print(5+3)
print(2*8)
print(3*(3+1))

print('2. 문자열 자료형')

print('풍선')
print("나비")
print("ㅋㅋㅋㅋㅋㅋ")
print("ㅋ"*6)

print('3. boolean 자료형')

print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)
print(not False)
print(not (5 > 10))

print('4. 변수')

print("우리집 강아지의 이름은 연탄이예요.")
print("연탄이는 4살이며, 산책을 아주 좋아해요.")
print("연탄이는 어른일까요? False")

animal = "고양이"
name = "솜솜이"
age = 4
hobby = "간식"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "예요.")
hobby = "공놀이"
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요.")
print(name + "는 어른일까요? " + str(is_adult))

# 우리집 고양이의 이름은 솜솜이예요.
# 솜솜이는 4살이며, 공놀이을 아주 좋아해요.
# 솜솜이는 어른일까요? True

print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요.")

# 솜솜이 는  4 살이며,  공놀이 을 아주 좋아해요.
# ,는 띄어쓰기가 들어간 채로 출력됨. 정수 그대로 출력돼서 age 그대로 써도 됨.

print('5. 주석')

'''이렇게
하면
여러 무장이
주석처리
됩니다.'''

# 맥 기준 command + / 

print('퀴즈 #1')
# 변수를 이용하여 다음 문장을 출력하시오
# 변수명 : station
# 변수값 : 사당, 신도림, 인천공항 순서대로 입력
# 출력문장 : XX행 열차가 들어오고 있습니다.

station = "사당"
print(station + "행 열차가 들어오고 있습니다.") 
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.") 
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")
