import string

encr="kjlijdliljhdjdhfkfkhhjkkhhkihlhnhghekfhmhjhkhfhekfkkkjkghghjhlhghmhhhfkikfkfhm"

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]


def encrypted_to_encoded(encr):
	encoded=''
	for i in range(len(encr)):
		s=ALPHABET.index(encr[i])
		t2=ord(key[0])-LOWERCASE_OFFSET
		t1= (s-t2) % 16
		encoded =encoded + chr(t1+LOWERCASE_OFFSET)
	return encoded

def b16_decode(enco) :
	decoded=''
	for i in range (0,len(enco),2):
		s1="{:04b}".format(ALPHABET.index(enco[i]))
		s2="{:04b}".format(ALPHABET.index(enco[i+1]))
		s=s1+s2
		number=int(s,2)
		decoded+=chr(number)
	return decoded

for key in string.ascii_lowercase[:16]:
	if b16_decode(encrypted_to_encoded(encr))[:6] == 'et_tu?':    # i knew it afterr resolving the challenge
		print(f"[*] FLAG :picoCTF{{{b16_decode(encrypted_to_encoded(encr))}}}")
