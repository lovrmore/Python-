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

### 存储数据

#### 使用 json.dump()和 json.load()

```python
import json

number = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(number, f_obj)
```

```python
import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
```

#### 保存和读取用户生成的数据

```python
import json

username = input('What is your name? ')

filename = 'username.json'
with open(filename, 'w') as f_obj:
    json.dump(username, f_obj)
    print("We'll remember you when you come back, " + username + '!')
```

```python
import json

filename = 'numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
```

```python
import json

# Load the username. if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input('What is your name? ')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + '!')
else:
    print('Welcome back, ' + username + '!')
```

#### 重构

```python
import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input('What is your name? ')
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + '!')
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + '!')

greet_user()
```

## 测试代码

### 测试函数

```python
def get_formatted_name(first, last):
    """Generate a neatly formatted full name"""
    full_name = first + ' ' + last
    return full_name.title()
```

```python
from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input('\nPlease give me a first name: ')
    if first == 'q':
        break
    last = input('\nPlease give me a last name: ')
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print('\tNeatly formatted name: ' + formatted_name + '.')
```

#### 可通过的测试

```python
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
```

#### 不能通过的测试

#### 添加新测试

```python
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

unittest.main()
```

### 测试类

#### 各种断言方法

#### 一个要测试的类

```python
class AnonymousSurvey():
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_results(self):
        """Show all the responses that have been given."""
        print('Survey results:')
        for response in self.responses:
            print('- ' + response)
```

```python
from survey import AnonymousSurvey

# Define a question, and make a survey.
question = 'What language did you first learn to speak?'
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question.
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results.
print('\nThank you to everyone who participated in the survey!')
my_survey.show_results()
```

#### 测试 AnonymousSurvey 类

```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = 'What language did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')

        self.assertIn('English', my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        question = 'What langugae did you first learn to speak?'
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for response in responses:
            my_survey.store_response(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)

unittest.main()
```

#### 方法 setUp()

unittest.TestCase类包含方法setUp()，让我们只需创建这些对象一次，并在每个测试方法中使用它们

```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        question = 'What language did you first learn to speak?'
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

unittest.main()
```

## 生成数据

### 安装 matplotlib

通过Anaconda安装了matplotlib，但是具体原理尚不清楚，有待学习

疑问：Anaconda和docker之间的区别，两者都能配置和生成环境

### 绘制简单的折线图

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

plt.plot(squares)
plt.show()

#### 修改标签文字和线条粗细

```python
import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)

# Set chart title and label axes.
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

plt.show()
```

#### 校正图形

```python
import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# Set chart title and label axes.
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', labelsize=14)

plt.show()
```

#### 使用 scatter()绘制散点图并设置其样式

```python
import matplotlib.pyplot as plt

plt.scatter(2, 4, s=200)

# Set chart title and label axes.

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
```

#### 使用 scatter()绘制一系列点

```python
import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=100)

# Set chart title and label axes.

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
```

#### 自动计算数据

```python
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, s=40)

# Set chart title and label axes.

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

plt.show()
```

#### 删除数据点的轮廓

```python
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, edgecolors='none', s=40)

# Set chart title and label axes.

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

plt.show()
```

#### 自定义颜色

```python
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)

# Set chart title and label axes.

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

plt.show()
```

#### 使用颜色映射

```python
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.scatter(
    x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# Set chart title and label axes.

plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)

# Set the range for each axis.
plt.axis([0, 1100, 0, 1100000])

plt.show()
```

#### 选择方向

```python
from random import choice

class RandomWalk():
    """A class to generate random walks."""
    
    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks start at (0, 0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        # Keep taking steps until the walk reaches the desired length.
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction.
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere.
            if x_step == 0 and y_step == 0:
                continue

            # Calculate the next x and y values.
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
```

#### 绘制随机漫步图

```python
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Make a random walk, and plot the points.
rw = RandomWalk()
rw.fill_walk()

plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
```

#### 模拟多次随机漫步

```python
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()

    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
```

#### 给点着色

```python
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors='none',
        s=15)
    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
```

