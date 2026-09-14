# None 값(다른 언어의 null , nil, undefined)
spam = print('Hello!')
print(None == spam)

# 명명된 매개변수

# end
print('Hello', end='') # 줄바꿈 제거(줄 바꿈 문자를 다른 문자열로 변경)
print('World')

# sep
print('cats', 'dogs', 'mice', sep=',') # 기본 구분 문자열 변경

# 지역, 전역 스코프

# 전역 스코프에 있는 코드는 지역 변수를 사용할 수 없음(오류)
def spam():
  eggs = 'sss' 
spam()
print(eggs)

# 지역 스코프에 있는 코드는 다른 지역 스코프의 변수를 사용할 수 없음
def spam():
    eggs = 'SPAMSPAM'
    bacon()
    print(eggs)  # Prints 'SPAMSPAM'

def bacon():
    ham = 'hamham'
    eggs = 'BACONBACON'

spam()

# 지역 스코프에 있는 코드는 전역 변수를 사용할 수 있음
def spam():
    print(eggs)  # Prints 'GLOBALGLOBAL'
eggs = 'GLOBALGLOBAL'
spam()
print(eggs)
