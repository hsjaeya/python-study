# This program says hello and asks for my name.

print('Hello, world!') # print() 함수, 괄호 안의 문자열을 출력
print('What is your name?')  # Ask for their name.
my_name = input('>') # input() 함수, 사용자가 입력하고 enter키를 누를때 까지 기다림
print('It is good to meet you, ' + my_name)
print('The length of your name is:')
print(len(my_name)) # len() 함수, 문자열 값을 전달하면 문자 수를 정수로 반환
print('What is your age?')  # Ask for their age.
my_age = input('>')
print('You will be ' + str(int(my_age) + 1) + ' in a year.')
# str() 함수, 문자열로 형 변환
# int() 함수, 정수로 형 변환
# float() 부동 소수점으로 형 변환