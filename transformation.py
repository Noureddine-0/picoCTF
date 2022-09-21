''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

# the purpose of the following script is to reverse engineering what was written above. 

a=input('Enter the enc content:')
flag=''
for i in a:
	l=ord(i)  
	b=l//256   
	flag=flag+str(chr(b))
	c=l-b*256
	flag=flag+str(chr(c))

print(flag)
