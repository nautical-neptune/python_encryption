#!/usr/bin/env /usr/bin/python3

import base64

def reverse_text(plaintext):
	ciphertext = ''
	i = len(plaintext) - 1
	while i >= 0:
		ciphertext = ciphertext + plaintext[i]
		i = i - 1

	return ciphertext

plaintext = "this is a test message"
plaintext = plaintext.encode()

base_plain = base64.b64encode(plaintext)
decoded_base_plain = base_plain.decode()

counter_1 = 0
counter_2 = 4
static_length = len(decoded_base_plain)
end_string = ""
print(decoded_base_plain)

while counter_2 <= static_length:
	chars_to_manipulate = decoded_base_plain[counter_1:counter_2]

	if chars_to_manipulate.endswith("=") == true:
#		chars_to_manipulate = reverse_text(ciphertext)
		end_string += chars_to_manipulate
		break

	ciphertext = reverse_text(chars_to_manipulate)
	end_string += ciphertext

	counter_1 += 4
	counter_2 += 4


print(end_string)

