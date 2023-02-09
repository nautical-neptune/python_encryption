#!/usr/bin/env /usr/bin/python3

alphabet = "abcdefghijklmnopqrstuvwxyz"

def rotation_encryption(rounds, plaintext):
	rotated_result = ""
	for letter in plaintext.lower():
		try:
			i = (alphabet.index(letter) + rounds) % 26
			rotated_result += alphabet[i]
		except valueerror:
			rotated_result += letter

	return rotated_result


plaintext = input("plaintext: ")
plaintext = plaintext.replace(' ','')

static_length_string = len(plaintext)
index_counter_var = 0
encrypted_final_string = ""
print("length of plaintext: ", static_length_string)
while index_counter_var <= static_length_string:
	rounds_input1 = int(input("number 1: "))
	rounds_input2 = int(input("number 2: "))

	rounds_calc = rounds_input2 - rounds_input1

	letter_to_encrypt = plaintext[index_counter_var:index_counter_var+1]
	rotated_letter = rotation_encryption(rounds_calc, letter_to_encrypt)
	encrypted_final_string += rotated_letter
	index_counter_var += 1

print("encrypted string: ", encrypted_final_string)
