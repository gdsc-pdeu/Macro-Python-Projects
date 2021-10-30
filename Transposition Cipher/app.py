def transpositionCipher():
    text=input("Enter Message\n")
    key=input("Enter the key\n")
    encrypt=int(input("Enter 0 for encryption and 1 for decryption\n"))
    i=0
    d={}
    p=[]
    j=0
    if encrypt==0:
        while j<len(text):
            for i in key:
               if j>=len(text):
                   d[i].append('_')
               elif i not in d:
                   d[i]=[text[j]]
               else:
                   d[i].append(text[j])
               j+=1           
        for i in sorted(key):
            for j in d[i]:
                print(j,end="")
    else:
        q=0
        q1=0
        k=sorted(key)
        c=len(text)
        c1=len(key)
        for i in k:
            d[i]=text[q:q+int(c/c1)]
            q=q+int(c/c1)        
        q=0
        for j in range(int(c/c1)):
            for i in key:
                if d[i][q]=='_':
                    break
                print(d[i][q],end="")
            q+=1
        
if __name__ == "__main__":
    transpositionCipher()
