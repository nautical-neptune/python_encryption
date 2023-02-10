#!/usr/bin/env /bin/python3

example_list = ['hello', 'world','this','is','an','example']

empty_string = ""

#for word in example_list:
#	index_char = word[0]
#	length = len(word)
#	addition = "" + index_char + str(length)
#	empty_string += addition

alphabet = "abcdeghijklmnopqrstuvwxyz"

def rot(rounds, plaintext):
	result = ''
	for l in plaintext:

		try:
			i = (alphabet.index(l) + rounds) % 26
			result += alphabet[i]

		except ValueError:
			result += l

	return result

ciphertext = ""

for word in example_list:
	rot_rounds = len(word)
	rot_text = rot(rot_rounds, word)
	ciphertext += rot_text
	ciphertext += " "


print(ciphertext)
