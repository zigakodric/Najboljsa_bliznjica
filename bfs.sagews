︠ca4d1c2d-49f7-42ab-9cdf-098acf506969s︠




#Izračuna povprečno razdaljo med vozlišči
def dolzine(graph):
    s = 0
    graph = Graph(graph)
    s = graph.average_distance()
    return(s)

def bliznjica(graph):
    #Trojica bližnjica (med dvema vozliščema), povprečna razdalja med vozlišči
    m = (0,0,99999999999999)
    povezave = [] #seznam preverjenih povezav
    k = list(graph.keys())
    for i in range(0,len(k)):
        for j in range(0,len(k)):
            #če povezave še ni in sta različni točki
            if k[j] not in graph.get(k[i]) and k[j] != k[i]:
                if (k[i],k[j]) not in povezave:
                    #dodamo nove povezave, graf neusmerjen
                    graph[k[i]].append(k[j])
                    graph[k[j]].append(k[i])
                    dol = dolzine(graph)  #izračunamo nove razdalje
                    graph[k[i]].remove(k[j])   #izbrišemo bližnjico
                    graph[k[j]].remove(k[i])
                    #dodamo bližnjico med že preverjene
                    povezave.append((k[i],k[j]))
                    povezave.append((k[j],k[i]))

                    if dol < m[2]:   #preverimo če je nova bližnjica boljša
                        m = (k[j],k[i], dol)
    return(m)

#Funkcija uporabi funkcijo za iskanje ene bližnjice.
#Predpostavimo, da prvo najboljšo bližnjico že poznamo. Funkcija jo doda v drevo in
# nato poišče v novem grafu
def dve_bliznjici1(graph, prva_bliznjica):
    #Najboljši bližnjici. Vrne peterico prve najboljše bližnjice
    #(med dvema vozliščema),
    #druge ter povprečno razdaljo med vozlišči.
    k = list(graph.keys())
    najboljsi_bliznjici = (0,0,0,0,0)
    prva = prva_bliznjica           #Prvo bližnjico že poznamo
    graph[prva[0]].append(prva[1])    #Dodamo v drevo
    graph[prva[1]].append(prva[0])
    druga = bliznjica(graph)          #Poiščemo drugo bližnjico
    najboljsi_bliznjici = (prva[0],prva[1],druga[0],druga[1],druga[2])
    graph[prva[0]].remove(prva[1])   #Izbrišemo bližnjico iz grafa
    graph[prva[1]].remove(prva[0])
    return(najboljsi_bliznjici)


#Funkcija je sestavljena na podoben način kot za eno bližnjico. Preveri vse možne povezave,
#hkrati pa preverja če je to povezavo že pregledala.
def dve_bliznjici2(graph):
    m2 = (0,0,0,0,99999999999999)
    preverjene = []
    g = []
    k = list(graph.keys())
    for i in range(0, len(k)):
        for j in range(0,len(k)):
            for s in range(0, len(k)):
                for l in range(0,len(k)):
                    if k[s] not in graph.get(k[i]):
                        if k[l] not in graph.get(k[j]):
                            if k[i] != k[s] :
                                if k[j] != k[l]:
                                    if k[i] != k[j]:
                                        if (k[i],k[s]) != (k[j],k[l]):
                                            if (k[s],k[i]) != (k[l],k[j]) and (k[s],k[i]) != (k[j],k[l]) and (k[i],k[s]) != (k[l],k[j]):
                                                if (k[i], k[s],k[j],k[l]) not in preverjene:
                                                    graph[k[i]].append(k[s])
                                                    graph[k[j]].append(k[l])
                                                    graph[k[s]].append(k[i])
                                                    graph[k[l]].append(k[j])
                                                    dol = dolzine(graph)
                                                    graph[k[i]].remove(k[s])
                                                    graph[k[j]].remove(k[l])
                                                    graph[k[s]].remove(k[i])
                                                    graph[k[l]].remove(k[j])
                                                    preverjene.append((k[i],k[s],k[j],k[l]))
                                                    preverjene.append((k[s],k[i],k[j],k[l]))
                                                    preverjene.append((k[i],k[s],k[l],k[j]))
                                                    preverjene.append((k[s],k[i],k[l],k[j]))
                                                    if dol < m2[4]:
                                                        m2 = (k[i],k[s],k[j],k[l],dol)
                                                    g.append((k[i], k[s],k[j],k[l]))
    return(m2)

#Iskanje bližnjice
#10 vozlišč:
drevo = graphs.RandomTree(10)
drevo.show()
drevo10 = drevo.to_dictionary()
dolzine(drevo10)
bliz = bliznjica(drevo10)
bliz
dve_bliznjici1(drevo10,bliz)
dve_bliznjici2(drevo10)

