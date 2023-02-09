#!/usr/bin/env /usr/bin/python3

import binascii

def xor_key(secret):
	secret = secret.encode()
	hexstr = binascii.hexlify(secret)
	key = int(hexstr, 16)
	return key

def xor_enc(msg, key):
	msg = msg.encode()
	hexstr = binascii.hexlify(msg)
	ciphertext = int(hexstr, 16) ^ key
#	print(ciphertext)
	return ciphertext

def reverse_text(plaintext):
	reversed_ciphertext = ''
	i = len(plaintext) - 1
	while i >= 0:
		reversed_ciphertext = reversed_ciphertext + plaintext[i]
		i = i - 1

	return reversed_ciphertext


#key = input('KEY: ')
key = 'test'
key = xor_key(key)
#msg = input('PLAINTEXT: ')
msg = 'watermelon'
enc_text = xor_enc(msg, key)
enc_text = str(enc_text)

end_string = ""

len_of_enc_text = len(enc_text)

if len_of_enc_text % 2 != 0:
	raise ValueError("Ensure the length of the encrypted string is even?")

half_len = len_of_enc_text // 2

first_half = enc_text[0:half_len]
second_half = enc_text[half_len:(half_len*2)]

print(second_half + first_half)
