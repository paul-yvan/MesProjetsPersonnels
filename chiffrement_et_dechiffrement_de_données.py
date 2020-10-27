import random
def convertLetters(text):

        accent = [' ','é', 'è', 'ê', 'à', 'ù', 'û', 'ç', 'ô', 'î', 'ï', 'â', '#','.',',','?',':','!','$','/','=','§','+','-',';','_','&']
        sans_accent = ['','e', 'e', 'e', 'a', 'u', 'u', 'c', 'o', 'i', 'i', 'a', '','','','','','','','','','','','','','','']
        i = 0
        while i < len(accent):
            text = text.replace(accent[i], sans_accent[i])
            i += 1
        text=text.upper()
        return text


def generateKey() :
    
    l=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    random.shuffle(l)
    c = "".join(l)
    
    return c

#print(generateKey())

def keyOK(key):
    
    l=list(generateKey())
    s=list(key)
    a=0
    
    for i in range(26):
        
        if (l[i] in s):
            if s.count(l[i])==1:
            
                a+=1
      
    if a==26:
        
        return True
    
    else:
        
        return False
    
#print(keyOK("SVCWXQDLUKBTEJGFHIAPNRMYOZ"))
 
def  shiftLeft(keyLeft,i) :
    
    kl=list(keyLeft)
    
    t=kl[0:i]
    
    del(kl[0:i])
    
    kl.extend(t)

    ab1=kl[1]
    
    kl[1]=" "
    
    for i in range(2,14):
        
        kl[i-1]=kl[i]
        
    
    kl[13]=ab1
    klf = "".join(kl)
    return klf

#print(shiftLeft("OAJTFYLQXCMPEDNVSBRUKHGWIZ",22))

def shiftRight(keyRight,i):
    
    kr=list(keyRight)
    
    t=kr[0:i+1]

    del(kr[0:i+1])

    kr.extend(t)

    ab2=kr[2]
    
    kr[2]=" "

    for i in range(3,14):
        
        kr[i-1]=kr[i]
        
    
    kr[13]=ab2
    krf = "".join(kr)
    
    return krf

#print(shiftRight("EWKFTYIQXUHPMABCNJRLDZSGVO",22))        

def algorithm1(text,cipher):
    
    a=convertLetters(text)
        
    b=list(a)

    keyLeft= "OAJTFYLQXCMPEDNVSBRUKHGWIZ"
    
    keyRight = "EWKFTYIQXUHPMABCNJRLDZSGVO"

    
    f=[]
    
    if cipher== "true":
        
        for j in range(len(b)):
                
            c=list(keyLeft)

            d=list(keyRight)    
            
            i=d.index(b[j])
            
            f.append(c[i])
            
            keyLeft=shiftLeft(keyLeft,i)
            
            keyRight=shiftRight(keyRight,i)

        result = "".join(f)
        
        return result
    
    if  cipher=="false":
        
        for j in range(len(b)):
                
            c=list(keyLeft)

            d=list(keyRight)
            
            i=c.index(b[j])
            
            f.append(d[i])
            
            keyLeft=shiftLeft(keyLeft,i)

            keyRight=shiftRight(keyRight,i)

        result = "".join(f)
        
        return result

cipher=input("Chiffrer (true) - Déchiffrer (false): ")

while cipher!="true" and cipher!="false":

    cipher=input("Chiffrer (true) - Déchiffrer (false):")
if cipher=="true":
        text=input("veuillez entrer la chaine de caractère à chiffrer: ")
if cipher=="false":
        text=input("veuillez entrer la chaine de caractère à déchiffrer: ")        


print("")

print(algorithm1(text,cipher))
