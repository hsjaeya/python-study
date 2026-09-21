# dictionary data type
my_cat = {'size': 'fat', 'color': 'gray', 'age': 17}
print(my_cat['size'])
print('My cat has ' + my_cat['color'] + ' fur.')

spam = {12345: 'Luggage Combination', 42: 'The Answer'} # 정수도 key가 될 수 있음
print(spam[12345])
print(spam[42])

spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
print(spam == bacon) # 같지 않다
eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
print(eggs == ham) # 같다

# keys, values 반환
spam = {'color': 'red', 'age': 42}
for v in spam.values(): # values 반환
    print(v)

for k in spam.keys(): # key 반완
    print(k)

print('color' in spam.keys())
print('age' not in spam.keys())
print('red' in spam.values())

for i in spam.items(): # key, values 반환
    print(i)

spam = {'color': 'red', 'age': 42}
print(spam.keys())
list(spam.keys()) # list로 반환

spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key: ' + str(k) + ' Value: ' + str(v))

# key 존재 여부 확인
picnic_items = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnic_items.get('cups', 0)) + ' cups.') # 키가 존재하지 않을시 대체 값을 지정하는 get() method
print('I am bringing ' + str(picnic_items.get('eggs', 0)) + ' eggs.')

# 기본 values 설정
spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
print(spam)

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')  # Sets 'color' key to 'black'
print(spam)
spam.setdefault('color', 'white')  # Does nothing
print(spam)

