print("hello world") # hello world

print(2 ** 3) # 지수
print(22 % 8) # 나머지
print(22 // 8) # 정수 나눗셈
print(22 / 8) # 나누기
print(3 * 5) # 곱하기
print(5 - 2) # 빼기
print(2 + 2) # 더하기

print("python" + "study") # 문자열 연결
print("I wanna go " + "\n" + "home! " * 5) # 문자열 복제

spam = 40 # 변수 저장
eggs = 2
print(spam)
print(spam + eggs)
spam = spam + 2
print(spam)

spam = "hello" # 변수 덮어쓰기
print(spam)

name = 'python'
print(type(42)) # type() 함수, 데이터 유형을 반환
print(type(42.0))
print(type(name))
print(type(len(name)))

print(round(3.14)) # round 함수, 부동 소수점 값을 인수로 받아 가장 가까운 정수를 반환
print(round(7.7))
print(round(3.14, 1)) # 반올림할 소수점 자릿수 지정 가능
print(round(7.7777, 3))

print(abs(25)) # 인수의 절댓값 반환
print(abs(-25))
print(abs(-3.14))
print(abs(0))

print(bin(1234)) # bin 함수, 10을 2진수(binary)로 변환
print(hex(1234)) # hex 함수, 10을 16진수(hexadecimal)로 변환