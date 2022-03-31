import math
class Etel:
    def __init__(self, egysor):
        darabok=egysor.strip('\n').split('\t')
        self.nev=darabok[0]
        self.ar=int(darabok[1])
        self.tipus=darabok[2]
def feladat2():
    print('2. feladat:')
    print('A listában',len(etelek),'étel szerepel')
    print('A listában '+str(len(etelek))+' étel szerepel')
def feladat3():
    db,osszeg=0,0
    for item in etelek:
        if item.tipus.lower()=='leves':
            db+=1
            osszeg+=item.ar
    print('3. feladat:')
    print('\tA levesek átlagos ára',math.floor(osszeg/db))
    print('\tA levesek átlagos ára',osszeg//db)

def feladat31():
    print('\tA levesek átlagos ára',sum([sor.ar for sor in etelek if sor.tipus.lower()=='leves'])//len([sor.ar for sor in etelek if sor.tipus.lower()=='leves'])) 


def feladat4():
    db=0
    for item in etelek:
        if item.tipus.lower()=='főétel':
            db+=1
    print('4. feladat:')
    print('\t',db, 'főétel van az étlapon.')

def feladat41():
    print('\t',len([sor.nev for sor in etelek if sor.tipus.lower()=='főétel']),'főétel van az étlapon.') 
with open('etelek.txt','r') as f:
    etelek=[Etel(sor) for sor in f]
    
f=open( 'etelek.txt','r')
beolvas=f.readlines()
etelek1=[] 
for sor in beolvas:
    etelek1.append(Etel(sor))
f.close()
feladat2()
feladat3()
feladat31()
feladat4()
feladat41()
    

