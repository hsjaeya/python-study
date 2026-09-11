# while 루프문
spam = 0
while spam < 5: # 거짓이면 정지
    print('Hello, world.')
    spam = spam + 1

name = ''
while not name:
    print('Enter your name:')
    name = input('>')
print('How many guests will you have?')
num_of_guests = int(input('>'))
if num_of_guests:
    print('Be sure to have enough room for all your guests.')
print('Done')
#  0 , 0.0 , 그리고 '' (빈 문자열)은 거짓으로 간주

# 가우스보다 빠르게 계산 하는 법
total = 0
for num in range(101):
    total = total + num
print(total)

# range() 함수의 인수

# 인수가 2개일 때
for i in range(12, 16): # 첫 번째 인수는 for 루프의 변수가 시작되는 위치, 두 번째 인수는 루프를 종료할 숫자까지의 범위
    print(i)

# 인수가 3개일 때
for i in range(0, 10, 2): #  첫 번째와 두 번째 인수는 시작 값과 종료 값, 세 번째 인수는 단계(step) 인수, 단계는 각 반복 후 변수가 증가하는 양
    print(i)

# 인수에 음수를 사용하여 감소
for i in range(5, -1, -1):
    print(i)