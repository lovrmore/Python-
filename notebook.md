## 字符串

```python
# 以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写，其余为小写

name = 'adDa lovelace'

print(name.title())

# 将字符串改为全部大写
print(name.upper())

# 将字符串改为全部小写
print(name.lower())

first_name = 'ada'
last_name = 'lovelace'
full_name = first_name + " " + last_name

print(full_name)

print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

# 使用制表符或换行符来添加空白

print('Python')

# 在字符串中添加制表符，\t
print('\tPython')

# 在字符串中添加换行符，\n
print("Languages:\nPython\nC\nJavaScript")

# 组合
print("Languages:\n\tPython\n\tC\n\tJavaScript")

#删除空白
favorite_language = 'python '
print(favorite_language)

print(favorite_language.rstrip())
```

## 数字

1. 整数

2. 浮点数

```python
>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4
>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004
```

**p.s.** 使用函数**str()**避免类型错误

```python
age = 23
#message = 'Happy ' + age + 'rd birthday!'
message = 'Happy ' + str(age) + 'rd birthday!'
print(message)
```

## 列表

```python
#列表
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
```
### 访问列表元素
```python
print(bicycles[0])
```

**p.s.** 

1. 请求列表元素时，Python只返回该元素（可调用元素方法），而不包括方括号和引号
```python
print(bicycles[0].title())
```

2. 左索引从0开始，右索引从-1开始

3. 特殊索引
```python
print(bicycles[-1])
```

### 修改列表元素

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)
```

### 在列表末尾添加元素

```python
motorcycles.append('ducati')
print(motorcycles)
```

```python
motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)
```

### 在列表中插入元素

```python
motorcycles = ['honda', 'yamaha', 'suzuki']

motorcycles.insert(0, 'ducati')
print(motorcycles)
```

### 从列表中删除元素

#### 使用del语句删除元素

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)
```

**p.s.** 

1. 知道要删除的元素在列表中的位置
2. 删除后无法访问被删除的元素

#### 使用方法pop()删除元素

```python
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

last_owned = motorcycles.pop()
print('The last motorcycle I owned was a ' + last_owned.title() + '.')

first_owned = motorcycles.pop(0)
print('The first motorcycle I owned was a ' + first_owned.title() + '.')
```

**p.s.** 

1. pop()内参数为空，默认为删除列表末尾的元素
2. 删除后可以继续访问元素，但是被弹出的元素不再在列表里
3. 删除列表末尾的元素相当于弹出栈顶元素

#### 根据值删除元素

```python
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

# motorcycles.remove('ducati')
# print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print('\nA ' + too_expensive.title() + ' is too expensive for me.')

```

**p.s.**

1. 删除后无法访问被删除的元素
2. 只删除第一个指定的值
3. 如果要删除的值可能在列表中出现多次，就需要
使用循环来判断是否删除了所有这样的值

### 组织列表

#### 使用方法sort()对列表进行永久性排序

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()

# 反序
cars.sort(reverse = True)
print(cars)
```

**p.s.** 

1. 对列表元素排列顺序的修改是永久性的

#### 使用函数sorted()对列表进行临时排序

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']

print('Here is the original list:')
print(cars)

print('\nHere is the sorted list:')
print(sorted(cars))

print('\nHere is the original list again:')
print(cars)
```

**p.s.**

1. 保留列表元素原来的排列顺序
2. 按与字母顺序相反的顺序显示列表，也可向函数sorted()传递参数reverse=True

#### 反转列表元素

```python
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
```

**p.s.**

1. 永久性地修改列表元素的排列顺序
2. **是反转而不是反序**

#### 确定列表的长度

```python
>>> cars = ['bmw', 'audi', 'toyota', 'subaru']
>>> len(cars)
4
```

#### 索引错误

1. 访问最后一个元素的方式会导致错误
2. 发生索引错误却找不到解决办法时，请尝试将列表或其长度打印出来,列表可能与你以为的截然不同

### 操作列表

#### 遍历列表

```python
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    # print(magician)

    print(magician.title() + ', that was a great trick!')
    print("I can't wait to see your next trick, " + magician.title() + '.\n')
```

