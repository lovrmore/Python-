# def greet_user(username):
#     """Display a simple greeting."""
#     print('Hello, ' + username.title() + '!')

# greet_user('jesse')

# def get_formatted_name(first_name, last_name):
#     """Return a full name, nealty formatted."""
#     full_name = first_name + ' ' + last_name
#     return full_name.title()

# # This is an infinite loop!
# while True:
#     print('\nPlease tell me your name:')
#     print("(enter 'q' at any time to quit)")

#     f_name = input('First name:')
#     if f_name == 'q':
#         break

#     l_name = input('Last name:')
#     if f_name == 'q':
#         break

#     formatted_name = get_formatted_name(f_name, l_name)
#     print('\nHello, ' + formatted_name + '!')

def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = 'Hello, ' + name.title() + '!'
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