#### 重新绘制起点和终点

```python
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))
    plt.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors='none',
        s=15)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(
        rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
```

#### 增加点数

```python
import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Keep making new walks, as long as the program is active.
while True:
    # Make a random walk, and plot the points.
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(
        rw.x_values,
        rw.y_values,
        c=point_numbers,
        cmap=plt.cm.Blues,
        edgecolors='none',
        s=1)

    # Emphasize the first and last points.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(
        rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break
```

### 使用 Pygal 模拟掷骰子

#### 创建 Die 类

```python
from random import randint

class Die():
    """A class representing a single die."""

    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)
```

#### 绘制直方图

```python
import pygal

from die import Die

# Create a D6.
die = Die()

# Make some rolls, and stone results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = 'Results of rolling one D6 1000 times.'
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
```

#### 同时掷两个骰子

```python
import pygal

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Make some rolls, and stone results in a list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
hist = pygal.Bar()

hist.title = 'Results of rolling two dice 1000 times.'
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6 + D6', frequencies)
hist.render_to_file('die_visual.svg')
```

#### 分析 CSV 文件头

csv.reader()，将存储的文件对象作为实参传递给它，从而创建一个与该文件相关联的阅读器（reader对象）。

模块csv包含函数next()，调用它并将阅读器对象传递给它时，它将返回文件中的下一行。在前面的代码中，我们只调用了next()一次，因此得到的是文件的第一行。

```python
import csv

filename = r'E:\programming\py\code\Python编程\16\sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
```

#### 打印文件头及其位置

对列表调用了enumerate()来获取每个元素的索引及其值

```python
import csv

filename = r'E:\programming\py\code\Python编程\16\sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index, column_header)
```

#### 提取并读取数据

阅读器对象从其停留的地方继续往下读取CSV文件，每次都自动返回当前所处位置的下一行。

由于我们已经读取了文件头行，这个循环将从第二行开始。

```python
import csv

filename = r'E:\programming\py\code\Python编程\16\sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs)
```

#### 绘制气温图表

```python
import csv

from matplotlib import pyplot as plt

# Get high temperatures from file.
filename = r'E:\programming\py\code\Python编程\16\sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(highs, c='red')

# Format plot.
plt.title('Daily high temperatures, July 2014', fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
```

#### 模块 datetime

```python
>>> from datetime import datetime
>>> first_date = datetime.strptime('2014-7-7', '%Y-%m-%d')
>>> print(first_date)
2014-07-07 00:00:00
```

**p.s.** 模块datetime中设置日期和时间格式的实参

#### 在图表中添加日期

```python
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get high temperatures from file.
filename = r'E:\programming\py\code\Python编程\16\sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# Format plot.
plt.title('Daily high temperatures, July 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
```

#### 涵盖更长的时间

```python
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get date and high temperatures from file.
filename = r'E:\programming\py\code\Python编程\16\sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# Format plot.
plt.title('Daily high temperatures - 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
```

#### 再绘制一个数据系列

```python
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get date, high, and low temperatures from file.
filename = r'E:\programming\py\code\Python编程\16\sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')

# Format plot.
plt.title('Daily high and low temperatures - 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
```

#### 给图表区域着色

```python
import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get date, high, and low temperatures from file.
filename = r'E:\programming\py\code\Python编程\16\sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)

        high = int(row[1])
        highs.append(high)

        low = int(row[3])
        lows.append(low)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
plt.title('Daily high and low temperatures - 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
```

### 制作世界人口地图：JSON 格式

#### 提取相关的数据

```python
import json

# Load the data into a list.
filename = r'E:\programming\py\code\Python编程\16\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Print the 2010 population for each country.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = pop_dict['Value']
        print(country_name + ': ' + population)
```

#### 获取两个字母的国别码

pygal_maps_world 已经更新，具体信息看官方文档

```python
from pygal.maps.world import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
```

```python
from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the pygal 2-digit country code for the given country"""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country wasn't found, return None.
    return None
```

