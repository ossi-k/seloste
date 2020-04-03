def tee_seloste(data):
    #alustetaan muuttujia
    tulostus = ""
    toimialat_sarakkeille = {}
    seloste_toimialoille = {}

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

    # päätellään muuttuja ja poistetaan otsikkorivi
    eka_rivi = lines[0].split(" ")
    muuttuja = eka_rivi[3][:11]
    lines.pop(0)

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


print(tee_seloste("C:\\Users\\ossik\\Downloads\\004_111y_2020m01.csv"))
#print(tee_seloste("C:\\Users\\ossik\\Downloads\\004_112d_2020m01.csv"))