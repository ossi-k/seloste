def tee_seloste(data):
    #alustetaan muuttujia
    tulostus = ""
    seloste_sarjoille = {} #lopulinen seloste, johon appendataan muuttujakohtaiset selosteet
    sarjat_sarake_nimi = {}
    muuttujat_sarake_nimi = {}
    mukana_olevat_muuttujat = set()
    seloste_sarjat_liikevaihto = {}
    seloste_sarjat_vienti = {}
    seloste_sarjat_henkilostomaara = {}
    seloste_sarjat_palkkasumma = {}

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

    for i in range(3, len(sarjat_sarake_nimi)):
        print(sarjat_sarake_nimi[i])
        if sarjat_sarake_nimi[i] not in seloste_sarjoille:
            seloste_sarjoille[sarjat_sarake_nimi[i]] = ""

    #päätellään sarakkeiden muuttujat
    muuttujat = lines[0].split(";")
    for i in range(3, len(muuttujat)):
        muuttujat_sarake_nimi[i] = muuttujat[i]
        if not mukana_olevat_muuttujat.__contains__(muuttujat[i]):
            mukana_olevat_muuttujat.add(muuttujat[i])

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

        #sijoitetaan sarjakohtaiset selosteet muuttujittain omiin hajautustauluihinsa
        for i in range(3, len(sarakkeet)):
            lisays = ""
            if float(sarakkeet[i]) > 0:
                if muuttujat_sarake_nimi[i].lower() == "liikevaihto":
                    if not seloste_sarjat_liikevaihto.get(sarjat_sarake_nimi[i]):
                        lisays = ""
                    else:
                        lisays = seloste_sarjat_liikevaihto.get(sarjat_sarake_nimi[i])
                    lisays += "Sarjan " + str(sarjat_sarake_nimi[i]) + " " + str(muuttujat_sarake_nimi[i]) + " kasvoi " + str(ajanjakso) + "/" + str(vuosi) + "-ajanjaksolla " + str(sarakkeet[i]) + " prosenttia. " + "\n"
                    seloste_sarjat_liikevaihto[sarjat_sarake_nimi[i]] = lisays
                elif muuttujat_sarake_nimi[i].lower() == "palkkasumma":
                    if not seloste_sarjat_palkkasumma.get(sarjat_sarake_nimi[i]):
                        lisays = ""
                    else:
                        lisays = seloste_sarjat_palkkasumma.get(sarjat_sarake_nimi[i])
                    lisays += "Sarjan " + str(sarjat_sarake_nimi[i]) + " " + str(muuttujat_sarake_nimi[i]) + " kasvoi " + str(ajanjakso) + "/" + str(vuosi) + "-ajanjaksolla " + str(sarakkeet[i]) + " prosenttia. " + "\n"
                    seloste_sarjat_palkkasumma[sarjat_sarake_nimi[i]] = lisays
                elif muuttujat_sarake_nimi[i].lower() == "vientiliikevaihto":
                    if not seloste_sarjat_vienti.get(sarjat_sarake_nimi[i]):
                        lisays = ""
                    else:
                        lisays = seloste_sarjat_vienti.get(sarjat_sarake_nimi[i])
                    lisays += "Sarjan " + str(sarjat_sarake_nimi[i]) + " " + str(muuttujat_sarake_nimi[i]) + " kasvoi " + str(ajanjakso) + "/" + str(vuosi) + "-ajanjaksolla " + str(sarakkeet[i]) + " prosenttia. " + "\n"
                    seloste_sarjat_vienti[sarjat_sarake_nimi[i]] = lisays
                elif muuttujat_sarake_nimi[i].lower() == "henkilöstömäärä":
                    if not seloste_sarjat_henkilostomaara.get(sarjat_sarake_nimi[i]):
                        lisays = ""
                    else:
                        lisays = seloste_sarjat_henkilostomaara.get(sarjat_sarake_nimi[i])
                    lisays += "Sarjan " + str(sarjat_sarake_nimi[i]) + " " + str(muuttujat_sarake_nimi[i]) + " kasvoi " + str(ajanjakso) + "/" + str(vuosi) + "-ajanjaksolla " + str(sarakkeet[i]) + " prosenttia. " + "\n"
                    seloste_sarjat_henkilostomaara[sarjat_sarake_nimi[i]] = lisays
            elif float(sarakkeet[i]) < 0:
                lisays += "Sarjan " + str(sarjat_sarake_nimi[i]) + " " + str( muuttujat_sarake_nimi[i]) + " kasvoi " + str(ajanjakso) + "/" + str(vuosi) + "-ajanjaksolla " + str(sarakkeet[i]) + " prosenttia. " + "\n"
                if muuttujat_sarake_nimi[i].lower() == "liikevaihto":
                    if not seloste_sarjat_liikevaihto.get(sarjat_sarake_nimi[i]):
                        lisays = ""
                    else:
                        lisays = seloste_sarjat_liikevaihto.get(sarjat_sarake_nimi[i])
                    lisays += "Sarjan " + str(sarjat_sarake_nimi[i]) + " " + str(muuttujat_sarake_nimi[i]) + " kasvoi " + str(ajanjakso) + "/" + str(vuosi) + "-ajanjaksolla " + str(sarakkeet[i]) + " prosenttia. " + "\n"
                    seloste_sarjat_liikevaihto[sarjat_sarake_nimi[i]] = lisays
                elif muuttujat_sarake_nimi[i].lower() == "palkkasumma":
                    if not seloste_sarjat_palkkasumma.get(sarjat_sarake_nimi[i]):
                        lisays = ""
                    else:
                        lisays = seloste_sarjat_palkkasumma.get(sarjat_sarake_nimi[i])
                    lisays += "Sarjan " + str(sarjat_sarake_nimi[i]) + " " + str(muuttujat_sarake_nimi[i]) + " kasvoi " + str(ajanjakso) + "/" + str(vuosi) + "-ajanjaksolla " + str(sarakkeet[i]) + " prosenttia. " + "\n"
                    seloste_sarjat_palkkasumma[sarjat_sarake_nimi[i]] = lisays
                elif muuttujat_sarake_nimi[i].lower() == "vientiliikevaihto":
                    if not seloste_sarjat_vienti.get(sarjat_sarake_nimi[i]):
                        lisays = ""
                    else:
                        lisays = seloste_sarjat_vienti.get(sarjat_sarake_nimi[i])
                    lisays += "Sarjan " + str(sarjat_sarake_nimi[i]) + " " + str(muuttujat_sarake_nimi[i]) + " kasvoi " + str(ajanjakso) + "/" + str(vuosi) + "-ajanjaksolla " + str(sarakkeet[i]) + " prosenttia. " + "\n"
                    seloste_sarjat_vienti[sarjat_sarake_nimi[i]] = lisays
                elif muuttujat_sarake_nimi[i].lower() == "henkilöstömäärä":
                    if not seloste_sarjat_henkilostomaara.get(sarjat_sarake_nimi[i]):
                        lisays = ""
                    else:
                        lisays = seloste_sarjat_henkilostomaara.get(sarjat_sarake_nimi[i])
                    lisays += "Sarjan " + str(sarjat_sarake_nimi[i]) + " " + str(muuttujat_sarake_nimi[i]) + " kasvoi " + str(ajanjakso) + "/" + str(vuosi) + "-ajanjaksolla " + str(sarakkeet[i]) + " prosenttia. " + "\n"
                    seloste_sarjat_henkilostomaara[sarjat_sarake_nimi[i]] = lisays
            else:
                if muuttujat_sarake_nimi[i].lower() == "liikevaihto":
                    if not seloste_sarjat_liikevaihto.get(sarjat_sarake_nimi[i]):
                        lisays = ""
                    else:
                        lisays = seloste_sarjat_liikevaihto.get(sarjat_sarake_nimi[i])
                    lisays += "Sarjan " + str(sarjat_sarake_nimi[i]) + " " + str(muuttujat_sarake_nimi[i]) + " ei kasvanut tai supistunut " + str(ajanjakso) + "/" + str(vuosi) + "-ajanjaksolla " + str(sarakkeet[i]) + ". \n"
                    seloste_sarjat_liikevaihto[sarjat_sarake_nimi[i]] = lisays
                elif muuttujat_sarake_nimi[i].lower() == "palkkasumma":
                    if not seloste_sarjat_palkkasumma.get(sarjat_sarake_nimi[i]):
                        lisays = ""
                    else:
                        lisays = seloste_sarjat_palkkasumma.get(sarjat_sarake_nimi[i])
                    lisays += "Sarjan " + str(sarjat_sarake_nimi[i]) + " " + str(muuttujat_sarake_nimi[i]) + " ei kasvanut tai supistunut " + str(ajanjakso) + "/" + str(vuosi) + "-ajanjaksolla " + str(sarakkeet[i]) + ". \n"
                    seloste_sarjat_palkkasumma[sarjat_sarake_nimi[i]] = lisays
                elif muuttujat_sarake_nimi[i].lower() == "vientiliikevaihto":
                    if not seloste_sarjat_vienti.get(sarjat_sarake_nimi[i]):
                        lisays = ""
                    else:
                        lisays = seloste_sarjat_vienti.get(sarjat_sarake_nimi[i])
                        lisays += "Sarjan " + str(sarjat_sarake_nimi[i]) + " " + str(muuttujat_sarake_nimi[i]) + " ei kasvanut tai supistunut " + str(ajanjakso) + "/" + str(vuosi) + "-ajanjaksolla " + str(sarakkeet[i]) + ". \n"
                    seloste_sarjat_vienti[sarjat_sarake_nimi[i]] = lisays
                elif muuttujat_sarake_nimi[i].lower() == "henkilöstömäärä":
                    if not seloste_sarjat_henkilostomaara.get(sarjat_sarake_nimi[i]):
                        lisays = ""
                    else:
                        lisays = seloste_sarjat_henkilostomaara.get(sarjat_sarake_nimi[i])
                        lisays += "Sarjan " + str(sarjat_sarake_nimi[i]) + " " + str(muuttujat_sarake_nimi[i]) + " ei kasvanut tai supistunut " + str(ajanjakso) + "/" + str(vuosi) + "-ajanjaksolla " + str(sarakkeet[i]) + ". \n"
                    seloste_sarjat_henkilostomaara[sarjat_sarake_nimi[i]] = lisays

    #liitetään muuttujittain ryhmitellyt selosteet yhdeksi selosteeksi oikean sarjan alle
    if seloste_sarjat_liikevaihto:
        for avain in seloste_sarjat_liikevaihto:
            seloste_sarjoille[avain] += seloste_sarjat_liikevaihto[avain]
    if seloste_sarjat_palkkasumma:
        for avain in seloste_sarjat_palkkasumma:
            seloste_sarjoille[avain] += seloste_sarjat_palkkasumma[avain]
    if seloste_sarjat_henkilostomaara:
        for avain in seloste_sarjat_henkilostomaara:
            seloste_sarjoille[avain] += seloste_sarjat_henkilostomaara[avain]
    if seloste_sarjat_vienti:
        for avain in seloste_sarjat_vienti:
            seloste_sarjoille[avain] += seloste_sarjat_vienti[avain]

    for avain in seloste_sarjoille:
        tulostus += seloste_sarjoille.get(avain) + "\n"

    with open("seloste.txt", "x") as f:
        f.write(tulostus)

    return tulostus


print(tee_seloste("C:\\Users\\ossik\\Desktop\\kokeiludata_oikealla_rakenteella.csv"))