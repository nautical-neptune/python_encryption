#!/usr/bin/env /usr/bin/python3

def atbash_cipher(plaintext):
	characters = list(plaintext.upper())
	atbash_result = ""
	for character in characters:
		if character in code_dictionary:
			atbash_result += code_dictionary.get(character)
		else:
			atbash_result += character
	return atbash_result

alphabet = list("abcdefghijklmnopqrstuvwxyz")
reverse_alphabet = list(reversed(alphabet))
code_dictionary = dict(zip(alphabet, reverse_alphabet))

plaintext = input("plaintext: ")
plaintext = plaintext.replace(' ','')
ciphertext = atbash_cipher(plaintext)

print(plaintext)
print(ciphertext)

index_counter_var = 0
static_length_var = len(plaintext)
end_encrypted_string = ""
while index_counter_var <= static_length_var:
	plaintext_index_char = plaintext[index_counter_var:index_counter_var+1]
	ciphertext_index_char = ciphertext[index_counter_var:index_counter_var+1]

	end_encrypted_string += plaintext_index_char
	end_encrypted_string += ciphertext_index_char
	end_encrypted_string += plaintext_index_char
	end_encrypted_string += ","

	index_counter_var += 1

print(end_encrypted_string)
