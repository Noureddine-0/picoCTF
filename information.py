##Walkthrough##

#first use hexdump  with the -C option anf find the source in the very first lines 
#the following script decode the base64 within python 
#if you work with linux do;
#$ echo cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9 | bas64 -d 

import base64


def decoding(s:str)->str:
	string_bytes=s.encode()
	decoded_bytes=base64.b64decode(string_bytes)
	return decoded_bytes.decode('ascii')

s='cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9'
print(decoding(s))
