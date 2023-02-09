#!/usr/bin/env /usr/bin/python3

index_counter_var = 0
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

end_string = ""

while index_counter_var <= len(plaintext):
	char_to_encrypt = plaintext[index_counter_var:index_counter_var+1]
	rotated_char = rotation_encryption(index_counter_var, char_to_encrypt)
	end_string += rotated_char

	index_counter_var += 1

print(end_string)