```python
import json

from country_codes import get_country_code

# Load the data into a list.
filename = r'E:\programming\py\code\Python编程\16\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Print the 2010 population for each country.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            print(code + ': ' + str(population))
        else:
            print('ERROR - ' + country_name)
```

#### 制作世界地图

```python
from pygal.maps.world import World

wm = World()
wm.title = 'North, Central, and South America'

wm.add('North America', ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', [
    'ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy',
    've'
])

wm.render_to_file('americas.svg')
```

#### 在世界地图上呈现数字数据

```python
from pygal.maps.world import World

wm = World()
wm.title = 'Population of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('na_populations.svg')
```

#### 绘制完整的世界人口地图

```python
import json

from pygal.maps.world import World

from country_codes import get_country_code

# Load the data into a list.
filename = r'E:\programming\py\code\Python编程\16\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        
wm = World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)

wm.render_to_file('world_population.svg')
```

#### 根据人口数量将国家分组

```python
import json

from pygal.maps.world import World

from country_codes import get_country_code

# Load the data into a list.
filename = r'E:\programming\py\code\Python编程\16\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Group the countries into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# See how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))
        
wm = World()
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
```

#### 使用 Pygal 设置世界地图的样式

```python
import json

from pygal.maps.world import World
from pygal.style import RotateStyle

from country_codes import get_country_code

# Load the data into a list.
filename = r'E:\programming\py\code\Python编程\16\population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population

# Group the countries into 3 population levels.
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop

# See how many countries are in each level.
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

wm_style = RotateStyle('#336699')
wm = World(style = wm_style)
wm.title = 'World Population in 2010, by Country'
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)

wm.render_to_file('world_population.svg')
```

### 使用API

#### 使用 API 调用请求数据

https://api.github.com/search/repositories?q=language:python&sort=stars 

第一部分（https://api.github.com/）将请求发送到GitHub网站中响应API调用的部分；接下来的一部分（search/repositories）让API搜索GitHub上的所有仓库。

repositories后面的问号指出我们要传递一个实参。q表示查询，而等号让我们能够开始指定查询（q=）。通过使用language:python，我们指出只想获取主要语言为Python的仓库的信息。最后一部分（&sort=stars）指定将项目按其获得的星级进行排序。

#### 处理 API 响应

```python
import requests 
 
# 执行API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status code:", r.status_code) 
 
# 将API响应存储在一个变量中
response_dict = r.json() 
 
# 处理结果 
print(response_dict.keys())
```

**p.s.** 执行更复杂的API调用时，程序应检查这个值

#### 处理响应字典

```python
import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

# Examine the first repository.
repo_dict = repo_dicts[0]
print('\nKeys:', len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
```

```python
import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

# Examine the first repository.
repo_dict = repo_dicts[0]

print('\nSelected information about first repository:')
print('Name:', repo_dict['name'])
print('Owner:', repo_dict['owner']['login'])
print('Stars:', repo_dict['stargazers_count'])
print('Repository:', repo_dict['html_url'])
print('Created:', repo_dict['created_at'])
print('Updated:', repo_dict['updated_at'])
print('Description:', repo_dict['description'])
```

提取repo_dict中与键相关联的值

```python
import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']
print('Repositories returned:', len(repo_dicts))

print('\nSelected information about each repository:')
for repo_dict in repo_dicts:
    print('\nName:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Description:', repo_dict['description'])
```

#### 添加自定义工具提示

```python
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
    {'value': 16101, 'label': 'Description of httpie.'},
    {'value': 15028, 'label': 'Description of django.'},
    {'value': 14798, 'label': 'Description of flask.'},
]

chart.add('', plot_dicts)
chart.render_to_file('bar_description.svg')
```

#### 根据数据绘图

```python
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
    }
    plot_dicts.append(plot_dict)

# Make visualization.
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
```

#### 在图表中添加可单击的链接

```python
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('Status code:', r.status_code)

# Store API response in a variable.
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories.
repo_dicts = response_dict['items']

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    
    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': repo_dict['description'],
        'xlink': repo_dict['html_url'],
    }
    plot_dicts.append(plot_dict)

# Make visualization.
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos.svg')
```
