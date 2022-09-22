
cipher = [102,
51,
105,
106,
105,
49,
106,
117,
53,
-135,
117,
101,
-138,
97,
-139,
-141,
52,
49,
-143,
49,
97,
102,
105,
-139,
-143,
-15,
-16]

rng = list(i for i in range(-128, 128))

idx = 0
for e in cipher:
	if e < 0:
		print(abs(e) - 128)	
	else:
		print(chr(e))
	idx += 1

print(rng)
