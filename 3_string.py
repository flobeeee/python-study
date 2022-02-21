from cmath import pi


print('1. 문자열')

sentence = '나는 직장인입니다.'
print(sentence)
sentence2 = "파이썬은 재밌어요."
print(sentence2)
sentence3 = """
나는 직장인이고,
파이썬은 재밌어요.
"""
print(sentence3)

print('2. 슬라이싱')

jumin = '901223-1234567'

print('성별: ' + jumin[7])
print('연: ' + jumin[0:2])
print('월: ' + jumin[2:4])
print('일: ' + jumin[4:6])

print('생년월일: ' + jumin[:6])  # 처음부터 인덱스6 직전까지
print('뒤 7자리: ' + jumin[7:])  # 7부터 끝까지
print('뒤 7자리 (뒤에부터): ' + jumin[-7:])  # 뒤 7자리(뒤에부터)

print('3. 문자열 처리 함수')

python = 'Python is Amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace('Python', 'Java'))

index = python.index('n')
print(index)
index = python.index('n', index + 1)
print(index)

print(python.find('n'))
# print(python.index('Java')) # 에러떠서 다음 hi 가 안찍힘
print('hi')

print(python.count('n'))

print('4. 문자열포맷')

print('a' + 'b')
print('a', 'b')

print('방법 1')
print('나는 %d살 입니다.' % 20)  # d 정수값
print('나는 %s을 좋아해요.' % '파이썬')  # s 문자열
print('apple은 %c로 시작해요.' % 'a')  # 캐릭터로 한 글자만 받겠다는 뜻

# %s
print('나는 %s 살입니다.' % 20)
print('나는 %s색과 %s색을 좋아해요.' % ('파란', '빨간'))

print('방법 2')
print('나는 {}살 입니다.'.format(20))
print('나는 {}색과 {}색을 좋아해요.'.format('파란', '빨간'))

print('방법 3')
print('나는 {age}살이며, {color}색을 좋아해요'.format(age=20, color='빨간'))

print('방법 4')
age = 20
color = '빨간'
print(f'나는 {age}살이며, {color}색을 좋아해요')

print('5. 탈출문자')

# \n : 줄바꿈(역슬래시)
print('백문이 불여일견\n백견이 불여일타')

# \" \' : 문장 내에서 따옴표
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \
print('C:\\users\\user0\\desktop\\pythonworkspace')

# \r : 커서를 맨 앞으로 이동
print('Red Apple\rPine')  # PineApple

# \b : 백스페이스 (한 글자 삭제)
print('Redd\b Apple')  # Red Apple

# \t : 탭
print('Red\tApple')

print('퀴즈 #3')

# 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.
# 예 ) http://naver.com
# 규칙1 : http:// 부분은 제외 -> naver.com
# 규칙2 : 처음 만나는 점(.)이후 부분은 제외 -> naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자갯수 + 글자 내 'e'갯수 + "!"로 구성
# 예 ) 생성된 비밀번호 : nav51!

url = 'http://naver.com'
rule1 = url[7:]
rule2 = rule1[:rule1.find('.')]
rule3 = rule2[0:3] + str(len(rule2)) + str(rule2.count('e')) + '!'
print(f'생성된 비밀번호 : {rule3}')
