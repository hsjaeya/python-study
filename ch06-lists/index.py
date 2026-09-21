import random
import copy

# list 데이터 타입
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)

# indexs
for i in spam: 
    print(i)

print('The ' + spam[1] + ' ate the ' + spam[0] + '.')

# 중첩된 list
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]

print(spam[0])
print(spam[0][1])
print(spam[1][4])

# 음수 index
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[-1])
print(spam[-3])
print('The ' + spam[-1] + ' is afraid of the ' + spam[-3] + '.')

# slices
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[0:4])
print(spam[1:3])
print(spam[0:-1])
print(spam[:2])
print(spam[:])

# len 함수
spam = ['cat', 'dog', 'moose']
print(len(spam))

# value 업데이트
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = "python"
print(spam)

spam[2] = spam[1]
print(spam)

spam[-1] = 12345
print(spam)

# 리스트 연결 및 복제
print([1, 2, 3] + ['A', 'B', 'C'])
print(['X', 'Y', 'Z'] * 3)
spam = [1, 2, 3]
spam = spam + ['A', 'B', 'C']
print(spam)

# del 문
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
print(spam)
del spam[2]
print(spam)

for i in [0, 1, 2, 3]:
    print(i)

supplies = ['pens', 'staplers', 'flamethrowers', 'binders']

# list의 index만큼 반복
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# in, not in 연산자
print('howdy' in ['hello', 'hi', 'howdy', 'heyas'])
spam = ['hello', 'hi', 'howdy', 'heyas']
print('cat' in spam)
print('howdy' not in spam)
print('cat' not in spam)

# 다중 할당 트릭

# 하나씩 할당
cat = ['fat', 'gray', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]

# 한 번에 할당(코드가 간결해짐)
# 변수와 리스트의 개수는 정확히 일치해야함
cat = ['fat', 'gray', 'loud']
size, color, disposition = cat

# list 항목 열거
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

# 무작위 선택
pets = ['Dog', 'Cat', 'Moose']
print(random.choice(pets))
print(random.choice(pets))
print(random.choice(pets))

# 무작위 재정렬
people = ['Alice', 'Bob', 'Carol', 'David']
random.shuffle(people)
print(people)
random.shuffle(people)
print(people)

# 복합 할당 연산자
spam = 42

spam += 1
spam -= 1
spam *= 1
spam /= 1
spam %= 1

spam = 'Hello,'
spam += ' world!'  # Same as spam = spam + 'world!'
print(spam)
bacon = ['Zophie']
bacon *= 3  # Same as bacon = bacon * 3
print(bacon)

# method

# 값 찾기
spam = ['hello', 'hi', 'howdy', 'heyas']
print(spam.index("hello"))
print(spam.index('heyas'))
spam = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
print(spam.index('Pooka')) # 같은 값이 여러개라면 가장 처음 값을 선택

# 값 추가
spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)

spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken') # 삽입될 값의 인덱스, 삽입될 값
print(spam)

# 값 삭제
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
print(spam)

spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
spam.remove('cat') # 같은 값이 여러개라면 가장 처음 값을 삭제
print(spam)

# 값 정렬
spam = [2, 5, 3.14, 1, -7]
spam.sort()
print(spam)

spam = ['Ants', 'Cats', 'Dogs', 'Badgers', 'Elephants']
spam.sort()
print(spam)

spam.sort(reverse=True) # 역순 정렬
print(spam)

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort() # 대문자 우선
print(spam)

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower) # 일반적인 알파벳 순서로 정렬해야 하는 경우 str.lower 사용
print(spam)

# 값 역정렬
spam = ['cat', 'dog', 'moose']
spam.reverse()
print(spam)

# 파이썬의 들여쓰기 규칙 예외

spam = ['apples',
 'oranges',
                  'bananas',
'cats'] # 소스 코드 파일에서 여러 줄에 걸쳐 나타날 수 있음
print(spam[0])

# 줄 바꿈
print('Four score and seven ' + \
      'years ago...')

# 단락 평가를 사용하는 boolean 연산자
spam = ['cat', 'dog']
if spam[0] == 'cat':
    print('A cat is the first item.')
else:
    print('The first item is not a cat.')

spam = []
if len(spam) > 0 and spam[0] == 'cat': # len(spam) > 0이 이미 거짓이기 때문에 뒷부분은 계산하지 않음
    print('A cat is the first item.')
else:
    print('The first item is not a cat.')

# Sequence Data Types
name = 'Zophie'
print(name)
print(name[-2])
print(name[0:4])
print('Zo' in name)
print('z' in name)
print('p' not in name)
for i in name:
    print('* * * ' + i + ' * * *')

# 문자열 변환
name = 'Zophie a cat'
new_name = name[0:7] + 'the' + name[8:12]
print(new_name)

# list 변경
eggs = ['A', 'B', 'C']
eggs = ['x', 'y', 'z']
print(eggs)

# list 수정(in-place 변경)
eggs = ['A', 'B', 'C']
del eggs[2]
del eggs[1]
del eggs[0]
eggs.append('x')
eggs.append('y')
eggs.append('z')
print(eggs)

#tuple data type 
eggs = ('hello', 42, 0.5) # 튜플은 변경이 불가능함
print(eggs[0])
print(eggs[1:3])
print(len(eggs))

print(type(('hello',))) # 괄호 안에서 쉼표를 붙여야지 튜플로 인식함
print(type(('hello'))) # 일반적인 string

# list와 tuple 타입 변환
print(tuple(['cat', 'dog', 5]))
print(list(('cat', 'dog', 5)))
print(list('hello'))

# references
spam = 42
eggs = spam
spam = 99
print(spam)
print(eggs)

spam = [0, 1, 2, 3]
eggs = spam
eggs[1] = 'Hello!'

print(spam)
print(eggs)
# 파이썬에서 변수는 값을 직접 저장하지 않는다. 변수는 값에 대한 참조만 저장한다
# 파이썬에서 '=' 연산자는 참조만 복사한다. 값 자체를 복사하지 않는다

# copy()와 deepcopy() 함수
spam = ['A', 'B', 'C']
cheese = copy.copy(spam)  # Creates a duplicate copy of the list
cheese[1] = 42  # Changes cheese
print(spam) # The spam variable is unchanged.
print(cheese) # The cheese variable is changed.