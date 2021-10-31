
from itertools import takewhile
def groupby(rules):
    d = {}
    ls = [ y[0] for y in rules ]
    initial = list(set(ls))
    for y in initial:
        for i in rules:
            if i[0]==y:
                if y not in d:
                    d[y] = []
                d[y].append(i)
    return d
def prefix(x):
    return len(set(x)) == 1
  
def non_deterministic_to_deterministic_grammar_converter():
    starting=""
    rules=[]
    common=[]
    alphabetset=["A'","B'","C'","D'","E'","F'","G'","H'","I'","J'","K'","L'","M'","N'","O'","P'","Q'","R'","S'","T'","U'","V'","W'","X'","Y'","Z'"]
    s=input("Enter the Non-deterministic grammar\n(Format: S->aAAbA|aAaAb|...|b\n\n")
    print("\nThe required deterministic grammar is :")
    #s="S->aAAbA|aAaAb|abb|b"
    rules=[]
    common=[]
    split=s.split("->")
    starting=split[0]
    for i in split[1].split("|"):
       rules.append(i)
    for k, l in groupby(rules).items():
        r = [l[0] for l in takewhile(prefix, zip(*l))]
        common.append(''.join(r))
    for i in common:
        newalphabet=alphabetset.pop()
        print(starting+"->"+i+newalphabet)
        index=[]
        for k in rules:
            if(k[0]==i):
                index.append(k)
        print(newalphabet+"->",end="")

        for j in index[:-1]:
            stringtoprint=j.replace(i,"", 1)+"|"
            if stringtoprint=="|":
                print("\u03B5","|",end="")
            else:
                print(j.replace(i,"", 1)+"|",end="")
        stringtoprint=index[-1].replace(i,"", 1)+"|"
        if stringtoprint=="|":
            print("\u03B5","",end="")
        else:
            print(index[-1].replace(i,"", 1)+"",end="")
        print("")
if __name__ == "__main__":
    transpositionCipher()
