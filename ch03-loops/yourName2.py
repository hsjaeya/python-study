# break 문
while True: # 무한 반복
    print('Please type your name.')
    name = input('>')
    if name == 'your name':
        break # 루프 절에서 즉시 빠져나옴
print('Thank you!')