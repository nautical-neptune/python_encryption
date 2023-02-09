#!/usr/bin/env /usr/bin/python3

def test(plaintext):
	test_array = []
	for i in range(0, len(plaintext)):
		test_element = ord(plaintext[i]) - 65
		test_array.append(test_element)
	return test_array

plaintext = input("text: ")
plaintext = plaintext.lower()
plaintext = plaintext.replace(' ','')
#print(plaintext)
enc_text = test(plaintext)
#print(enc_text)

end_final_string = []
for letter in enc_text:
	end_final_string.append(str(letter))
	doubled_element = letter * 2
	end_final_string.append(str(doubled_element))

#print(end_final_string)

empty_string = ""
for letter in end_final_string:
	letter = int(letter)
	empty_string += chr(letter)

print(empty_string)
