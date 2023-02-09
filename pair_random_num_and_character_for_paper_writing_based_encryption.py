#!/usr/bin/env /usr/bin/python3

import random
all_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
all_nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25']

static_length_var = len(all_chars)
index_counter = 0

while index_counter <= static_length_var:

	try:

		char_choice = random.choice(all_chars)
		num_choice = random.choice(all_nums)
		all_chars.remove(char_choice)
		all_nums.remove(num_choice)
		print(char_choice, ":", num_choice)

		index_counter += 1

	except indexerror:
		break