#### 创建数值列表

##### 使用函数range()

从指定的第一个值开始数，并在到达你指定的第二个值后停止，因此输出不包含第二个值

```python
for value in range(1, 5):   
    print(value)
```

##### 使用函数range()创建数字列表

```python
numbers = list(range(1,6))
print(numbers)

# 指定步长
even_numbers = list(range(2,11,2))
print(even_numbers)

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)
```

##### 对数字列表执行简单的统计计算

```python
>>> digits = [1,2,3,4,5,6,7,8,9,0]
>>> min(digits)
0
>>> max(digits)
9
>>> sum(digits)
45
```

##### 列表解析

[expression for iter_val in iterable]

[expression for iter_val in iterable if cond_expr]

```python
squares = [value**2 for value in range(1,11)]
print(squares)

num = [value for value in range(3,31) if value % 3 == 0]
print(num)
```

#### 使用列表的一部分

##### 切片

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']

# 第1~3个元素
# print(players[0:3])

# 第2~4个元素
# print(players[1:4])

# 第1~4个元素
# print(players[:4])

# 第3~个元素
# print(players[2:])

# 第3~个元素
# print(players[-3:])

print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())
```

**p.s.** 

1. 到达指定的第二个索引前面的元素后停止

##### 遍历切片

```python
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print('Here are the first three players on my team:')
for player in players[:3]:
    print(player.title())
```

##### 复制列表

同时省略起始索引和终止索引（[:]）

```python
my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods[:]
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print('My favorite foods are:')
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
```

## 元组

### 定义元组

```python
dimensions = (200, 50)
# dimensions[0] = 250

# print(dimensions[0])
# print(dimensions[1])
```

**p.s.**

1. 不能给元组的元素赋值,但可以给存储元组的变量赋值

### 遍历元组中的所有值

```python
dimensions = (200, 50)

for dimension in dimensions:
    print(dimension)
```

### 修改元组变量

相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都
不变，可使用元组

```python
dimensions = (200, 50)

print('Original dimensions')
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print('\nModified dimensions')
for dimension in dimensions:
    print(dimension)
```

## if语句

### 条件测试

值为**True**或**False**的表达式

True执行，false忽略

```python
age = 12

# if age < 4:
#     print('Your admission cost is $0.')
# elif age < 18:
#     print('Your admission cost is $5.')
# else:
#     print('Your admission cost is $10')

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10  
# else:
#     price = 5
elif age >= 65:
    price = 5

print('Your admission cost is $' + str(price) + '.')
```

```python
# requested_topping = 'mushrooms'

# if requested_topping != 'anchovies':
#     print('Hold the anchovies!')
    
# requested_toppings = ['mushrooms','extra cheese']

# if 'mushrooms' in requested_toppings:
#     print('Adding mushrooms')
# if 'pepperoni' in requested_toppings:
#     print('Adding pepperoni.')
# if 'extra cheese' in requested_toppings:
#     print('Adding extra cheese')

# print('\nFinished making your pizza!')

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('Sorry, we are out of green peppers right now.')
    else:
        print('Adding ' + requested_topping + '.')
    
print('\nFinished making your pizza!')
```

**p.s.**

1. 省略 else 代码块更清晰

## 字典

### 简单的字典

```python
alien_0 = {'color':'green', 'points':5}

