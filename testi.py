def tee_seloste(data):
    #alustetaan muuttujia
    tulostus = ""
    toimialat_sarakkeille = {}
    seloste_toimialoille = {}
    sarjat_sarake_nimi = {}

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
    sarjojen_nimet_rivi = lines[0].split(" ")
    for i in range(len(sarjojen_nimet_rivi)):
        alkio = sarjojen_nimet_rivi[i]
        if alkio.__contains__(";"):
            alkio = alkio.replace(";", "")
        alkio = alkio.lower()
        if alkio.__contains__("sarja"):
            alkio = alkio.replace("sarja", "")
        sarjat_sarake_nimi[i] = alkio
    lines.pop(0) #poistetaan sarjojen otsikkorivi
    lines.pop(0) #poistetaan muuttujien lyhenne-rivi

    #muodostetaan seloste
    rivi = 0
    for line in lines:
        sarakkeet = line.split(";")

        if rivi == 0:
            for i in range(1, len(sarakkeet)):
                sisalto = sarakkeet[i].replace('"', '').split(" ")
                toimiala = ""
                #for y in range(len(sarakkeet[i])):
                #    if sisalto[y] == " ":
                #       break
                for sana in sisalto:
                    if sana.lower() == muuttuja.lower():
                        break
                    toimiala += sana + " "
                toimialat_sarakkeille[i] = toimiala.lstrip()

        #for i in range(len(toimialat_sarakkeille)):
        #    seloste_toimialoille[i] = toimialat_sarakkeille.get(i)
            for avain in toimialat_sarakkeille:
                seloste_toimialoille[toimialat_sarakkeille.get(avain)] = ""

        #sarakkeiden lukumäärän päättely
        sarakkeet_lkm = len(sarakkeet)

        #muutetaan pilkut pisteiksi, jotta muuntaminen floatiksi onnistuu
        for i in range(1, sarakkeet_lkm):
            sarakkeet[i] = sarakkeet[i].replace(",", ".")

        if rivi > 0:
            #päätellään, onko kasvua vai laskua ja lisätään selosteeseen oikea tulostus
            for i in range(1, sarakkeet_lkm):
                if float(sarakkeet[i]) > 0:
                    lisays = seloste_toimialoille.get(toimialat_sarakkeille[i])
                    lisays += "Toimialan " + str(toimialat_sarakkeille[i]) + " " + str(muuttuja) + " kasvoi " + str(sarakkeet[0]) + " neljänneksellä " + str(sarakkeet[i]) + " prosenttia. " + "\n"
                    seloste_toimialoille[toimialat_sarakkeille[i]] = lisays
                    #tulostus += "Toimialan " + str(toimialat_sarakkeille[i]) + " " + str(muuttuja) + " kasvoi " + str(sarakkeet[0]) + " neljänneksellä " + str(sarakkeet[i]) + " prosenttia. " + "\n"
                elif float(sarakkeet[i]) < 0:
                    lisays = seloste_toimialoille.get(toimialat_sarakkeille[i])
                    lisays += "Toimialan " + str(toimialat_sarakkeille[i]) + " " + str(muuttuja) + " supistui " + str(sarakkeet[0]) + " neljänneksellä " + str(sarakkeet[i]) + " prosenttia. " + "\n"
                    seloste_toimialoille[toimialat_sarakkeille[i]] = lisays
                    #tulostus += "Toimialan " + str(toimialat_sarakkeille[i]) + " " + str(muuttuja) + " supistui " + str(sarakkeet[0]) + " neljänneksellä " + str(sarakkeet[i]) + " prosenttia. " + "\n"
                else:
                    lisays = seloste_toimialoille.get(toimialat_sarakkeille[i])
                    lisays += "Toimialan " + str(toimialat_sarakkeille[i]) + " " + str(muuttuja) + " ei kasvanut eikä supistunut " + str(sarakkeet[0]) + " neljänneksellä." + "\n"
                    seloste_toimialoille[toimialat_sarakkeille[i]] = lisays
                    #tulostus += "Toimialan " + str(toimialat_sarakkeille[i]) + " " + str(muuttuja) + " ei kasvanut eikä supistunut " + str(sarakkeet[0]) + " neljänneksellä." + "\n"
        rivi += 1

    for avain in seloste_toimialoille:
        tulostus += seloste_toimialoille.get(avain) + "\n"

    with open("seloste.txt", "x") as f:
        f.write(tulostus)

    return tulostus



print(tee_seloste("C:\\Users\\ossik\\Desktop\\kokeiludata_oikealla_rakenteella.csv"))