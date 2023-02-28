from gtts import *
from random import *
import os

sõnastik={}
def Loe_failist(fail:dict):
    """
    loeb failist
    """
    #riik_pealinn={}
    #pealinn_riik={}
    file=open("riigid_pealinnad.txt",'r',encoding="utf-8-sig")
    for line in file:
        k, v=line.strip().split('-')
        sõnastik[k.strip()] = v.strip()
        #riik_pealinn[k]=v
        #pealinn_riik[v]=k
    file.close()
    #return riik_pealinn, pealinn_riik
    print(sõnastik)

def Kirjuta_failisse(fail:dict):
    """
    sisetab failise
    """
    file=open("riigid_pealinnad.txt",'r',encoding="utf-8-sig")
    for line in file:
        k, v=line.strip().split('-')
        sõnastik[k.strip()] = v.strip()    
    riik=input("Lisa riik: ")
    pealinn=input("Tema pealinn: ")
    sõnastik.update({riik:pealinn})
    file.close()
    print(sõnastik)
    return sõnastik


def heli(fail:dict):
    print()

def vaata_sõnastiku(fail:dict):
    """
    Näitab kogu sõnastiku
    """
    riik_pealinn={}
    pealinn_riik={}
    file=open("riigid_pealinnad.txt",'r',encoding="utf-8-sig")
    for line in file:
        k, v=line.strip().split('-')       
        riik_pealinn[k]=v
        pealinn_riik[v]=k
    file.close()
    print(riik_pealinn, pealinn_riik)   
    return riik_pealinn, pealinn_riik

def riik_ja_pealinn_näita(fail:dict):
    file=open("riigid_pealinnad.txt",'r',encoding="utf-8-sig")
    for line in file:
        k, v=line.strip().split('-')
        sõnastik[k.strip()] = v.strip()
    RvP=input("Otsime riigi või pealinna: ")
    while RvP not in ["riik","pealinn"]:
        RvP=input("riik või pealinn: ")
    if RvP=="riik":
        OtsimeR=input("Kirjuta riigi nimi: ")
        while OtsimeR not in [sõnastik.keys()]:
            OtsimeR=input("Kirjuta riigi nimi sõnastikust: ")
        tulemus=sõnastik.get(OtsimeR)
        print(tulemus)
    file.close()
    return tulemus
        #elif RvP=="pealinn":
        #    OtsimeP=input("Kirjuta pealinna nimi: ")            
        #    sõnastik.values(k:OtsimeP)
          

def paranda(fail:dict):
    """
    parandab viga
    """
    file=open("riigid_pealinnad.txt",'r',encoding="utf-8-sig")
    for line in file:
        k, v=line.strip().split('-')
        sõnastik[k.strip()] = v.strip()    
        Rparanda=input("Millist riigi soovite parandada? ")
        while Rparanda not in sõnastik.get(Rparanda):
            Rparanda=input("Kirjutage õige riigi nimi: ")
        Rparandatud=input("Kirjutage parandatud riigi nimi: ")
        while Rparandatud.isdigit():
            Rparandatud=input("Kirjutage riigi nimi: ")
        Pparanda=input("Millist pealinna soovite parandada? ")
        while Pparanda not in sõnastik.values:
            Pparanda=input("Kirjutage õige pealinna nimi: ")
        Pparandatud=input("Kirjutage parandatud pealinna nimi: ")
        while Pparandatud.isdigit():
            Pparandatud=input("Kirjutage pealinna nimi: ")
        sõnastik[Rparandatud:Pparandatud]=sõnastik.pop[Rparanda:Pparanda]
        f=open(fail,"w",encoding="utf-8-sig")
        f.writelines(sõnastik)
        print(sõnastik)
    file.close()

def test(fail:dict):
    """
    õigekiri test
    """
    a=[]
    võit=kaotus=0
    game=[]
    file=open("riigid_pealinnad.txt",'r',encoding="utf-8-sig")
    for line in file:
        k, v=line.strip().split('-')
        sõnastik[k.strip()] = v.strip()
    file.close()
    Riigid = list(sõnastik.keys())
    Pealinnad = list(sõnastik.values())
    x=int(input("palju korda mängime: "))
    for i in range (x):
        num=randint(0,(len(Riigid)-1))
        while num in a:
            num=randint(0,(len(Riigid)-1))
        valik=input("Kas võtame riigi või pealinna? (riik või pealinn) ").lower()
        while valik not in ["riik","pealinn"]:
            valik=input("Kirjuta riik või pealinn: ")
        if valik=="riik":
            rana=Riigid[num]
            tematähendus=input(f"Mis on riigi {rana} pealinn: ")
            if tematähendus==Pealinnad[num]:
                game.append(f"{i+1} {valik} mäng - võit")
                print("Võit")
                võit+=1
            else:
                game.append(f"{i+1}, {valik} mäng - kaotus") 
                print("Kaotus")
                kaotus+=1
        else:
            rana=Pealinnad[num]
            tematähendus=input(f"Mis on riigi {rana} pealinn: ") 
            if tematähendus==Pealinnad[num]:
                game.append(f"{i+1} {valik} mäng - võit")
                print("Võit")
                võit+=1
            else:
                game.append(f"{i+1}, {valik} mäng - kaotus") 
                print("Kaotus")
                kaotus+=1       
        a.append(num)
    print()
    print(game)
    if kaotus==0:
        resÕ=100
        resV=0
    elif võit==0:
        resÕ=0
        resV=100
    else:
        resÕ=round((võit/i)*100),1
        resV=round((kaotus/i)*100),1
    print(f"Võiduprotsent - {resÕ}%")
    print(f"Kaotusprotsent - {resV}%")