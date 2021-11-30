import random

print('''welcome to your password generator''')

caratteri = '''abcdefghijklmnopqrstuwxyzABCDEFGHIJKLMNOPQRSTUWXYZ1234567890!?-%&'''

lunghezza = int (input ('''sets the password length: '''))

password= ""

for x in range (lunghezza):
    password+= random.choice (caratteri)

print("these is your new password!: ", password)
