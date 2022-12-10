file1=open("file.txt",'r')
Tvowel=0
Tconsonant=0
while True:
    vowel=0
    line=file1.readline()
    line=line.lower()
    if line=="":
            break    
    if line.find('a')!=-1:
        vowel+=line.count('a')
    if line.find('e')!=-1:
        vowel+=line.count('e')
    if line.find('i')!=-1:
        vowel+=line.count('i')
    if line.find('o')!=-1:
        vowel+=line.count('o')
    if line.find('u')!=-1:
        vowel+=line.count('u')
    Tconsonant+= len(line)-1-vowel
    Tvowel+=vowel
print("Tvowel",Tvowel,"Tconsonant",Tconsonant)
file1.close()