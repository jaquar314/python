str="sai kiran"
vowels=0
space=0
digits=0
for i in range(0,len(str)):
    ch=str[i]
    if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' ):
        vowels+=1
print(vowels)
for i in range(0 , len(str)):
    ch=str[i]
    if( str[i]== " " ):
        space+=1
print(space)
for i in range(0,len(str)):
    digits+=1
print(digits)

