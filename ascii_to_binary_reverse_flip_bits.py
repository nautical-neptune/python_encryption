#!/usr/bin/env /usr/bin/python3

starter_string = input("ASCII TEXT: ")

#encryption from text to binary #
encoded_starter_string = starter_string.encode()
binary_starter_string = bin(int.from_bytes(encoded_starter_string, "big"))
#

rm_two_binary_string = binary_starter_string.replace("0b","")

def reverse_cipher(text):
	result = ""
	i = len(text) - 1
	while i >= 0:
		result = result + text[i]
		i = i - 1
	return result


reversed_starter = reverse_cipher(rm_two_binary_string)

# implement better way to flip bits? ### e.g.	~a	# ?

alt_char_flip = reversed_starter.replace("0","Z")
first_flip = alt_char_flip.replace("1","0")
second_flip = first_flip.replace("Z","1")
encrypted_binary = "0b" + second_flip
print("Encrypted binary text: ", encrypted_binary)

# unflip bits

undo_first_flip = second_flip.replace("1","Z")
undo_second_flip = undo_first_flip.replace("0","1")
undo_third_flip = undo_second_flip.replace("Z","0")

undo_reverse = reverse_cipher(undo_third_flip)

regular_binary_string = "0b" + undo_reverse

# decryption from binary to text #
test = int(regular_binary_string, 2)
aaaa = (test.to_bytes((test.bit_length() + 7) // 8, 'big').decode())
#

print(aaaa)