print(alien_0['color'])
print(alien_0['points'])
```
### 使用字典

#### 访问字典中的值

指定字典名和放在方括号内的键

#### 添加键—值对

```python
alien_0 = {'color':'green', 'points':5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```

**p.s.**

1. 键—值对的排列顺序与添加顺序不同,Python不关心键—值对的添加顺序，而只关心键和值之间的关联关系

#### 创建空字典

```python
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
```

#### 修改字典中的值

```python
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print('Original x_position: ' + str(alien_0['x_position']))

# Move the alien to the right
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print('New x-position: ' + str(alien_0['x_position']))
```

#### 删除键—值对

```python
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
```

**p.s.**

1. 删除的键—值对永远消失

#### 由类似对象组成的字典

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite languages is " + 
    favorite_languages['sarah'].title() + 
    '.')

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + '.')
```

### 遍历字典

#### 遍历所有的键—值对

```python
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print('\nKey: ' + key)
    print('Value: ' + value)
```

#### 遍历字典中的所有键

```python
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(' Hi ' + name.title() +
        ', I see your favorite language is ' +
        favorite_languages[name].title() + '!')
```

#### 按顺序遍历字典中的所有键

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name in sorted(favorite_languages.keys()):
    print(name.title() + ', thank you for taking the poll.')
```

#### 遍历字典中的所有值

```python
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# 不考虑重复
# print('The following languages have been mentioned:')
# for language in favorite_languages.values():
#     print(language.title())

# 考虑重复
# 剔除重复项，可使用集合（set）
# 集合类似于列表，但每个元素都必须是独一无二的
print('The following languages have been mentioned:')
for language in set(favorite_languages.values()):
    print(language.title())
```

### 嵌套

#### 字典列表

```python
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     print(alien)

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print('...')

# Show how many aliens have been created.
# print('Total number of aliens: ' + str(len(aliens)))
```

**p.s.**

1. 在这个列表中，所有字典的结构都需相同，这样才可以遍历这个列表，并以相同的方式处理其中的每个字典

#### 在字典中存储列表

```python
# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings' : ['mushrooms', 'extra cheese'],
}

# Summarize the order.
print('You ordered a ' + pizza['crust']+ '-crust pizza ' +
    'with the following toppings:')

for topping in pizza['toppings']:
    print('\t' + topping)
```

```python
favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print('\n' + name.title() + "'s favorite languages are:")
    for language in languages:
        print('\t' + language.title())
```

**p.s.**

1. 嵌套不应太多

#### 在字典中存储字典

```python
user = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'einstein',
        'location': 'princeton',
    },
}

for username, user_info in user.items():
    print('\nUsername: ' + username)
    full_name = user_info['first'] + ' ' + user_info['last']
    location = user_info['location']

    print('\tFull name: ' + full_name.title())
    print('\tLocation: ' + location.title())
```

**p.s.**

1. 嵌套结构尽量相同

## 用户输入和while循环

```python
message = input('Tell me something, and I will repeat it back to you: ')
print(message)
```

### 函数 input()的工作原理

#### 编写清晰的程序

```python
# name = input('Please enter your name: ')
# print('Hello, ' + name + '!')

prompt = 'If you tell us who you are, we can personalize the messages you see.'
prompt += '\nWhat is your first name? '

name = input(prompt)
print('\nHello, ' + name + '!')
```

**p.s.**

1. 通过在提示末尾（这里是冒号后面）包含一个空格，可将提示与用户输入分开，让用户清楚地知道其输入始于何处

#### 使用 int()来获取数值输入

```python
height = input('How tall are you, in inches? ')
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
```

#### 求模运算符

```python
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print('\nThe number ' + str(number) + ' is even.')
else:
    print('\nThe number ' + str(number) + ' is odd.')
```

### while 循环简介

for循环用于针对集合中的每个元素都一个代码块，而while循环不断地运行，直到指定的条件不满足为止

#### 使用 while 循环

```python
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
```

#### 让用户选择何时退出

```python
prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end the program. "

message = ''
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)
```

#### 使用标志

```python
prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
```

#### 使用 break 退出循环

```python
prompt = '\nPlease enter the name of a city you have visited:'
prompt += "\n(Enter 'quit' when you are finished. )"

while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + '!')
```

**p.s.**

1. 可以在任何Python循环中都可使用break语句

#### 在循环中使用 continue

```python
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)
```

**p.s.**

1. 返回到循环开头，并根据条件测试结果决定是否继续执行循环

### 使用 while 循环来处理列表和字典

for循环是一种遍历列表的有效方式，但在for循环中不应修改列表，否则将导致Python难以跟踪其中的元素。要在遍历列表的同时对其进行修改，可使用while循环。通过将while循环同列表和字典结合起来使用，可收集、存储并组织大量输入，供以后查看和显示

#### 在列表之间移动元素

```python
# Start with users that need to be verified,
#  and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print('Verifying user: ' + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.
print('\nThe following users have been confirmed:')
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
```

#### 删除包含特定值的所有列表元素

```python
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
```

#### 使用用户输入来填充字典

```python
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input('\nWhat is your name? ')
    response = input('Which mountain would you like to climb someday? ')

    # Store the response in the dictionary:
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input('Would you like to let another person respond? (yes/ no) ')
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print('\n--- Poll Results ---')
for name, response in responses.items():
    print(name + ' would like to climb ' + response + '.')