#30 vozlišč
drevo = graphs.RandomTree(30)
drevo.show()
drevo30 = drevo.to_dictionary()
dolzine(drevo30)
bliz = bliznjica(drevo30)
bliz
dve_bliznjici1(drevo30,bliz)


#70 vozlišč
drevo = graphs.RandomTree(70)
drevo.show()
drevo70 = drevo.to_dictionary()
dolzine(drevo70)
bliz = bliznjica(drevo70)
bliz
dve_bliznjici1(drevo70,bliz)

#150 vozlišč
drevo = graphs.RandomTree(150)
drevo.show()
drevo150 = drevo.to_dictionary()
dolzine(drevo150)
#bliz = bliznjica(drevo150)
#bliz

# Pogledamo, za koliko se spremeni povprečna razdalja.
# Funkcija razlika_razdalj sprejme argumenta n, m ter stevilo_bliznjic.
# n je število vozlišč drevesa, m število ponovitev in stevilo_bliznjic(1 ali 2) število bližnjic, ki jih dodamo v graf.
# Vrne par, kjer prvo število predstavlja povprečno število razdalj v drevesu brez bližnjice in drugo v drevesu z bližnjico.
def razlika_razdalj(n,m, stevilo_bliznjic):
    i = 0
    seznam_razdalj_dve = []
    seznam_razdalj = []
    seznam_razdalj_bliznjica = []
    if stevilo_bliznjic == 1:
        while i < m:
            drevo1 = graphs.RandomTree(n).to_dictionary()
            seznam_razdalj.append(dolzine(drevo1))
            seznam_razdalj_bliznjica.append(bliznjica(drevo1)[2])
            i += 1
        return((sum(seznam_razdalj)/m,sum(seznam_razdalj_bliznjica)/m))
    if stevilo_bliznjic == 2:
        while i < m:
            drevo1 = graphs.RandomTree(n).to_dictionary()
            seznam_razdalj.append(dolzine(drevo1))
            prva_bliznjica = bliznjica(drevo1)
            seznam_razdalj_bliznjica.append(prva_bliznjica[2])
            seznam_razdalj_dve.append(dve_bliznjici1(drevo1,prva_bliznjica)[4])
            i += 1
        return((sum(seznam_razdalj)/m,sum(seznam_razdalj_dve)/m))
    else:
        return("Funkcija kot stevilo_bliznjic sprejema števila 1 ali 2")

#Ena bliznjica 100 ponovitev na drevesu z 10 vozlišči
r = razlika_razdalj(10,100,1)
r

#Ena bliznjica 70 ponovitev na drevesu s 30 vozlišči
rr = razlika_razdalj(30,70,1)
rr

#Dve bliznjici 50 ponovitev, 15 vozlišč
rrr = razlika_razdalj(15,50,2)

#Spreminjanje razdalje glede na število vozlišč.
#Gledamo, za koliko se spremeni povprečna razdalja v drevesu z od 4 do 20 vozlišči na 100 ponovitev, če dodajamo eno bližnjico
#(V poročilu uporabljeno na drevesu z od 4 do 30 vozlišči)
razdalje_vozlisca = []
for i in range(4,21):
    m = razlika_razdalj(i,100,1)
    razdalje_vozlisca.append(m)
razdalje_vozlisca

#Časovna zahtevnost algoritma
#Funkcija sprejme argumente n, m in stevilo_bliznjic. n je število vozlišč, m pa število ponovitev.
# Če je stevilo_bliznjic enako 1, funkcija uporabi funkcijo bliznjica(), če 2 dve_bliznjici1()
# in 3 dve_bliznjici2(). Funkcija vrne potreben čas.
def casovna_zahtevnost(n,m,stevilo_bliznjic):
    import time
    funkcija = [bliznjica, dve_bliznjici1, dve_bliznjici2][stevilo_bliznjic-1]
    start = time.time()
    for i in xrange(m):
        if funkcija == dve_bliznjici1:
            drevo=graphs.RandomTree(n).to_dictionary()
            funkcija(drevo,bliznjica(drevo))
        else:
            funkcija(graphs.RandomTree(n).to_dictionary())
    konec = time.time()
    return(konec-start)
casovna_zahtevnost(200,1,1)
casovna_zahtevnost(10,100,2)
casovna_zahtevnost(10,100,3)
casovna_zahtevnost(20,100,1)
#casovna_zahtevnost(120,130,1)
# Rezultati so recimo (za primerjavo):
# 57.819862842559814
# 0.9815769195556641
# 52.104007959365845
# 3.494917869567871
# 1285.5924899578094

#Časovna zahtevnost glede na število vozlišč (v poročilu uporabljeno na
# drevesih z od 4 do 30 vozlišči, ponovimo 100x namesto 20x)
casovna_vozlisca = []
for i in range(4,21):
    casovna_vozlisca.append(casovna_zahtevnost(i,20,1))
casovna_vozlisca

print("To je to :)")
