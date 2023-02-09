#!/usr/bin/env /usr/bin/python3

import random

plaintext = input("PLAINTEXT: ")
plaintext_array = []
for char in plaintext:
	plaintext_array.append(char)

plaintext = plaintext_array

length_counter = 1
length_array = []

while length_counter <= len(plaintext):
	length_array.append(str(length_counter))
	length_counter += 1

end_string_for_final_msg = ""


while True:
	try:
		rand_num_choice = random.choice(length_array)
		length_array.remove(rand_num_choice)

		msg_en_rand_choice = random.choice(plaintext)
		plaintext.remove(msg_en_rand_choice)

		end_string_for_final_msg += str(rand_num_choice)
		end_string_for_final_msg += ": "
		end_string_for_final_msg += str(msg_en_rand_choice)
		end_string_for_final_msg += "\n"


	except IndexError:
		break

print(end_string_for_final_msg)
