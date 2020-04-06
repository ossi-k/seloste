def tee_seloste(data):
    #alustetaan muuttujia
    tulostus = ""
    seloste_sarjoille = {}
    sarjat_sarake_nimi = {}
    muuttujat_sarake_nimi = {}

    #luetaan data
    data = open(data, encoding="latin-1")
    lines = data.readlines()
    y = 0
    while(y < len(lines)):
        lines[y] = lines[y].strip()
        if not lines[y] or lines[y] == ";":
            lines.remove(lines[y])
            y = y - 1
        y += 1

    # päätellään sarjojen nimet ja poistetaan otsikkorivi
    lines.pop(0) #poistetaan tiedoston otsikkorivi
    lines.pop(0)#poistetaan laskentajoukon otsikkorivi
    sarjojen_nimet_rivi = lines[0].split(";")
    sarjan_nimi = ""
    for i in range(3, len(sarjojen_nimet_rivi)):
        if sarjojen_nimet_rivi[i] != "":
            sarjan_nimi = sarjojen_nimet_rivi[i]
        sarjat_sarake_nimi[i] = sarjan_nimi
    lines.pop(0) #poistetaan sarjojen otsikkorivi
    lines.pop(0) #poistetaan muuttujien lyhenne-rivi

    #alustetaan seloste-hajautustaulu
    for i in range(len(sarjat_sarake_nimi)):
        seloste_sarjoille[i] = ""

    #päätellään sarakkeiden muuttujat
    muuttujat = lines[0].split(";")
    for i in range(3, len(muuttujat)):
        muuttujat_sarake_nimi[i] = muuttujat[i]

    lines.pop(0) #poistetaan muuttujien nimeämisrivi
    lines.pop(0) #poistetaan tietojen otsikkorivi
    lines.pop(0) #poistetaan tietojen toinen otsikkorivi

    #alustetaan vuosi loopin ulkopuolella
    vuosi = ""
    #muodostetaan seloste
    for line in lines:
        sarakkeet = line.split(";")

        #päätellään vuosi
        if sarakkeet[0] != "":
            vuosi = sarakkeet[0]

        #ajanjakso
        ajanjakso = sarakkeet[2]

        #muutetaan pilkut pisteiksi, jotta muuntaminen floatiksi onnistuu
        for i in range(3, len(sarakkeet)):
            sarakkeet[i] = sarakkeet[i].replace(",", ".")

        #päätellään, onko kasvua vai laskua ja lisätään selosteeseen oikea tulostus
        for i in range(3, len(sarakkeet)):
            lisays = ""
            if float(sarakkeet[i]) > 0:
                if not seloste_sarjoille.get(sarjat_sarake_nimi[i]):
                    lisays = ""
                else:
                    lisays = seloste_sarjoille.get(sarjat_sarake_nimi[i])
                lisays += "Sarjan " + str(sarjat_sarake_nimi[i]) + " " + str(muuttujat_sarake_nimi[i]) + " kasvoi " + str(ajanjakso) + "/" + str(vuosi) + "-ajanjaksolla " + str(sarakkeet[i]) + " prosenttia. " + "\n"
                seloste_sarjoille[sarjat_sarake_nimi[i]] = lisays
                #tulostus += "Toimialan " + str(toimialat_sarakkeille[i]) + " " + str(muuttuja) + " kasvoi " + str(sarakkeet[0]) + " neljänneksellä " + str(sarakkeet[i]) + " prosenttia. " + "\n"
            elif float(sarakkeet[i]) < 0:
                if seloste_sarjoille.get(sarjat_sarake_nimi[i]):
                    lisays = ""
                else:
                    lisays = seloste_sarjoille.get(sarjat_sarake_nimi[i])
                lisays += "Sarjan " + str(sarjat_sarake_nimi[i]) + " " + str( muuttujat_sarake_nimi[i]) + " kasvoi " + str(ajanjakso) + "/" + str(vuosi) + "-ajanjaksolla " + str(sarakkeet[i]) + " prosenttia. " + "\n"
                seloste_sarjoille[sarjat_sarake_nimi[i]] = lisays
                #tulostus += "Toimialan " + str(toimialat_sarakkeille[i]) + " " + str(muuttuja) + " supistui " + str(sarakkeet[0]) + " neljänneksellä " + str(sarakkeet[i]) + " prosenttia. " + "\n"
            else:
                if seloste_sarjoille.get(sarjat_sarake_nimi[i]):
                    lisays = ""
                else:
                    lisays = seloste_sarjoille.get(sarjat_sarake_nimi[i])
                lisays += "Sarjan " + str(sarjat_sarake_nimi[i]) + " " + str(muuttujat_sarake_nimi[i]) + " ei kasvanut tai supistunut " + str(ajanjakso) + "/" + str(vuosi) + "-ajanjaksolla " + str(sarakkeet[i]) + ". \n"
                seloste_sarjoille[sarjat_sarake_nimi[i]] = lisays
                #tulostus += "Toimialan " + str(toimialat_sarakkeille[i]) + " " + str(muuttuja) + " ei kasvanut eikä supistunut " + str(sarakkeet[0]) + " neljänneksellä." + "\n"

    for avain in seloste_sarjoille:
        tulostus += seloste_sarjoille.get(avain) + "\n"

    with open("seloste.txt", "x") as f:
        f.write(tulostus)

    return tulostus



print(tee_seloste("C:\\Users\\ossik\\Desktop\\kokeiludata_oikealla_rakenteella.csv"))