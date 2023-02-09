#!/usr/bin/env /usr/bin/python3

def key_creation(key_text):
	key_array = []
	for i in range(0, len(key_text)):
		key_element = ord(key_text[i]) - 65
		key_array.append(key_element)
	return key_array

def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q,r = b//a, b%a
		m,n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y

def modinv(a, m):
	gcd, x, y = egcd(a, m)
	if gcd != 1:
		return None
	else:
		return x % m

def encrypt(text, key):
	return ''.join([chr(((key[0]*(ord(t) - ord('A')) + key[1]) % 26) + ord('A')) for t in text.upper().replace(' ','')])

def reverse_cipher(regular_text):
	reversed_text = ''
	i = len(regular_text) - 1
	while i >= 0:
		reversed_text = reversed_text + regular_text[i]
		i = i - 1
	return reversed_text

secret_key = input("KEY: ")
key = key_creation(secret_key)
print(key)

text = input("PLAINTEXT: ")

if len(text) % 2 != 0:
	raise IndexError

encrypted_text = encrypt(text, key)
print("ENCRYPTED: {}".format(encrypted_text))

divided_length = int(len(encrypted_text) / 2)


split_index_first_half = encrypted_text[0:divided_length]
split_index_second_half = encrypted_text[divided_length:len(encrypted_text)]

print(split_index_first_half)
print(split_index_second_half)

reversed_first_half = reverse_cipher(split_index_first_half)
reversed_second_half = reverse_cipher(split_index_second_half)

print(reversed_second_half + reversed_first_half)
