def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1

    print(result, end=' ')
    return result


num = int(input())

print(num, end=' ')

while num != 1:
    num = collatz(num)

