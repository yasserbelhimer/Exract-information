#coding:utf-8
import re,sys
corpus = open(sys.argv[1],'r',encoding="utf-8").readlines()

var  = open("subst.dic",'r',encoding='utf-16-le')
subst = var.readlines()
var.close()

subst_enri = list()
i = 0
for pos in corpus:
    x=re.search("^-? ?(\w+) :? ?(\d+|,)+ (mg|ml).+", pos)
    if x:
        sub = x.group(1).lower()+",.N+subst\n"
        if sub not in subst :
            subst.append(sub)
        if sub not in subst_enri :
            i+=1
            subst_enri.append(sub)
            print(str(i) +") "+x.group(1).lower())

subst.sort()
subst_enri.sort()

substDic = open('subst.dic','w+',encoding='utf-16-le')
substDic.write('\ufeff') # pour active le BOM LE
for sub in subst:
    substDic.write(sub)
substDic.close()

substEnriDic  = open('subst_enri.dic','w+',encoding='utf-16-le')
substEnriDic.write('\ufeff') # pour active le BOM LE
for sub in subst_enri:
    substEnriDic.write(sub)
substEnriDic.close()

dico = dict()

nbl = 1

for i in range(len(subst_enri)-1):
    lettre1 = ord(subst_enri[i][0]) 
    if subst_enri[i+1][0] == chr(lettre1) :
        nbl+=1
    else :
        dico[chr(lettre1)]  = nbl
        nbl = 1
lettre1  = subst_enri[len(subst_enri)-1][0]
dico[lettre1]  = nbl

myInfo = open('infos2.txt','w+',encoding="utf-8")

for cle in dico.keys() :
    myInfo.write("le nombre de médicaments issus de l’enrichissement pour la lettre '"+cle.upper()+"' est : "+" "+str(dico[cle]) + "\n")
myInfo.write("le nombre total de médicaments issus de l’enrichissement est : "+str(len(subst_enri)))
    