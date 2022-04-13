"""
[3.feladat Az Európai Unió tagállamai] 

Az UTF-8-as karakterkódolású EUcsatlakozas.txt állomány (file) tartalmazza az Európai Unió tagállamait és csatlakozási dátumait a következő minta szerint.

Az állomány pár sora például: 

Ausztria;1995.01.01
Belgium;1958.01.01
Bulgária;2007.01.01
…

Ahol az adattagok jelentése rendre a következők:
•	Az ország neve: [Auszria]
•	Az adott ország csatlakozási dátuma: [1995.01.01]
Az állomány sorai a tagállamok neve szerint ábécérendben tárolja országok nevét, és az Európai Unióhoz történő csatlakozási dátumát tartalmazza. A sorok azonos szerkezetűek, az adatokat Pontosvessző választja el. 

3.1 Készítsen konzolalkalmazást (projektet) a következő feladatok megoldásához, amelynek forráskódját EU néven mentse el!

3.2  Hozzon létre egy osztályt (class), ami reprezentálja egy ország példányait (object isntance). Az osztály konstruktora (constructor) paraméterként kapjon meg egy beolvasott sort, és ebből határozza meg meg az adott attribútumokat (property). Az osztály használata nem KÖTELEZŐ DE több pontot kaphat érte!!! 
Továbbá olvassa be az UTF-8 kódolású EUcsatlakozas.txt állományban sorait és tárolja el adatokat egy homogén listába, amely használatával a további feladatok megoldhatók! A terminálra való kiírás legyen a mintának megfelelő!

3.3 Határozza meg és írja ki a képernyőre a minta szerint, hogy hány tagállam található a forrásállományban! 

3.4 Határozza meg és írja ki a képernyőre a minta szerint a 2007-ben csatlakozott országok számát! 

3.5 Határozza meg és írja ki a képernyőre a minta szerint Magyarország csatlakozásának dátumát!

3.6 Határozza meg, hogy májusban történt-e csatlakozás az EU-hoz!

"""

#Ausztria;1995.01.01
#1-2
class Eu:
  def __init__(self,sor):
    sor = sor.strip().split(";")
    self.orszag = sor[0]
    self.ev = int(sor[1][:4])
    self.honap = sor[1][5:7]
    self.nap = int(sor[1][8:10])
    self.datum = sor[1]

with open("EUcsatlakozas.txt","r",encoding="latin2") as f:
  lista = [Eu(sor) for sor in f]

#3
  
print(f"3.feladat: Eu tagállamainak száma: {len(lista)} db")

#4