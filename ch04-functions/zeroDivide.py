# 예외 처리
def spam(divide_by):
    try: # 오류가 발생할 가능성이 있는 코드
        # Any code in this block that causes ZeroDivisionError won't crash the program:
        return 42 / divide_by
    except ZeroDivisionError: # 오류가 발생하면 프로그램 실행
        # If ZeroDivisionError happened, the code in this block runs:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))