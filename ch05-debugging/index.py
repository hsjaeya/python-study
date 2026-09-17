# raise문, 예외를 발생시킬 수 있다
# raise Exception('This is the error message.') # 예외 오류 메시지를 표시

# assert문, 조건이 false면 AssertionError를 던지고 프로그램 종료

# true일때
ages = [26, 57, 92, 54, 22, 15, 17, 80, 47, 73]
ages.sort()
print(ages)
assert ages[0] <= ages[-1]

# false일때
ages.reverse()
print(ages)
assert ages[0] <= ages[-1] # AssertionError 발생