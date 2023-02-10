#!/usr/bin/env /usr/bin/python3

import argparse

def main():

	print("------------------------------------------")
	print("1) Arc4")
	print("2) alt_chacha [PIP]")
	print("3) chacha [CRYPTODOME]")
	print("4) Aes")
	print("5) Vernam")
	print("6) Sals20")
	print("------------------------------------------")

	parser = argparse.ArgumentParser()
	parser.add_argument("--cipher", help="Cipher to choose")
	parser.add_argument("--plaintext", help="Plaintext to encrypt")
	parser.add_argument("--save_file", help="Filename to save to")
	args = parser.parse_args()

	CIPHER = args.cipher
	PLAINTEXT = args.plaintext
	FILE_NAME = args.save_file


##############
#### ARC4 ####
##############

	if CIPHER == '1' or CIPHER == 'arc4' or CIPHER == 'arc':

		def arc4(data, key):
			x = 0
			box = range(256)
			for i in range(256):
				x = (x + box[i] + ord(key[i % len(key)])) % 256
				box = list(box)
				box[i], box[x] = box[x], box[i]
			x = 0
			y = 0
			out = []
			for char in data:
				x = (x + 1) % 256
				y = (y + box[x]) % 256

				box[x], box[y] = box[y], box[x]
				out.append(chr(ord(char) ^ box[(box[x] + box[y]) % 256]))

			return ''.join(out)


		key = input("ARC KEY: ")
		arc_ciphertext = arc4(PLAINTEXT, key)
		print("Arc ciphertext is \n\n{}".format(arc_ciphertext))


		try:
			with open(FILE_NAME, "wb") as fw:
				fw.write(arc_ciphertext)
		except TypeError:
			pass


#################
#### ALT CHA ####
#################


	elif CIPHER == '2' or CIPHER == 'import_chacha' or CIPHER == 'alt_chacha':

		import os

		try:
			from chachapoly1035 import ChaChaPoly1305

			key = os.urandom(32)
			print("Key used : {}".format(key))
			plaintext = PLAINTEXT.encode
			iv = os.urandom(12)
			print("Iv used: {}".format(iv))
			cip = ChaChaPoly1305(key)
			ciphertext = cip.encrypt(iv, plaintext)
			print(ciphertext)

			try:
				with open(FILE_NAME, "wb") as fw:
					fw.write(ciphertext)
			except TypeError:
				pass

		except ModuleNotFoundError:
			print("pip install chachapoly1305")
			pass


################
#### CHACHA ####
################

	elif CIPHER == '3' or CIPHER == 'chacha' or CIPHER == 'cryptodome_chacha':

		import json
		from base64 import b64encode
		from Cryptodome.Cipher import ChaCha20
		from Cryptodome.Random import get_random_bytes

		plaintext = PLAINTEXT.encode()
		key = get_random_bytes(32)
		print("key used: {}".format(key))
		cipher = ChaCha20.new(key=key)
		ciphertext = cipher.encrypt(plaintext)
		nonce = b64encode(cipher.nonce).decode('utf-8')
		ct = b64encode(ciphertext).decode('utf-8')
		result = json.dumps({'nonce':nonce, 'ciphertext':ct})
		print(result)

		try:
			with open(FILE_NAME, "wb") as fw:
				fw.write(ct)
		except TypeError:
			pass


#############
#### AES ####
#############


	elif CIPHER == '4' or CIPHER == 'aes' or CIPHER == 'AES':

		from base64 import b64encode
		from Cryptodome.Cipher import AES
		from Cryptodome.Util.Padding import pad
		import binascii
		import os
		import random

		data = PLAINTEXT.encode()
		key = binascii.hexlify(os.urandom(16))
		print("Key used: {}".format(key))
		iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))

		cipher = AES.new(key, AES.MODE_CBC)
		ct_bytes = cipher.encrypt(pad(data, AES.block_size))
		ct = b64encode(ct_bytes).decode('utf-8')
		print("iv: {}".format(iv))
		print("Ciphertext: {}".format(ct))


		try:
			with open(FILE_NAME, "wb") as fw:
				fw.write(ct)
		except TypeError:
			pass


################
#### VERNAM ####
################


	elif CIPHER == '5' or CIPHER == 'vernam' or CIPHER == 'Vernam':

		def vernam(text, key):
			result = ""
			ptr = 0
			for char in text:
				result = result + chr(ord(char) ^ ord(key[ptr]))
				ptr = ptr + 1
				if ptr == len(key):
					ptr = 0
			return result

		key = input("KEY : ")
		ciphertext = vernam(PLAINTEXT, key)
		print("Ciphertext is" + ciphertext)

		try:
			with open(FILE_NAME, "w") as fw:
				fw.write(ciphertext)
		except TypeError:
			pass


###############
#### SALSA ####
###############


	elif CIPHER == '6' or CIPHER == 'salsa' or CIPHER == 'salsa20':

		try:
			from salsa20 import XSalsa20_xor
			from os import urandom

			iv = urandom(24)
			print("Iv used: {}".format(iv))
			key = input("SALSA KEY: ")
			key = key.encode()
			plaintext = PLAINTEXT.encode()
			ciphertext = XSalsa_xor(plaintext, iv, key)
			print("Ciphertext: {}".format(ciphertext))


		except ModuleNotFoundError:
			print("pip install salsa20")
			pass

		try:
			with open(FILE_NAME, "wb") as fw:
				fw.write(ciphertext)
		except TypeError:
			pass


#############
#### DES ####
#############


	elif CIPHER == '7' or CIPHER == 'des' or CIPHER == 'DES' or CIPHER == 'Des':

		from Cryptodome.Cipher import DES

		key = input("8 bit key: ")

		if len(key) != 8:
			raise IndexError("Incorrect key length")
		else:
			key = key.encode()

		plaintext = PLAINTEXT.encode()
		des = DES.new(key, DES.MODE_ECB)
		ciphertext = des.encrypt(plaintext)

		print("Ciphertext is: {}".format(ciphertext))

		try:
			with open(FILE_NAME, "wb") as fw:
				fw.write(ciphertext)
		except TypeError:
			pass


if __name__ == '__main__':
	main()

