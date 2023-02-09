#!/usr/bin/env /usr/bin/python3

import random
import base64

def test(plaintext):
	test_array = []
	for i in range(0, len(plaintext)):
		test_element = ord(plaintext[i]) - 65
		test_array.append(test_element)
	return test_array

plaintext = input("text: ")
plaintext = plaintext.lower()
plaintext = plaintext.replace(' ','')
print(plaintext)
enc_text = test(plaintext)
print(enc_text)

print("#")

str_and_double_list = []
for letter in enc_text:
	str_and_double_list.append(str(letter))
	doubled_element = letter * 2
	str_and_double_list.append(str(doubled_element))

print(str_and_double_list)


final_string_with_random = ""

for letter in str_and_double_list:
	letter = int(letter)
	final_string_with_random += chr(letter)
	random_1 = random.randint(0,255)
	random_2 = random.randint(0,255)
	final_string_with_random += chr(random_1)
	final_string_with_random += chr(random_2)

print(final_string_with_random)

testing = final_string_with_random.encode()
base_string = base64.b64encode(testing)
print(base_string.decode())
