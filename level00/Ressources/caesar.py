import string

cipher = input()
alphabet = string.ascii_lowercase

keys = [i for i in range(0, 26)]

for k in keys:
	plain = ""
	for c in cipher:
		plain += alphabet[(alphabet.find(c) + k) % len(alphabet)]
	print(plain)
