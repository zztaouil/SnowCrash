

def	decrypt(cipher):
	clear = ""
	for i in range(len(cipher)):
		clear += chr(ord(cipher[i]) - i)
		print(ord(cipher[i]))
	print()
	return clear

cipher = input().decode('utf-8')
print(cipher)

#print(decrypt(cipher))	

