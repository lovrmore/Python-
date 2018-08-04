# squares = []
# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)

# print(squares)

squares = [value**2 for value in range(1,11)]
print(squares)

num = [value for value in range(3,31) if value % 3 == 0]
print(num)