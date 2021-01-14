import random
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
pun = string.punctuation
pass_up = ''.join(random.choice(upper)for i in range(2))
pass_down = ''.join(random.choice(lower)for i in range(2))
punctuation = ''.join(random.choice(pun) for i in range(2))
num1 = str(random.randint(0, 9))
num2 = str(random.randint(0, 9))
password = list(pass_up+pass_down+num1+num2+punctuation)
random.shuffle(password)
print("Hello your required password is - \" "+''.join(password)+" \"")