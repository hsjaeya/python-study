# 부울 값
spam = True
spam = False
print(spam)

# 비교 연산자
print(5 == 5) # 같다
print(1 != 2) # 같지 않다
print(10 < 5) # ~보다 작다
print(1 + 1 > 4 + 8) # ~보다 크다
print(4 <= 5) # 이하
print(5 >= 4) # 이상

# 불리언 연산자
print(True and True) # and, 둘다 참일때 참
print(True and False)
print(True or True) # or, 하나라도 참일때 참
print(True or False)
print(not True) # not, 반대 불리언 값으로
print(not not not not True)

# 코드 블록
username = 'Mary'
password = 'swordfish'
if username == 'Mary':
    print('Hello, Mary')
    if password == 'swordfish':
        print('Access granted.')
    else:
        print('Wrong password.')

# 들여쓰기가 증가하면 새로운 블록이 시작됩니다.
# 블록은 다른 블록을 포함할 수 있습니다.
# 블록의 들여쓰기가 0이 되거나 상위 블록의 들여쓰기와 같아지면 블록이 끝납니다.
# 파이썬은 콜론으로 끝나는 문장 바로 뒤에 새로운 블록이 와야 한다고 예상합니다.

# 흐름 제어문
name = 'Carol'
age = 3000
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')

spam = int(input(">"))
if spam == 1:
    print("hello")
elif spam == 2:
    print("Howdy")
else:
    print("Greetings")   