```

## 函数

### 定义函数

```python
def greet_user():
    """Display a simple greeting."""
    print('Hello!')

greet_user()
```

### 向函数传递信息

```python
def greet_user(username):
    """Display a simple greeting."""
    print('Hello, ' + username.title() + '!')

greet_user('jesse')
```

### 传递实参

三种方法：

1. 位置实参

2. 关键字实参

3. 列表和字典

#### 位置实参

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet('hamster', 'harry')
```

##### 调用函数多次

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
```

##### 位置实参的顺序很重要

#### 关键字实参

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

describe_pet(animal_type = 'hamster', pet_name = 'harry')
```
**p.s.**

1. 使用关键字实参时，务必准确地指定函数定义中的形参名

#### 默认值

```python
def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet."""
    print('\nI have a ' + animal_type + '.')
    print('My ' + animal_type + "'s name is " + pet_name.title() + '.')

# describe_pet('hamster', 'harry')
# describe_pet('dog', 'willie')

describe_pet(pet_name = 'harry')
```

**p.s.**

1. 使用默认值时，在形参列表中必须先列出没有默认值的形参，再列出有默认值的实参。这让Python依然能够正确地解读位置实参

### 返回值

#### 返回简单值 

```python
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
```
#### 让实参变成可选的

```python
def get_formatted_name(first_name, last_name, middle_name = ''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name +' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)
```

#### 返回字典

```python
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)
```

### 传递列表

```python
def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
```

#### 在函数中修改列表

```python
# # Start with some designs that need to be printed.
# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()

#     # Simulate creating a 3D print from the design.
#     print('Printing model: ' + current_design)
#     completed_models.append(current_design)

# # Display all completed models.
# print('\nThe following models have been printed:')
# for completed_model in completed_models:
#     print(completed_model)

def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    More each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        # Simulate creating a 3D print from the design.
        print('Printing model: ' + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print('\nThe following models have been printed:')
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
```

#### 禁止函数修改列表

function_name(list_name[:])

向函数传递列表的副本而不是原件

#### 传递任意数量的实参

```python
# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extre cheese')

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print('\nMaking a pizza with the following toppings:')
    for topping in toppings:
        print('-' + topping)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extre cheese')
```

#### 结合使用位置实参和任意数量实参

```python
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')
print(user_profile)
```

#### 导入整个模块

import module_name

module_name.function_name()

```python
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

#### 导入特定的函数

1. from module_name import function_name
2. from module_name import function_0, function_1, function_2

function_name()

```python
from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

#### 使用 as 给函数指定别名

from module_name import function_name as fn

```python
from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
```

#### 使用 as 给模块指定别名

import module_name as mn

```python
import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

#### 导入模块中的所有函数

from module_name import * 

```python
from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```

**p.s**

不建议此用法，要么只导入你需要使用的函数，要么导入整个模块并使用句点表示法

## 类

### 创建和使用类

#### 创建 Dog 类

```python
class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + ' is now sitting.')

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + ' rolled over!')
```

**p.s.**

1. 每个方法都必须先传入self

#### 根据类创建实例

##### 访问属性

```python
my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
```

##### 调用方法

```python
my_dog.sit() 
my_dog.roll_over()
```

##### 创建多个实例

```python
my_dog = Dog('willie', 6) 
your_dog = Dog('lucy', 3) 
 
print("My dog's name is " + my_dog.name.title() + ".") 
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit() 
 
