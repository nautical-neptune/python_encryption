#!/usr/bin/env /usr/bin/python3

alphabet = "abcdefghijklmnopqrstuvwxyz"

def rotation_encryption(rounds, plaintext):
	rotated_result = ""
	for letter in plaintext.lower():
		try:
			i = (alphabet.index(letter) + rounds) % 26
			rotated_result += alphabet[i]
		except ValueError:
			rotated_result += letter

	return rotated_result

index_counter = 0
end_string = ""
plaintext = input("PLAINTEXT: ")
plaintext = plaintext.replace(' ','')

static_length = len(plaintext)

even_rounds = int(input("EVEN ROUNDS: "))
odd_rounds = int(input("ODD ROUNDS: "))

while index_counter <= static_length:

	if index_counter % 2 == 0:
		rounds = even_rounds

	elif index_counter % 2 != 0:
		rounds = odd_rounds

	letter_to_encrypt = plaintext[index_counter:index_counter+1]
	encrypted_letter = rotation_encryption(rounds,letter_to_encrypt)
	end_string += encrypted_letter
	index_counter += 1

print(end_string)
