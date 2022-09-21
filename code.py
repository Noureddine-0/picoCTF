a=input('Enter your phrase:')
s=''
for i in a:
	l=ord(i)  
	b=l//256   
	s=s+str(chr(b))
	c=l-b*256
	s=s+str(chr(c))

print(s)
