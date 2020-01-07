#coding:utf-8
import sys,re,os
from urllib.request import urlopen
import socket


port =sys.argv[2]

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('localhost',int(port)))
if result == 0:
    myUrl = 'http://localhost:'+port+'/vidal/'
    urlpath = urlopen(myUrl)
    string = urlpath.read().decode("utf-8")
    pattern = re.compile('vidal-Sommaires-Substances-[A-Z].htm"') 
    filelist = pattern.findall(string)
    bornInf = sys.argv[1][0].upper()
    bornSup = sys.argv[1][2].upper()
    myDic = open('subst.dic','w+',encoding='utf-16-le')
    myInfo = open('infos.txt','w+',encoding="utf-8")
    myDic.write('\ufeff') # pour active le BOM LE
    nombreEntite = 0
    for i in range(ord(bornInf),ord(bornSup)+1):
        filename=filelist[i-65][:-1]
        substance = urlopen(myUrl + filename).readlines()
        nombreEntiteParLettre = 0
        for sub in substance : 
            found1 = re.search("<a href=\"Substance/(.*)\">(.*)</a>",sub.decode("utf-8"))
            if found1 :
                myDic.write(found1.group(2)+",.N+subst\n")
                nombreEntite +=1
                nombreEntiteParLettre +=1
        myInfo.write("le nombre d’entités médicales par substance active du dictionnaire « subst.dic » généré préalablement, pour la lettre '"+chr(i).upper()+"' est : " + str(nombreEntiteParLettre)+"\n")
    myInfo.write("le nombre total d’entités médicales par substance active du dictionnaire « subst.dic » généré préalablement est : "+str(nombreEntite))
    myDic.close()
    myInfo.close()
else:
   print ("Port is not open try another port")
sock.close()





