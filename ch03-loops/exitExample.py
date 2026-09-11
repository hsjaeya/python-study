# sys.exit()를 사용하여 프로그램을 조기에 종료하기
import sys

while True:
    print('Type exit to exit.')
    response = input('>')
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')