print("\nYour dog's name is " + your_dog.name.title() + ".") 
print("Your dog is " + str(your_dog.age) + " years old.") 
your_dog.sit()
```

#### 使用类和实例

##### Car 类

```python
class Car():
    """A simple attempt attributes to describe a car."""

    def __init__(self, make, model, year):
        """Initialize attributes descriptive name."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
```

##### 给属性指定默认值

```python
class Car():
    """A simple attempt attributes to describe a car."""

    def __init__(self, make, model, year):
        """Initialize attributes descriptive name."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's milleage."""
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
```

#### 修改属性的值

##### 直接修改属性的值

```python
my_new_car.odometer_reading = 23 
my_new_car.read_odometer()
```

##### 通过方法修改属性的值

```python
    def update_odometer(self, mileage): 
        """将里程表读数设置为指定的值""" 
        self.odometer_reading = mileage

my_new_car.update_odometer(23) 
my_new_car.read_odometer()
```

##### 通过方法对属性的值进行递增

```python
    def increment_odometer(self, miles): 
        """将里程表读数增加指定的量""" 
        self.odometer_reading += miles

my_used_car = Car('subaru', 'outback', 2013) 
print(my_used_car.get_descriptive_name()) 
 
my_used_car.update_odometer(23500) 
my_used_car.read_odometer() 
 
my_used_car.increment_odometer(100) 
my_used_car.read_odometer() 
```

**p.s.**

1. 除了进行基本检查外，还需特别注意细节

### 继承

#### 子类的方法__init__()

```python
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric vehicles."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
```

#### 给子类定义属性和方法

```python
class Car():
    """A simple attempt attributes to describe a car."""

    def __init__(self, make, model, year):
        """Initialize attributes descriptive name."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's milleage."""
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car): 
    """Represent aspects of a car, specific to electric vehicles."""
 
    def __init__(self, make, model, year):
        """
        电动汽车的独特之处
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 70
         
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
 
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
```

#### 重写父类的方法

```python
def ElectricCar(Car): 
    --snip--
 
    def fill_gas_tank():
        """电动汽车没有油箱"""
        print("This car doesn't need a gas tank!")
```

#### 将实例用作属性

```python
class Car():
    """A simple attempt attributes to describe a car."""

    def __init__(self, make, model, year):
        """Initialize attributes descriptive name."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's milleage."""
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement desciribing the battery size."""
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge.'
        print(message)

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric vehicles."""
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

**报错**

```python
class Car():
    """A simple attempt attributes to describe a car."""

    def __init__(self, make, model, year):
        """Initialize attributes descriptive name."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's milleage."""
        print('This car has ' + str(self.odometer_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement desciribing the battery size."""
        print('This car has a ' + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = 'This car can go approximately ' + str(range)
        message += ' miles on a full charge.'
        print(message)

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year, battery_size):
        """Initialize attributes of the parent class.
        Then initialize attributes specific to an electric vehicles."""
        super().__init__(make, model, year)
        self.battery = Battery(battery_size)

my_tesla = ElectricCar('tesla', 'model s', 2016, 80)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

Traceback (most recent call last):
  File "f:/program/py/text/Python编程/9/electric_car.py", line 69, in <module>
    my_tesla.battery.get_range()
  File "f:/program/py/text/Python编程/9/electric_car.py", line 52, in get_range
    message = 'This car can go approximately ' + str(range)
UnboundLocalError: local variable 'range' referenced before assignment(本地变量没有定义就调用)

错误原因：如果if判断不符合，则不会进入if中，使得range没有被定义。

### 导入类

引入模块的程序必须使用更具体的文件名

#### 导入单个类

```python
from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```

#### 在一个模块中存储多个类

```python
from car import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
```

#### 从一个模块中导入多个类

```python
from car import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
```

#### 导入整个模块

```python
import car

