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


key = input('KEY: ')
key = xor_key(key)
msg = input('PLAINTEXT: ')
enc_text = xor_enc(msg, key)
enc_text = str(enc_text)

end_string = ""

for letter in enc_text:
	letter = int(letter)
	letter += 1
	end_string += str(letter)

print(end_string)


final_string = reverse_text(end_string)
print(final_string)
