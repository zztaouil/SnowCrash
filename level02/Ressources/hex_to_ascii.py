hex_str = "00 0d 0a 50 61 73 73 77 6f 72 64 3a 20 66 74 5f 77 61 6e 64 72 7f 7f 7f 4e 44 52 65 6c 7f 4c 30 4c 0d 00 0d 0a 01"

def	is_printable(decimal):
	if (decimal > 32 and decimal < 127):
		return True
	return False	

ott = ""
for e in hex_str.split():
	dcr = int(e, 16)
	if (is_printable(dcr)):
		ott += chr(dcr)
	else:
		ott += '?('+str(e)+')'

print(ott)
