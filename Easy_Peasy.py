# In your terminal type :
# $ python3 -c "print('p'*49968 + '\n' +'p'*32)" | "followed by nc ..." 
# and take the last line which you'll put it to encrypted_test_message variable in the python script

encrypted_flag = '0345376e1e5406691d5c076c4050046e4000036a1a005c6b1904531d3941055d'
string=bytes.fromhex(encrypted_flag)
encrypted_test_message='1257212c0813122c0848112c0812442c0840442c0816482c0840400b2c081414'
L=[i for i in encrypted_test_message]
M=[]
for i in range(0,len(L),2):
	a=''.join(L[i:i+2])
	M.append(a)

flag=''
key=''
for i in range(len(string)):
	key_element = ord('p') ^ int(M[i],16) 
	key=key + str(key_element)
	flag = flag + chr(string[i] ^ key_element)
	
print(f"[*] KEY : {key}")
print(f"[*] FLAG : {flag}")


# THIS TYPE OF CHALLENGES NEED A GOOD COMPREHENSION OF THE SCRIPT GENERATING THE SERVER .
