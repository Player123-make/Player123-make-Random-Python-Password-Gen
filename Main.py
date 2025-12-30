import random # random function
import math # math function

#========= Functions Section ==========

# Generate a random key for an array.
def randKey(val):
    return math.floor(random.random() * val)

#===================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] # All the digits
characters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"] # All the characters of the alphabet
special = ["@","#","$","%","*","&","§","=","+","?","/"] # All the special characters that can be used to confuse someone. 👍 

n1 = len(numbers) # Numbers array length
n2 = len(characters) # Characters array length
n3 = len(special) # Special Characters array length

kp = str(numbers[randKey(n1)]) + characters[randKey(n2)] + special[randKey(n3)] # Unique code in a single string.
kp2 = str(numbers[randKey(n1)]) + characters[randKey(n2)] + special[randKey(n3)]
kp3 = str(numbers[randKey(n1)]) + characters[randKey(n2)] + special[randKey(n3)]
kp4 = str(numbers[randKey(n1)]) + characters[randKey(n2)] + special[randKey(n3)]

print(kp + kp2 + kp3 + kp4) # I haven't automated this part yet ( ˶>˶˶<˶)
