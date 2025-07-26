import random
import string

length = int(input('How long should your password be?'))


all_chars = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(all_chars) for i in range(length))

print('your password is:', password)
