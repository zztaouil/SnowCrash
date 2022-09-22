

def	decrypt(cipher):
	clear = ""
	for i in range(len(cipher)):
		clear += chr(ord(cipher[i]) - i)
	return clear

print(decrypt("f4kmm6p|=�p�n��DB�Du{��"))	

