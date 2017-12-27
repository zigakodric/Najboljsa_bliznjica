graph = {"A": ["B", "D"],
         "B": ["A","C"],
         "C": ["B"],
         "D": ["A","E"],
         "E": ["D"]}

k = list(graph.keys())

def bfs_najkrajsa_pot(graph, start, cilj):
    # sledi že obiskanim vozliščem
    obiskani = []
    # spremlja vse poti, ki bodo obiskane
    vrsta = [[start]]
 
    # vrne pot, če je start že na začetku enak cilju
    if start == cilj:
        return "To je bilo enostavno! Start = cilj"
 
    # zanka teče dokler ne preveri vseh možnih poti
    while vrsta:
        # doda (pop) prvo pot iz vrste
        pot = vrsta.pop(0)
        # dobimo zadnje vozlišče s poti
        vozlisce = pot[-1]
        if vozlisce not in obiskani:
            sosedje = graph[vozlisce]
            # gre skozi vsa sosednja vozlišča, konstruira novo pot in
            # jo doda v vrsto
            for sosed in sosedje:
                nova_pot = list(pot)
                nova_pot.append(sosed)
                vrsta.append(nova_pot)
                # vrne pot, če je sosed cilj
                if sosed == cilj:
                    return nova_pot
 
            # označi vozlišče, ko je obiskano (ga doda v seznam obiskanih)
            obiskani.append(vozlisce)
 
    # v primeru, ko ni poti med dvema vozliščema
    return "Povezujoča pot ne obstaja :("

# dobimo razdaljo vseh vozlišč od začetnega vozlišča, podano v seznamu
# ker hočemo povprečno razdaljo med vozlišči,
# moramo sešteti vse razdalje in deliti s številom vozlišč (brez začetnega)
def dolzine(graph):
    s = []
    for i in range(1,len(k)):
        s.append(len(bfs_najkrajsa_pot(graph, k[0],k[i]))-1)
    return(sum(s)/(len(k)-1))
    
print(dolzine(graph))

def bliznjica(graph):
    #Trojica bližnjica (med dvema vozliščema), povprečna razdalja med vozlišči
    m = (0,0,99999999999999)
    povezave = [] #seznam preverjenih povezav
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

#funkcija uporabi funkcijo za iskanje ene bližnjice
#Najprej poišče prvo bližnjico, jo doda v drevo in
# nato poišče v novem grafu
def dve_bliznjici(graph):
    #Najboljši bližnjici. Vrne peterico prve najboljše bližnjice
    #(med dvema vozliščema),
    #druge ter povprečno razdaljo med vozlišči.
    najboljsi_bliznjici = (0,0,0,0,0)
    prva = bliznjica(graph)           #Poiščemo prvo bližnjico
    graph[prva[0]].append(prva[1])    #Dodamo v drevo
    graph[prva[1]].append(prva[0])  
    druga = bliznjica(graph)          #Poiščemo drugo bližnjico
    najboljsi_bliznjici = (prva[0],prva[1],druga[0],druga[1],druga[2])
    return(najboljsi_bliznjici)

print(dve_bliznjici(graph))

#Kodo je treba še izboljšati, samo osnutek
m2 = (0,0,0,0,99999999999999)
preverjene = []
for i in range(0, len(k)):
    for j in range(0,len(k)):
        for s in range(0, len(k)):
            for l in range(0,len(k)):
                if k[s] not in graph.get(k[i]):
                    if k[l] not in graph.get(k[j]):
                        if k[i] != k[s]:
                            if (k[i], k[l],k[s],k[j]) not in preverjene:
                                dic = graph
                                graph[k[i]].append(k[s])
                                graph[k[j]].append(k[l])
                                dol = dolzine(graph)
                                preverjene.append((k[i],k[j],k[s],k[l]))
                                preverjene.append((k[j],k[i],k[s],k[l]))
                                preverjene.append((k[i],k[j],k[l],k[s]))
                                preverjene.append((k[j],k[i],k[l],k[s]))
                                graph = dic
                                print(m2)
                                if dol < m2[4]:
                                    m2 = (k[i],k[s],k[j],k[l],dol)
print(m2)
print(preverjene)
