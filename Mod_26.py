# the following shows how to encrypt and decrypt rot , to solve the chaleng  type : print(decrypt_rot(13 , "what's given by pico")

s=str(input("what do you want to encrypt:"))
n=int(input("which rot encryption you want to encrypt with:"))
L_1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
L_2=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
p=''

def encrypt_rot(s:str , n:int)-> str:
	if n<1 or n >25:
		return "print a valid rot-_-"
	else :
		for i in range(len(s)):
			if s[i] in L_1:
				j=L_1.index(s[i])
				k=(j+n)%26
				p=p+str(L_1[k])
			elif s[i] in L_2:
				j=L_2.index(s[i])
				k=(j+n)%26
				p=p+str(L_2[k])
			else:
				p=p+s[i]

		return p


def decrypt_rot(n:int , s:str):
	for i in s :
		if i in L_1:
			j=L_1.index(i)
			p=p+str(L_1[(j-n)%26])
		elif i in L_2:
			j=L_2.index(i)
			p=p+str(L_2[(j-n)%26])
		else:
			p=p+i
	return p
