while True:
    print('Who are you?')
    name = input('>')
    if name != 'Joe':
        continue # 반복문의 시작 부분으로 이동
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input('>')
    if password == 'swordfish':
          break
print('Access granted.')   