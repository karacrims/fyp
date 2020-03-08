#!/usr/bin/python

import itertools
import string
import random
import time

#Using these variables made it easier to set password length
passlength = 6
cracklength = passlength + 1 
guess = ''

#Chars represents all the ascii letters (upper and lowercase) and digits which make up a possible password
#Chars can be changed to string.printable to include all possible typed characters or string.ascii_letters and string.digits for just letters and numbers (takes less time)
chars = string.printable

def create_password(chars):
	passwd = []  #password is stored as an array
	for _ in range(0, passlength):   #upper number is the length of the password
	#for _in range(random.randint(0, x) for random password lengths
		passwd.append(random.choice(chars))  #randomly add a character from chars to the passwd array
	return "".join(passwd)

def cracker(passwd):
	start = time.time()	
	attempts = 0
	for password_length in range(0, cracklength):  #Upper number has to be larger than max in create_password loop
		for guess in itertools.product(chars, repeat=password_length):  #Itertools iterates through chracters
			attempts +=1
			guess = ''.join(guess)
			if guess == passwd:
				end = time.time()
				crackTimeSec = (end-start)
				crackTimeMin = crackTimeSec/60
				crackTimeSec = str(round(crackTimeSec, 2))
				crackTimeMin = str(round(crackTimeMin, 2))	
				print 'Password is {} found in {} guesses. This took {} seconds or {} minutes'.format(guess, attempts, crackTimeSec, crackTimeMin)
				return guess
def pass_assessor(guess):
	upCase = sum(1 for c in guess if c.isupper())
	digit = sum(1 for c in guess if c.isdigit())
	symbol = sum(1 for c in guess if c in string.punctuation)
	assessment = "This password has:\n"
	grade = 0
	if upCase >= 1:
		assessment = assessment + 'At least one upper case letter\n'
		grade +=1
	if digit >= 1:
		assessment = assessment + 'At least one digit\n'
		grade +=1
	if symbol >= 1:
		assessment = assessment + 'At least one symbol\n' 
		grade +=1
	if len(guess) >= 8:
		assessment = assessment +  'At least 8 characters\n'
		grade +=1
	if len(guess) < 8:
		assessment = assessment +  'Fewer than 8 characters\n'
	else:
		assessment = assessment + 'All lower case characters and is shorter than 8 characters\n'
	
	if grade == 0:
		assessment = assessment + 'This is a very weak password'
	elif grade == 1:
		assessment = assessment + 'This is a weak password'
	elif grade == 2: 
		assessment = assessment + 'This password could be stronger'
	elif grade == 3: 
		assessment = assessment + 'This is a strong password'
	elif grade == 4:
		assessment = assessment + 'This is a very strong password'
	return assessment

passwd = create_password(chars)
print '****************************************************************************************************'
guess = cracker(passwd)
print(pass_assessor(guess))
print '****************************************************************************************************'
