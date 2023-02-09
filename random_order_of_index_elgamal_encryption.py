#!/usr/bin/env /usr/bin/python3

import random
from math import pow

a = random.randint(2,10)

def gcd(a,b):
	if a < b:
		return gcd(b,a)
	elif a % b == 0:
		return b
	else:
		return gcd(b, a % b)

def gen_key(q):
	key = random.randint(pow(10,20),q)
	while gcd(q, key) != 1:
		key = random.randint(pow(10,20), q)
	return key

def power(a,b,c):
	x = 1
	y = a
	while b > 0:
		if b % 2 == 0:
			x = (x * y) % c
		y = (y * y) % c
		b = int(b / 2)

	return x % c

def encrypt(msg, q, h, g):
	en_msg = []
	k = gen_key(q)
	s = power(h, k, q)
	p = power(g, k, q)

	for i in range(0, len(msg)):
		en_msg.append(msg[i])

#	print("g^k used: ", p)
#	print("g^ak used: ", s)
	for i in range(0, len(en_msg)):
		en_msg[i] = s * ord(en_msg[i])

	return en_msg, p

msg = input("PLAINTEXT: ")
q = random.randint(pow(10,20), pow(10, 50))
g = random.randint(2, q)

key = gen_key(q)
h = power(g, key, q)

#print("g used: ", g)
#print("g^a used: ", h)

en_msg, p = encrypt(msg, q, h, g)
#print("ENCRYPTED MSG: ", en_msg)

length_counter = 1
length_array = []

while length_counter <= len(en_msg):
	length_array.append(str(length_counter))
	length_counter += 1

end_string_for_final_msg = ""


while True:
	try:
		rand_num_choice = random.choice(length_array)
		length_array.remove(rand_num_choice)

		msg_en_rand_choice = random.choice(en_msg)
		en_msg.remove(msg_en_rand_choice)

		end_string_for_final_msg += str(rand_num_choice)
		end_string_for_final_msg += ": "
		end_string_for_final_msg += str(msg_en_rand_choice)
		end_string_for_final_msg += "\n"


	except IndexError:
		break

print(end_string_for_final_msg)
