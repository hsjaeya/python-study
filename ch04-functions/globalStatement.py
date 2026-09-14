# 전역 선언

def spam():
    global eggs
    eggs = 'spam'

eggs = 'global'
spam()
print(eggs)  # Prints 'spam'