my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
```

#### 导入模块中的所有类

from module_name import *

**p.s.** 需要从一个模块中导入很多类时，最好导入整个模块，并使用module_name.class_name语法来访问类。

#### 在一个模块中导入另一个模块

```python
from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
```

#### 自定义工作流程

1. 一开始应让代码结构尽可能简单。先尽可能在一个文件中完成所有的工作，确定一切都能正确运行后，再将类移到独立的模块中

2. 先找出让你能够编写出可行代码的方式，再尝试让代码更为组织有序

#### Python 标准库

创建字典并记录其中的键—值对的添加顺序，可使用模块collections中的OrderedDict类

```python
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite languages is " + language.title() + '.')
```

#### 类编码风格

1. 类名采用驼峰命名法，类名中的每个单词的首字母大写，不使用下划线

2. 实例名和模块名采用小写格式，在单词直接加下划线

3. 类定义后包含一个文档字符串，简单描述类的功能

4. 模块后包含一个文档字符串，对其中的类的功能进行描述

5. 在类中使用一个空行分隔方法；在模块中使用两个空行分隔类

6. 同时导入标准库中的模块和编写的模块，先导入标准库模块，再添加一个空行，再导入编写的模块

## 文件和异常

### 从文件中读取数据

#### 读取整个文件

open('打开文件的名称')

1. Python在当前执行的文件所在的目录中查找指定的文件

2. 返回一个表示文件的对象

with

1. 关键字with在不再需要访问文件后将其关闭

```python
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
```

#### 文件路径

#### 逐行读取

```python
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
```

**p.s.** 在文件中，每行的末尾都有一个看不见的换行符，而print语句也会加上一个换行符，因此每行末尾都有两个换行符：一个来自文件，另一个来自print语句。要消除这些多余的空白行，可在print语句中使用rstrip()

#### 创建一个包含文件各行内容的列表

方法readlines()从文件中读取每一行，并将其存储在一个列表中

```python
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
```

#### 使用文件的内容

rstrip() 删除字符串末尾的换行符

strip() 删除字符串开头和末尾的换行符

```python
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))
```

#### 圆周率值中包含你的生日吗

```python
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form mmddyy:")
if birthday in pi_string:
    print('Your birthday appears in the first million digits of pi!')
else:
    print('Your birthday does not appear in the first million digits of pi.')
```

#### 写入空文件

open()的第二个参数为操作文件的模式

r 读取模式 默认
w 写入模式 如果文件不存在，将会创造该文件；**如果存在，文件会被清空**
a 附加模式
r+ 读取和写入模式

```python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming.')
```

**p.s.** Python只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数str()将其转换为字符串格式。

#### 写入多行

可以使用空格、制表符和空行来设置这些输出的格式

```python
filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write('I love programming.\n')
    file_object.write('I love creating new games.\n')
```

#### 附加到文件

1. 以附加模式打开文件时，Python不会在返回文件对象前清空文件，而你写入到文件的行都将添加到文件末尾

2. 指定的文件不存在，Python将为你创建一个空文件
```python
filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write('I also love finding meaning in large datasets.\n')
    file_object.write('I love creating apps that can run in a browser.\n')
```

### 异常

#### 处理 ZeroDivisionError 异常

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

#### 使用 try-except 代码块

```python
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
```

#### 使用异常避免崩溃

```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    secend_number = input('Second number: ')
    if secend_number == 'q':
        break
    answer = int(first_number) / int(secend_number)
    print(answer)
```

#### else 代码块

```python
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    secend_number = input('Second number: ')
    if secend_number == 'q':
        break
    try:
        answer = int(first_number) / int(secend_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
```

#### 处理 FileNotFoundError 异常

```python
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + ' does not exist.'
    print(msg)
```

#### 分析文本

```python
filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = 'Sorry, the file ' + filename + ' does not exist.'
    print(msg)
else:
    # Count the approximate number of words in the file.
    words = contents.split()
    num_words = len(words)
    print('The file ' + filename + ' has about ' + str(num_words) + ' words.')
```

#### 使用多个文件

```python
def count_words(filename):
    """Count the approximate number of words in a file"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + ' does not exist.'
        print(msg)
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print('The file ' + filename + ' has about ' + str(num_words) + ' words.')

filename = 'alice.txt'
count_words(filename)
```

#### 失败时一声不吭

```python
def count_words(filename): 
    """计算一个文件大致包含多少个单词""" 
    try: 
        --snip-- 
    except FileNotFoundError: 
       pass 
    else: 
        --snip-- 
 
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt'] 
for filename in filenames: 
    count_words(filename) 
```
